from generated.formats.base.basic import Uint64
from generated.formats.fgm.compounds.GenericInfo import GenericInfo


class AttribInfo(GenericInfo):

	"""
	part of fgm fragment, repeated per attribute
	"""

	__name__ = 'AttribInfo'

	_import_path = 'generated.formats.fgm.compounds.AttribInfo'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# byte offset to first value in the data_lib pointer, usually or always sorted in stock
		self._value_offset = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self._value_offset = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance._value_offset = Uint64.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint64.to_stream(stream, instance._value_offset)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield '_value_offset', Uint64, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'AttribInfo [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
