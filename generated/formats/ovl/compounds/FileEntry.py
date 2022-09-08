
from generated.formats.ovl.versions import *
from hashes import constants_jwe, constants_pz, constants_jwe2, constants_pc, constants_dla


from generated.base_struct import BaseStruct
from generated.formats.base.basic import Byte
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Ushort


class FileEntry(BaseStruct):

	"""
	Description of one file in the archive
	"""

	__name__ = 'FileEntry'

	_import_path = 'generated.formats.ovl.compounds.FileEntry'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# offset in the ovl's names block; start offset of zero terminated string
		self.offset = 0

		# this hash is used to retrieve the file name from inside the archive
		self.file_hash = 0

		# pool type of this file's sizedstr pointer, if part of a set, it's usually the same as set pool type
		self.pool_type = 0

		# if this file is part of a set, the set's root entry's pool type, else 0
		self.set_pool_type = 0

		# index into 'Extensions' array
		self.extension = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.offset = 0
		self.file_hash = 0
		self.pool_type = 0
		self.set_pool_type = 0
		self.extension = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.offset = Uint.from_stream(stream, instance.context, 0, None)
		instance.file_hash = Uint.from_stream(stream, instance.context, 0, None)
		instance.pool_type = Byte.from_stream(stream, instance.context, 0, None)
		instance.set_pool_type = Byte.from_stream(stream, instance.context, 0, None)
		instance.extension = Ushort.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint.to_stream(stream, instance.offset)
		Uint.to_stream(stream, instance.file_hash)
		Byte.to_stream(stream, instance.pool_type)
		Byte.to_stream(stream, instance.set_pool_type)
		Ushort.to_stream(stream, instance.extension)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'offset', Uint, (0, None), (False, None)
		yield 'file_hash', Uint, (0, None), (False, None)
		yield 'pool_type', Byte, (0, None), (False, None)
		yield 'set_pool_type', Byte, (0, None), (False, None)
		yield 'extension', Ushort, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'FileEntry [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def update_constants(self, ovl):
		"""Update the constants"""

		# update offset using the name buffer
		if is_jwe(ovl):
			constants = constants_jwe
		elif is_pz(ovl) or is_pz16(ovl):
			constants = constants_pz
		elif is_jwe2(ovl):
			constants = constants_jwe2
		elif is_pc(ovl):
			constants = constants_pc
		elif is_dla(ovl):
			constants = constants_dla
		else:
			raise ValueError(f"Unsupported game {get_game(ovl)}")
		self.pool_type = constants.files_pool_type[self.ext]
		self.set_pool_type = constants.files_set_pool_type[self.ext]

