# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: AuthProto.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'AuthProto.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x41uthProto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"}\n\rUserAuthProto\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\x12.\n\nexpires_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rrefresh_token\x18\x04 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'AuthProto_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERAUTHPROTO']._serialized_start=52
  _globals['_USERAUTHPROTO']._serialized_end=177
# @@protoc_insertion_point(module_scope)
