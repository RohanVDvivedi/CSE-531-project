# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: branch.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x62ranch.proto\"\'\n\x07Request\x12\x12\n\x05money\x18\x04 \x01(\x05H\x00\x88\x01\x01\x42\x08\n\x06_money\"=\n\x08Response\x12\x0f\n\x07success\x18\x03 \x01(\x08\x12\x14\n\x07\x62\x61lance\x18\x04 \x01(\x05H\x00\x88\x01\x01\x42\n\n\x08_balance2\xc6\x01\n\x06\x42ranch\x12\x1e\n\x05Query\x12\x08.Request\x1a\t.Response\"\x00\x12!\n\x08Withdraw\x12\x08.Request\x1a\t.Response\"\x00\x12 \n\x07\x44\x65posit\x12\x08.Request\x1a\t.Response\"\x00\x12+\n\x12Propogate_Withdraw\x12\x08.Request\x1a\t.Response\"\x00\x12*\n\x11Propogate_Deposit\x12\x08.Request\x1a\t.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'branch_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=16
  _globals['_REQUEST']._serialized_end=55
  _globals['_RESPONSE']._serialized_start=57
  _globals['_RESPONSE']._serialized_end=118
  _globals['_BRANCH']._serialized_start=121
  _globals['_BRANCH']._serialized_end=319
# @@protoc_insertion_point(module_scope)
