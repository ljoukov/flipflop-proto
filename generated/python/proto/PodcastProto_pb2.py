# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PodcastProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"{\n\x1cPodcastStreamApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12\x35\n\x0b\x63reate_plan\x18\x02 \x01(\x0b\x32\x1e.CreatePodcastPlanRequestProtoH\x00\x42\t\n\x07request\"\xae\x02\n#PodcastStreamApiResponseHeaderProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12\x43\n\x12\x63reate_plan_header\x18\x02 \x01(\x0b\x32%.CreatePodcastPlanResponseHeaderProtoH\x00\x12\x46\n\tlatencies\x18\x64 \x03(\x0b\x32\x33.PodcastStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\x08\n\x06header\"y\n\"PodcastStreamApiResponseDeltaProto\x12\x41\n\x11\x63reate_plan_delta\x18\x01 \x01(\x0b\x32$.CreatePodcastPlanResponseDeltaProtoH\x00\x42\x10\n\x0eresponse_delta\"/\n\x1d\x43reatePodcastPlanRequestProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"&\n$CreatePodcastPlanResponseHeaderProto\"\x85\x01\n#CreatePodcastPlanResponseDeltaProto\x12\x13\n\tseparator\x18\x01 \x01(\x08H\x00\x12\x18\n\x0e\x65rror_no_topic\x18\x02 \x01(\x08H\x00\x12\'\n\nplan_delta\x18\n \x01(\x0b\x32\x11.PodcastPlanProtoH\x00\x42\x06\n\x04type\"\xa6\x01\n\x10PodcastPlanProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05title\x18\n \x01(\t\x12\x13\n\x0btitle_emoji\x18\x0b \x01(\t\x12\x0c\n\x04hook\x18\x0c \x01(\t\x12\x10\n\x08segments\x18\r \x03(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PodcastProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _PODCASTSTREAMAPIREQUESTPROTO._serialized_start=87
  _PODCASTSTREAMAPIREQUESTPROTO._serialized_end=210
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO._serialized_start=213
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO._serialized_end=515
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_start=430
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_end=505
  _PODCASTSTREAMAPIRESPONSEDELTAPROTO._serialized_start=517
  _PODCASTSTREAMAPIRESPONSEDELTAPROTO._serialized_end=638
  _CREATEPODCASTPLANREQUESTPROTO._serialized_start=640
  _CREATEPODCASTPLANREQUESTPROTO._serialized_end=687
  _CREATEPODCASTPLANRESPONSEHEADERPROTO._serialized_start=689
  _CREATEPODCASTPLANRESPONSEHEADERPROTO._serialized_end=727
  _CREATEPODCASTPLANRESPONSEDELTAPROTO._serialized_start=730
  _CREATEPODCASTPLANRESPONSEDELTAPROTO._serialized_end=863
  _PODCASTPLANPROTO._serialized_start=866
  _PODCASTPLANPROTO._serialized_end=1032
# @@protoc_insertion_point(module_scope)
