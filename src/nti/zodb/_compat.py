#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import six

PY3 = six.PY3

text_type = six.text_type
class_types = six.class_types
string_types = six.string_types
integer_types = six.integer_types

if PY3:  # pragma: no cover
    def _unicode(s): return str(s)
else:
    _unicode = unicode


def unicode_(s, encoding='utf-8', err='strict'):
    """
    Decode a byte sequence and unicode result
    """
    s = s.decode(encoding, err) if isinstance(s, bytes) else s
    return _unicode(s) if s is not None else None
to_unicode = unicode_


try:
    from gevent import sleep
except ImportError:
    from time import sleep

sleep = sleep  # pylint
