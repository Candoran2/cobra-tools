from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint


class StreamEntry(BaseStruct):

	"""
	Description of one streamed file instance. One for every file stored in an ovs.
	Links the main pointers of a streamed file to its user, eg. a texturestream to a tex file.
	--These appear sorted in the order of sizedstr entries per ovs.-- only true for lod0, not lod1
	the order does not seem to be consistent
	interestingly, the order of root_entry entries per ovs is consistent with decreasing pool offset
	"""

	__name__ = 'StreamEntry'

	_import_path = 'generated.formats.ovl.compounds.StreamEntry'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# offset to the stream's root_entry pointer inside the flattened mempools
		self.stream_offset = 0

		# offset to the user file's root_entry pointer (in STATIC) inside the flattened mempools
		self.file_offset = 0
		self.zero = 0
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'stream_offset', Uint, (0, None), (False, None)
		yield 'file_offset', Uint, (0, None), (False, None)
		yield 'zero', Uint, (0, None), (False, None)
