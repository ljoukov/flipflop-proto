# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BlipProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x42lipProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"g\n\x13\x42lipApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12*\n\tget_blips\x18\x02 \x01(\x0b\x32\x15.GetBlipsRequestProtoH\x00\x42\t\n\x07request\"\xfa\x01\n\x14\x42lipApiResponseProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12+\n\tget_blips\x18\x02 \x01(\x0b\x32\x16.GetBlipsResponseProtoH\x00\x12\x37\n\tlatencies\x18\x64 \x03(\x0b\x32$.BlipApiResponseProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\n\n\x08response\"\x16\n\x14GetBlipsRequestProto\"2\n\x15GetBlipsResponseProto\x12\x19\n\x05\x62lips\x18\x01 \x03(\x0b\x32\n.BlipProto\"\\\n\x0f\x42lipsCacheProto\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x05\x62lips\x18\x02 \x03(\x0b\x32\n.BlipProto\"\x90\x01\n\tBlipProto\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x04 \x01(\t\x12\x0c\n\x04\x62ody\x18\x05 \x01(\t\x12\x15\n\rclosure_emoji\x18\x06 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'BlipProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BLIPAPIRESPONSEPROTO_LATENCIESENTRY._options = None
  _BLIPAPIRESPONSEPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _BLIPAPIREQUESTPROTO._serialized_start=84
  _BLIPAPIREQUESTPROTO._serialized_end=187
  _BLIPAPIRESPONSEPROTO._serialized_start=190
  _BLIPAPIRESPONSEPROTO._serialized_end=440
  _BLIPAPIRESPONSEPROTO_LATENCIESENTRY._serialized_start=353
  _BLIPAPIRESPONSEPROTO_LATENCIESENTRY._serialized_end=428
  _GETBLIPSREQUESTPROTO._serialized_start=442
  _GETBLIPSREQUESTPROTO._serialized_end=464
  _GETBLIPSRESPONSEPROTO._serialized_start=466
  _GETBLIPSRESPONSEPROTO._serialized_end=516
  _BLIPSCACHEPROTO._serialized_start=518
  _BLIPSCACHEPROTO._serialized_end=610
  _BLIPPROTO._serialized_start=613
  _BLIPPROTO._serialized_end=757
# @@protoc_insertion_point(module_scope)
