from datetime import date, datetime
from decimal import Decimal
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Sequence, Set, Tuple, Type, Union, overload
from uuid import UUID

from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.utils import CursorWrapper
from django.db.models.base import Model
from django.db.models.expressions import BaseExpression, Expression
from django.db.models.sql.query import Query
from django.db.models.sql.subqueries import AggregateQuery, DeleteQuery, InsertQuery, UpdateQuery
from typing_extensions import Literal

_ParamT = Union[str, int]
_ParamsT = List[_ParamT]
_AsSqlType = Tuple[str, _ParamsT]

class SQLCompiler:
    query: Query = ...
    connection: BaseDatabaseWrapper = ...
    using: Optional[str] = ...
    quote_cache: Any = ...
    select: Any = ...
    annotation_col_map: Any = ...
    klass_info: Any = ...
    ordering_parts: Any = ...
    def __init__(self, query: Query, connection: BaseDatabaseWrapper, using: Optional[str]) -> None: ...
    col_count: Optional[int] = ...
    def setup_query(self) -> None: ...
    has_extra_select: Any = ...
    def pre_sql_setup(
        self,
    ) -> Tuple[
        List[Tuple[Expression, _AsSqlType, None]],
        List[Tuple[Expression, Tuple[str, _ParamsT, bool]]],
        List[_AsSqlType],
    ]: ...
    def get_group_by(
        self,
        select: List[Tuple[BaseExpression, _AsSqlType, Optional[str]]],
        order_by: List[Tuple[Expression, Tuple[str, _ParamsT, bool]]],
    ) -> List[_AsSqlType]: ...
    def collapse_group_by(
        self, expressions: List[Expression], having: Union[List[Expression], Tuple]
    ) -> List[Expression]: ...
    def get_select(
        self,
    ) -> Tuple[List[Tuple[Expression, _AsSqlType, Optional[str]]], Optional[Dict[str, Any]], Dict[str, int],]: ...
    def get_order_by(self) -> List[Tuple[Expression, Tuple[str, _ParamsT, bool]]]: ...
    def get_extra_select(
        self,
        order_by: List[Tuple[Expression, Tuple[str, _ParamsT, bool]]],
        select: List[Tuple[Expression, _AsSqlType, Optional[str]]],
    ) -> List[Tuple[Expression, _AsSqlType, None]]: ...
    def quote_name_unless_alias(self, name: str) -> str: ...
    def compile(self, node: BaseExpression) -> _AsSqlType: ...
    def get_combinator_sql(self, combinator: str, all: bool) -> Tuple[List[str], Union[List[int], List[str]]]: ...
    def as_sql(self, with_limits: bool = ..., with_col_aliases: bool = ...) -> _AsSqlType: ...
    def get_default_columns(
        self, start_alias: Optional[str] = ..., opts: Optional[Any] = ..., from_parent: Optional[Type[Model]] = ...
    ) -> List[Expression]: ...
    def get_distinct(self) -> Tuple[List[Any], List[Any]]: ...
    def find_ordering_name(
        self,
        name: str,
        opts: Any,
        alias: Optional[str] = ...,
        default_order: str = ...,
        already_seen: Optional[Set[Tuple[Optional[Tuple[Tuple[str, str]]], Tuple[Tuple[str, str]]]]] = ...,
    ) -> List[Tuple[Expression, bool]]: ...
    def get_from_clause(self) -> Tuple[List[str], _ParamsT]: ...
    def get_related_selections(
        self,
        select: List[Tuple[Expression, Optional[str]]],
        opts: Optional[Any] = ...,
        root_alias: Optional[str] = ...,
        cur_depth: int = ...,
        requested: Optional[Dict[str, Dict[str, Dict[str, Dict[Any, Any]]]]] = ...,
        restricted: Optional[bool] = ...,
    ) -> List[Dict[str, Any]]: ...
    def get_select_for_update_of_arguments(self) -> List[Any]: ...
    def deferred_to_columns(self) -> Dict[Type[Model], Set[str]]: ...
    def get_converters(self, expressions: List[Expression]) -> Dict[int, Tuple[List[Callable], Expression]]: ...
    def apply_converters(
        self, rows: Iterable[Iterable[Any]], converters: Dict[int, Tuple[List[Callable], Expression]]
    ) -> Iterator[List[Union[None, date, datetime, float, Decimal, UUID, bytes, str]]]: ...
    def results_iter(
        self,
        results: Optional[Iterable[List[Sequence[Any]]]] = ...,
        tuple_expected: bool = ...,
        chunked_fetch: bool = ...,
        chunk_size: int = ...,
    ) -> Iterator[Sequence[Any]]: ...
    def has_results(self) -> bool: ...
    @overload
    def execute_sql(  # type: ignore
        self, result_type: Literal["cursor"] = ..., chunked_fetch: bool = ..., chunk_size: int = ...
    ) -> CursorWrapper: ...
    @overload
    def execute_sql(
        self, result_type: Optional[Literal["no results"]] = ..., chunked_fetch: bool = ..., chunk_size: int = ...
    ) -> None: ...
    @overload
    def execute_sql(  # type: ignore
        self, result_type: Literal["single"] = ..., chunked_fetch: bool = ..., chunk_size: int = ...
    ) -> Optional[Iterable[Sequence[Any]]]: ...
    @overload
    def execute_sql(
        self, result_type: Literal["multi"] = ..., chunked_fetch: bool = ..., chunk_size: int = ...
    ) -> Optional[Iterable[List[Sequence[Any]]]]: ...
    def as_subquery_condition(self, alias: str, columns: List[str], compiler: SQLCompiler) -> _AsSqlType: ...
    def explain_query(self) -> Iterator[str]: ...

class SQLInsertCompiler(SQLCompiler):
    query: InsertQuery
    returning_fields: Optional[Sequence[Any]] = ...
    returning_params: Sequence[Any] = ...
    def field_as_sql(self, field: Any, val: Any) -> _AsSqlType: ...
    def prepare_value(self, field: Any, value: Any) -> Any: ...
    def pre_save_val(self, field: Any, obj: Any) -> Any: ...
    def assemble_as_sql(self, fields: Any, value_rows: Any) -> Tuple[List[List[str]], List[List[Any]]]: ...
    def as_sql(self) -> List[_AsSqlType]: ...  # type: ignore
    def execute_sql(  # type: ignore
        self, returning_fields: Optional[Sequence[str]] = ...
    ) -> List[Tuple[Any]]: ...  # 1-tuple

class SQLDeleteCompiler(SQLCompiler):
    query: DeleteQuery
    @property
    def single_alias(self) -> bool: ...
    @property
    def contains_self_reference_subquery(self) -> bool: ...
    def as_sql(self) -> _AsSqlType: ...  # type: ignore

class SQLUpdateCompiler(SQLCompiler):
    query: UpdateQuery
    def as_sql(self) -> _AsSqlType: ...  # type: ignore
    def execute_sql(self, result_type: Literal["cursor", "no results"]) -> int: ...  # type: ignore
    def pre_sql_setup(self) -> None: ...  # type: ignore

class SQLAggregateCompiler(SQLCompiler):
    query: AggregateQuery
    col_count: int = ...
    def as_sql(self) -> _AsSqlType: ...  # type: ignore

def cursor_iter(
    cursor: CursorWrapper, sentinel: Any, col_count: Optional[int], itersize: int
) -> Iterator[List[Sequence[Any]]]: ...
