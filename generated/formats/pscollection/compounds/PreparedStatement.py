from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer
from generated.formats.pscollection.compounds.Arg import Arg


class PreparedStatement(MemStruct):

	__name__ = 'PreparedStatement'

	_import_path = 'generated.formats.pscollection.compounds.PreparedStatement'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.arg_count = 0
		self.args = ArrayPointer(self.context, self.arg_count, Arg)
		self.statement_name = Pointer(self.context, 0, ZString)
		self.sql_query = Pointer(self.context, 0, ZString)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.arg_count = 0
		self.args = ArrayPointer(self.context, self.arg_count, Arg)
		self.statement_name = Pointer(self.context, 0, ZString)
		self.sql_query = Pointer(self.context, 0, ZString)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.args = ArrayPointer.from_stream(stream, instance.context, instance.arg_count, Arg)
		instance.arg_count = Uint64.from_stream(stream, instance.context, 0, None)
		instance.statement_name = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.sql_query = Pointer.from_stream(stream, instance.context, 0, ZString)
		if not isinstance(instance.args, int):
			instance.args.arg = instance.arg_count
		if not isinstance(instance.statement_name, int):
			instance.statement_name.arg = 0
		if not isinstance(instance.sql_query, int):
			instance.sql_query.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		ArrayPointer.to_stream(stream, instance.args)
		Uint64.to_stream(stream, instance.arg_count)
		Pointer.to_stream(stream, instance.statement_name)
		Pointer.to_stream(stream, instance.sql_query)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'args', ArrayPointer, (instance.arg_count, Arg), (False, None)
		yield 'arg_count', Uint64, (0, None), (True, 0)
		yield 'statement_name', Pointer, (0, ZString), (False, None)
		yield 'sql_query', Pointer, (0, ZString), (False, None)

	def get_info_str(self, indent=0):
		return f'PreparedStatement [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* args = {self.fmt_member(self.args, indent+1)}'
		s += f'\n	* arg_count = {self.fmt_member(self.arg_count, indent+1)}'
		s += f'\n	* statement_name = {self.fmt_member(self.statement_name, indent+1)}'
		s += f'\n	* sql_query = {self.fmt_member(self.sql_query, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
