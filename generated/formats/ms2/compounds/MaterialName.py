from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Ushort


class MaterialName(BaseStruct):

	__name__ = 'MaterialName'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# index into ms2 names array
		self.name_index = 0

		# unknown, nonzero in PZ flamingo juvenile, might be junk (padding)
		self.some_index = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		if self.context.version >= 47:
			self.name_index = 0
		if self.context.version <= 32:
			self.name_index = 0
		if self.context.version >= 47:
			self.some_index = 0
		if self.context.version <= 32:
			self.some_index = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		if instance.context.version >= 47:
			instance.name_index = Uint.from_stream(stream, instance.context, 0, None)
		if instance.context.version <= 32:
			instance.name_index = Ushort.from_stream(stream, instance.context, 0, None)
		if instance.context.version >= 47:
			instance.some_index = Uint.from_stream(stream, instance.context, 0, None)
		if instance.context.version <= 32:
			instance.some_index = Ushort.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		if instance.context.version >= 47:
			Uint.to_stream(stream, instance.name_index)
		if instance.context.version <= 32:
			Ushort.to_stream(stream, instance.name_index)
		if instance.context.version >= 47:
			Uint.to_stream(stream, instance.some_index)
		if instance.context.version <= 32:
			Ushort.to_stream(stream, instance.some_index)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		if instance.context.version >= 47:
			yield 'name_index', Uint, (0, None), (False, None)
		if instance.context.version <= 32:
			yield 'name_index', Ushort, (0, None), (False, None)
		if instance.context.version >= 47:
			yield 'some_index', Uint, (0, None), (False, None)
		if instance.context.version <= 32:
			yield 'some_index', Ushort, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'MaterialName [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* name_index = {self.fmt_member(self.name_index, indent+1)}'
		s += f'\n	* some_index = {self.fmt_member(self.some_index, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
