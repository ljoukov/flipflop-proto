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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fTaskProto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd1\x01\n\tTaskProto\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x10generate_podcast\x18\n \x01(\x0b\x32\x19.GeneratePodcastTaskProtoH\x00\x12\x44\n\x14generate_suggestions\x18\x0b \x01(\x0b\x32$.GeneratePodcastSuggestionsTaskProtoH\x00\x42\x06\n\x04type\"?\n\x18GeneratePodcastTaskProto\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\npodcast_id\x18\x02 \x01(\t\"6\n#GeneratePodcastSuggestionsTaskProto\x12\x0f\n\x07user_id\x18\x01 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TaskProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TASKPROTO._serialized_start=53
  _TASKPROTO._serialized_end=262
  _GENERATEPODCASTTASKPROTO._serialized_start=264
  _GENERATEPODCASTTASKPROTO._serialized_end=327
  _GENERATEPODCASTSUGGESTIONSTASKPROTO._serialized_start=329
  _GENERATEPODCASTSUGGESTIONSTASKPROTO._serialized_end=383
# @@protoc_insertion_point(module_scope)
