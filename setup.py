import codecs
from setuptools import setup, find_packages

VERSION = '0.0.0'

entry_points = {
    'console_scripts': [
    ],
}

TESTS_REQUIRE = [
    'fudge',
    'nose',
    'nose-timer',
    'nose-pudb',
    'nose-progressive',
    'nose2[coverage_plugin]',
    'pyhamcrest',
    'zope.testing',
    'nti.nose_traceback_info',
    'nti.testing'
]

setup(
    name='nti.zodb',
    version=VERSION,
    author='Jason Madden',
    author_email='jason@nextthought.com',
    description="NTI ZODB",
    long_description=codecs.open('README.rst', encoding='utf-8').read(),
    license='Proprietary',
    keywords='ZODB',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['nti'],
    tests_require=TESTS_REQUIRE,
    install_requires=[
        'setuptools',
        'BTrees',
        'nti.schema',
        'perfmetrics',
        'persistent',
        'repoze.zodbconn',
        'zc.zlibstorage',
        'ZODB',
        'zope.component',
        'zope.copy',
        'zope.deprecation',
        'zope.interface',
        'zope.minmax',
        'zope.processlifetime',
        'zope.security'
    ],
    extras_require={
        'test': TESTS_REQUIRE,
    },
    entry_points=entry_points
)
