from setuptools import setup


setup(
    name='netlify-redirects',
    author='DareDoes',
    author_email='me@daredoes.work',
    version='0.1',
    url='http://github.com/daredoes/lektor-netlify-redirects',
    license='MIT',
    packages=['lektor_netlify_redirects'],
    description='Adds redirects to netlify',
    entry_points={
        'lektor.plugins': [
            'hello-world = lektor_netlify_redirects:NetlifyRedirectsPlugin',
        ]
    },
)
