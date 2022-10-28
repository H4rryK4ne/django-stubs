from datetime import date
from datetime import datetime as builtin_datetime
from datetime import time as builtin_time
from typing import Any, Optional, Pattern, Union

from django.utils.timezone import _TzInfoT
from typing_extensions import Literal

re_formatchars: Pattern[str]
re_escaped: Pattern[str]

class Formatter:
    def format(self, formatstr: str) -> str: ...

class TimeFormat(Formatter):
    data: Union[builtin_datetime, builtin_time] = ...
    timezone: Optional[_TzInfoT] = ...
    def __init__(self, obj: Union[builtin_datetime, builtin_time]) -> None: ...
    def a(self) -> str: ...
    def A(self) -> str: ...
    def e(self) -> str: ...
    def f(self) -> Union[int, str]: ...
    def g(self) -> int: ...
    def G(self) -> int: ...
    def h(self) -> str: ...
    def H(self) -> str: ...
    def i(self) -> str: ...
    def O(self) -> str: ...
    def P(self) -> str: ...
    def s(self) -> str: ...
    def T(self) -> str: ...
    def u(self) -> str: ...
    def Z(self) -> Union[int, Literal[""]]: ...

class DateFormat(TimeFormat):
    data: Union[builtin_datetime, date, builtin_time]  # type: ignore
    timezone: Optional[_TzInfoT]
    year_days: Any = ...
    def __init__(self, obj: Union[builtin_datetime, builtin_time, date]) -> None: ...
    def b(self) -> str: ...
    def c(self) -> str: ...
    def d(self) -> str: ...
    def D(self) -> str: ...
    def E(self) -> str: ...
    def F(self) -> str: ...
    def I(self) -> str: ...
    def j(self) -> int: ...
    def l(self) -> str: ...
    def L(self) -> bool: ...
    def m(self) -> str: ...
    def M(self) -> str: ...
    def n(self) -> int: ...
    def N(self) -> str: ...
    def o(self) -> int: ...
    def r(self) -> str: ...
    def S(self) -> str: ...
    def t(self) -> str: ...
    def U(self) -> int: ...
    def w(self) -> int: ...
    def W(self) -> int: ...
    def y(self) -> str: ...
    def Y(self) -> int: ...
    def z(self) -> int: ...

def format(value: Union[builtin_datetime, date, builtin_time], format_string: str) -> str: ...
def time_format(value: Union[builtin_datetime, builtin_time], format_string: str) -> str: ...
