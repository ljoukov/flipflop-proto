# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ChatProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x43hatProto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"j\n\x11\x43hatActivityProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x65scription_prompt\x18\x03 \x01(\t\x12\x15\n\raction_prompt\x18\x04 \x01(\t\"&\n\x16\x43hatSystemMessageProto\x12\x0c\n\x04text\x18\x01 \x01(\t\"@\n\x19\x43hatAssistantMessageProto\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x15\n\ractivity_name\x18\x02 \x03(\t\"9\n\x14\x43hatUserMessageProto\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63tion_name\x18\x02 \x01(\t\"\xc8\x01\n\x0b\x43hatMessage\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x06system\x18\x02 \x01(\x0b\x32\x17.ChatSystemMessageProtoH\x00\x12/\n\tassistant\x18\x03 \x01(\x0b\x32\x1a.ChatAssistantMessageProtoH\x00\x12%\n\x04user\x18\x04 \x01(\x0b\x32\x15.ChatUserMessageProtoH\x00\x42\x06\n\x04typeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ChatProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHATACTIVITYPROTO._serialized_start=52
  _CHATACTIVITYPROTO._serialized_end=158
  _CHATSYSTEMMESSAGEPROTO._serialized_start=160
  _CHATSYSTEMMESSAGEPROTO._serialized_end=198
  _CHATASSISTANTMESSAGEPROTO._serialized_start=200
  _CHATASSISTANTMESSAGEPROTO._serialized_end=264
  _CHATUSERMESSAGEPROTO._serialized_start=266
  _CHATUSERMESSAGEPROTO._serialized_end=323
  _CHATMESSAGE._serialized_start=326
  _CHATMESSAGE._serialized_end=526
# @@protoc_insertion_point(module_scope)
