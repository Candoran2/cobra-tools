from generated.formats.base.basic import Float
from generated.formats.habitatboundary.structs.HbPostSize import HbPostSize
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class HbPhysicsOffsets(MemStruct):

	"""
	Physics values for barriers.
	"""

	__name__ = 'HbPhysicsOffsets'

	_import_path = 'generated.formats.habitatboundary.structs.HbPhysicsOffsets'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# Wall thickness. Affects navcut, selection, and climb nav width. Must be under a certain value or it crashes.
		self.thickness = 0.0
		self.post_size = HbPostSize(self.context, 0, None)

		# Wall size above wall_height. Affects navcut, selection, and climb nav height.
		self.wall_pad_top = 0.0

		# Distance between post center and start of wall. Larger values create a visual and nav gap between the post and wall segment.
		self.wall_post_gap = 0.0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.thickness = 0.0
		self.post_size = HbPostSize(self.context, 0, None)
		self.wall_pad_top = 0.0
		self.wall_post_gap = 0.0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.thickness = Float.from_stream(stream, instance.context, 0, None)
		instance.post_size = HbPostSize.from_stream(stream, instance.context, 0, None)
		instance.wall_pad_top = Float.from_stream(stream, instance.context, 0, None)
		instance.wall_post_gap = Float.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Float.to_stream(stream, instance.thickness)
		HbPostSize.to_stream(stream, instance.post_size)
		Float.to_stream(stream, instance.wall_pad_top)
		Float.to_stream(stream, instance.wall_post_gap)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'thickness', Float, (0, None), (False, None)
		yield 'post_size', HbPostSize, (0, None), (False, None)
		yield 'wall_pad_top', Float, (0, None), (False, None)
		yield 'wall_post_gap', Float, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'HbPhysicsOffsets [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* thickness = {self.fmt_member(self.thickness, indent+1)}'
		s += f'\n	* post_size = {self.fmt_member(self.post_size, indent+1)}'
		s += f'\n	* wall_pad_top = {self.fmt_member(self.wall_pad_top, indent+1)}'
		s += f'\n	* wall_post_gap = {self.fmt_member(self.wall_post_gap, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
