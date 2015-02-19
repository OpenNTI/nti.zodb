import codecs
from setuptools import setup, find_packages

VERSION = '0.0.0'

import platform
py_impl = getattr(platform, 'python_implementation', lambda: None)
IS_PYPY = py_impl() == 'PyPy'

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
    'nti.testing',
    'nti.nose_traceback_info',
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
        'Programming Language :: Python :: Implementation :: CPython'
    ],
	packages=find_packages('src'),
	package_dir={'': 'src'},
	namespace_packages=['nti'],
    tests_require=TESTS_REQUIRE,
	install_requires=[
		'setuptools',
        'perfmetrics',
        'repoze.zodbconn' if not IS_PYPY else '', 
        'ZODB',
        'zope.component',
        'zope.copy',
        'zope.file',
        'zope.interface',
        'zope.minmax',
        'zope.security',
        'nti.common',
        'nti.schema',
	],
    dependency_links=[
        'git+https://github.com/NextThought/nti.schema.git#egg=nti.schema',
        'git+https://github.com/NextThought/nti.nose_traceback_info.git#egg=nti.nose_traceback_info'
    ],
	entry_points=entry_points
)
