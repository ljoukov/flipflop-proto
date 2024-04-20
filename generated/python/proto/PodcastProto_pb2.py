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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x81\x01\n\x1cPodcastStreamApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12;\n\x0e\x63reate_preview\x18\x02 \x01(\x0b\x32!.CreatePodcastPreviewRequestProtoH\x00\x42\t\n\x07request\"\xb4\x02\n#PodcastStreamApiResponseHeaderProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12I\n\x15\x63reate_preview_header\x18\x02 \x01(\x0b\x32(.CreatePodcastPreviewResponseHeaderProtoH\x00\x12\x46\n\tlatencies\x18\x64 \x03(\x0b\x32\x33.PodcastStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\x08\n\x06header\"\x7f\n\"PodcastStreamApiResponseDeltaProto\x12G\n\x14\x63reate_preview_delta\x18\x01 \x01(\x0b\x32\'.CreatePodcastPreviewResponseDeltaProtoH\x00\x42\x10\n\x0eresponse_delta\"2\n CreatePodcastPreviewRequestProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\")\n\'CreatePodcastPreviewResponseHeaderProto\"\x8e\x01\n&CreatePodcastPreviewResponseDeltaProto\x12\x13\n\tseparator\x18\x01 \x01(\x08H\x00\x12\x18\n\x0e\x65rror_no_topic\x18\x02 \x01(\x08H\x00\x12-\n\rpreview_delta\x18\n \x01(\x0b\x32\x14.PodcastPreviewProtoH\x00\x42\x06\n\x04type\"\xa3\x01\n\x13PodcastPreviewProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05title\x18\x04 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x05 \x01(\t\x12\x10\n\x08synopsis\x18\x06 \x01(\t\"G\n\x16PodcastTranscriptEntry\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x8d\x02\n\x0cPodcastProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12!\n\x05state\x18\x04 \x01(\x0e\x32\x12.PodcastStateProto\x12\x11\n\treasoning\x18\x05 \x01(\t\x12\r\n\x05title\x18\x06 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x07 \x01(\t\x12\x10\n\x08synopsis\x18\x08 \x01(\t\x12\x0c\n\x04plan\x18\t \x01(\t\x12+\n\ntranscript\x18\n \x03(\x0b\x32\x17.PodcastTranscriptEntry*n\n\x10PodcastHostProto\x12\x1e\n\x1aPODCAST_HOST_PROTO_UNKNOWN\x10\x00\x12\x1b\n\x17PODCAST_HOST_PROTO_MALE\x10\x01\x12\x1d\n\x19PODCAST_HOST_PROTO_FEMALE\x10\x02*\xb7\x01\n\x11PodcastStateProto\x12\x1f\n\x1bPODCAST_STATE_PROTO_UNKNOWN\x10\x00\x12 \n\x1cPODCAST_STATE_PROTO_SYNOPSYS\x10\x01\x12\x1c\n\x18PODCAST_STATE_PROTO_PLAN\x10\x02\x12\"\n\x1ePODCAST_STATE_PROTO_TRANSCRIPT\x10\x03\x12\x1d\n\x19PODCAST_STATE_PROTO_AUDIO\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PodcastProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _PODCASTHOSTPROTO._serialized_start=1410
  _PODCASTHOSTPROTO._serialized_end=1520
  _PODCASTSTATEPROTO._serialized_start=1523
  _PODCASTSTATEPROTO._serialized_end=1706
  _PODCASTSTREAMAPIREQUESTPROTO._serialized_start=88
  _PODCASTSTREAMAPIREQUESTPROTO._serialized_end=217
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO._serialized_start=220
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO._serialized_end=528
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_start=443
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_end=518
  _PODCASTSTREAMAPIRESPONSEDELTAPROTO._serialized_start=530
  _PODCASTSTREAMAPIRESPONSEDELTAPROTO._serialized_end=657
  _CREATEPODCASTPREVIEWREQUESTPROTO._serialized_start=659
  _CREATEPODCASTPREVIEWREQUESTPROTO._serialized_end=709
  _CREATEPODCASTPREVIEWRESPONSEHEADERPROTO._serialized_start=711
  _CREATEPODCASTPREVIEWRESPONSEHEADERPROTO._serialized_end=752
  _CREATEPODCASTPREVIEWRESPONSEDELTAPROTO._serialized_start=755
  _CREATEPODCASTPREVIEWRESPONSEDELTAPROTO._serialized_end=897
  _PODCASTPREVIEWPROTO._serialized_start=900
  _PODCASTPREVIEWPROTO._serialized_end=1063
  _PODCASTTRANSCRIPTENTRY._serialized_start=1065
  _PODCASTTRANSCRIPTENTRY._serialized_end=1136
  _PODCASTPROTO._serialized_start=1139
  _PODCASTPROTO._serialized_end=1408
# @@protoc_insertion_point(module_scope)
