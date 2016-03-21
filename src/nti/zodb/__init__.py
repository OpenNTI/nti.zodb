#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

# pylint:disable=W0212

from ZODB.interfaces import IBroken

from ZODB.POSException import POSError
from ZODB.POSException import POSKeyError

def readCurrent(obj, container=True):
	"""
	Persistence safe wrapper around zodb connection readCurrent;
	also has some built in smarts about typical objects that need
	to be read together.
	"""

	# Per notes from session_storage.py, remember to activate
	# the objects first; otherwise the serial that gets recorded
	# tends to be 0 (if we had a ghost) which immediately changes
	# which leads to falce conflicts
	try:
		obj._p_activate()
		obj._p_jar.readCurrent(obj)
	except (TypeError, AttributeError):
		pass

	if container:  # BTree containers
		try:
			data = obj._SampleContainer__data
			data._p_activate()
			data._p_jar.readCurrent(data)
		except AttributeError:
			pass
	return obj

def isBroken(obj, uid=None):
	result = False
	try:
		if obj is None:
			msg = uid if uid is not None else u''
			logger.warn("Ignoring NULL object %s", msg)
			result = (uid is not None)
		else:
			if hasattr(obj, '_p_activate'):
				obj._p_activate()
			result = IBroken.providedBy(obj)
	except (POSError, TypeError):
		logger.error("Ignoring broken object %s, %s", type(obj), uid)
		result = True
	return result
is_broken = isBroken
