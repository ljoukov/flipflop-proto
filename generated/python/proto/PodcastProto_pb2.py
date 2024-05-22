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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcf\x01\n\x1cPodcastStreamApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12,\n\x06\x63reate\x18\x02 \x01(\x0b\x32\x1a.CreatePodcastRequestProtoH\x00\x12\x30\n\x08generate\x18\x03 \x01(\x0b\x32\x1c.GeneratePodcastRequestProtoH\x00\x12)\n\x04list\x18\x04 \x01(\x0b\x32\x19.ListPodcastsRequestProtoH\x00\x42\t\n\x07request\"\x90\x03\n#PodcastStreamApiResponseHeaderProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12:\n\rcreate_header\x18\x02 \x01(\x0b\x32!.CreatePodcastResponseHeaderProtoH\x00\x12\x37\n\x08generate\x18\x03 \x01(\x0b\x32#.GeneratePodcastResponseHeaderProtoH\x00\x12\x30\n\x04list\x18\x04 \x01(\x0b\x32 .ListPodcastsResponseHeaderProtoH\x00\x12\x46\n\tlatencies\x18\x64 \x03(\x0b\x32\x33.PodcastStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\x08\n\x06header\"\xe5\x01\n\"PodcastStreamApiResponseDeltaProto\x12\x38\n\x0c\x63reate_delta\x18\x01 \x01(\x0b\x32 .CreatePodcastResponseDeltaProtoH\x00\x12<\n\x0egenerate_delta\x18\x02 \x01(\x0b\x32\".GeneratePodcastResponseDeltaProtoH\x00\x12\x35\n\nlist_delta\x18\x03 \x01(\x0b\x32\x1f.ListPodcastsResponseDeltaProtoH\x00\x42\x10\n\x0eresponse_delta\"+\n\x19\x43reatePodcastRequestProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"\"\n CreatePodcastResponseHeaderProto\"z\n\x1f\x43reatePodcastResponseDeltaProto\x12\x13\n\tseparator\x18\x01 \x01(\x08H\x00\x12\x18\n\x0e\x65rror_no_topic\x18\x02 \x01(\x08H\x00\x12 \n\x07podcast\x18\n \x01(\x0b\x32\r.PodcastProtoH\x00\x42\x06\n\x04type\"1\n\x1bGeneratePodcastRequestProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"$\n\"GeneratePodcastResponseHeaderProto\"m\n!GeneratePodcastResponseDeltaProto\x12*\n\x0cstate_update\x18\x01 \x01(\x0e\x32\x12.PodcastStateProtoH\x00\x12\x14\n\naudio_path\x18\x02 \x01(\tH\x00\x42\x06\n\x04type\"\x1a\n\x18ListPodcastsRequestProto\"B\n\x1fListPodcastsResponseHeaderProto\x12\x1f\n\x08podcasts\x18\x01 \x03(\x0b\x32\r.PodcastProto\"\x80\x01\n\x1eListPodcastsResponseDeltaProto\x12\x0e\n\x04ping\x18\x01 \x01(\x08H\x00\x12(\n\x0fupdated_podcast\x18\x02 \x01(\x0b\x32\r.PodcastProtoH\x00\x12\x1c\n\x12\x64\x65leted_podcast_id\x18\x03 \x01(\tH\x00\x42\x06\n\x04type\"\xce\x02\n\x0cPodcastProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12!\n\x05state\x18\x05 \x01(\x0e\x32\x12.PodcastStateProto\x12\r\n\x05title\x18\x06 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x07 \x01(\t\x12\x10\n\x08synopsis\x18\x08 \x01(\t\x12\x16\n\x0eshort_synopsis\x18\t \x01(\t\x12\x12\n\naudio_path\x18\n \x01(\t\x12\x31\n\x0e\x61udio_duration\x18\x0b \x01(\x0b\x32\x19.google.protobuf.Duration\"\xd5\x03\n\x12StoredPodcastProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0buser_prompt\x18\x05 \x01(\t\x12!\n\x05state\x18\x06 \x01(\x0e\x32\x12.PodcastStateProto\x12\x11\n\treasoning\x18\x07 \x01(\t\x12\r\n\x05title\x18\x08 \x01(\t\x12\x13\n\x0btitle_emoji\x18\t \x01(\t\x12\x0c\n\x04hook\x18\n \x01(\t\x12\x12\n\nshort_hook\x18\x0b \x01(\t\x12\x0c\n\x04plan\x18\x0c \x01(\t\x12+\n\ntranscript\x18\r \x01(\x0b\x32\x17.PodcastTranscriptProto\x12\x11\n\taudio_key\x18\x0e \x01(\t\x12\x31\n\x0e\x61udio_duration\x18\x0f \x01(\x0b\x32\x19.google.protobuf.Duration\x12%\n\x07visuals\x18\x10 \x01(\x0b\x32\x14.PodcastVisualsProto\"z\n\x16PodcastTranscriptProto\x12\x14\n\x0cimages_style\x18\x01 \x01(\t\x12\x18\n\x10thumbnail_prompt\x18\x02 \x01(\t\x12\x30\n\x08sections\x18\x03 \x03(\x0b\x32\x1e.PodcastSectionTranscriptProto\"~\n\x1dPodcastSectionTranscriptProto\x12.\n\x0csection_type\x18\x01 \x01(\x0e\x32\x18.PodcastSectionTypeProto\x12-\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x1c.PodcastTranscriptEntryProto\"f\n\x1bPodcastTranscriptEntryProto\x12\'\n\x04host\x18\x01 \x01(\x0b\x32\x17.PodcastHostSpeechProtoH\x00\x12\x16\n\x0cimage_prompt\x18\x02 \x01(\tH\x00\x42\x06\n\x04type\"G\n\x16PodcastHostSpeechProto\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12\x0c\n\x04text\x18\x02 \x01(\t\"R\n\x13PodcastVisualsProto\x12\x15\n\rthumbnail_key\x18\x01 \x01(\t\x12$\n\x07visuals\x18\x02 \x03(\x0b\x32\x13.PodcastVisualProto\"A\n\x12PodcastVisualProto\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x05\x12\x11\n\timage_key\x18\x02 \x01(\t*\xf0\x03\n\x11PodcastStateProto\x12\x1f\n\x1bPODCAST_STATE_PROTO_UNKNOWN\x10\x00\x12\x1d\n\x19PODCAST_STATE_PROTO_READY\x10\x01\x12+\n\'PODCAST_STATE_PROTO_GENERATING_SYNOPSYS\x10\x02\x12&\n\"PODCAST_STATE_PROTO_SYNOPSYS_READY\x10\x03\x12\'\n#PODCAST_STATE_PROTO_GENERATING_PLAN\x10\x04\x12\"\n\x1ePODCAST_STATE_PROTO_PLAN_READY\x10\x05\x12-\n)PODCAST_STATE_PROTO_GENERATING_TRANSCRIPT\x10\x06\x12(\n$PODCAST_STATE_PROTO_TRANSCRIPT_READY\x10\x07\x12(\n$PODCAST_STATE_PROTO_GENERATING_AUDIO\x10\x08\x12#\n\x1fPODCAST_STATE_PROTO_AUDIO_READY\x10\t\x12*\n&PODCAST_STATE_PROTO_GENERATING_VISUALS\x10\n\x12%\n!PODCAST_STATE_PROTO_VISUALS_READY\x10\x0b*\xc1\x01\n\x17PodcastSectionTypeProto\x12&\n\"PODCAST_SECTION_TYPE_PROTO_UNKNOWN\x10\x00\x12+\n\'PODCAST_SECTION_TYPE_PROTO_INTRODUCTION\x10\x01\x12&\n\"PODCAST_SECTION_TYPE_PROTO_SECTION\x10\x02\x12)\n%PODCAST_SECTION_TYPE_PROTO_CONCLUSION\x10\x03*n\n\x10PodcastHostProto\x12\x1e\n\x1aPODCAST_HOST_PROTO_UNKNOWN\x10\x00\x12\x1b\n\x17PODCAST_HOST_PROTO_MALE\x10\x01\x12\x1d\n\x19PODCAST_HOST_PROTO_FEMALE\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PodcastProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _PODCASTSTATEPROTO._serialized_start=2954
  _PODCASTSTATEPROTO._serialized_end=3450
  _PODCASTSECTIONTYPEPROTO._serialized_start=3453
  _PODCASTSECTIONTYPEPROTO._serialized_end=3646
  _PODCASTHOSTPROTO._serialized_start=3648
  _PODCASTHOSTPROTO._serialized_end=3758
  _PODCASTSTREAMAPIREQUESTPROTO._serialized_start=88
  _PODCASTSTREAMAPIREQUESTPROTO._serialized_end=295
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO._serialized_start=298
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO._serialized_end=698
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_start=613
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_end=688
  _PODCASTSTREAMAPIRESPONSEDELTAPROTO._serialized_start=701
  _PODCASTSTREAMAPIRESPONSEDELTAPROTO._serialized_end=930
  _CREATEPODCASTREQUESTPROTO._serialized_start=932
  _CREATEPODCASTREQUESTPROTO._serialized_end=975
  _CREATEPODCASTRESPONSEHEADERPROTO._serialized_start=977
  _CREATEPODCASTRESPONSEHEADERPROTO._serialized_end=1011
  _CREATEPODCASTRESPONSEDELTAPROTO._serialized_start=1013
  _CREATEPODCASTRESPONSEDELTAPROTO._serialized_end=1135
  _GENERATEPODCASTREQUESTPROTO._serialized_start=1137
  _GENERATEPODCASTREQUESTPROTO._serialized_end=1186
  _GENERATEPODCASTRESPONSEHEADERPROTO._serialized_start=1188
  _GENERATEPODCASTRESPONSEHEADERPROTO._serialized_end=1224
  _GENERATEPODCASTRESPONSEDELTAPROTO._serialized_start=1226
  _GENERATEPODCASTRESPONSEDELTAPROTO._serialized_end=1335
  _LISTPODCASTSREQUESTPROTO._serialized_start=1337
  _LISTPODCASTSREQUESTPROTO._serialized_end=1363
  _LISTPODCASTSRESPONSEHEADERPROTO._serialized_start=1365
  _LISTPODCASTSRESPONSEHEADERPROTO._serialized_end=1431
  _LISTPODCASTSRESPONSEDELTAPROTO._serialized_start=1434
  _LISTPODCASTSRESPONSEDELTAPROTO._serialized_end=1562
  _PODCASTPROTO._serialized_start=1565
  _PODCASTPROTO._serialized_end=1899
  _STOREDPODCASTPROTO._serialized_start=1902
  _STOREDPODCASTPROTO._serialized_end=2371
  _PODCASTTRANSCRIPTPROTO._serialized_start=2373
  _PODCASTTRANSCRIPTPROTO._serialized_end=2495
  _PODCASTSECTIONTRANSCRIPTPROTO._serialized_start=2497
  _PODCASTSECTIONTRANSCRIPTPROTO._serialized_end=2623
  _PODCASTTRANSCRIPTENTRYPROTO._serialized_start=2625
  _PODCASTTRANSCRIPTENTRYPROTO._serialized_end=2727
  _PODCASTHOSTSPEECHPROTO._serialized_start=2729
  _PODCASTHOSTSPEECHPROTO._serialized_end=2800
  _PODCASTVISUALSPROTO._serialized_start=2802
  _PODCASTVISUALSPROTO._serialized_end=2884
  _PODCASTVISUALPROTO._serialized_start=2886
  _PODCASTVISUALPROTO._serialized_end=2951
# @@protoc_insertion_point(module_scope)
