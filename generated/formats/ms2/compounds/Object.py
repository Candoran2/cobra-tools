from generated.base_struct import BaseStruct
from generated.formats.base.basic import Ushort


class Object(BaseStruct):

	__name__ = 'Object'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# index into material name array
		self.material_index = 0

		# index into mesh array
		self.mesh_index = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.material_index = 0
		self.mesh_index = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.material_index = Ushort.from_stream(stream, instance.context, 0, None)
		instance.mesh_index = Ushort.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Ushort.to_stream(stream, instance.material_index)
		Ushort.to_stream(stream, instance.mesh_index)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'material_index', Ushort, (0, None), (False, None)
		yield 'mesh_index', Ushort, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'Object [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* material_index = {self.fmt_member(self.material_index, indent+1)}'
		s += f'\n	* mesh_index = {self.fmt_member(self.mesh_index, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
