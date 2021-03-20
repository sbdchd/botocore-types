from typing import Any, Optional

from botocore.compat import ETree as ETree
from botocore.compat import XMLParseError as XMLParseError
from botocore.eventstream import EventStream as EventStream
from botocore.eventstream import NoInitialResponseError as NoInitialResponseError
from botocore.utils import is_json_value_header as is_json_value_header
from botocore.utils import lowercase_dict as lowercase_dict
from botocore.utils import merge_dicts as merge_dicts
from botocore.utils import parse_timestamp as parse_timestamp

DEFAULT_TIMESTAMP_PARSER = parse_timestamp

class ResponseParserFactory:
    def __init__(self) -> None: ...
    def set_parser_defaults(self, **kwargs: Any) -> None: ...
    def create_parser(self, protocol_name: Any) -> Any: ...

def create_parser(protocol: Any) -> Any: ...

class ResponseParserError(Exception): ...

class ResponseParser:
    DEFAULT_ENCODING: str = ...
    EVENT_STREAM_PARSER_CLS: Any = ...
    def __init__(
        self, timestamp_parser: Optional[Any] = ..., blob_parser: Optional[Any] = ...
    ) -> None: ...
    def parse(self, response: Any, shape: Any) -> Any: ...

class BaseXMLResponseParser(ResponseParser):
    def __init__(
        self, timestamp_parser: Optional[Any] = ..., blob_parser: Optional[Any] = ...
    ) -> None: ...

class QueryParser(BaseXMLResponseParser): ...
class EC2QueryParser(QueryParser): ...
class BaseJSONParser(ResponseParser): ...
class BaseEventStreamParser(ResponseParser): ...
class EventStreamJSONParser(BaseEventStreamParser, BaseJSONParser): ...
class EventStreamXMLParser(BaseEventStreamParser, BaseXMLResponseParser): ...

class JSONParser(BaseJSONParser):
    EVENT_STREAM_PARSER_CLS: Any = ...

class BaseRestParser(ResponseParser): ...

class RestJSONParser(BaseRestParser, BaseJSONParser):
    EVENT_STREAM_PARSER_CLS: Any = ...

class RestXMLParser(BaseRestParser, BaseXMLResponseParser):
    EVENT_STREAM_PARSER_CLS: Any = ...

PROTOCOL_PARSERS: Any
