# Base imports
import inspect
from typing import (
    Any,
    List,
    Optional,
)


def retrieve_name(var: Any) -> List[Optional[str]]:
    callers_local_vars = inspect. \
        currentframe() \
            .f_back \
            .f_locals \
            .items()

    return [
        var_name for var_name, var_val in callers_local_vars
        if var_val is var
    ]
