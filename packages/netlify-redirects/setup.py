from setuptools import setup

setup(
    name='lektor-netlify-redirects',
    version='0.1',
    author=u'DareDoes',
    author_email='me@daredoes.work',
    license='MIT',
    py_modules=['lektor_netlify_redirects'],
    entry_points={
        'lektor.plugins': [
            'netlify-redirects = lektor_netlify_redirects:NetlifyRedirectsPlugin',
        ]
    }
)
