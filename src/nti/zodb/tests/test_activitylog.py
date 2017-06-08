#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

from hamcrest import assert_that
from hamcrest import has_property

import unittest

from nti.zodb.activitylog import AbstractActivityMonitor as ActivityMonitor


class TestBase(unittest.TestCase):

    def test_base(self):

        class Base(object):
            b = 1

        base = Base()
        mon = ActivityMonitor(base)

        assert_that(mon, has_property('b', 1))
