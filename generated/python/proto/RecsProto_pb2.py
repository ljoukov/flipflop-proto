# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RecsProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fRecsProto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa3\x01\n\x0fStoryEmbedProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12#\n\nembed_type\x18\x03 \x01(\x0e\x32\x0f.EmbedTypeProto\x12\x12\n\ninput_hash\x18\x04 \x01(\x0c\x12\x15\n\tembedding\x18\x05 \x03(\x02\x42\x02\x10\x01\"i\n\x16StoriesEmbedCacheProto\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x05\x65mbed\x18\x02 \x03(\x0b\x32\x10.StoryEmbedProto*@\n\x0e\x45mbedTypeProto\x12\x16\n\x12\x45MBED_TYPE_UNKNOWN\x10\x00\x12\x16\n\x12\x45MBED_TYPE_ADA_002\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RecsProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STORYEMBEDPROTO.fields_by_name['embedding']._options = None
  _STORYEMBEDPROTO.fields_by_name['embedding']._serialized_options = b'\020\001'
  _EMBEDTYPEPROTO._serialized_start=325
  _EMBEDTYPEPROTO._serialized_end=389
  _STORYEMBEDPROTO._serialized_start=53
  _STORYEMBEDPROTO._serialized_end=216
  _STORIESEMBEDCACHEPROTO._serialized_start=218
  _STORIESEMBEDCACHEPROTO._serialized_end=323
# @@protoc_insertion_point(module_scope)
