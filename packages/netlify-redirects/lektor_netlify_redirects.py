# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from lektor.db import Query, F
from lektor.utils import get_cache_dir
from lektor.project import Project
from lektor.publisher import Publisher

from urllib import quote_plus
import os, shutil


class CopyPublisher(Publisher):

    def publish(self, target_url, credentials=None, **extra):
        pad = self.env.new_pad()
        myQuery = Query('/', pad)
        items = myQuery.filter(F._model == 'portal')
        output_location = self.output_path
        #print(output_location)
        with open('{}/_redirect'.format(output_location), 'wb') as redirect_file:
            for item in items:
                for block in item['body'].blocks:
                    try:
                        status = block['status']
                    except KeyError as e:
                        status = ''
                    try:
                        slug = quote_plus(block['slug'])
                        redirect_file.write("{} {} {}".format(
                        "/{}/{}".format(item['_slug'], slug),
                        block['url'], status))
                    except KeyError as e:
                        yield 'skipping {}'.format(block['title'])

        target_dir = os.getcwd() + target_url.path
        yield "copying to local directory %s" % target_dir

        # Clear the target directory if it exists
        yield "clearing target directory"
        shutil.rmtree(target_dir, ignore_errors=True)

        # Copy the build output to the target directory
        yield "copying tree"
        shutil.copytree(self.output_path, target_dir)


class NetlifyRedirectsPlugin(Plugin):
    name = u'Netlify Redirects'
    description = u'Automatically creates redirects on netlify'

    def on_setup_env(self, **extra):
        pass
        #self.env.add_publisher('redirect', CopyPublisher)

    def on_process_template_context(self, context, **extra):
        def test_function():
            return 'Value from plugin %s' % self.name
        context['test_function'] = test_function

    def on_after_build_all(self, builder, **options):
        pad = self.env.new_pad()
        myQuery = Query('/', pad)
        items = myQuery.filter(F._model == 'portal')
        output_location = self.builder.destination_path
        #print(output_location)
        with open('{}/_redirect'.format(output_location), 'wb') as redirect_file:
            for item in items:
                for block in item['body'].blocks:
                    try:
                        status = block['status']
                    except KeyError as e:
                        status = ''
                    try:
                        slug = quote_plus(block['slug'])
                        redirect_file.write("{} {} {}".format(
                        "/{}/{}".format(item['_slug'], slug),
                        block['url'], status))
                    except KeyError as e:
                        yield 'skipping {}'.format(block['title'])
