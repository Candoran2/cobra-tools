from generated.formats.base.enums import UshortEnum


class SubCurveType(UshortEnum):

	__name__ = 'SubCurveType'
	CONSTANT = 0
	LINEAR = 1
	POLYNOMIAL = 2
	EXPONENTIAL = 3
	S_CURVE = 4
	BEZIER = 5
