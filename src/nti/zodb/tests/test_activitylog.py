#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import assert_that
from hamcrest import has_property

import unittest

from nti.zodb.activitylog import _AbstractActivityMonitor as ActivityMonitor

from nti.zodb.tests import SharedConfiguringTestLayer


class TestBase(unittest.TestCase):

    layer = SharedConfiguringTestLayer

    def test_base(self):

        class Base(object):
            b = 1

        base = Base()
        mon = ActivityMonitor(base)

        assert_that(mon, has_property('b', 1))
