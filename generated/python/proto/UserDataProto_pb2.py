# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UserDataProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13UserDataProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"k\n\x12StoryUserDataProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12\x34\n\x10last_modified_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05liked\x18\x03 \x01(\x08\"\x19\n\x17GetUserDataRequestProto\"E\n\x18GetUserDataResponseProto\x12)\n\x0cstories_data\x18\x01 \x03(\x0b\x32\x13.StoryUserDataProto\"S\n\x13UserApiRequestProto\x12\x31\n\rget_user_data\x18\x01 \x01(\x0b\x32\x18.GetUserDataRequestProtoH\x00\x42\t\n\x07request\"\xdc\x01\n\x14UserApiResponseProto\x12\x32\n\rget_user_data\x18\x01 \x01(\x0b\x32\x19.GetUserDataResponseProtoH\x00\x12\x37\n\tlatencies\x18\x05 \x03(\x0b\x32$.UserApiResponseProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\n\n\x08responseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'UserDataProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERAPIRESPONSEPROTO_LATENCIESENTRY._options = None
  _USERAPIRESPONSEPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _STORYUSERDATAPROTO._serialized_start=88
  _STORYUSERDATAPROTO._serialized_end=195
  _GETUSERDATAREQUESTPROTO._serialized_start=197
  _GETUSERDATAREQUESTPROTO._serialized_end=222
  _GETUSERDATARESPONSEPROTO._serialized_start=224
  _GETUSERDATARESPONSEPROTO._serialized_end=293
  _USERAPIREQUESTPROTO._serialized_start=295
  _USERAPIREQUESTPROTO._serialized_end=378
  _USERAPIRESPONSEPROTO._serialized_start=381
  _USERAPIRESPONSEPROTO._serialized_end=601
  _USERAPIRESPONSEPROTO_LATENCIESENTRY._serialized_start=514
  _USERAPIRESPONSEPROTO_LATENCIESENTRY._serialized_end=589
# @@protoc_insertion_point(module_scope)
