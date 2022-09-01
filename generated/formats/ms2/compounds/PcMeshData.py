
import math
import logging
import numpy as np
from generated.formats.ms2.compounds.packing_utils import *
from plugin.utils.tristrip import triangulate
from generated.formats.base.basic import Float
from generated.formats.base.basic import Uint
from generated.formats.ms2.bitfields.ModelFlag import ModelFlag
from generated.formats.ms2.compounds.MeshData import MeshData


class PcMeshData(MeshData):

	__name__ = 'PcMeshData'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# repeat
		self.tri_index_count_a = 0
		self.vertex_count = 0

		# x*16 = offset
		self.tri_offset = 0

		# number of index entries in the triangle index list; (not: number of triangles, byte count of tri buffer)
		self.tri_index_count = 0

		# x*16 = offset
		self.vertex_offset = 0

		# x*16 = offset
		self.weights_offset = 0

		# x*16 = offset
		self.uv_offset = 0

		# always zero
		self.zero_b = 0

		# x*16 = offset
		self.vertex_color_offset = 0

		# ?
		self.vertex_offset_within_lod = 0

		# power of 2 increasing with lod index
		self.poweroftwo = 0

		# always zero
		self.zero = 0

		# some floats
		self.unknown_07 = 0.0

		# bitfield
		self.flag = ModelFlag(self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.tri_index_count_a = 0
		self.vertex_count = 0
		self.tri_offset = 0
		self.tri_index_count = 0
		self.vertex_offset = 0
		self.weights_offset = 0
		self.uv_offset = 0
		self.zero_b = 0
		self.vertex_color_offset = 0
		self.vertex_offset_within_lod = 0
		self.poweroftwo = 0
		self.zero = 0
		self.unknown_07 = 0.0
		self.flag = ModelFlag(self.context, 0, None)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.tri_index_count_a = Uint.from_stream(stream, instance.context, 0, None)
		instance.vertex_count = Uint.from_stream(stream, instance.context, 0, None)
		instance.tri_offset = Uint.from_stream(stream, instance.context, 0, None)
		instance.tri_index_count = Uint.from_stream(stream, instance.context, 0, None)
		instance.vertex_offset = Uint.from_stream(stream, instance.context, 0, None)
		instance.weights_offset = Uint.from_stream(stream, instance.context, 0, None)
		instance.uv_offset = Uint.from_stream(stream, instance.context, 0, None)
		instance.zero_b = Uint.from_stream(stream, instance.context, 0, None)
		instance.vertex_color_offset = Uint.from_stream(stream, instance.context, 0, None)
		instance.vertex_offset_within_lod = Uint.from_stream(stream, instance.context, 0, None)
		instance.poweroftwo = Uint.from_stream(stream, instance.context, 0, None)
		instance.zero = Uint.from_stream(stream, instance.context, 0, None)
		instance.unknown_07 = Float.from_stream(stream, instance.context, 0, None)
		instance.flag = ModelFlag.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint.to_stream(stream, instance.tri_index_count_a)
		Uint.to_stream(stream, instance.vertex_count)
		Uint.to_stream(stream, instance.tri_offset)
		Uint.to_stream(stream, instance.tri_index_count)
		Uint.to_stream(stream, instance.vertex_offset)
		Uint.to_stream(stream, instance.weights_offset)
		Uint.to_stream(stream, instance.uv_offset)
		Uint.to_stream(stream, instance.zero_b)
		Uint.to_stream(stream, instance.vertex_color_offset)
		Uint.to_stream(stream, instance.vertex_offset_within_lod)
		Uint.to_stream(stream, instance.poweroftwo)
		Uint.to_stream(stream, instance.zero)
		Float.to_stream(stream, instance.unknown_07)
		ModelFlag.to_stream(stream, instance.flag)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'tri_index_count_a', Uint, (0, None), (False, None)
		yield 'vertex_count', Uint, (0, None), (False, None)
		yield 'tri_offset', Uint, (0, None), (False, None)
		yield 'tri_index_count', Uint, (0, None), (False, None)
		yield 'vertex_offset', Uint, (0, None), (False, None)
		yield 'weights_offset', Uint, (0, None), (False, None)
		yield 'uv_offset', Uint, (0, None), (False, None)
		yield 'zero_b', Uint, (0, None), (False, None)
		yield 'vertex_color_offset', Uint, (0, None), (False, None)
		yield 'vertex_offset_within_lod', Uint, (0, None), (False, None)
		yield 'poweroftwo', Uint, (0, None), (False, None)
		yield 'zero', Uint, (0, None), (False, None)
		yield 'unknown_07', Float, (0, None), (False, None)
		yield 'flag', ModelFlag, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'PcMeshData [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* tri_index_count_a = {self.fmt_member(self.tri_index_count_a, indent+1)}'
		s += f'\n	* vertex_count = {self.fmt_member(self.vertex_count, indent+1)}'
		s += f'\n	* tri_offset = {self.fmt_member(self.tri_offset, indent+1)}'
		s += f'\n	* tri_index_count = {self.fmt_member(self.tri_index_count, indent+1)}'
		s += f'\n	* vertex_offset = {self.fmt_member(self.vertex_offset, indent+1)}'
		s += f'\n	* weights_offset = {self.fmt_member(self.weights_offset, indent+1)}'
		s += f'\n	* uv_offset = {self.fmt_member(self.uv_offset, indent+1)}'
		s += f'\n	* zero_b = {self.fmt_member(self.zero_b, indent+1)}'
		s += f'\n	* vertex_color_offset = {self.fmt_member(self.vertex_color_offset, indent+1)}'
		s += f'\n	* vertex_offset_within_lod = {self.fmt_member(self.vertex_offset_within_lod, indent+1)}'
		s += f'\n	* poweroftwo = {self.fmt_member(self.poweroftwo, indent+1)}'
		s += f'\n	* zero = {self.fmt_member(self.zero, indent+1)}'
		s += f'\n	* unknown_07 = {self.fmt_member(self.unknown_07, indent+1)}'
		s += f'\n	* flag = {self.fmt_member(self.flag, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s

	def init_arrays(self):
		self.vertices = np.empty((self.vertex_count, 3), np.float32)
		self.use_blended_weights = np.empty(self.vertex_count, np.bool)
		self.normals = np.empty((self.vertex_count, 3), np.float32)
		self.tangents = np.empty((self.vertex_count, 3), np.float32)
		try:
			uv_shape = self.dt_uv["uvs"].shape
			self.uvs = np.empty((self.vertex_count, *uv_shape), np.float32)
		except:
			self.uvs = None
		try:
			colors_shape = self.dt["colors"].shape
			self.colors = np.empty((self.vertex_count, *colors_shape), np.float32)
		except:
			self.colors = None
		self.weights_info = {}

	def update_dtype(self):
		"""Update MeshData.dt (numpy dtype) according to MeshData.flag"""
		# basic shared stuff
		dt = [
			("pos", np.uint64),
			("normal", np.ubyte, (3,)),
			("winding", np.ubyte),
			("tangent", np.ubyte, (3,)),
			("bone index", np.ubyte),
		]
		dt_uv = [
			("uvs", np.ushort, (1, 2)),
		]
		dt_w = [
			("bone ids", np.ubyte, (4,)),
			("bone weights", np.ubyte, (4,)),
		]
		self.dt = np.dtype(dt)
		self.dt_uv = np.dtype(dt_uv)
		self.dt_w = np.dtype(dt_w)
		self.update_shell_count()
		# logging.debug(f"PC size of vertex: {self.dt.itemsize}")
		# logging.debug(f"PC size of uv: {self.dt_uv.itemsize}")
		# logging.debug(f"PC size of weights: {self.dt_w.itemsize}")

	def read_pc_array(self, dt, offset, count):
		arr = np.empty(dtype=dt, shape=count)
		self.buffer_info.verts.seek(offset * 16)
		# logging.debug(f"VERTS at {self.buffer_info.verts.tell()}")
		self.buffer_info.verts.readinto(arr)
		return arr

	def read_verts(self):
		# get dtype according to which the vertices are packed
		self.update_dtype()
		# read a vertices of this mesh
		self.verts_data = self.read_pc_array(self.dt, self.vertex_offset, self.vertex_count)
		self.uv_data = self.read_pc_array(self.dt_uv, self.uv_offset, self.vertex_count)
		self.weights_data = self.read_pc_array(self.dt_w, self.weights_offset, self.vertex_count)
		# todo - PC ostrich download has self.weights_offset = 0 for eyes and lashes, which consequently get wrong weights
		# create arrays for the unpacked ms2_file
		self.init_arrays()
		# first cast to the float uvs array so unpacking doesn't use int division
		if self.uvs is not None:
			self.uvs[:] = self.uv_data["uvs"]
			unpack_ushort_vector(self.uvs)
		self.normals[:] = self.verts_data["normal"]
		self.tangents[:] = self.verts_data["tangent"]
		unpack_int64_vector(self.verts_data["pos"], self.vertices, self.use_blended_weights)
		scale_unpack_vectorized(self.vertices, self.base)
		unpack_ubyte_vector(self.normals)
		unpack_ubyte_vector(self.tangents)
		unpack_swizzle_vectorized(self.vertices)
		unpack_swizzle_vectorized(self.normals)
		unpack_swizzle_vectorized(self.tangents)

		# PC does not use use_blended_weights, nor a flag
		if self.weights_offset != 0:
			bone_weights = self.weights_data["bone weights"].astype(np.float32) / 255
			self.get_blended_weights(self.weights_data["bone ids"], bone_weights)
		else:
			self.get_static_weights(self.verts_data["bone index"], self.use_blended_weights)
		# print(self.vertices)

	def read_tris(self):
		# tris are stored in the verts stream for PC
		# read all tri indices for this mesh, but only as many as needed if there are shells
		index_count = self.tri_index_count // self.shell_count
		self.tri_indices = self.read_pc_array(np.uint16, self.tri_offset, index_count)

