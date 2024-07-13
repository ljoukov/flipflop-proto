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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x87\x02\n\x1cPodcastStreamApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12,\n\x06\x63reate\x18\x02 \x01(\x0b\x32\x1a.CreatePodcastRequestProtoH\x00\x12\x30\n\x08generate\x18\x03 \x01(\x0b\x32\x1c.GeneratePodcastRequestProtoH\x00\x12&\n\x03get\x18\x04 \x01(\x0b\x32\x17.GetPodcastRequestProtoH\x00\x12\x39\n\x0bsuggestions\x18\x05 \x01(\x0b\x32\".GetPodcastSuggestionsRequestProtoH\x00\x42\t\n\x07request\"\xcf\x03\n#PodcastStreamApiResponseHeaderProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12:\n\rcreate_header\x18\x02 \x01(\x0b\x32!.CreatePodcastResponseHeaderProtoH\x00\x12\x37\n\x08generate\x18\x03 \x01(\x0b\x32#.GeneratePodcastResponseHeaderProtoH\x00\x12-\n\x03get\x18\x04 \x01(\x0b\x32\x1e.GetPodcastResponseHeaderProtoH\x00\x12@\n\x0bsuggestions\x18\x05 \x01(\x0b\x32).GetPodcastSuggestionsResponseHeaderProtoH\x00\x12\x46\n\tlatencies\x18\x64 \x03(\x0b\x32\x33.PodcastStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\x08\n\x06header\"\xa9\x02\n\"PodcastStreamApiResponseDeltaProto\x12\x38\n\x0c\x63reate_delta\x18\x01 \x01(\x0b\x32 .CreatePodcastResponseDeltaProtoH\x00\x12<\n\x0egenerate_delta\x18\x02 \x01(\x0b\x32\".GeneratePodcastResponseDeltaProtoH\x00\x12\x32\n\tget_delta\x18\x03 \x01(\x0b\x32\x1d.GetPodcastResponseDeltaProtoH\x00\x12\x45\n\x11suggestions_delta\x18\x05 \x01(\x0b\x32(.GetPodcastSuggestionsResponseDeltaProtoH\x00\x42\x10\n\x0eresponse_delta\"+\n\x19\x43reatePodcastRequestProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"6\n CreatePodcastResponseHeaderProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"\xa0\x01\n\x1f\x43reatePodcastResponseDeltaProto\x12#\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x12.PodcastErrorProtoH\x00\x12+\n\x06\x61nswer\x18\x02 \x01(\x0b\x32\x19.PodcastPromptAnswerProtoH\x00\x12#\n\x05point\x18\x03 \x01(\x0b\x32\x12.PodcastPointProtoH\x00\x42\x06\n\x04type\"\x93\x01\n\x1bGeneratePodcastRequestProto\x12\x31\n\x06points\x18\x01 \x01(\x0b\x32\x1f.GeneratePodcastFromPointsProtoH\x00\x12\x39\n\nsuggestion\x18\x02 \x01(\x0b\x32#.GeneratePodcastFromSuggestionProtoH\x00\x42\x06\n\x04type\"G\n\x1eGeneratePodcastFromPointsProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x11\n\tpoint_ids\x18\x02 \x03(\t\"Z\n\"GeneratePodcastFromSuggestionProto\x12\x16\n\x0esuggestions_id\x18\x01 \x01(\t\x12\x1c\n\x14suggested_podcast_id\x18\x02 \x01(\t\"$\n\"GeneratePodcastResponseHeaderProto\"N\n!GeneratePodcastResponseDeltaProto\x12!\n\x04\x63\x61rd\x18\x01 \x01(\x0b\x32\x11.PodcastCardProtoH\x00\x42\x06\n\x04type\",\n\x16GetPodcastRequestProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"?\n\x1dGetPodcastResponseHeaderProto\x12\x1e\n\x07podcast\x18\x01 \x01(\x0b\x32\r.PodcastProto\"\x1e\n\x1cGetPodcastResponseDeltaProto\"#\n!GetPodcastSuggestionsRequestProto\"Y\n(GetPodcastSuggestionsResponseHeaderProto\x12-\n\x0bsuggestions\x18\x01 \x01(\x0b\x32\x18.PodcastSuggestionsProto\")\n\'GetPodcastSuggestionsResponseDeltaProto\"\xda\x02\n\x0cPodcastProto\x12.\n\nupdated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\tthumbnail\x18\x02 \x01(\x0b\x32\x16.PodcastThumbnailProto\x12!\n\x05\x61udio\x18\x03 \x01(\x0b\x32\x12.PodcastAudioProto\x12%\n\x07visuals\x18\x04 \x01(\x0b\x32\x14.PodcastVisualsProto\x12+\n\ntranscript\x18\x05 \x01(\x0b\x32\x17.PodcastTranscriptProto\x12!\n\x05\x63\x61rds\x18\x06 \x01(\x0b\x32\x12.PodcastCardsProto\x12*\n\nkey_points\x18\x07 \x01(\x0b\x32\x16.PodcastKeyPointsProto\x12)\n\tfollowups\x18\x08 \x01(\x0b\x32\x16.PodcastFollowupsProto\"r\n\x15\x46irestorePodcastProto\x12.\n\nupdated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\tthumbnail\x18\x02 \x01(\x0b\x32\x16.PodcastThumbnailProto\"\xb1\x01\n\x1a\x46irestorePodcastsHomeProto\x12.\n\nupdated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x13your_podcasts_shelf\x18\x02 \x01(\x0b\x32\x17.YourPodcastsShelfProto\x12-\n\x0bsuggestions\x18\x03 \x01(\x0b\x32\x18.PodcastSuggestionsProto\"D\n\x16YourPodcastsShelfProto\x12*\n\nthumbnails\x18\x01 \x03(\x0b\x32\x16.PodcastThumbnailProto\"Z\n\x11PodcastPointProto\x12\x10\n\x08point_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"\xc1\x01\n\x15PodcastThumbnailProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12#\n\x06status\x18\x02 \x01(\x0e\x32\x13.PodcastStatusProto\x12\x16\n\x0e\x64isplay_status\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x05 \x01(\t\x12\x0c\n\x04path\x18\x06 \x01(\t\x12+\n\x08\x64uration\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\"N\n\x11PodcastAudioProto\x12\x0c\n\x04path\x18\x01 \x01(\t\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"G\n\x11PodcastCardsProto\x12\x10\n\x08is_ready\x18\x01 \x01(\x08\x12 \n\x05\x63\x61rds\x18\x02 \x03(\x0b\x32\x11.PodcastCardProto\"\xd1\x01\n\x10PodcastCardProto\x12\x0f\n\x07\x63\x61rd_id\x18\x01 \x01(\t\x12\x10\n\x08is_ready\x18\x02 \x01(\x08\x12/\n\tknowledge\x18\n \x01(\x0b\x32\x1a.PodcastKnowledgeCardProtoH\x00\x12:\n\x0fmultiple_choice\x18\x0b \x01(\x0b\x32\x1f.PodcastMultipleChoiceCardProtoH\x00\x12%\n\x04poll\x18\x0c \x01(\x0b\x32\x15.PodcastPollCardProtoH\x00\x42\x06\n\x04type\"$\n\x11PodcastErrorProto\x12\x0f\n\x07message\x18\x01 \x01(\t\"(\n\x18PodcastPromptAnswerProto\x12\x0c\n\x04text\x18\x01 \x01(\t\";\n\x13PodcastVisualsProto\x12$\n\x07visuals\x18\x01 \x03(\x0b\x32\x13.PodcastVisualProto\"\xa6\x01\n\x12PodcastVisualProto\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x05\x12\x12\n\nimage_path\x18\x02 \x01(\t\x12/\n\tanimation\x18\x04 \x01(\x0b\x32\x1c.PodcastVisualAnimationProto\x12\x31\n\ntransition\x18\x03 \x01(\x0e\x32\x1d.PodcastVisualTransitionProto\"^\n\x1bPodcastVisualAnimationProto\x12\x17\n\x0f\x64uration_millis\x18\x01 \x01(\x05\x12\x13\n\x0bstart_scale\x18\x02 \x01(\x02\x12\x11\n\tend_scale\x18\x03 \x01(\x02\"G\n\x16PodcastTranscriptProto\x12-\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1c.PodcastTranscriptEntryProto\"`\n\x1bPodcastTranscriptEntryProto\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12 \n\x05words\x18\x02 \x03(\x0b\x32\x11.PodcastWordProto\"]\n\x10PodcastWordProto\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x14\n\x0cstart_millis\x18\x02 \x01(\x05\x12\x12\n\nend_millis\x18\x03 \x01(\x05\x12\x11\n\tseparator\x18\x04 \x01(\t\"r\n\x19PodcastKnowledgeCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x13\n\x0b\x65xplanation\x18\x04 \x01(\t\"\xdd\x01\n\x1ePodcastMultipleChoiceCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x10\n\x08question\x18\x03 \x01(\t\x12\x32\n\x07options\x18\x04 \x03(\x0b\x32!.PodcastMultipleChoiceOptionProto\x12\x1d\n\x15\x63orrect_answer_number\x18\x05 \x01(\x05\x12\r\n\x05hints\x18\x06 \x03(\t\x12\x13\n\x0b\x65xplanation\x18\x07 \x01(\t\"\x86\x01\n\x14PodcastPollCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x10\n\x08question\x18\x03 \x01(\t\x12(\n\x07options\x18\x04 \x03(\x0b\x32\x17.PodcastPollOptionProto\"9\n\x14PodcastCardHeroProto\x12\r\n\x05\x65moji\x18\x01 \x01(\t\x12\x12\n\nlottie_url\x18\x02 \x01(\t\"0\n PodcastMultipleChoiceOptionProto\x12\x0c\n\x04text\x18\x01 \x01(\t\"&\n\x16PodcastPollOptionProto\x12\x0c\n\x04text\x18\x01 \x01(\t\"Q\n\x15PodcastKeyPointsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12)\n\nkey_points\x18\x02 \x03(\x0b\x32\x15.PodcastKeyPointProto\"P\n\x15PodcastFollowupsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12(\n\tfollowups\x18\x02 \x03(\x0b\x32\x15.PodcastFollowupProto\"K\n\x14PodcastFollowupProto\x12\x13\n\x0b\x66ollowup_id\x18\x01 \x01(\t\x12\r\n\x05\x65moji\x18\x02 \x01(\t\x12\x0f\n\x07outline\x18\x03 \x01(\t\"a\n\x14PodcastKeyPointProto\x12\x14\n\x0ckey_point_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"\x94\x01\n\x17PodcastSuggestionsProto\x12\x16\n\x0esuggestions_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x08sections\x18\x03 \x03(\x0b\x32\x1f.PodcastSuggestionsSectionProto\"\xf9\x01\n\x1ePodcastSuggestionsSectionProto\x12\x12\n\nsection_id\x18\x01 \x01(\t\x12\x15\n\rsection_title\x18\x02 \x01(\t\x12\x31\n\x11\x62\x61nner_suggestion\x18\x03 \x01(\x0b\x32\x16.PodcastThumbnailProto\x12\x31\n\x11\x66ooter_suggestion\x18\x04 \x01(\x0b\x32\x16.PodcastThumbnailProto\x12\"\n\x06story1\x18\x05 \x01(\x0b\x32\x12.PodcastStoryProto\x12\"\n\x06story2\x18\x06 \x01(\x0b\x32\x12.PodcastStoryProto\"T\n\x11PodcastStoryProto\x12\x18\n\x10podcast_story_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x16\n\x0ethumbnail_path\x18\x03 \x01(\t*\x9e\x01\n\x12PodcastStatusProto\x12\"\n\x1ePODCAST_STATUS_PROTO_UNDEFINED\x10\x00\x12#\n\x1fPODCAST_STATUS_PROTO_GENERATING\x10\x01\x12\x1e\n\x1aPODCAST_STATUS_PROTO_READY\x10\x02\x12\x1f\n\x1bPODCAST_STATUS_PROTO_FAILED\x10\x03*\x84\x02\n\x1cPodcastVisualTransitionProto\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_UNDEFINED\x10\x00\x12,\n(PODCAST_VISUAL_TRANSITION_PROTO_DISSOLVE\x10\x01\x12)\n%PODCAST_VISUAL_TRANSITION_PROTO_SWIPE\x10\x02\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_BAR_SWIPE\x10\x03\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_PAGE_CURL\x10\x04*n\n\x10PodcastHostProto\x12\x1e\n\x1aPODCAST_HOST_PROTO_UNKNOWN\x10\x00\x12\x1b\n\x17PODCAST_HOST_PROTO_MALE\x10\x01\x12\x1d\n\x19PODCAST_HOST_PROTO_FEMALE\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PodcastProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._options = None
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _PODCASTSTATUSPROTO._serialized_start=5627
  _PODCASTSTATUSPROTO._serialized_end=5785
  _PODCASTVISUALTRANSITIONPROTO._serialized_start=5788
  _PODCASTVISUALTRANSITIONPROTO._serialized_end=6048
  _PODCASTHOSTPROTO._serialized_start=6050
  _PODCASTHOSTPROTO._serialized_end=6160
  _PODCASTSTREAMAPIREQUESTPROTO._serialized_start=88
  _PODCASTSTREAMAPIREQUESTPROTO._serialized_end=351
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO._serialized_start=354
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO._serialized_end=817
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_start=732
  _PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_end=807
  _PODCASTSTREAMAPIRESPONSEDELTAPROTO._serialized_start=820
  _PODCASTSTREAMAPIRESPONSEDELTAPROTO._serialized_end=1117
  _CREATEPODCASTREQUESTPROTO._serialized_start=1119
  _CREATEPODCASTREQUESTPROTO._serialized_end=1162
  _CREATEPODCASTRESPONSEHEADERPROTO._serialized_start=1164
  _CREATEPODCASTRESPONSEHEADERPROTO._serialized_end=1218
  _CREATEPODCASTRESPONSEDELTAPROTO._serialized_start=1221
  _CREATEPODCASTRESPONSEDELTAPROTO._serialized_end=1381
  _GENERATEPODCASTREQUESTPROTO._serialized_start=1384
  _GENERATEPODCASTREQUESTPROTO._serialized_end=1531
  _GENERATEPODCASTFROMPOINTSPROTO._serialized_start=1533
  _GENERATEPODCASTFROMPOINTSPROTO._serialized_end=1604
  _GENERATEPODCASTFROMSUGGESTIONPROTO._serialized_start=1606
  _GENERATEPODCASTFROMSUGGESTIONPROTO._serialized_end=1696
  _GENERATEPODCASTRESPONSEHEADERPROTO._serialized_start=1698
  _GENERATEPODCASTRESPONSEHEADERPROTO._serialized_end=1734
  _GENERATEPODCASTRESPONSEDELTAPROTO._serialized_start=1736
  _GENERATEPODCASTRESPONSEDELTAPROTO._serialized_end=1814
  _GETPODCASTREQUESTPROTO._serialized_start=1816
  _GETPODCASTREQUESTPROTO._serialized_end=1860
  _GETPODCASTRESPONSEHEADERPROTO._serialized_start=1862
  _GETPODCASTRESPONSEHEADERPROTO._serialized_end=1925
  _GETPODCASTRESPONSEDELTAPROTO._serialized_start=1927
  _GETPODCASTRESPONSEDELTAPROTO._serialized_end=1957
  _GETPODCASTSUGGESTIONSREQUESTPROTO._serialized_start=1959
  _GETPODCASTSUGGESTIONSREQUESTPROTO._serialized_end=1994
  _GETPODCASTSUGGESTIONSRESPONSEHEADERPROTO._serialized_start=1996
  _GETPODCASTSUGGESTIONSRESPONSEHEADERPROTO._serialized_end=2085
  _GETPODCASTSUGGESTIONSRESPONSEDELTAPROTO._serialized_start=2087
  _GETPODCASTSUGGESTIONSRESPONSEDELTAPROTO._serialized_end=2128
  _PODCASTPROTO._serialized_start=2131
  _PODCASTPROTO._serialized_end=2477
  _FIRESTOREPODCASTPROTO._serialized_start=2479
  _FIRESTOREPODCASTPROTO._serialized_end=2593
  _FIRESTOREPODCASTSHOMEPROTO._serialized_start=2596
  _FIRESTOREPODCASTSHOMEPROTO._serialized_end=2773
  _YOURPODCASTSSHELFPROTO._serialized_start=2775
  _YOURPODCASTSSHELFPROTO._serialized_end=2843
  _PODCASTPOINTPROTO._serialized_start=2845
  _PODCASTPOINTPROTO._serialized_end=2935
  _PODCASTTHUMBNAILPROTO._serialized_start=2938
  _PODCASTTHUMBNAILPROTO._serialized_end=3131
  _PODCASTAUDIOPROTO._serialized_start=3133
  _PODCASTAUDIOPROTO._serialized_end=3211
  _PODCASTCARDSPROTO._serialized_start=3213
  _PODCASTCARDSPROTO._serialized_end=3284
  _PODCASTCARDPROTO._serialized_start=3287
  _PODCASTCARDPROTO._serialized_end=3496
  _PODCASTERRORPROTO._serialized_start=3498
  _PODCASTERRORPROTO._serialized_end=3534
  _PODCASTPROMPTANSWERPROTO._serialized_start=3536
  _PODCASTPROMPTANSWERPROTO._serialized_end=3576
  _PODCASTVISUALSPROTO._serialized_start=3578
  _PODCASTVISUALSPROTO._serialized_end=3637
  _PODCASTVISUALPROTO._serialized_start=3640
  _PODCASTVISUALPROTO._serialized_end=3806
  _PODCASTVISUALANIMATIONPROTO._serialized_start=3808
  _PODCASTVISUALANIMATIONPROTO._serialized_end=3902
  _PODCASTTRANSCRIPTPROTO._serialized_start=3904
  _PODCASTTRANSCRIPTPROTO._serialized_end=3975
  _PODCASTTRANSCRIPTENTRYPROTO._serialized_start=3977
  _PODCASTTRANSCRIPTENTRYPROTO._serialized_end=4073
  _PODCASTWORDPROTO._serialized_start=4075
  _PODCASTWORDPROTO._serialized_end=4168
  _PODCASTKNOWLEDGECARDPROTO._serialized_start=4170
  _PODCASTKNOWLEDGECARDPROTO._serialized_end=4284
  _PODCASTMULTIPLECHOICECARDPROTO._serialized_start=4287
  _PODCASTMULTIPLECHOICECARDPROTO._serialized_end=4508
  _PODCASTPOLLCARDPROTO._serialized_start=4511
  _PODCASTPOLLCARDPROTO._serialized_end=4645
  _PODCASTCARDHEROPROTO._serialized_start=4647
  _PODCASTCARDHEROPROTO._serialized_end=4704
  _PODCASTMULTIPLECHOICEOPTIONPROTO._serialized_start=4706
  _PODCASTMULTIPLECHOICEOPTIONPROTO._serialized_end=4754
  _PODCASTPOLLOPTIONPROTO._serialized_start=4756
  _PODCASTPOLLOPTIONPROTO._serialized_end=4794
  _PODCASTKEYPOINTSPROTO._serialized_start=4796
  _PODCASTKEYPOINTSPROTO._serialized_end=4877
  _PODCASTFOLLOWUPSPROTO._serialized_start=4879
  _PODCASTFOLLOWUPSPROTO._serialized_end=4959
  _PODCASTFOLLOWUPPROTO._serialized_start=4961
  _PODCASTFOLLOWUPPROTO._serialized_end=5036
  _PODCASTKEYPOINTPROTO._serialized_start=5038
  _PODCASTKEYPOINTPROTO._serialized_end=5135
  _PODCASTSUGGESTIONSPROTO._serialized_start=5138
  _PODCASTSUGGESTIONSPROTO._serialized_end=5286
  _PODCASTSUGGESTIONSSECTIONPROTO._serialized_start=5289
  _PODCASTSUGGESTIONSSECTIONPROTO._serialized_end=5538
  _PODCASTSTORYPROTO._serialized_start=5540
  _PODCASTSTORYPROTO._serialized_end=5624
# @@protoc_insertion_point(module_scope)
