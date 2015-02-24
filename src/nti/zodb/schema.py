#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import numbers

from zope.schema import Float

from zope.schema.interfaces import TooShort
from zope.schema.interfaces import ValidationError
from zope.schema.interfaces import WrongContainedType

# TODO: Remove when nti.schema is py3 ready

class FieldValidationMixin(object):
	"""
	A field mixin that causes slightly better errors to be created.
	"""

	def _fixup_validation_error_args( self, e, value ):
		# Called when the exception has one argument, which is usually, though not always,
		# the message
		e.args = (value, e.args[0], self.__name__)

	def _fixup_validation_error_no_args(self, e, value ):
		# Called when there are no arguments
		e.args = (value, str(e), self.__name__ )

	def _reraise_validation_error(self, e, value, _raise=False):
		if len(e.args) == 1: # typically the message is the only thing
			self._fixup_validation_error_args( e, value )
		elif len(e.args) == 0: # Typically a SchemaNotProvided. Grr.
			self._fixup_validation_error_no_args( e, value )
		elif isinstance( e, TooShort ) and len(e.args) == 2:
			# Note we're capitalizing the field in the message.
			e.i18n_message = _(	'${field} is too short.', 
								mapping={'field': self.__name__.capitalize(),
										 'minLength': e.args[1]})
			e.args = ( self.__name__.capitalize() + ' is too short.',
					   self.__name__,
					   value )
		e.field = self
		if not getattr( e, 'value', None):
			e.value  = value
		if _raise:
			raise e
		raise

	def _validate(self, value):
		try:
			super(FieldValidationMixin,self)._validate( value )
		except WrongContainedType as e:
			# args[0] will either be a list of Exceptions or a list of tuples, (name, exception),
			# depending who did the validating (dm.zope.schema doing the later)
			e.errors = [arg[1] if isinstance(arg, tuple) else arg for arg in e.args[0]]
			e.value = value
			e.field = self
			raise
		except ValidationError as e:
			self._reraise_validation_error( e, value )
			
# TODO: Remove when nti.schema is py3 ready

class Number(FieldValidationMixin, Float):
	_type = numbers.Number
