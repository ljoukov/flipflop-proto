# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: TaskProto.proto
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
    'TaskProto.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fTaskProto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x91\x03\n\tTaskProto\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x10generate_podcast\x18\n \x01(\x0b\x32\x19.GeneratePodcastTaskProtoH\x00\x12\x38\n\x0egenerate_story\x18\x0b \x01(\x0b\x32\x1e.GeneratePodcastStoryTaskProtoH\x00\x12@\n\x12\x63reate_suggestions\x18\x0c \x01(\x0b\x32\".CreatePodcastSuggestionsTaskProtoH\x00\x12\x44\n\x14generate_suggestions\x18\r \x01(\x0b\x32$.GeneratePodcastSuggestionsTaskProtoH\x00\x12\x42\n\x13publish_suggestions\x18\x0e \x01(\x0b\x32#.PublishPodcastSuggestionsTaskProtoH\x00\x42\x06\n\x04type\".\n\x18GeneratePodcastTaskProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"1\n\x1dGeneratePodcastStoryTaskProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\"{\n!CreatePodcastSuggestionsTaskProto\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\"\n\x1aignore_partially_generated\x18\x02 \x01(\x08\x12!\n\x19ignore_recently_generated\x18\x03 \x01(\x08\"=\n#GeneratePodcastSuggestionsTaskProto\x12\x16\n\x0esuggestions_id\x18\x01 \x01(\t\"<\n\"PublishPodcastSuggestionsTaskProto\x12\x16\n\x0esuggestions_id\x18\x01 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TaskProto_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TASKPROTO']._serialized_start=53
  _globals['_TASKPROTO']._serialized_end=454
  _globals['_GENERATEPODCASTTASKPROTO']._serialized_start=456
  _globals['_GENERATEPODCASTTASKPROTO']._serialized_end=502
  _globals['_GENERATEPODCASTSTORYTASKPROTO']._serialized_start=504
  _globals['_GENERATEPODCASTSTORYTASKPROTO']._serialized_end=553
  _globals['_CREATEPODCASTSUGGESTIONSTASKPROTO']._serialized_start=555
  _globals['_CREATEPODCASTSUGGESTIONSTASKPROTO']._serialized_end=678
  _globals['_GENERATEPODCASTSUGGESTIONSTASKPROTO']._serialized_start=680
  _globals['_GENERATEPODCASTSUGGESTIONSTASKPROTO']._serialized_end=741
  _globals['_PUBLISHPODCASTSUGGESTIONSTASKPROTO']._serialized_start=743
  _globals['_PUBLISHPODCASTSUGGESTIONSTASKPROTO']._serialized_end=803
# @@protoc_insertion_point(module_scope)
