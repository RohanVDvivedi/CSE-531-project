from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["customer_request_id", "logical_clock", "money"]
    CUSTOMER_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_CLOCK_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    customer_request_id: int
    logical_clock: int
    money: int
    def __init__(self, customer_request_id: _Optional[int] = ..., logical_clock: _Optional[int] = ..., money: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["customer_request_id", "logical_clock", "success", "balance"]
    CUSTOMER_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_CLOCK_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    customer_request_id: int
    logical_clock: int
    success: bool
    balance: int
    def __init__(self, customer_request_id: _Optional[int] = ..., logical_clock: _Optional[int] = ..., success: bool = ..., balance: _Optional[int] = ...) -> None: ...
