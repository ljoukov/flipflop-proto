# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TaskProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import PodcastProto_pb2 as PodcastProto__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fTaskProto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x12PodcastProto.proto\"\x87\x01\n\tTaskProto\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x0e\x63reate_podcast\x18\n \x01(\x0b\x32\x17.CreatePodcastTaskProtoH\x00\x42\x06\n\x04type\"X\n\x16\x43reatePodcastTaskProto\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12-\n\x07request\x18\x02 \x01(\x0b\x32\x1c.GeneratePodcastRequestProtob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TaskProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TASKPROTO._serialized_start=73
  _TASKPROTO._serialized_end=208
  _CREATEPODCASTTASKPROTO._serialized_start=210
  _CREATEPODCASTTASKPROTO._serialized_end=298
# @@protoc_insertion_point(module_scope)
