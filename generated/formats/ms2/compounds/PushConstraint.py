from generated.array import Array
from generated.formats.ms2.compounds.Constraint import Constraint
from generated.formats.ms2.imports import name_type_map


class PushConstraint(Constraint):

	"""
	used in JWE Pteranodon
	no longer used in PZ, JWE2
	might be some sort of avoidance
	"""

	__name__ = 'PushConstraint'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.floats = Array(self.context, 0, None, (0,), name_type_map['Float'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'floats', Array, (0, None, (3,), name_type_map['Float']), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'floats', Array, (0, None, (3,), name_type_map['Float']), (False, None)
