import generated.formats.base.basic
import generated.formats.cinematic.compounds.State
from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class CinematicData(MemStruct):

	__name__ = 'CinematicData'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.next_level_count = 0
		self.default_name = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.next_levels = ArrayPointer(self.context, self.next_level_count, generated.formats.cinematic.compounds.State.State)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.next_level_count = 0
		self.default_name = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.next_levels = ArrayPointer(self.context, self.next_level_count, generated.formats.cinematic.compounds.State.State)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.default_name = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.next_levels = ArrayPointer.from_stream(stream, instance.context, instance.next_level_count, generated.formats.cinematic.compounds.State.State)
		instance.next_level_count = Uint64.from_stream(stream, instance.context, 0, None)
		if not isinstance(instance.default_name, int):
			instance.default_name.arg = 0
		if not isinstance(instance.next_levels, int):
			instance.next_levels.arg = instance.next_level_count

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.default_name)
		ArrayPointer.to_stream(stream, instance.next_levels)
		Uint64.to_stream(stream, instance.next_level_count)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'default_name', Pointer, (0, generated.formats.base.basic.ZString), (False, None)
		yield 'next_levels', ArrayPointer, (instance.next_level_count, generated.formats.cinematic.compounds.State.State), (False, None)
		yield 'next_level_count', Uint64, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'CinematicData [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* default_name = {self.fmt_member(self.default_name, indent+1)}'
		s += f'\n	* next_levels = {self.fmt_member(self.next_levels, indent+1)}'
		s += f'\n	* next_level_count = {self.fmt_member(self.next_level_count, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
