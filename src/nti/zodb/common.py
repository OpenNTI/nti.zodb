#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import os

def make_cache_dir(cache_name, env_var=None):
	"""
	Global utility to create and return a cache directory in the
	most appropriate position.

	This takes into account environment settings for an active application
	server first. Following that, the python virtual installation is used, and
	finally a system-specific cache location. If all that fails, and the current
	working directory is writable, it will be used.

	:param str cache_name: The specific (filesystem) name of the type of cache
	:param str env_var: If given, then names an environment variable that will be
		queried first. If the environment variable exists, then we will attempt to use
		it in preference to anything else.
	:return: A string giving a path to a directory for the cache.
	:raises ValueError: If no cache location can be found.
	"""

	result = None

	if env_var:
		result = os.environ.get(env_var)

	if result is None:
		child_parts = ('var', 'caches', cache_name)
		# In preference order
		for env_var in ('DATASERVER_ENV', 'DATASERVER_DIR', 'VIRTUAL_ENV'):
			if env_var in os.environ:
				parent = os.environ[env_var]
				result = os.path.join(parent, *child_parts)
				break

	# Ok, no environment to be found. How about some system specific stuff?
	if result is None:
		for system_loc in ("~/Library/Caches/",  # OS x
							"~/.cache"):  # Linux
			system_loc = os.path.expanduser(system_loc)
			if os.path.isdir(system_loc):
				result = os.path.join(system_loc, "com.nextthought",
									   "nti.dataserver", cache_name)
				break

	if result is None:
		result = os.path.join(os.getcwd(), '.caches', cache_name)

	try:
		os.makedirs(result)
	except OSError:
		pass

	if not os.path.isdir(result):
		raise ValueError("Unable to find cache location for " + cache_name +
						  " using " + result)
	return os.path.abspath(os.path.expanduser(result))
