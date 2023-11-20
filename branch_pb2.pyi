from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["money"]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    money: int
    def __init__(self, money: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["success", "balance"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    balance: int
    def __init__(self, success: bool = ..., balance: _Optional[int] = ...) -> None: ...
