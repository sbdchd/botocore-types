from typing import Any

from botocore.retries import bucket as bucket
from botocore.retries import standard as standard
from botocore.retries import throttling as throttling

def register_retry_handler(client: Any) -> Any: ...

class ClientRateLimiter:
    def __init__(
        self,
        rate_adjustor: Any,
        rate_clocker: Any,
        token_bucket: Any,
        throttling_detector: Any,
        clock: Any,
    ) -> None: ...
    def on_sending_request(self, request: Any, **kwargs: Any) -> None: ...
    def on_receiving_response(self, **kwargs: Any) -> None: ...

class RateClocker:
    def __init__(
        self, clock: Any, smoothing: Any = ..., time_bucket_range: Any = ...
    ) -> None: ...
    def record(self, amount: int = ...) -> Any: ...
    @property
    def measured_rate(self) -> Any: ...
