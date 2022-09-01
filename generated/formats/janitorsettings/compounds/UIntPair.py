from generated.formats.base.basic import Uint
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class UIntPair(MemStruct):

	__name__ = 'UIntPair'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.value_0 = 0
		self.value_1 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.value_0 = 0
		self.value_1 = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.value_0 = Uint.from_stream(stream, instance.context, 0, None)
		instance.value_1 = Uint.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint.to_stream(stream, instance.value_0)
		Uint.to_stream(stream, instance.value_1)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'value_0', Uint, (0, None), (False, None)
		yield 'value_1', Uint, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'UIntPair [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* value_0 = {self.fmt_member(self.value_0, indent+1)}'
		s += f'\n	* value_1 = {self.fmt_member(self.value_1, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
