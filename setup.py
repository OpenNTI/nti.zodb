import codecs
from setuptools import setup, find_packages


TESTS_REQUIRE = [
    'nti.testing',
    'zope.testrunner',
    'fudge',
    'coverage',
]


def _read(fname):
    with codecs.open(fname, encoding='utf-8') as f:
        return f.read()

setup(
    name='nti.zodb',
    version='1.3.0',
    author='Jason Madden',
    author_email='jason@nextthought.com',
    description="Utilities for ZODB",
    long_description=(_read('README.rst') + '\n\n' + _read('CHANGES.rst')),
    license='Apache',
    keywords='ZODB',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Framework :: ZODB",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    url="https://github.com/NextThought/nti.zodb",
    zip_safe=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    namespace_packages=['nti'],
    tests_require=TESTS_REQUIRE,
    install_requires=[
        'setuptools',
        'nti.property', # BWC exports
        'nti.schema',
        'nti.wref',
        'perfmetrics',
        'persistent',
        'repoze.zodbconn',
        'zc.zlibstorage',
        'ZODB',
        # BTrees is a dependency of ZODB, but we use it directly here,
        # and want to make sure we have a decent version.
        'BTrees >= 4.7.2',
        # ZConfig is also a ZODB dep that we use directly here.
        'ZConfig',
        'zope.component',
        'zope.copy',
        'zope.copypastemove',
        'zope.deprecation',
        'zope.interface',
        'zope.minmax',
        'zope.processlifetime',
        'zope.security',
    ],
    extras_require={
        'test': TESTS_REQUIRE,
        'docs': [
            'Sphinx',
            'repoze.sphinx.autointerface',
            'sphinx_rtd_theme',
        ]
    },
)
