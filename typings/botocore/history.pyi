from typing import Any

HISTORY_RECORDER: Any
logger: Any

class BaseHistoryHandler:
    def emit(self, event_type: Any, payload: Any, source: Any) -> None: ...

class HistoryRecorder:
    def __init__(self) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def add_handler(self, handler: Any) -> None: ...
    def record(self, event_type: Any, payload: Any, source: str = ...) -> None: ...

def get_global_history_recorder() -> Any: ...
