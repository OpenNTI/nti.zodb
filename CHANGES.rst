=========
 Changes
=========


1.1.0 (2020-07-15)
==================

- Add support for Python 3.7 and 3.8.

- Loading this package's configuration no longer marks
  ``persistent.list.PersistentList`` as implementing the deprecated
  interface ``zope.interface.common.sequence.ISequence``. This
  conflicts with a strict resolution order. Prefer
  ``zope.interface.common.collections.ISequence`` or its mutable
  descendent, which ``PersistentList`` already implements.

- Rework ``nti.zodb.activitylog`` to be faster. Client code may need
  to adapt for best efficiency.

- The monitors in ``nti.zodb.activitylog`` now include information
  about the ZODB connection pool. See `issue 4
  <https://github.com/NextThought/nti.zodb/issues/4>`_.

- The log monitor now has a configurable threshold, defaulting to at
  least one load or store. See `issue 3
  <https://github.com/NextThought/nti.zodb/issues/3>`_.

1.0.0 (2017-06-08)
==================

- First PyPI release.
- Add support for Python 3.
- Remove nti.zodb.common. See
  https://github.com/NextThought/nti.zodb/issues/1.
  ``ZlibClientStorageURIResolver`` will no longer try to set a ``var``
  directory to store persistent cache files automatically.
- ``CopyingWeakRef`` now implements ``ICachingWeakRef``.
