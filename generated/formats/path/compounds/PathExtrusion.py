import generated.formats.base.basic
from generated.formats.base.basic import Float
from generated.formats.ovl_base.basic import Bool
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class PathExtrusion(MemStruct):

	__name__ = PathExtrusion

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.unk_float_1 = 0.0
		self.unk_float_2 = 0.0
		self.is_kerb = False
		self.is_not_ground = True
		self.model = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.post_model = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.endcap_model = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.unk_float_1 = 0.0
		self.unk_float_2 = 0.0
		self.is_kerb = False
		self.is_not_ground = True
		self.model = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.post_model = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.endcap_model = Pointer(self.context, 0, generated.formats.base.basic.ZString)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.model = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.post_model = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.endcap_model = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.unk_float_1 = Float.from_stream(stream, instance.context, 0, None)
		instance.unk_float_2 = Float.from_stream(stream, instance.context, 0, None)
		instance.is_kerb = Bool.from_stream(stream, instance.context, 0, None)
		instance.is_not_ground = Bool.from_stream(stream, instance.context, 0, None)
		if not isinstance(instance.model, int):
			instance.model.arg = 0
		if not isinstance(instance.post_model, int):
			instance.post_model.arg = 0
		if not isinstance(instance.endcap_model, int):
			instance.endcap_model.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.model)
		Pointer.to_stream(stream, instance.post_model)
		Pointer.to_stream(stream, instance.endcap_model)
		Float.to_stream(stream, instance.unk_float_1)
		Float.to_stream(stream, instance.unk_float_2)
		Bool.to_stream(stream, instance.is_kerb)
		Bool.to_stream(stream, instance.is_not_ground)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'model', Pointer, (0, generated.formats.base.basic.ZString), (False, None)
		yield 'post_model', Pointer, (0, generated.formats.base.basic.ZString), (False, None)
		yield 'endcap_model', Pointer, (0, generated.formats.base.basic.ZString), (False, None)
		yield 'unk_float_1', Float, (0, None), (False, None)
		yield 'unk_float_2', Float, (0, None), (False, None)
		yield 'is_kerb', Bool, (0, None), (False, None)
		yield 'is_not_ground', Bool, (0, None), (False, True)

	def get_info_str(self, indent=0):
		return f'PathExtrusion [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* model = {self.fmt_member(self.model, indent+1)}'
		s += f'\n	* post_model = {self.fmt_member(self.post_model, indent+1)}'
		s += f'\n	* endcap_model = {self.fmt_member(self.endcap_model, indent+1)}'
		s += f'\n	* unk_float_1 = {self.fmt_member(self.unk_float_1, indent+1)}'
		s += f'\n	* unk_float_2 = {self.fmt_member(self.unk_float_2, indent+1)}'
		s += f'\n	* is_kerb = {self.fmt_member(self.is_kerb, indent+1)}'
		s += f'\n	* is_not_ground = {self.fmt_member(self.is_not_ground, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
