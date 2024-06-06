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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcf\x01\n\x1cPodcastStreamApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12,\n\x06\x63reate\x18\x02 \x01(\x0b\x32\x1a.CreatePodcastRequestProtoH\x00\x12\x30\n\x08generate\x18\x03 \x01(\x0b\x32\x1c.GeneratePodcastRequestProtoH\x00\x12)\n\x04list\x18\x04 \x01(\x0b\x32\x19.ListPodcastsRequestProtoH\x00\x42\t\n\x07request\"\x90\x03\n#PodcastStreamApiResponseHeaderProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12:\n\rcreate_header\x18\x02 \x01(\x0b\x32!.CreatePodcastResponseHeaderProtoH\x00\x12\x37\n\x08generate\x18\x03 \x01(\x0b\x32#.GeneratePodcastResponseHeaderProtoH\x00\x12\x30\n\x04list\x18\x04 \x01(\x0b\x32 .ListPodcastsResponseHeaderProtoH\x00\x12\x46\n\tlatencies\x18\x64 \x03(\x0b\x32\x33.PodcastStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\x08\n\x06header\"\xe5\x01\n\"PodcastStreamApiResponseDeltaProto\x12\x38\n\x0c\x63reate_delta\x18\x01 \x01(\x0b\x32 .CreatePodcastResponseDeltaProtoH\x00\x12<\n\x0egenerate_delta\x18\x02 \x01(\x0b\x32\".GeneratePodcastResponseDeltaProtoH\x00\x12\x35\n\nlist_delta\x18\x03 \x01(\x0b\x32\x1f.ListPodcastsResponseDeltaProtoH\x00\x42\x10\n\x0eresponse_delta\"+\n\x19\x43reatePodcastRequestProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"\"\n CreatePodcastResponseHeaderProto\"\xa7\x01\n\x1f\x43reatePodcastResponseDeltaProto\x12\x13\n\tseparator\x18\x01 \x01(\x08H\x00\x12\x18\n\x0e\x65rror_no_topic\x18\x02 \x01(\x08H\x00\x12 \n\x07podcast\x18\n \x01(\x0b\x32\r.PodcastProtoH\x00\x12+\n\x06\x61nswer\x18\x0b \x01(\x0b\x32\x19.PodcastPromptAnswerProtoH\x00\x42\x06\n\x04type\"K\n\x1bGeneratePodcastRequestProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x18\n\x10\x64uration_seconds\x18\x02 \x01(\x05\"$\n\"GeneratePodcastResponseHeaderProto\"M\n!GeneratePodcastResponseDeltaProto\x12 \n\x07podcast\x18\x01 \x01(\x0b\x32\r.PodcastProtoH\x00\x42\x06\n\x04type\"\x1a\n\x18ListPodcastsRequestProto\"B\n\x1fListPodcastsResponseHeaderProto\x12\x1f\n\x08podcasts\x18\x01 \x03(\x0b\x32\r.PodcastProto\"\x80\x01\n\x1eListPodcastsResponseDeltaProto\x12\x0e\n\x04ping\x18\x01 \x01(\x08H\x00\x12(\n\x0fupdated_podcast\x18\x02 \x01(\x0b\x32\r.PodcastProtoH\x00\x12\x1c\n\x12\x64\x65leted_podcast_id\x18\x03 \x01(\tH\x00\x42\x06\n\x04type\"\xac\x03\n\x0cPodcastProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08is_ready\x18\x05 \x01(\x08\x12\x16\n\x0e\x64isplay_status\x18\x06 \x01(\t\x12%\n\x07preview\x18\x07 \x01(\x0b\x32\x14.PodcastPreviewProto\x12)\n\tthumbnail\x18\x08 \x01(\x0b\x32\x16.PodcastThumbnailProto\x12!\n\x05\x61udio\x18\t \x01(\x0b\x32\x12.PodcastAudioProto\x12%\n\x07visuals\x18\n \x01(\x0b\x32\x14.PodcastVisualsProto\x12+\n\ntranscript\x18\x0b \x01(\x0b\x32\x17.PodcastTranscriptProto\x12!\n\x05\x63\x61rds\x18\x0c \x01(\x0b\x32\x12.PodcastCardsProto\"K\n\x13PodcastPreviewProto\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x02 \x01(\t\x12\x10\n\x08synopsis\x18\x03 \x01(\t\"W\n\x15PodcastThumbnailProto\x12\r\n\x05title\x18\x01 \x01(\t\x12!\n\x05\x62\x61\x64ge\x18\x02 \x01(\x0e\x32\x12.PodcastBadgeProto\x12\x0c\n\x04path\x18\x03 \x01(\t\"N\n\x11PodcastAudioProto\x12\x0c\n\x04path\x18\x01 \x01(\t\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"5\n\x11PodcastCardsProto\x12 \n\x05\x63\x61rds\x18\x01 \x03(\x0b\x32\x11.PodcastCardProto\"\x8e\x01\n\x10PodcastCardProto\x12\x0f\n\x07\x63\x61rd_id\x18\x01 \x01(\t\x12:\n\x0fmultiple_choice\x18\n \x01(\x0b\x32\x1f.PodcastMultipleChoiceCardProtoH\x00\x12%\n\x04poll\x18\x0b \x01(\x0b\x32\x15.PodcastPollCardProtoH\x00\x42\x06\n\x04type\"(\n\x18PodcastPromptAnswerProto\x12\x0c\n\x04text\x18\x01 \x01(\t\";\n\x13PodcastVisualsProto\x12$\n\x07visuals\x18\x01 \x03(\x0b\x32\x13.PodcastVisualProto\"\xa6\x01\n\x12PodcastVisualProto\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x05\x12\x12\n\nimage_path\x18\x02 \x01(\t\x12/\n\tanimation\x18\x04 \x01(\x0b\x32\x1c.PodcastVisualAnimationProto\x12\x31\n\ntransition\x18\x03 \x01(\x0e\x32\x1d.PodcastVisualTransitionProto\"^\n\x1bPodcastVisualAnimationProto\x12\x17\n\x0f\x64uration_millis\x18\x01 \x01(\x05\x12\x13\n\x0bstart_scale\x18\x02 \x01(\x02\x12\x11\n\tend_scale\x18\x03 \x01(\x02\"G\n\x16PodcastTranscriptProto\x12-\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1c.PodcastTranscriptEntryProto\"`\n\x1bPodcastTranscriptEntryProto\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12 \n\x05words\x18\x02 \x03(\x0b\x32\x11.PodcastWordProto\"]\n\x10PodcastWordProto\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x14\n\x0cstart_millis\x18\x02 \x01(\x05\x12\x12\n\nend_millis\x18\x03 \x01(\x05\x12\x11\n\tseparator\x18\x04 \x01(\t\"r\n\x19PodcastKnowledgeCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x13\n\x0b\x65xplanation\x18\x04 \x01(\t\"\xdd\x01\n\x1ePodcastMultipleChoiceCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x10\n\x08question\x18\x03 \x01(\t\x12\x32\n\x07options\x18\x04 \x03(\x0b\x32!.PodcastMultipleChoiceOptionProto\x12\x1d\n\x15\x63orrect_answer_number\x18\x05 \x01(\x05\x12\r\n\x05hints\x18\x06 \x03(\t\x12\x13\n\x0b\x65xplanation\x18\x07 \x01(\t\"\x86\x01\n\x14PodcastPollCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x10\n\x08question\x18\x03 \x01(\t\x12(\n\x07options\x18\x04 \x03(\x0b\x32\x17.PodcastPollOptionProto\"9\n\x14PodcastCardHeroProto\x12\r\n\x05\x65moji\x18\x01 \x01(\t\x12\x12\n\nlottie_url\x18\x02 \x01(\t\"0\n PodcastMultipleChoiceOptionProto\x12\x0c\n\x04text\x18\x01 \x01(\t\"&\n\x16PodcastPollOptionProto\x12\x0c\n\x04text\x18\x01 \x01(\t*\x92\x01\n\x11PodcastBadgeProto\x12!\n\x1dPODCAST_BADGE_PROTO_UNDEFINED\x10\x00\x12\x1c\n\x18PODCAST_BADGE_PROTO_NONE\x10\x01\x12\x1e\n\x1aPODCAST_BADGE_PROTO_LISTEN\x10\x02\x12\x1c\n\x18PODCAST_BADGE_PROTO_POLL\x10\x03*\x84\x02\n\x1cPodcastVisualTransitionProto\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_UNDEFINED\x10\x00\x12,\n(PODCAST_VISUAL_TRANSITION_PROTO_DISSOLVE\x10\x01\x12)\n%PODCAST_VISUAL_TRANSITION_PROTO_SWIPE\x10\x02\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_BAR_SWIPE\x10\x03\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_PAGE_CURL\x10\x04*n\n\x10PodcastHostProto\x12\x1e\n\x1aPODCAST_HOST_PROTO_UNKNOWN\x10\x00\x12\x1b\n\x17PODCAST_HOST_PROTO_MALE\x10\x01\x12\x1d\n\x19PODCAST_HOST_PROTO_FEMALE\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PodcastProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _PODCASTBADGEPROTO._serialized_start=3742
  _PODCASTBADGEPROTO._serialized_end=3888
  _PODCASTVISUALTRANSITIONPROTO._serialized_start=3891
  _PODCASTVISUALTRANSITIONPROTO._serialized_end=4151
  _PODCASTHOSTPROTO._serialized_start=4153
  _PODCASTHOSTPROTO._serialized_end=4263
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
  _CREATEPODCASTRESPONSEDELTAPROTO._serialized_start=1014
  _CREATEPODCASTRESPONSEDELTAPROTO._serialized_end=1181
  _GENERATEPODCASTREQUESTPROTO._serialized_start=1183
  _GENERATEPODCASTREQUESTPROTO._serialized_end=1258
  _GENERATEPODCASTRESPONSEHEADERPROTO._serialized_start=1260
  _GENERATEPODCASTRESPONSEHEADERPROTO._serialized_end=1296
  _GENERATEPODCASTRESPONSEDELTAPROTO._serialized_start=1298
  _GENERATEPODCASTRESPONSEDELTAPROTO._serialized_end=1375
  _LISTPODCASTSREQUESTPROTO._serialized_start=1377
  _LISTPODCASTSREQUESTPROTO._serialized_end=1403
  _LISTPODCASTSRESPONSEHEADERPROTO._serialized_start=1405
  _LISTPODCASTSRESPONSEHEADERPROTO._serialized_end=1471
  _LISTPODCASTSRESPONSEDELTAPROTO._serialized_start=1474
  _LISTPODCASTSRESPONSEDELTAPROTO._serialized_end=1602
  _PODCASTPROTO._serialized_start=1605
  _PODCASTPROTO._serialized_end=2033
  _PODCASTPREVIEWPROTO._serialized_start=2035
  _PODCASTPREVIEWPROTO._serialized_end=2110
  _PODCASTTHUMBNAILPROTO._serialized_start=2112
  _PODCASTTHUMBNAILPROTO._serialized_end=2199
  _PODCASTAUDIOPROTO._serialized_start=2201
  _PODCASTAUDIOPROTO._serialized_end=2279
  _PODCASTCARDSPROTO._serialized_start=2281
  _PODCASTCARDSPROTO._serialized_end=2334
  _PODCASTCARDPROTO._serialized_start=2337
  _PODCASTCARDPROTO._serialized_end=2479
  _PODCASTPROMPTANSWERPROTO._serialized_start=2481
  _PODCASTPROMPTANSWERPROTO._serialized_end=2521
  _PODCASTVISUALSPROTO._serialized_start=2523
  _PODCASTVISUALSPROTO._serialized_end=2582
  _PODCASTVISUALPROTO._serialized_start=2585
  _PODCASTVISUALPROTO._serialized_end=2751
  _PODCASTVISUALANIMATIONPROTO._serialized_start=2753
  _PODCASTVISUALANIMATIONPROTO._serialized_end=2847
  _PODCASTTRANSCRIPTPROTO._serialized_start=2849
  _PODCASTTRANSCRIPTPROTO._serialized_end=2920
  _PODCASTTRANSCRIPTENTRYPROTO._serialized_start=2922
  _PODCASTTRANSCRIPTENTRYPROTO._serialized_end=3018
  _PODCASTWORDPROTO._serialized_start=3020
  _PODCASTWORDPROTO._serialized_end=3113
  _PODCASTKNOWLEDGECARDPROTO._serialized_start=3115
  _PODCASTKNOWLEDGECARDPROTO._serialized_end=3229
  _PODCASTMULTIPLECHOICECARDPROTO._serialized_start=3232
  _PODCASTMULTIPLECHOICECARDPROTO._serialized_end=3453
  _PODCASTPOLLCARDPROTO._serialized_start=3456
  _PODCASTPOLLCARDPROTO._serialized_end=3590
  _PODCASTCARDHEROPROTO._serialized_start=3592
  _PODCASTCARDHEROPROTO._serialized_end=3649
  _PODCASTMULTIPLECHOICEOPTIONPROTO._serialized_start=3651
  _PODCASTMULTIPLECHOICEOPTIONPROTO._serialized_end=3699
  _PODCASTPOLLOPTIONPROTO._serialized_start=3701
  _PODCASTPOLLOPTIONPROTO._serialized_end=3739
# @@protoc_insertion_point(module_scope)
