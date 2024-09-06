# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: UserDataProto.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'UserDataProto.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13UserDataProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x19\n\x17GetUserDataRequestProto\"=\n\x18GetUserDataResponseProto\x12!\n\tuser_data\x18\x01 \x01(\x0b\x32\x0e.UserDataProto\"?\n\x1aUpdateUserDataRequestProto\x12!\n\tuser_data\x18\x01 \x01(\x0b\x32\x0e.UserDataProto\"@\n\x1bUpdateUserDataResponseProto\x12!\n\tuser_data\x18\x01 \x01(\x0b\x32\x0e.UserDataProto\"\x1f\n\x1d\x44\x65leteUserHistoryRequestProto\" \n\x1e\x44\x65leteUserHistoryResponseProto\"\xe6\x01\n\x13UserApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12\x31\n\rget_user_data\x18\x02 \x01(\x0b\x32\x18.GetUserDataRequestProtoH\x00\x12\x37\n\x10update_user_data\x18\x03 \x01(\x0b\x32\x1b.UpdateUserDataRequestProtoH\x00\x12=\n\x13\x64\x65lete_user_history\x18\x04 \x01(\x0b\x32\x1e.DeleteUserHistoryRequestProtoH\x00\x42\t\n\x07request\"\xfb\x02\n\x14UserApiResponseProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12\x32\n\rget_user_data\x18\x02 \x01(\x0b\x32\x19.GetUserDataResponseProtoH\x00\x12\x38\n\x10update_user_data\x18\x03 \x01(\x0b\x32\x1c.UpdateUserDataResponseProtoH\x00\x12>\n\x13\x64\x65lete_user_history\x18\x04 \x01(\x0b\x32\x1f.DeleteUserHistoryResponseProtoH\x00\x12\x37\n\tlatencies\x18\x64 \x03(\x0b\x32$.UserApiResponseProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\n\n\x08response\"\x80\x01\n\x11\x43\x61rdUserDataProto\x12\x0f\n\x07\x63\x61rd_id\x18\x01 \x01(\t\x12\x34\n\x10last_modified_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1e\n\x16selected_option_number\x18\x04 \x01(\x05J\x04\x08\x03\x10\x04\"\xe3\x01\n\x12StoryUserDataProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12\x34\n\x10last_modified_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12%\n\x0blike_status\x18\x06 \x01(\x0e\x32\x10.LikeStatusProto\x12&\n\ncards_data\x18\x04 \x03(\x0b\x32\x12.CardUserDataProto\x12\x30\n\rview_duration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationJ\x04\x08\x03\x10\x04\"\xb1\x01\n\rUserDataProto\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10last_modified_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x0cstories_data\x18\x01 \x03(\x0b\x32\x13.StoryUserDataProto*\\\n\x0fLikeStatusProto\x12\x17\n\x13LIKE_STATUS_UNKNOWN\x10\x00\x12\x16\n\x12LIKE_STATUS_ACTIVE\x10\x01\x12\x18\n\x14LIKE_STATUS_INACTIVE\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'UserDataProto_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERAPIRESPONSEPROTO_LATENCIESENTRY']._loaded_options = None
  _globals['_USERAPIRESPONSEPROTO_LATENCIESENTRY']._serialized_options = b'8\001'
  _globals['_LIKESTATUSPROTO']._serialized_start=1532
  _globals['_LIKESTATUSPROTO']._serialized_end=1624
  _globals['_GETUSERDATAREQUESTPROTO']._serialized_start=88
  _globals['_GETUSERDATAREQUESTPROTO']._serialized_end=113
  _globals['_GETUSERDATARESPONSEPROTO']._serialized_start=115
  _globals['_GETUSERDATARESPONSEPROTO']._serialized_end=176
  _globals['_UPDATEUSERDATAREQUESTPROTO']._serialized_start=178
  _globals['_UPDATEUSERDATAREQUESTPROTO']._serialized_end=241
  _globals['_UPDATEUSERDATARESPONSEPROTO']._serialized_start=243
  _globals['_UPDATEUSERDATARESPONSEPROTO']._serialized_end=307
  _globals['_DELETEUSERHISTORYREQUESTPROTO']._serialized_start=309
  _globals['_DELETEUSERHISTORYREQUESTPROTO']._serialized_end=340
  _globals['_DELETEUSERHISTORYRESPONSEPROTO']._serialized_start=342
  _globals['_DELETEUSERHISTORYRESPONSEPROTO']._serialized_end=374
  _globals['_USERAPIREQUESTPROTO']._serialized_start=377
  _globals['_USERAPIREQUESTPROTO']._serialized_end=607
  _globals['_USERAPIRESPONSEPROTO']._serialized_start=610
  _globals['_USERAPIRESPONSEPROTO']._serialized_end=989
  _globals['_USERAPIRESPONSEPROTO_LATENCIESENTRY']._serialized_start=902
  _globals['_USERAPIRESPONSEPROTO_LATENCIESENTRY']._serialized_end=977
  _globals['_CARDUSERDATAPROTO']._serialized_start=992
  _globals['_CARDUSERDATAPROTO']._serialized_end=1120
  _globals['_STORYUSERDATAPROTO']._serialized_start=1123
  _globals['_STORYUSERDATAPROTO']._serialized_end=1350
  _globals['_USERDATAPROTO']._serialized_start=1353
  _globals['_USERDATAPROTO']._serialized_end=1530
# @@protoc_insertion_point(module_scope)
