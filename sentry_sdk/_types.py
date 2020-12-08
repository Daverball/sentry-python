try:
    from typing import TYPE_CHECKING as MYPY
except ImportError:
    MYPY = False


if MYPY:
    from numbers import Real
    from types import TracebackType
    from typing import Any
    from typing import Callable
    from typing import Dict
    from typing import Optional
    from typing import Tuple
    from typing import Type
    from typing import Union
    from typing_extensions import Literal

    ExcInfo = Tuple[
        Optional[Type[BaseException]], Optional[BaseException], Optional[TracebackType]
    ]

    Event = Dict[str, Any]
    Hint = Dict[str, Any]

    Breadcrumb = Dict[str, Any]
    BreadcrumbHint = Dict[str, Any]

    SamplingContext = Dict[str, Any]

    EventProcessor = Callable[[Event, Hint], Optional[Event]]
    ErrorProcessor = Callable[[Event, ExcInfo], Optional[Event]]
    BreadcrumbProcessor = Callable[[Breadcrumb, BreadcrumbHint], Optional[Breadcrumb]]

    TracesSampler = Callable[[SamplingContext], Union[Real, bool]]

    # https://github.com/python/mypy/issues/5710
    NotImplementedType = Any

    EventDataCategory = Literal[
        "default", "error", "crash", "transaction", "security", "attachment", "session"
    ]
    SessionStatus = Literal["ok", "exited", "crashed", "abnormal"]
    EndpointType = Literal["store", "envelope"]

    FlushCallback = Callable[[int, float], None]
