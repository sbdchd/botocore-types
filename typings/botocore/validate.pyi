from typing import Any

from botocore.exceptions import ParamValidationError as ParamValidationError
from botocore.utils import is_json_value_header as is_json_value_header
from botocore.utils import parse_to_aware_datetime as parse_to_aware_datetime

def validate_parameters(params: Any, shape: Any) -> None: ...
def type_check(valid_types: Any) -> Any: ...
def range_check(
    name: Any, value: Any, shape: Any, error_type: Any, errors: Any
) -> None: ...

class ValidationErrors:
    def __init__(self) -> None: ...
    def has_errors(self) -> Any: ...
    def generate_report(self) -> Any: ...
    def report(self, name: Any, reason: Any, **kwargs: Any) -> None: ...

class ParamValidator:
    def validate(self, params: Any, shape: Any) -> Any: ...

class ParamValidationDecorator:
    def __init__(self, param_validator: Any, serializer: Any) -> None: ...
    def serialize_to_request(self, parameters: Any, operation_model: Any) -> Any: ...
