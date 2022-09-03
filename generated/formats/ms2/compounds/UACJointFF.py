import numpy
from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.base.basic import Int
from generated.formats.base.basic import Uint


class UACJointFF(BaseStruct):

	__name__ = 'UACJointFF'

	_import_path = 'generated.formats.ms2.compounds.UACJointFF'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# must be 11
		self.eleven = 0

		# bunch of -1's, and constants
		self.f_fs = Array((0,), Int, self.context, 0, None)
		self.name_offset = 0
		self.hitcheck_count = 0

		# 12 bytes of zeros
		self.zeros = Array((0,), Uint, self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.eleven = 0
		self.f_fs = numpy.zeros((4,), dtype=numpy.dtype('int32'))
		self.name_offset = 0
		self.hitcheck_count = 0
		self.zeros = numpy.zeros((3,), dtype=numpy.dtype('uint32'))

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.eleven = Uint.from_stream(stream, instance.context, 0, None)
		instance.f_fs = Array.from_stream(stream, instance.context, 0, None, (4,), Int)
		instance.name_offset = Uint.from_stream(stream, instance.context, 0, None)
		instance.hitcheck_count = Uint.from_stream(stream, instance.context, 0, None)
		instance.zeros = Array.from_stream(stream, instance.context, 0, None, (3,), Uint)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint.to_stream(stream, instance.eleven)
		Array.to_stream(stream, instance.f_fs, (4,), Int, instance.context, 0, None)
		Uint.to_stream(stream, instance.name_offset)
		Uint.to_stream(stream, instance.hitcheck_count)
		Array.to_stream(stream, instance.zeros, (3,), Uint, instance.context, 0, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'eleven', Uint, (0, None), (False, None)
		yield 'f_fs', Array, ((4,), Int, 0, None), (False, None)
		yield 'name_offset', Uint, (0, None), (False, None)
		yield 'hitcheck_count', Uint, (0, None), (False, None)
		yield 'zeros', Array, ((3,), Uint, 0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'UACJointFF [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* eleven = {self.fmt_member(self.eleven, indent+1)}'
		s += f'\n	* f_fs = {self.fmt_member(self.f_fs, indent+1)}'
		s += f'\n	* name_offset = {self.fmt_member(self.name_offset, indent+1)}'
		s += f'\n	* hitcheck_count = {self.fmt_member(self.hitcheck_count, indent+1)}'
		s += f'\n	* zeros = {self.fmt_member(self.zeros, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
