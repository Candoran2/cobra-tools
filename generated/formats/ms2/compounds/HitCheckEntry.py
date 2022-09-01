from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Ushort
from generated.formats.ms2.compounds.BoundingBox import BoundingBox
from generated.formats.ms2.compounds.Capsule import Capsule
from generated.formats.ms2.compounds.ConvexHull import ConvexHull
from generated.formats.ms2.compounds.Cylinder import Cylinder
from generated.formats.ms2.compounds.MeshCollision import MeshCollision
from generated.formats.ms2.compounds.Sphere import Sphere
from generated.formats.ms2.enums.CollisionType import CollisionType


class HitCheckEntry(BaseStruct):

	__name__ = 'HitCheckEntry'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.dtype = CollisionType(self.context, 0, None)

		# 0
		self.flag_0 = 0

		# JWE1: 16, PZ, JWE2: 0
		self.flag_1 = 0

		# JWE1: 564267, PZ: seen 17 and 22, JWE2: 34, 30
		self.flag_2 = 0

		# JWE1: 46, PZ: same as above, JWE2: 21, 27
		self.flag_3 = 0

		# ?
		self.zero_extra_pc_unk = 0

		# offset into joint names
		self.name_offset = 0
		self.collider = MeshCollision(self.context, 0, None)

		# ?
		self.zero_extra_zt = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		# leaving self.dtype alone
		self.flag_0 = 0
		self.flag_1 = 0
		self.flag_2 = 0
		self.flag_3 = 0
		if self.context.version < 47:
			self.zero_extra_pc_unk = 0
		self.name_offset = 0
		if self.dtype == 0:
			self.collider = Sphere(self.context, 0, None)
		if self.dtype == 1:
			self.collider = BoundingBox(self.context, 0, None)
		if self.dtype == 2:
			self.collider = Capsule(self.context, 0, None)
		if self.dtype == 3:
			self.collider = Cylinder(self.context, 0, None)
		if self.dtype == 7:
			self.collider = ConvexHull(self.context, 0, None)
		if self.dtype == 8:
			self.collider = ConvexHull(self.context, 0, None)
		if self.dtype == 10:
			self.collider = MeshCollision(self.context, 0, None)
		if self.context.version == 13:
			self.zero_extra_zt = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.dtype = CollisionType.from_stream(stream, instance.context, 0, None)
		instance.flag_0 = Ushort.from_stream(stream, instance.context, 0, None)
		instance.flag_1 = Ushort.from_stream(stream, instance.context, 0, None)
		instance.flag_2 = Uint.from_stream(stream, instance.context, 0, None)
		instance.flag_3 = Uint.from_stream(stream, instance.context, 0, None)
		if instance.context.version < 47:
			instance.zero_extra_pc_unk = Uint.from_stream(stream, instance.context, 0, None)
		instance.name_offset = Uint.from_stream(stream, instance.context, 0, None)
		if instance.dtype == 0:
			instance.collider = Sphere.from_stream(stream, instance.context, 0, None)
		if instance.dtype == 1:
			instance.collider = BoundingBox.from_stream(stream, instance.context, 0, None)
		if instance.dtype == 2:
			instance.collider = Capsule.from_stream(stream, instance.context, 0, None)
		if instance.dtype == 3:
			instance.collider = Cylinder.from_stream(stream, instance.context, 0, None)
		if instance.dtype == 7:
			instance.collider = ConvexHull.from_stream(stream, instance.context, 0, None)
		if instance.dtype == 8:
			instance.collider = ConvexHull.from_stream(stream, instance.context, 0, None)
		if instance.dtype == 10:
			instance.collider = MeshCollision.from_stream(stream, instance.context, 0, None)
		if instance.context.version == 13:
			instance.zero_extra_zt = Uint.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		CollisionType.to_stream(stream, instance.dtype)
		Ushort.to_stream(stream, instance.flag_0)
		Ushort.to_stream(stream, instance.flag_1)
		Uint.to_stream(stream, instance.flag_2)
		Uint.to_stream(stream, instance.flag_3)
		if instance.context.version < 47:
			Uint.to_stream(stream, instance.zero_extra_pc_unk)
		Uint.to_stream(stream, instance.name_offset)
		if instance.dtype == 0:
			Sphere.to_stream(stream, instance.collider)
		if instance.dtype == 1:
			BoundingBox.to_stream(stream, instance.collider)
		if instance.dtype == 2:
			Capsule.to_stream(stream, instance.collider)
		if instance.dtype == 3:
			Cylinder.to_stream(stream, instance.collider)
		if instance.dtype == 7:
			ConvexHull.to_stream(stream, instance.collider)
		if instance.dtype == 8:
			ConvexHull.to_stream(stream, instance.collider)
		if instance.dtype == 10:
			MeshCollision.to_stream(stream, instance.collider)
		if instance.context.version == 13:
			Uint.to_stream(stream, instance.zero_extra_zt)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'dtype', CollisionType, (0, None), (False, None)
		yield 'flag_0', Ushort, (0, None), (False, None)
		yield 'flag_1', Ushort, (0, None), (False, None)
		yield 'flag_2', Uint, (0, None), (False, None)
		yield 'flag_3', Uint, (0, None), (False, None)
		if instance.context.version < 47:
			yield 'zero_extra_pc_unk', Uint, (0, None), (False, None)
		yield 'name_offset', Uint, (0, None), (False, None)
		if instance.dtype == 0:
			yield 'collider', Sphere, (0, None), (False, None)
		if instance.dtype == 1:
			yield 'collider', BoundingBox, (0, None), (False, None)
		if instance.dtype == 2:
			yield 'collider', Capsule, (0, None), (False, None)
		if instance.dtype == 3:
			yield 'collider', Cylinder, (0, None), (False, None)
		if instance.dtype == 7:
			yield 'collider', ConvexHull, (0, None), (False, None)
		if instance.dtype == 8:
			yield 'collider', ConvexHull, (0, None), (False, None)
		if instance.dtype == 10:
			yield 'collider', MeshCollision, (0, None), (False, None)
		if instance.context.version == 13:
			yield 'zero_extra_zt', Uint, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'HitCheckEntry [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* dtype = {self.fmt_member(self.dtype, indent+1)}'
		s += f'\n	* flag_0 = {self.fmt_member(self.flag_0, indent+1)}'
		s += f'\n	* flag_1 = {self.fmt_member(self.flag_1, indent+1)}'
		s += f'\n	* flag_2 = {self.fmt_member(self.flag_2, indent+1)}'
		s += f'\n	* flag_3 = {self.fmt_member(self.flag_3, indent+1)}'
		s += f'\n	* zero_extra_pc_unk = {self.fmt_member(self.zero_extra_pc_unk, indent+1)}'
		s += f'\n	* name_offset = {self.fmt_member(self.name_offset, indent+1)}'
		s += f'\n	* collider = {self.fmt_member(self.collider, indent+1)}'
		s += f'\n	* zero_extra_zt = {self.fmt_member(self.zero_extra_zt, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
