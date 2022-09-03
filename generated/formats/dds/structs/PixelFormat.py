from generated.base_struct import BaseStruct
from generated.formats.dds.basic import Uint
from generated.formats.dds.bitstructs.PixelFormatFlags import PixelFormatFlags
from generated.formats.dds.enums.FourCC import FourCC


class PixelFormat(BaseStruct):

	__name__ = 'PixelFormat'

	_import_path = 'generated.formats.dds.structs.PixelFormat'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# Always 32.
		self.size = 32

		# Non-zero for DX9, zero for DX10.
		self.flags = PixelFormatFlags(self.context, 0, None)

		# Determines compression type. Zero means no compression.
		self.four_c_c = FourCC(self.context, 0, None)

		# For non-compressed types, this is either 24 or 32 depending on whether there is an alpha channel. For compressed types, this describes the number of bits per block, which can be either 256 or 512.
		self.bit_count = 0

		# For non-compressed types, this determines the red mask. Usually 0x00FF0000. Is zero for compressed textures.
		self.r_mask = 0

		# For non-compressed types, this determines
		# the green mask. Usually 0x0000FF00. Is zero for compressed textures.
		self.g_mask = 0

		# For non-compressed types, this determines
		# the blue mask. Usually 0x00FF0000. Is zero for compressed textures.
		self.b_mask = 0

		# For non-compressed types, this determines
		# the alpha mask. Usually 0x00000000 if there is no alpha channel and 0xFF000000 if there is an alpha channel. Is zero for compressed textures.
		self.a_mask = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.size = 32
		self.flags = PixelFormatFlags(self.context, 0, None)
		self.four_c_c = FourCC(self.context, 0, None)
		self.bit_count = 0
		self.r_mask = 0
		self.g_mask = 0
		self.b_mask = 0
		self.a_mask = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.size = Uint.from_stream(stream, instance.context, 0, None)
		instance.flags = PixelFormatFlags.from_stream(stream, instance.context, 0, None)
		instance.four_c_c = FourCC.from_stream(stream, instance.context, 0, None)
		instance.bit_count = Uint.from_stream(stream, instance.context, 0, None)
		instance.r_mask = Uint.from_stream(stream, instance.context, 0, None)
		instance.g_mask = Uint.from_stream(stream, instance.context, 0, None)
		instance.b_mask = Uint.from_stream(stream, instance.context, 0, None)
		instance.a_mask = Uint.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint.to_stream(stream, instance.size)
		PixelFormatFlags.to_stream(stream, instance.flags)
		FourCC.to_stream(stream, instance.four_c_c)
		Uint.to_stream(stream, instance.bit_count)
		Uint.to_stream(stream, instance.r_mask)
		Uint.to_stream(stream, instance.g_mask)
		Uint.to_stream(stream, instance.b_mask)
		Uint.to_stream(stream, instance.a_mask)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'size', Uint, (0, None), (False, 32)
		yield 'flags', PixelFormatFlags, (0, None), (False, None)
		yield 'four_c_c', FourCC, (0, None), (False, None)
		yield 'bit_count', Uint, (0, None), (False, None)
		yield 'r_mask', Uint, (0, None), (False, None)
		yield 'g_mask', Uint, (0, None), (False, None)
		yield 'b_mask', Uint, (0, None), (False, None)
		yield 'a_mask', Uint, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'PixelFormat [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* size = {self.fmt_member(self.size, indent+1)}'
		s += f'\n	* flags = {self.fmt_member(self.flags, indent+1)}'
		s += f'\n	* four_c_c = {self.fmt_member(self.four_c_c, indent+1)}'
		s += f'\n	* bit_count = {self.fmt_member(self.bit_count, indent+1)}'
		s += f'\n	* r_mask = {self.fmt_member(self.r_mask, indent+1)}'
		s += f'\n	* g_mask = {self.fmt_member(self.g_mask, indent+1)}'
		s += f'\n	* b_mask = {self.fmt_member(self.b_mask, indent+1)}'
		s += f'\n	* a_mask = {self.fmt_member(self.a_mask, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
