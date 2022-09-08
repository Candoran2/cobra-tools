import numpy
from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.base.basic import Ubyte
from generated.formats.base.basic import Uint64
from generated.formats.ms2.compounds.NasutoJointEntry import NasutoJointEntry
from generated.formats.ms2.compounds.UACJoint import UACJoint
from generated.formats.ovl_base.compounds.SmartPadding import SmartPadding


class Struct7(BaseStruct):

	__name__ = 'Struct7'

	_import_path = 'generated.formats.ms2.compounds.Struct7'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# needed for ZTUAC
		self.weird_padding = SmartPadding(self.context, 0, None)

		# repeat
		self.count_7 = 0

		# seen 0
		self.zero_0 = 0

		# seen 0, 2, 4
		self.flag = 0
		self.zero_2 = 0

		# 36 bytes per entry

		# 60 bytes per entry
		self.unknown_list = Array(self.context, 0, None, (0,), NasutoJointEntry)

		# align list to multiples of 8
		self.padding = Array(self.context, 0, None, (0,), Ubyte)

		# latest PZ and jwe2 only - if flag is non-zero, 8 bytes, else 0
		self.alignment = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		if self.context.version <= 13:
			self.weird_padding = SmartPadding(self.context, 0, None)
		self.count_7 = 0
		self.zero_0 = 0
		if self.context.version >= 48:
			self.flag = 0
			self.zero_2 = 0
		if self.context.version <= 13:
			self.unknown_list = Array(self.context, 0, None, (self.count_7,), UACJoint)
		if self.context.version >= 32:
			self.unknown_list = Array(self.context, 0, None, (self.count_7,), NasutoJointEntry)
		self.padding = numpy.zeros(((8 - ((self.count_7 * 60) % 8)) % 8,), dtype=numpy.dtype('uint8'))
		if self.context.version >= 50 and self.flag:
			self.alignment = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		if instance.context.version <= 13:
			instance.weird_padding = SmartPadding.from_stream(stream, instance.context, 0, None)
		instance.count_7 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.zero_0 = Uint64.from_stream(stream, instance.context, 0, None)
		if instance.context.version >= 48:
			instance.flag = Uint64.from_stream(stream, instance.context, 0, None)
			instance.zero_2 = Uint64.from_stream(stream, instance.context, 0, None)
		if instance.context.version <= 13:
			instance.unknown_list = Array.from_stream(stream, instance.context, 0, None, (instance.count_7,), UACJoint)
		if instance.context.version >= 32:
			instance.unknown_list = Array.from_stream(stream, instance.context, 0, None, (instance.count_7,), NasutoJointEntry)
		instance.padding = Array.from_stream(stream, instance.context, 0, None, ((8 - ((instance.count_7 * 60) % 8)) % 8,), Ubyte)
		if instance.context.version >= 50 and instance.flag:
			instance.alignment = Uint64.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		if instance.context.version <= 13:
			SmartPadding.to_stream(stream, instance.weird_padding)
		Uint64.to_stream(stream, instance.count_7)
		Uint64.to_stream(stream, instance.zero_0)
		if instance.context.version >= 48:
			Uint64.to_stream(stream, instance.flag)
			Uint64.to_stream(stream, instance.zero_2)
		if instance.context.version <= 13:
			Array.to_stream(stream, instance.unknown_list, instance.context, 0, None, (instance.count_7,), UACJoint)
		if instance.context.version >= 32:
			Array.to_stream(stream, instance.unknown_list, instance.context, 0, None, (instance.count_7,), NasutoJointEntry)
		Array.to_stream(stream, instance.padding, instance.context, 0, None, ((8 - ((instance.count_7 * 60) % 8)) % 8,), Ubyte)
		if instance.context.version >= 50 and instance.flag:
			Uint64.to_stream(stream, instance.alignment)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		if instance.context.version <= 13:
			yield 'weird_padding', SmartPadding, (0, None), (False, None)
		yield 'count_7', Uint64, (0, None), (False, None)
		yield 'zero_0', Uint64, (0, None), (False, None)
		if instance.context.version >= 48:
			yield 'flag', Uint64, (0, None), (False, None)
			yield 'zero_2', Uint64, (0, None), (False, None)
		if instance.context.version <= 13:
			yield 'unknown_list', Array, (0, None, (instance.count_7,), UACJoint), (False, None)
		if instance.context.version >= 32:
			yield 'unknown_list', Array, (0, None, (instance.count_7,), NasutoJointEntry), (False, None)
		yield 'padding', Array, (0, None, ((8 - ((instance.count_7 * 60) % 8)) % 8,), Ubyte), (False, None)
		if instance.context.version >= 50 and instance.flag:
			yield 'alignment', Uint64, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'Struct7 [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* weird_padding = {self.fmt_member(self.weird_padding, indent+1)}'
		s += f'\n	* count_7 = {self.fmt_member(self.count_7, indent+1)}'
		s += f'\n	* zero_0 = {self.fmt_member(self.zero_0, indent+1)}'
		s += f'\n	* flag = {self.fmt_member(self.flag, indent+1)}'
		s += f'\n	* zero_2 = {self.fmt_member(self.zero_2, indent+1)}'
		s += f'\n	* unknown_list = {self.fmt_member(self.unknown_list, indent+1)}'
		s += f'\n	* padding = {self.fmt_member(self.padding, indent+1)}'
		s += f'\n	* alignment = {self.fmt_member(self.alignment, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
