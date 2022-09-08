import numpy
from generated.array import Array
from generated.formats.base.basic import Float
from generated.formats.base.basic import Uint
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class WsmHeader(MemStruct):

	"""
	56 bytes for JWE2
	"""

	__name__ = 'WsmHeader'

	_import_path = 'generated.formats.wsm.compounds.WsmHeader'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.duration = 0.0

		# likely
		self.frame_count = 0

		# unk
		self.unknowns = Array(self.context, 0, None, (0,), Float)
		self.locs = ArrayPointer(self.context, self.frame_count, WsmHeader._import_path_map["generated.formats.wsm.compounds.Vector3"])
		self.quats = ArrayPointer(self.context, self.frame_count, WsmHeader._import_path_map["generated.formats.wsm.compounds.Vector4"])
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.duration = 0.0
		self.frame_count = 0
		self.unknowns = numpy.zeros((8,), dtype=numpy.dtype('float32'))
		self.locs = ArrayPointer(self.context, self.frame_count, WsmHeader._import_path_map["generated.formats.wsm.compounds.Vector3"])
		self.quats = ArrayPointer(self.context, self.frame_count, WsmHeader._import_path_map["generated.formats.wsm.compounds.Vector4"])

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.duration = Float.from_stream(stream, instance.context, 0, None)
		instance.frame_count = Uint.from_stream(stream, instance.context, 0, None)
		instance.unknowns = Array.from_stream(stream, instance.context, 0, None, (8,), Float)
		instance.locs = ArrayPointer.from_stream(stream, instance.context, instance.frame_count, WsmHeader._import_path_map["generated.formats.wsm.compounds.Vector3"])
		instance.quats = ArrayPointer.from_stream(stream, instance.context, instance.frame_count, WsmHeader._import_path_map["generated.formats.wsm.compounds.Vector4"])
		if not isinstance(instance.locs, int):
			instance.locs.arg = instance.frame_count
		if not isinstance(instance.quats, int):
			instance.quats.arg = instance.frame_count

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Float.to_stream(stream, instance.duration)
		Uint.to_stream(stream, instance.frame_count)
		Array.to_stream(stream, instance.unknowns, Float)
		ArrayPointer.to_stream(stream, instance.locs)
		ArrayPointer.to_stream(stream, instance.quats)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'duration', Float, (0, None), (False, None)
		yield 'frame_count', Uint, (0, None), (False, None)
		yield 'unknowns', Array, (0, None, (8,), Float), (False, None)
		yield 'locs', ArrayPointer, (instance.frame_count, WsmHeader._import_path_map["generated.formats.wsm.compounds.Vector3"]), (False, None)
		yield 'quats', ArrayPointer, (instance.frame_count, WsmHeader._import_path_map["generated.formats.wsm.compounds.Vector4"]), (False, None)

	def get_info_str(self, indent=0):
		return f'WsmHeader [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
