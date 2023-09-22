from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["id", "interface", "money"]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    id: int
    interface: str
    money: int
    def __init__(self, id: _Optional[int] = ..., interface: _Optional[str] = ..., money: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["interface", "success", "balance"]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    interface: str
    success: str
    balance: int
    def __init__(self, interface: _Optional[str] = ..., success: _Optional[str] = ..., balance: _Optional[int] = ...) -> None: ...
