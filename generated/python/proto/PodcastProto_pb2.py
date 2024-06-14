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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcf\x01\n\x1cPodcastStreamApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12,\n\x06\x63reate\x18\x02 \x01(\x0b\x32\x1a.CreatePodcastRequestProtoH\x00\x12\x30\n\x08generate\x18\x03 \x01(\x0b\x32\x1c.GeneratePodcastRequestProtoH\x00\x12)\n\x04list\x18\x04 \x01(\x0b\x32\x19.ListPodcastsRequestProtoH\x00\x42\t\n\x07request\"\x90\x03\n#PodcastStreamApiResponseHeaderProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12:\n\rcreate_header\x18\x02 \x01(\x0b\x32!.CreatePodcastResponseHeaderProtoH\x00\x12\x37\n\x08generate\x18\x03 \x01(\x0b\x32#.GeneratePodcastResponseHeaderProtoH\x00\x12\x30\n\x04list\x18\x04 \x01(\x0b\x32 .ListPodcastsResponseHeaderProtoH\x00\x12\x46\n\tlatencies\x18\x64 \x03(\x0b\x32\x33.PodcastStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\x08\n\x06header\"\xe5\x01\n\"PodcastStreamApiResponseDeltaProto\x12\x38\n\x0c\x63reate_delta\x18\x01 \x01(\x0b\x32 .CreatePodcastResponseDeltaProtoH\x00\x12<\n\x0egenerate_delta\x18\x02 \x01(\x0b\x32\".GeneratePodcastResponseDeltaProtoH\x00\x12\x35\n\nlist_delta\x18\x03 \x01(\x0b\x32\x1f.ListPodcastsResponseDeltaProtoH\x00\x42\x10\n\x0eresponse_delta\"+\n\x19\x43reatePodcastRequestProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"\"\n CreatePodcastResponseHeaderProto\"\xae\x01\n\x1f\x43reatePodcastResponseDeltaProto\x12\x13\n\tseparator\x18\x01 \x01(\x08H\x00\x12\x18\n\x0e\x65rror_no_topic\x18\x02 \x01(\x08H\x00\x12+\n\x06\x61nswer\x18\n \x01(\x0b\x32\x19.PodcastPromptAnswerProtoH\x00\x12\'\n\x07preview\x18\x0b \x01(\x0b\x32\x14.PodcastPreviewProtoH\x00\x42\x06\n\x04type\"1\n\x1bGeneratePodcastRequestProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"$\n\"GeneratePodcastResponseHeaderProto\"N\n!GeneratePodcastResponseDeltaProto\x12!\n\x04\x63\x61rd\x18\x01 \x01(\x0b\x32\x11.PodcastCardProtoH\x00\x42\x06\n\x04type\"\x1a\n\x18ListPodcastsRequestProto\"B\n\x1fListPodcastsResponseHeaderProto\x12\x1f\n\x08podcasts\x18\x01 \x03(\x0b\x32\r.PodcastProto\"\x80\x01\n\x1eListPodcastsResponseDeltaProto\x12\x0e\n\x04ping\x18\x01 \x01(\x08H\x00\x12(\n\x0fupdated_podcast\x18\x02 \x01(\x0b\x32\r.PodcastProtoH\x00\x12\x1c\n\x12\x64\x65leted_podcast_id\x18\x03 \x01(\tH\x00\x42\x06\n\x04type\"\x82\x03\n\x0cPodcastProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12%\n\x07preview\x18\n \x01(\x0b\x32\x14.PodcastPreviewProto\x12)\n\tthumbnail\x18\x0b \x01(\x0b\x32\x16.PodcastThumbnailProto\x12!\n\x05\x61udio\x18\x0c \x01(\x0b\x32\x12.PodcastAudioProto\x12%\n\x07visuals\x18\r \x01(\x0b\x32\x14.PodcastVisualsProto\x12+\n\ntranscript\x18\x0e \x01(\x0b\x32\x17.PodcastTranscriptProto\x12!\n\x05\x63\x61rds\x18\x0f \x01(\x0b\x32\x12.PodcastCardsProto\"K\n\x13PodcastPreviewProto\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x02 \x01(\t\x12\x10\n\x08synopsis\x18\x03 \x01(\t\"\xae\x01\n\x15PodcastThumbnailProto\x12\r\n\x05title\x18\x01 \x01(\t\x12!\n\x05\x62\x61\x64ge\x18\x02 \x01(\x0e\x32\x12.PodcastBadgeProto\x12\x0c\n\x04path\x18\x03 \x01(\t\x12+\n\x08\x64uration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x10\n\x08is_ready\x18\x05 \x01(\x08\x12\x16\n\x0e\x64isplay_status\x18\x06 \x01(\t\"N\n\x11PodcastAudioProto\x12\x0c\n\x04path\x18\x01 \x01(\t\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"5\n\x11PodcastCardsProto\x12 \n\x05\x63\x61rds\x18\x01 \x03(\x0b\x32\x11.PodcastCardProto\"\xbf\x01\n\x10PodcastCardProto\x12\x0f\n\x07\x63\x61rd_id\x18\x01 \x01(\t\x12/\n\tknowledge\x18\n \x01(\x0b\x32\x1a.PodcastKnowledgeCardProtoH\x00\x12:\n\x0fmultiple_choice\x18\x0b \x01(\x0b\x32\x1f.PodcastMultipleChoiceCardProtoH\x00\x12%\n\x04poll\x18\x0c \x01(\x0b\x32\x15.PodcastPollCardProtoH\x00\x42\x06\n\x04type\"(\n\x18PodcastPromptAnswerProto\x12\x0c\n\x04text\x18\x01 \x01(\t\";\n\x13PodcastVisualsProto\x12$\n\x07visuals\x18\x01 \x03(\x0b\x32\x13.PodcastVisualProto\"\xa6\x01\n\x12PodcastVisualProto\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x05\x12\x12\n\nimage_path\x18\x02 \x01(\t\x12/\n\tanimation\x18\x04 \x01(\x0b\x32\x1c.PodcastVisualAnimationProto\x12\x31\n\ntransition\x18\x03 \x01(\x0e\x32\x1d.PodcastVisualTransitionProto\"^\n\x1bPodcastVisualAnimationProto\x12\x17\n\x0f\x64uration_millis\x18\x01 \x01(\x05\x12\x13\n\x0bstart_scale\x18\x02 \x01(\x02\x12\x11\n\tend_scale\x18\x03 \x01(\x02\"G\n\x16PodcastTranscriptProto\x12-\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1c.PodcastTranscriptEntryProto\"`\n\x1bPodcastTranscriptEntryProto\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12 \n\x05words\x18\x02 \x03(\x0b\x32\x11.PodcastWordProto\"]\n\x10PodcastWordProto\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x14\n\x0cstart_millis\x18\x02 \x01(\x05\x12\x12\n\nend_millis\x18\x03 \x01(\x05\x12\x11\n\tseparator\x18\x04 \x01(\t\"r\n\x19PodcastKnowledgeCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x13\n\x0b\x65xplanation\x18\x04 \x01(\t\"\xdd\x01\n\x1ePodcastMultipleChoiceCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x10\n\x08question\x18\x03 \x01(\t\x12\x32\n\x07options\x18\x04 \x03(\x0b\x32!.PodcastMultipleChoiceOptionProto\x12\x1d\n\x15\x63orrect_answer_number\x18\x05 \x01(\x05\x12\r\n\x05hints\x18\x06 \x03(\t\x12\x13\n\x0b\x65xplanation\x18\x07 \x01(\t\"\x86\x01\n\x14PodcastPollCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x10\n\x08question\x18\x03 \x01(\t\x12(\n\x07options\x18\x04 \x03(\x0b\x32\x17.PodcastPollOptionProto\"9\n\x14PodcastCardHeroProto\x12\r\n\x05\x65moji\x18\x01 \x01(\t\x12\x12\n\nlottie_url\x18\x02 \x01(\t\"0\n PodcastMultipleChoiceOptionProto\x12\x0c\n\x04text\x18\x01 \x01(\t\"&\n\x16PodcastPollOptionProto\x12\x0c\n\x04text\x18\x01 \x01(\t*\x92\x01\n\x11PodcastBadgeProto\x12!\n\x1dPODCAST_BADGE_PROTO_UNDEFINED\x10\x00\x12\x1c\n\x18PODCAST_BADGE_PROTO_NONE\x10\x01\x12\x1e\n\x1aPODCAST_BADGE_PROTO_LISTEN\x10\x02\x12\x1c\n\x18PODCAST_BADGE_PROTO_POLL\x10\x03*\x84\x02\n\x1cPodcastVisualTransitionProto\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_UNDEFINED\x10\x00\x12,\n(PODCAST_VISUAL_TRANSITION_PROTO_DISSOLVE\x10\x01\x12)\n%PODCAST_VISUAL_TRANSITION_PROTO_SWIPE\x10\x02\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_BAR_SWIPE\x10\x03\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_PAGE_CURL\x10\x04*n\n\x10PodcastHostProto\x12\x1e\n\x1aPODCAST_HOST_PROTO_UNKNOWN\x10\x00\x12\x1b\n\x17PODCAST_HOST_PROTO_MALE\x10\x01\x12\x1d\n\x19PODCAST_HOST_PROTO_FEMALE\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PodcastProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _PODCASTBADGEPROTO._serialized_start=3819
  _PODCASTBADGEPROTO._serialized_end=3965
  _PODCASTVISUALTRANSITIONPROTO._serialized_start=3968
  _PODCASTVISUALTRANSITIONPROTO._serialized_end=4228
  _PODCASTHOSTPROTO._serialized_start=4230
  _PODCASTHOSTPROTO._serialized_end=4340
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
  _CREATEPODCASTRESPONSEDELTAPROTO._serialized_end=1188
  _GENERATEPODCASTREQUESTPROTO._serialized_start=1190
  _GENERATEPODCASTREQUESTPROTO._serialized_end=1239
  _GENERATEPODCASTRESPONSEHEADERPROTO._serialized_start=1241
  _GENERATEPODCASTRESPONSEHEADERPROTO._serialized_end=1277
  _GENERATEPODCASTRESPONSEDELTAPROTO._serialized_start=1279
  _GENERATEPODCASTRESPONSEDELTAPROTO._serialized_end=1357
  _LISTPODCASTSREQUESTPROTO._serialized_start=1359
  _LISTPODCASTSREQUESTPROTO._serialized_end=1385
  _LISTPODCASTSRESPONSEHEADERPROTO._serialized_start=1387
  _LISTPODCASTSRESPONSEHEADERPROTO._serialized_end=1453
  _LISTPODCASTSRESPONSEDELTAPROTO._serialized_start=1456
  _LISTPODCASTSRESPONSEDELTAPROTO._serialized_end=1584
  _PODCASTPROTO._serialized_start=1587
  _PODCASTPROTO._serialized_end=1973
  _PODCASTPREVIEWPROTO._serialized_start=1975
  _PODCASTPREVIEWPROTO._serialized_end=2050
  _PODCASTTHUMBNAILPROTO._serialized_start=2053
  _PODCASTTHUMBNAILPROTO._serialized_end=2227
  _PODCASTAUDIOPROTO._serialized_start=2229
  _PODCASTAUDIOPROTO._serialized_end=2307
  _PODCASTCARDSPROTO._serialized_start=2309
  _PODCASTCARDSPROTO._serialized_end=2362
  _PODCASTCARDPROTO._serialized_start=2365
  _PODCASTCARDPROTO._serialized_end=2556
  _PODCASTPROMPTANSWERPROTO._serialized_start=2558
  _PODCASTPROMPTANSWERPROTO._serialized_end=2598
  _PODCASTVISUALSPROTO._serialized_start=2600
  _PODCASTVISUALSPROTO._serialized_end=2659
  _PODCASTVISUALPROTO._serialized_start=2662
  _PODCASTVISUALPROTO._serialized_end=2828
  _PODCASTVISUALANIMATIONPROTO._serialized_start=2830
  _PODCASTVISUALANIMATIONPROTO._serialized_end=2924
  _PODCASTTRANSCRIPTPROTO._serialized_start=2926
  _PODCASTTRANSCRIPTPROTO._serialized_end=2997
  _PODCASTTRANSCRIPTENTRYPROTO._serialized_start=2999
  _PODCASTTRANSCRIPTENTRYPROTO._serialized_end=3095
  _PODCASTWORDPROTO._serialized_start=3097
  _PODCASTWORDPROTO._serialized_end=3190
  _PODCASTKNOWLEDGECARDPROTO._serialized_start=3192
  _PODCASTKNOWLEDGECARDPROTO._serialized_end=3306
  _PODCASTMULTIPLECHOICECARDPROTO._serialized_start=3309
  _PODCASTMULTIPLECHOICECARDPROTO._serialized_end=3530
  _PODCASTPOLLCARDPROTO._serialized_start=3533
  _PODCASTPOLLCARDPROTO._serialized_end=3667
  _PODCASTCARDHEROPROTO._serialized_start=3669
  _PODCASTCARDHEROPROTO._serialized_end=3726
  _PODCASTMULTIPLECHOICEOPTIONPROTO._serialized_start=3728
  _PODCASTMULTIPLECHOICEOPTIONPROTO._serialized_end=3776
  _PODCASTPOLLOPTIONPROTO._serialized_start=3778
  _PODCASTPOLLOPTIONPROTO._serialized_end=3816
# @@protoc_insertion_point(module_scope)
