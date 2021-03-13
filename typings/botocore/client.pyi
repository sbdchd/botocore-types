from typing import Any, Dict, Optional, Union

from botocore import UNSIGNED as UNSIGNED
from botocore import waiter as waiter
from botocore import xform_name as xform_name
from botocore.args import ClientArgsCreator as ClientArgsCreator
from botocore.auth import AUTH_TYPE_MAPS as AUTH_TYPE_MAPS
from botocore.awsrequest import prepare_request_dict as prepare_request_dict
from botocore.config import Config as Config
from botocore.discovery import EndpointDiscoveryHandler as EndpointDiscoveryHandler
from botocore.discovery import EndpointDiscoveryManager as EndpointDiscoveryManager
from botocore.discovery import (
    block_endpoint_discovery_required_operations as block_endpoint_discovery_required_operations,
)
from botocore.exceptions import ClientError as ClientError
from botocore.exceptions import DataNotFoundError as DataNotFoundError
from botocore.exceptions import (
    InvalidEndpointDiscoveryConfigurationError as InvalidEndpointDiscoveryConfigurationError,
)
from botocore.exceptions import OperationNotPageableError as OperationNotPageableError
from botocore.exceptions import (
    UnknownSignatureVersionError as UnknownSignatureVersionError,
)
from botocore.history import get_global_history_recorder as get_global_history_recorder
from botocore.hooks import first_non_none_response as first_non_none_response
from botocore.model import ServiceModel as ServiceModel
from botocore.paginate import Paginator as Paginator
from botocore.retries import adaptive as adaptive
from botocore.retries import standard as standard
from botocore.utils import CachedProperty as CachedProperty
from botocore.utils import S3ArnParamHandler as S3ArnParamHandler
from botocore.utils import S3ControlArnParamHandler as S3ControlArnParamHandler
from botocore.utils import S3ControlEndpointSetter as S3ControlEndpointSetter
from botocore.utils import S3EndpointSetter as S3EndpointSetter
from botocore.utils import S3RegionRedirector as S3RegionRedirector
from botocore.utils import ensure_boolean as ensure_boolean
from botocore.utils import get_service_module_name as get_service_module_name

class ClientCreator:
    def __init__(
        self,
        loader: Any,
        endpoint_resolver: Any,
        user_agent: str,
        event_emitter: Any,
        retry_handler_factory: Any,
        retry_config_translator: Any,
        response_parser_factory: Optional[Any] = ...,
        exceptions_factory: Optional[Any] = ...,
        config_store: Optional[Any] = ...,
    ) -> None: ...
    def create_client(
        self,
        service_name: str,
        region_name: str,
        is_secure: bool = ...,
        endpoint_url: Optional[str] = ...,
        verify: Optional[Union[str, bool]] = ...,
        credentials: Optional[Any] = ...,
        scoped_config: Optional[Any] = ...,
        api_version: Optional[str] = ...,
        client_config: Optional[Config] = ...,
    ) -> None: ...
    def create_client_class(
        self, service_name: str, api_version: Optional[Any] = ...
    ) -> None: ...

class ClientEndpointBridge:
    DEFAULT_ENDPOINT: str = ...
    service_signing_name: Any = ...
    endpoint_resolver: Any = ...
    scoped_config: Any = ...
    client_config: Any = ...
    default_endpoint: Any = ...
    def __init__(
        self,
        endpoint_resolver: Any,
        scoped_config: Optional[Any] = ...,
        client_config: Optional[Any] = ...,
        default_endpoint: Optional[str] = ...,
        service_signing_name: Optional[Any] = ...,
    ) -> None: ...
    def resolve(
        self,
        service_name: Any,
        region_name: Optional[str] = ...,
        endpoint_url: Optional[str] = ...,
        is_secure: bool = ...,
    ) -> None: ...

class BaseClient:
    meta: ClientMeta
    def __init__(
        self,
        serializer: Any,
        endpoint: str,
        response_parser: Any,
        event_emitter: Any,
        request_signer: Any,
        service_model: Any,
        loader: Any,
        client_config: Config,
        partition: Any,
        exceptions_factory: Any,
    ) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def get_paginator(self, operation_name: str) -> Paginator: ...
    def can_paginate(self, operation_name: str) -> bool: ...
    def get_waiter(self, waiter_name: str) -> waiter.Waiter: ...
    def waiter_names(self) -> None: ...
    @property
    def exceptions(self) -> Any: ...

class ClientMeta:
    events: Any = ...
    def __init__(
        self,
        events: Any,
        client_config: Config,
        endpoint_url: str,
        service_model: Any,
        method_to_api_mapping: Dict[str, str],
        partition: Any,
    ) -> None: ...
    @property
    def service_model(self) -> Any: ...
    @property
    def region_name(self) -> str: ...
    @property
    def endpoint_url(self) -> str: ...
    @property
    def config(self) -> Any: ...
    @property
    def method_to_api_mapping(self) -> Dict[str, str]: ...
    @property
    def partition(self) -> str: ...
