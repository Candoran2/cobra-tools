from generated.formats.base.basic import Float
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Uint64
from generated.formats.path.compounds.SupportAttach import SupportAttach


class SupportAttachExtra(SupportAttach):

	__name__ = SupportAttachExtra

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.unk_float_1 = 0.0
		self.unk_int_3 = 0
		self.padding = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.unk_float_1 = 0.0
		self.unk_int_3 = 0
		self.padding = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.unk_float_1 = Float.from_stream(stream, instance.context, 0, None)
		instance.unk_int_3 = Uint.from_stream(stream, instance.context, 0, None)
		instance.padding = Uint64.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Float.to_stream(stream, instance.unk_float_1)
		Uint.to_stream(stream, instance.unk_int_3)
		Uint64.to_stream(stream, instance.padding)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'unk_float_1', Float, (0, None), (False, None)
		yield 'unk_int_3', Uint, (0, None), (False, None)
		yield 'padding', Uint64, (0, None), (True, 0)

	def get_info_str(self, indent=0):
		return f'SupportAttachExtra [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* unk_float_1 = {self.fmt_member(self.unk_float_1, indent+1)}'
		s += f'\n	* unk_int_3 = {self.fmt_member(self.unk_int_3, indent+1)}'
		s += f'\n	* padding = {self.fmt_member(self.padding, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
