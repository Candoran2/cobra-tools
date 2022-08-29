import numpy
from generated.array import Array
from generated.formats.base.basic import Byte
from generated.formats.base.basic import Ubyte
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class Int8Data(MemStruct):

	"""
	8 bytes
	"""

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.imin = 0
		self.imax = 0
		self.ivalue = 0
		self.ioptional = 0
		self.unused = Array((0,), Ubyte, self.context, 0, None)
		self.enum = Pointer(self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.imin = 0
		self.imax = 0
		self.ivalue = 0
		self.ioptional = 0
		self.unused = numpy.zeros((4,), dtype=numpy.dtype('uint8'))
		self.enum = Pointer(self.context, 0, None)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.imin = Byte.from_stream(stream, instance.context, 0, None)
		instance.imax = Byte.from_stream(stream, instance.context, 0, None)
		instance.ivalue = Byte.from_stream(stream, instance.context, 0, None)
		instance.ioptional = Byte.from_stream(stream, instance.context, 0, None)
		instance.unused = Array.from_stream(stream, instance.context, 0, None, (4,), Ubyte)
		instance.enum = Pointer.from_stream(stream, instance.context, 0, None)
		if not isinstance(instance.enum, int):
			instance.enum.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Byte.to_stream(stream, instance.imin)
		Byte.to_stream(stream, instance.imax)
		Byte.to_stream(stream, instance.ivalue)
		Byte.to_stream(stream, instance.ioptional)
		Array.to_stream(stream, instance.unused, (4,), Ubyte, instance.context, 0, None)
		Pointer.to_stream(stream, instance.enum)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'imin', Byte, (0, None), (False, None)
		yield 'imax', Byte, (0, None), (False, None)
		yield 'ivalue', Byte, (0, None), (False, None)
		yield 'ioptional', Byte, (0, None), (False, None)
		yield 'unused', Array, ((4,), Ubyte, 0, None), (False, None)
		yield 'enum', Pointer, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'Int8Data [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* imin = {self.fmt_member(self.imin, indent+1)}'
		s += f'\n	* imax = {self.fmt_member(self.imax, indent+1)}'
		s += f'\n	* ivalue = {self.fmt_member(self.ivalue, indent+1)}'
		s += f'\n	* ioptional = {self.fmt_member(self.ioptional, indent+1)}'
		s += f'\n	* unused = {self.fmt_member(self.unused, indent+1)}'
		s += f'\n	* enum = {self.fmt_member(self.enum, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
