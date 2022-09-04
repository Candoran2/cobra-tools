from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint


class ZlibInfo(BaseStruct):

	"""
	Description of one zlib archive
	"""

	__name__ = 'ZlibInfo'

	_import_path = 'generated.formats.ovl.compounds.ZlibInfo'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# seemingly unused in JWE
		self.zlib_thing_1 = 0

		# seemingly unused in JWE, subtracting this from ovs uncompressed_size to get length of the uncompressed ovs header
		self.zlib_thing_2 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.zlib_thing_1 = 0
		self.zlib_thing_2 = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.zlib_thing_1 = Uint.from_stream(stream, instance.context, 0, None)
		instance.zlib_thing_2 = Uint.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint.to_stream(stream, instance.zlib_thing_1)
		Uint.to_stream(stream, instance.zlib_thing_2)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'zlib_thing_1', Uint, (0, None), (False, None)
		yield 'zlib_thing_2', Uint, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'ZlibInfo [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* zlib_thing_1 = {self.fmt_member(self.zlib_thing_1, indent+1)}'
		s += f'\n	* zlib_thing_2 = {self.fmt_member(self.zlib_thing_2, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
