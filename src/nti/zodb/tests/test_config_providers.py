# -*- coding: utf-8 -*-
"""
Tests for config_providers.py

"""

import unittest

from nti.testing.base import ConfiguringTestBase
from nti.testing.matchers import verifiably_provides

from hamcrest import assert_that
from hamcrest import has_length
from hamcrest import is_
from hamcrest import same_instance


class TestInMemoryDemoStorageZConfigProvider(unittest.TestCase):

    def _getFUT(self):
        from ..config_providers import InMemoryDemoStorageZConfigProvider as FUT
        return FUT

    def _makeOne(self):
        return self._getFUT()()

    def test_provides(self):
        from ..interfaces import IZODBZConfigProvider
        inst = self._makeOne()
        assert_that(inst, verifiably_provides(IZODBZConfigProvider))


class TestZConfigProviderToDatabase(ConfiguringTestBase):
    set_up_packages = (__name__,)

    def test_adapts(self):
        from ZODB.interfaces import IDatabase
        from ZODB.interfaces import IStorage

        from ..config_providers import InMemoryDemoStorageZConfigProvider as ZCP

        db = IDatabase(ZCP())
        # The DB itself doesn't validly provide IDatabase :(
        assert_that(db.storage, verifiably_provides(IStorage))



class TestProvideDatabases(ConfiguringTestBase):
    set_up_packages = (__name__,)

    def test_provide_temp_database(self):
        from zope import component
        from ZODB.interfaces import IDatabase
        from zope.processlifetime import DatabaseOpened

        from ..config_providers import provideDatabases

        events:list = []
        component.provideHandler(events.append, (None,))

        provideDatabases()
        # Because it's the only database provided, it
        # is registered both under its choosen name, and the
        # default name.
        default_db = component.getUtility(IDatabase)
        named_db = component.getUtility(IDatabase, "mtemp")

        assert_that(named_db, is_(same_instance(default_db)))
        # We sent an event
        # registered mtemp, registered '', DatabaseOpened
        assert_that(events, has_length(3))
        assert_that(events[-1], is_(DatabaseOpened))

        # Doing it again refuses to change anything, all names are duplicated
        with self.assertRaisesRegex(ValueError, 'already registered'):
            provideDatabases()

if __name__ == '__main__':
    unittest.main()
