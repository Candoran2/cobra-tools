from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Ushort
from generated.formats.ms2.compounds.QuatWFirst import QuatWFirst
from generated.formats.ms2.compounds.Vector3 import Vector3


class TriChunk(BaseStruct):

	"""
	JWE2 Biosyn: 64 bytes
	"""

	__name__ = 'TriChunk'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# the smallest coordinates across all axes, min of unpacked vert coords if loc is 0,0,0
		self.bounds_min = Vector3(self.context, 0, None)
		self.material_index = 0
		self.tris_count = 0

		# the biggest coordinates across all axes, max of unpacked vert coords if loc is 0,0,0
		self.bounds_max = Vector3(self.context, 0, None)
		self.tris_offset = 0

		# can be 0,0,0, no obvious range, not always within range of bounds
		self.loc = Vector3(self.context, 0, None)

		# can be 1, 0, 0, 0; w always in range -1, +1
		self.rot = QuatWFirst(self.context, 0, None)
		self.u_2 = 0
		self.u_3 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.bounds_min = Vector3(self.context, 0, None)
		self.material_index = 0
		self.tris_count = 0
		self.bounds_max = Vector3(self.context, 0, None)
		self.tris_offset = 0
		self.loc = Vector3(self.context, 0, None)
		self.rot = QuatWFirst(self.context, 0, None)
		self.u_2 = 0
		self.u_3 = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.bounds_min = Vector3.from_stream(stream, instance.context, 0, None)
		instance.material_index = Ushort.from_stream(stream, instance.context, 0, None)
		instance.tris_count = Ushort.from_stream(stream, instance.context, 0, None)
		instance.bounds_max = Vector3.from_stream(stream, instance.context, 0, None)
		instance.tris_offset = Uint.from_stream(stream, instance.context, 0, None)
		instance.loc = Vector3.from_stream(stream, instance.context, 0, None)
		instance.rot = QuatWFirst.from_stream(stream, instance.context, 0, None)
		instance.u_2 = Ushort.from_stream(stream, instance.context, 0, None)
		instance.u_3 = Ushort.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Vector3.to_stream(stream, instance.bounds_min)
		Ushort.to_stream(stream, instance.material_index)
		Ushort.to_stream(stream, instance.tris_count)
		Vector3.to_stream(stream, instance.bounds_max)
		Uint.to_stream(stream, instance.tris_offset)
		Vector3.to_stream(stream, instance.loc)
		QuatWFirst.to_stream(stream, instance.rot)
		Ushort.to_stream(stream, instance.u_2)
		Ushort.to_stream(stream, instance.u_3)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'bounds_min', Vector3, (0, None), (False, None)
		yield 'material_index', Ushort, (0, None), (False, None)
		yield 'tris_count', Ushort, (0, None), (False, None)
		yield 'bounds_max', Vector3, (0, None), (False, None)
		yield 'tris_offset', Uint, (0, None), (False, None)
		yield 'loc', Vector3, (0, None), (False, None)
		yield 'rot', QuatWFirst, (0, None), (False, None)
		yield 'u_2', Ushort, (0, None), (False, None)
		yield 'u_3', Ushort, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'TriChunk [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* bounds_min = {self.fmt_member(self.bounds_min, indent+1)}'
		s += f'\n	* material_index = {self.fmt_member(self.material_index, indent+1)}'
		s += f'\n	* tris_count = {self.fmt_member(self.tris_count, indent+1)}'
		s += f'\n	* bounds_max = {self.fmt_member(self.bounds_max, indent+1)}'
		s += f'\n	* tris_offset = {self.fmt_member(self.tris_offset, indent+1)}'
		s += f'\n	* loc = {self.fmt_member(self.loc, indent+1)}'
		s += f'\n	* rot = {self.fmt_member(self.rot, indent+1)}'
		s += f'\n	* u_2 = {self.fmt_member(self.u_2, indent+1)}'
		s += f'\n	* u_3 = {self.fmt_member(self.u_3, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
