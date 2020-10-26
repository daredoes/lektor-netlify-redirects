from setuptools import setup


setup(
    name='lektor-netlify-redirects',
    version='1.0',
    author=u'DareDoes',
    author_email='me@daredoes.work',
    url='https://github.com/daredoes/lektor-netlify-redirects',
    description='Adds Netlify style redirects to Lektor',
    license='MIT',
    py_modules=['lektor_netlify_redirects'],
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'lektor.plugins': [
            'netlify-redirects = lektor_netlify_redirects:NetlifyRedirectsPlugin',
        ]
    }
)
