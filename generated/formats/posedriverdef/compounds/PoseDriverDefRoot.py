from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.posedriverdef.compounds.Driver import Driver


class PoseDriverDefRoot(MemStruct):

	__name__ = 'PoseDriverDefRoot'

	_import_path = 'generated.formats.posedriverdef.compounds.PoseDriverDefRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.count = 0
		self.drivers = ArrayPointer(self.context, self.count, Driver)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.count = 0
		self.drivers = ArrayPointer(self.context, self.count, Driver)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.drivers = ArrayPointer.from_stream(stream, instance.context, instance.count, Driver)
		instance.count = Uint64.from_stream(stream, instance.context, 0, None)
		if not isinstance(instance.drivers, int):
			instance.drivers.arg = instance.count

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		ArrayPointer.to_stream(stream, instance.drivers)
		Uint64.to_stream(stream, instance.count)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'drivers', ArrayPointer, (instance.count, Driver), (False, None)
		yield 'count', Uint64, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'PoseDriverDefRoot [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* drivers = {self.fmt_member(self.drivers, indent+1)}'
		s += f'\n	* count = {self.fmt_member(self.count, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
