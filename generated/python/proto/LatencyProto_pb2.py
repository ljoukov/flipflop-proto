# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LatencyProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12LatencyProto.proto\x1a\x1egoogle/protobuf/duration.proto\"\x90\x01\n\x0eLatenciesProto\x12\x31\n\tlatencies\x18\x01 \x03(\x0b\x32\x1e.LatenciesProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'LatencyProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LATENCIESPROTO_LATENCIESENTRY._options = None
  _LATENCIESPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _LATENCIESPROTO._serialized_start=55
  _LATENCIESPROTO._serialized_end=199
  _LATENCIESPROTO_LATENCIESENTRY._serialized_start=124
  _LATENCIESPROTO_LATENCIESENTRY._serialized_end=199
# @@protoc_insertion_point(module_scope)
