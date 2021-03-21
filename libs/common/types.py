# Base imports
from typing import (
    Any,
    List,
    Optional,
    Tuple,
    Type,
    Union,
)

# Third-party imports
from typeguard import check_type

# Project imports
from libs.common.utils import retrieve_name


NumberType = Union[int, float]

AxisType = List[Optional[NumberType]]

PointType = Tuple[float, Optional[float]]

PointTable2DType = List[PointType]


def is_of_type(value: Any, type_class: Type) -> bool:
    var_name = retrieve_name(value)

    try:
        check_type(var_name, value, type_class)
    except TypeError:
        return False
    else:
        return True
