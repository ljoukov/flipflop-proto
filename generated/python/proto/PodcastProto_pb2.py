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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb3\x01\n\x1cPodcastStreamApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12;\n\x0e\x63reate_preview\x18\x02 \x01(\x0b\x32!.CreatePodcastPreviewRequestProtoH\x00\x12\x30\n\x08generate\x18\x03 \x01(\x0b\x32\x1c.GeneratePodcastRequestProtoH\x00\x42\t\n\x07request\"\xed\x02\n#PodcastStreamApiResponseHeaderProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12I\n\x15\x63reate_preview_header\x18\x02 \x01(\x0b\x32(.CreatePodcastPreviewResponseHeaderProtoH\x00\x12\x37\n\x08generate\x18\x03 \x01(\x0b\x32#.GeneratePodcastResponseHeaderProtoH\x00\x12\x46\n\tlatencies\x18\x64 \x03(\x0b\x32\x33.PodcastStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\x08\n\x06header\"\xbd\x01\n\"PodcastStreamApiResponseDeltaProto\x12G\n\x14\x63reate_preview_delta\x18\x01 \x01(\x0b\x32\'.CreatePodcastPreviewResponseDeltaProtoH\x00\x12<\n\x0egenerate_delta\x18\x02 \x01(\x0b\x32\".GeneratePodcastResponseDeltaProtoH\x00\x42\x10\n\x0eresponse_delta\"2\n CreatePodcastPreviewRequestProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\")\n\'CreatePodcastPreviewResponseHeaderProto\"\x8e\x01\n&CreatePodcastPreviewResponseDeltaProto\x12\x13\n\tseparator\x18\x01 \x01(\x08H\x00\x12\x18\n\x0e\x65rror_no_topic\x18\x02 \x01(\x08H\x00\x12-\n\rpreview_delta\x18\n \x01(\x0b\x32\x14.PodcastPreviewProtoH\x00\x42\x06\n\x04type\"1\n\x1bGeneratePodcastRequestProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"$\n\"GeneratePodcastResponseHeaderProto\"\x8a\x01\n!GeneratePodcastResponseDeltaProto\x12\x12\n\x08planning\x18\x01 \x01(\x08H\x00\x12\x1e\n\x14producing_transcript\x18\x02 \x01(\x08H\x00\x12\x13\n\tnarrating\x18\x03 \x01(\x08H\x00\x12\x14\n\naudio_path\x18\x04 \x01(\tH\x00\x42\x06\n\x04type\"\xa3\x01\n\x13PodcastPreviewProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05title\x18\x04 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x05 \x01(\t\x12\x10\n\x08synopsis\x18\x06 \x01(\t\"\xd2\x02\n\x0cPodcastProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0buser_prompt\x18\x05 \x01(\t\x12!\n\x05state\x18\x06 \x01(\x0e\x32\x12.PodcastStateProto\x12\x11\n\treasoning\x18\x07 \x01(\t\x12\r\n\x05title\x18\x08 \x01(\t\x12\x13\n\x0btitle_emoji\x18\t \x01(\t\x12\x10\n\x08synopsis\x18\n \x01(\t\x12\x0c\n\x04plan\x18\x0b \x01(\t\x12+\n\ntranscript\x18\x0c \x01(\x0b\x32\x17.PodcastTranscriptProto\"J\n\x16PodcastTranscriptProto\x12\x30\n\x08sections\x18\x01 \x03(\x0b\x32\x1e.PodcastSectionTranscriptProto\"~\n\x1dPodcastSectionTranscriptProto\x12.\n\x0csection_type\x18\x01 \x01(\x0e\x32\x18.PodcastSectionTypeProto\x12-\n\x07\x65ntries\x18\x02 \x01(\x0b\x32\x1c.PodcastTranscriptEntryProto\"L\n\x1bPodcastTranscriptEntryProto\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12\x0c\n\x04text\x18\x02 \x01(\t*\xb7\x01\n\x11PodcastStateProto\x12\x1f\n\x1bPODCAST_STATE_PROTO_UNKNOWN\x10\x00\x12 \n\x1cPODCAST_STATE_PROTO_SYNOPSYS\x10\x01\x12\x1c\n\x18PODCAST_STATE_PROTO_PLAN\x10\x02\x12\"\n\x1ePODCAST_STATE_PROTO_TRANSCRIPT\x10\x03\x12\x1d\n\x19PODCAST_STATE_PROTO_AUDIO\x10\x04*\xc1\x01\n\x17PodcastSectionTypeProto\x12&\n\"PODCAST_SECTION_TYPE_PROTO_UNKNOWN\x10\x00\x12+\n\'PODCAST_SECTION_TYPE_PROTO_INTRODUCTION\x10\x01\x12&\n\"PODCAST_SECTION_TYPE_PROTO_SECTION\x10\x02\x12)\n%PODCAST_SECTION_TYPE_PROTO_CONCLUSION\x10\x03*n\n\x10PodcastHostProto\x12\x1e\n\x1aPODCAST_HOST_PROTO_UNKNOWN\x10\x00\x12\x1b\n\x17PODCAST_HOST_PROTO_MALE\x10\x01\x12\x1d\n\x19PODCAST_HOST_PROTO_FEMALE\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PodcastProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _PODCASTSTATEPROTO._serialized_start=2089
  _PODCASTSTATEPROTO._serialized_end=2272
  _PODCASTSECTIONTYPEPROTO._serialized_start=2275
  _PODCASTSECTIONTYPEPROTO._serialized_end=2468
  _PODCASTHOSTPROTO._serialized_start=2470
  _PODCASTHOSTPROTO._serialized_end=2580
  _PODCASTSTREAMAPIREQUESTPROTO._serialized_start=88
  _PODCASTSTREAMAPIREQUESTPROTO._serialized_end=267
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO._serialized_start=270
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO._serialized_end=635
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_start=550
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_end=625
  _PODCASTSTREAMAPIRESPONSEDELTAPROTO._serialized_start=638
  _PODCASTSTREAMAPIRESPONSEDELTAPROTO._serialized_end=827
  _CREATEPODCASTPREVIEWREQUESTPROTO._serialized_start=829
  _CREATEPODCASTPREVIEWREQUESTPROTO._serialized_end=879
  _CREATEPODCASTPREVIEWRESPONSEHEADERPROTO._serialized_start=881
  _CREATEPODCASTPREVIEWRESPONSEHEADERPROTO._serialized_end=922
  _CREATEPODCASTPREVIEWRESPONSEDELTAPROTO._serialized_start=925
  _CREATEPODCASTPREVIEWRESPONSEDELTAPROTO._serialized_end=1067
  _GENERATEPODCASTREQUESTPROTO._serialized_start=1069
  _GENERATEPODCASTREQUESTPROTO._serialized_end=1118
  _GENERATEPODCASTRESPONSEHEADERPROTO._serialized_start=1120
  _GENERATEPODCASTRESPONSEHEADERPROTO._serialized_end=1156
  _GENERATEPODCASTRESPONSEDELTAPROTO._serialized_start=1159
  _GENERATEPODCASTRESPONSEDELTAPROTO._serialized_end=1297
  _PODCASTPREVIEWPROTO._serialized_start=1300
  _PODCASTPREVIEWPROTO._serialized_end=1463
  _PODCASTPROTO._serialized_start=1466
  _PODCASTPROTO._serialized_end=1804
  _PODCASTTRANSCRIPTPROTO._serialized_start=1806
  _PODCASTTRANSCRIPTPROTO._serialized_end=1880
  _PODCASTSECTIONTRANSCRIPTPROTO._serialized_start=1882
  _PODCASTSECTIONTRANSCRIPTPROTO._serialized_end=2008
  _PODCASTTRANSCRIPTENTRYPROTO._serialized_start=2010
  _PODCASTTRANSCRIPTENTRYPROTO._serialized_end=2086
# @@protoc_insertion_point(module_scope)
