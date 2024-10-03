# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: PodcastProto.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'PodcastProto.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa0\x01\n\x17PodcastRequestAuthProto\x12\x19\n\x11\x66irebase_id_token\x18\x01 \x01(\t\x12\x16\n\x0e\x61ppcheck_token\x18\x02 \x01(\t\x12\x14\n\x0cis_anonomous\x18\x03 \x01(\x08\x12<\n\rsubscriptions\x18\x04 \x01(\x0b\x32%.PodcastSubscriptionTransactionsProto\"\xf8\x03\n\x1cPodcastStreamApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12.\n\x0crequest_auth\x18\x64 \x01(\x0b\x32\x18.PodcastRequestAuthProto\x12,\n\x06\x63reate\x18\x02 \x01(\x0b\x32\x1a.CreatePodcastRequestProtoH\x00\x12\x30\n\x08generate\x18\x03 \x01(\x0b\x32\x1c.GeneratePodcastRequestProtoH\x00\x12*\n\x07podcast\x18\x04 \x01(\x0b\x32\x17.GetPodcastRequestProtoH\x00\x12-\n\x05story\x18\x05 \x01(\x0b\x32\x1c.GetPodcastStoryRequestProtoH\x00\x12=\n\x11suggestion_points\x18\x06 \x01(\x0b\x32 .GetPodcastSuggestionPointsProtoH\x00\x12\x45\n\x13refresh_suggestions\x18\x07 \x01(\x0b\x32&.RefreshPodcastSuggestionsRequestProtoH\x00\x12\x41\n\x11\x61pply_transaction\x18\x08 \x01(\x0b\x32$.ApplyPodcastTransactionRequestProtoH\x00\x42\t\n\x07request\"\xba\x05\n#PodcastStreamApiResponseHeaderProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12:\n\rcreate_header\x18\x02 \x01(\x0b\x32!.CreatePodcastResponseHeaderProtoH\x00\x12\x37\n\x08generate\x18\x03 \x01(\x0b\x32#.GeneratePodcastResponseHeaderProtoH\x00\x12\x31\n\x07podcast\x18\x04 \x01(\x0b\x32\x1e.GetPodcastResponseHeaderProtoH\x00\x12;\n\x0cstory_header\x18\x05 \x01(\x0b\x32#.GetPodcastStoryResponseHeaderProtoH\x00\x12R\n\x18suggestion_points_header\x18\x06 \x01(\x0b\x32..GetPodcastSuggestionPointsResponseHeaderProtoH\x00\x12L\n\x13refresh_suggestions\x18\x07 \x01(\x0b\x32-.RefreshPodcastSuggestionsResponseHeaderProtoH\x00\x12H\n\x11\x61pply_transaction\x18\x08 \x01(\x0b\x32+.ApplyPodcastTransactionResponseHeaderProtoH\x00\x12\x46\n\tlatencies\x18\x64 \x03(\x0b\x32\x33.PodcastStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\x08\n\x06header\"\x89\x04\n\"PodcastStreamApiResponseDeltaProto\x12\x38\n\x0c\x63reate_delta\x18\x01 \x01(\x0b\x32 .CreatePodcastResponseDeltaProtoH\x00\x12<\n\x0egenerate_delta\x18\x02 \x01(\x0b\x32\".GeneratePodcastResponseDeltaProtoH\x00\x12\x36\n\rpodcast_delta\x18\x03 \x01(\x0b\x32\x1d.GetPodcastResponseDeltaProtoH\x00\x12\x39\n\x0bstory_delta\x18\x04 \x01(\x0b\x32\".GetPodcastStoryResponseDeltaProtoH\x00\x12P\n\x17suggestion_points_delta\x18\x06 \x01(\x0b\x32-.GetPodcastSuggestionPointsResponseDeltaProtoH\x00\x12K\n\x13refresh_suggestions\x18\x07 \x01(\x0b\x32,.RefreshPodcastSuggestionsResponseDeltaProtoH\x00\x12G\n\x11\x61pply_transaction\x18\x08 \x01(\x0b\x32*.ApplyPodcastTransactionResponseDeltaProtoH\x00\x42\x10\n\x0eresponse_delta\"+\n\x19\x43reatePodcastRequestProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"6\n CreatePodcastResponseHeaderProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"\xa0\x01\n\x1f\x43reatePodcastResponseDeltaProto\x12#\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x12.PodcastErrorProtoH\x00\x12+\n\x06\x61nswer\x18\x02 \x01(\x0b\x32\x19.PodcastPromptAnswerProtoH\x00\x12#\n\x05point\x18\x03 \x01(\x0b\x32\x12.PodcastPointProtoH\x00\x42\x06\n\x04type\"\x93\x01\n\x1bGeneratePodcastRequestProto\x12\x31\n\x06points\x18\x01 \x01(\x0b\x32\x1f.GeneratePodcastFromPointsProtoH\x00\x12\x39\n\nsuggestion\x18\x02 \x01(\x0b\x32#.GeneratePodcastFromSuggestionProtoH\x00\x42\x06\n\x04type\"G\n\x1eGeneratePodcastFromPointsProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x11\n\tpoint_ids\x18\x02 \x03(\t\"K\n\"GeneratePodcastFromSuggestionProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x11\n\tpoint_ids\x18\x02 \x03(\t\"$\n\"GeneratePodcastResponseHeaderProto\"N\n!GeneratePodcastResponseDeltaProto\x12!\n\x04\x63\x61rd\x18\x01 \x01(\x0b\x32\x11.PodcastCardProtoH\x00\x42\x06\n\x04type\",\n\x16GetPodcastRequestProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"?\n\x1dGetPodcastResponseHeaderProto\x12\x1e\n\x07podcast\x18\x01 \x01(\x0b\x32\r.PodcastProto\"\x1e\n\x1cGetPodcastResponseDeltaProto\"/\n\x1bGetPodcastStoryRequestProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\"$\n\"GetPodcastStoryResponseHeaderProto\"\x81\x01\n!GetPodcastStoryResponseDeltaProto\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x18.PodcastStoryHeaderProtoH\x00\x12(\n\x05slide\x18\x02 \x01(\x0b\x32\x17.PodcastStorySlideProtoH\x00\x42\x06\n\x04type\"5\n\x1fGetPodcastSuggestionPointsProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"/\n-GetPodcastSuggestionPointsResponseHeaderProto\"[\n,GetPodcastSuggestionPointsResponseDeltaProto\x12#\n\x05point\x18\x01 \x01(\x0b\x32\x12.PodcastPointProtoH\x00\x42\x06\n\x04type\"\'\n%RefreshPodcastSuggestionsRequestProto\".\n,RefreshPodcastSuggestionsResponseHeaderProto\"-\n+RefreshPodcastSuggestionsResponseDeltaProto\"p\n#ApplyPodcastTransactionRequestProto\x12\x41\n\x15\x61pp_store_transaction\x18\x01 \x01(\x0b\x32 .PodcastAppStoreTransactionProtoH\x00\x42\x06\n\x04type\",\n*ApplyPodcastTransactionResponseHeaderProto\"+\n)ApplyPodcastTransactionResponseDeltaProto\"\xda\x02\n\x0cPodcastProto\x12.\n\nupdated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\tthumbnail\x18\x02 \x01(\x0b\x32\x16.PodcastThumbnailProto\x12!\n\x05\x61udio\x18\x03 \x01(\x0b\x32\x12.PodcastAudioProto\x12%\n\x07visuals\x18\x04 \x01(\x0b\x32\x14.PodcastVisualsProto\x12+\n\ntranscript\x18\x05 \x01(\x0b\x32\x17.PodcastTranscriptProto\x12!\n\x05\x63\x61rds\x18\x06 \x01(\x0b\x32\x12.PodcastCardsProto\x12*\n\nkey_points\x18\x07 \x01(\x0b\x32\x16.PodcastKeyPointsProto\x12)\n\tfollowups\x18\x08 \x01(\x0b\x32\x16.PodcastFollowupsProto\"\xf1\x01\n FirestorePodcastSuggestionsProto\x12.\n\nupdated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x13your_podcasts_shelf\x18\x02 \x01(\x0b\x32\x17.YourPodcastsShelfProto\x12-\n\x0bsuggestions\x18\x03 \x01(\x0b\x32\x18.PodcastSuggestionsProto\x12\x38\n\x11query_completions\x18\x04 \x01(\x0b\x32\x1d.PodcastQueryCompletionsProto\"\xa0\x01\n\x16YourPodcastsShelfProto\x12;\n\nthumbnails\x18\x01 \x03(\x0b\x32\'.YourPodcastsShelfProto.ThumbnailsEntry\x1aI\n\x0fThumbnailsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.PodcastThumbnailProto:\x02\x38\x01\"Z\n\x11PodcastPointProto\x12\x10\n\x08point_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"\x85\x02\n\x15PodcastThumbnailProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12#\n\x06status\x18\x02 \x01(\x0e\x32\x13.PodcastStatusProto\x12\x16\n\x0e\x64isplay_status\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x12\n\nlong_title\x18\t \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x05 \x01(\t\x12\x0c\n\x04path\x18\x06 \x01(\t\x12+\n\x08\x64uration\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"N\n\x11PodcastAudioProto\x12\x0c\n\x04path\x18\x01 \x01(\t\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"G\n\x11PodcastCardsProto\x12\x10\n\x08is_ready\x18\x01 \x01(\x08\x12 \n\x05\x63\x61rds\x18\x02 \x03(\x0b\x32\x11.PodcastCardProto\"\xd1\x01\n\x10PodcastCardProto\x12\x0f\n\x07\x63\x61rd_id\x18\x01 \x01(\t\x12\x10\n\x08is_ready\x18\x02 \x01(\x08\x12/\n\tknowledge\x18\n \x01(\x0b\x32\x1a.PodcastKnowledgeCardProtoH\x00\x12:\n\x0fmultiple_choice\x18\x0b \x01(\x0b\x32\x1f.PodcastMultipleChoiceCardProtoH\x00\x12%\n\x04poll\x18\x0c \x01(\x0b\x32\x15.PodcastPollCardProtoH\x00\x42\x06\n\x04type\"$\n\x11PodcastErrorProto\x12\x0f\n\x07message\x18\x01 \x01(\t\"(\n\x18PodcastPromptAnswerProto\x12\x0c\n\x04text\x18\x01 \x01(\t\";\n\x13PodcastVisualsProto\x12$\n\x07visuals\x18\x01 \x03(\x0b\x32\x13.PodcastVisualProto\"\xa6\x01\n\x12PodcastVisualProto\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x05\x12\x12\n\nimage_path\x18\x02 \x01(\t\x12/\n\tanimation\x18\x04 \x01(\x0b\x32\x1c.PodcastVisualAnimationProto\x12\x31\n\ntransition\x18\x03 \x01(\x0e\x32\x1d.PodcastVisualTransitionProto\"^\n\x1bPodcastVisualAnimationProto\x12\x17\n\x0f\x64uration_millis\x18\x01 \x01(\x05\x12\x13\n\x0bstart_scale\x18\x02 \x01(\x02\x12\x11\n\tend_scale\x18\x03 \x01(\x02\"G\n\x16PodcastTranscriptProto\x12-\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1c.PodcastTranscriptEntryProto\"`\n\x1bPodcastTranscriptEntryProto\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12 \n\x05words\x18\x02 \x03(\x0b\x32\x11.PodcastWordProto\"]\n\x10PodcastWordProto\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x14\n\x0cstart_millis\x18\x02 \x01(\x05\x12\x12\n\nend_millis\x18\x03 \x01(\x05\x12\x11\n\tseparator\x18\x04 \x01(\t\"r\n\x19PodcastKnowledgeCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x13\n\x0b\x65xplanation\x18\x04 \x01(\t\"\xdd\x01\n\x1ePodcastMultipleChoiceCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x10\n\x08question\x18\x03 \x01(\t\x12\x32\n\x07options\x18\x04 \x03(\x0b\x32!.PodcastMultipleChoiceOptionProto\x12\x1d\n\x15\x63orrect_answer_number\x18\x05 \x01(\x05\x12\r\n\x05hints\x18\x06 \x03(\t\x12\x13\n\x0b\x65xplanation\x18\x07 \x01(\t\"\x86\x01\n\x14PodcastPollCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x10\n\x08question\x18\x03 \x01(\t\x12(\n\x07options\x18\x04 \x03(\x0b\x32\x17.PodcastPollOptionProto\"9\n\x14PodcastCardHeroProto\x12\r\n\x05\x65moji\x18\x01 \x01(\t\x12\x12\n\nlottie_url\x18\x02 \x01(\t\"0\n PodcastMultipleChoiceOptionProto\x12\x0c\n\x04text\x18\x01 \x01(\t\"&\n\x16PodcastPollOptionProto\x12\x0c\n\x04text\x18\x01 \x01(\t\"Q\n\x15PodcastKeyPointsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12)\n\nkey_points\x18\x02 \x03(\x0b\x32\x15.PodcastKeyPointProto\"P\n\x15PodcastFollowupsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12(\n\tfollowups\x18\x02 \x03(\x0b\x32\x15.PodcastFollowupProto\"K\n\x14PodcastFollowupProto\x12\x13\n\x0b\x66ollowup_id\x18\x01 \x01(\t\x12\r\n\x05\x65moji\x18\x02 \x01(\t\x12\x0f\n\x07outline\x18\x03 \x01(\t\"a\n\x14PodcastKeyPointProto\x12\x14\n\x0ckey_point_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"\xbb\x01\n\x17PodcastSuggestionsProto\x12\x16\n\x0esuggestions_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x08sections\x18\x03 \x03(\x0b\x32\x1f.PodcastSuggestionsSectionProto\x12%\n\x07routine\x18\x04 \x01(\x0b\x32\x14.PodcastRoutineProto\"\x8b\x02\n\x1ePodcastSuggestionsSectionProto\x12\x12\n\nsection_id\x18\x01 \x01(\t\x12\x15\n\rsection_title\x18\x02 \x01(\t\x12\x31\n\x11\x62\x61nner_suggestion\x18\x03 \x01(\x0b\x32\x16.PodcastThumbnailProto\x12\x31\n\x11\x66ooter_suggestion\x18\x04 \x01(\x0b\x32\x16.PodcastThumbnailProto\x12+\n\x06story1\x18\x05 \x01(\x0b\x32\x1b.PodcastStoryThumbnailProto\x12+\n\x06story2\x18\x06 \x01(\x0b\x32\x1b.PodcastStoryThumbnailProto\"W\n\x1cPodcastQueryCompletionsProto\x12\x37\n\x11query_completions\x18\x01 \x03(\x0b\x32\x1c.PodcastQueryCompletionProto\",\n\x1bPodcastQueryCompletionProto\x12\r\n\x05query\x18\x01 \x01(\t\"U\n\x1aPodcastStoryThumbnailProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x16\n\x0ethumbnail_path\x18\x03 \x01(\t\"(\n\x17PodcastStoryHeaderProto\x12\r\n\x05\x62\x61\x64ge\x18\x01 \x01(\t\"r\n\x16PodcastStorySlideProto\x12\x10\n\x08slide_id\x18\x01 \x01(\t\x12\x15\n\ris_text_ready\x18\x02 \x01(\x08\x12\r\n\x05title\x18\x03 \x01(\t\x12\x12\n\nimage_path\x18\x04 \x01(\t\x12\x0c\n\x04text\x18\x05 \x01(\t\"D\n\x13PodcastRoutineProto\x12-\n\x08segments\x18\x01 \x03(\x0b\x32\x1b.PodcastRoutineSegmentProto\"h\n\x1aPodcastRoutineSegmentProto\x12\x12\n\nsegment_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\'\n\x05steps\x18\x03 \x03(\x0b\x32\x18.PodcastRoutineStepProto\"Q\n\x17PodcastRoutineStepProto\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07outline\x18\x02 \x01(\t\x12\x16\n\x0ethumbnail_path\x18\x03 \x01(\t\".\n\x1fPodcastAppStoreTransactionProto\x12\x0b\n\x03jws\x18\x01 \x01(\t\"w\n#PodcastSubscriptionTransactionProto\x12\x38\n\x11subscription_type\x18\x01 \x01(\x0e\x32\x1d.PodcastSubscriptionTypeProto\x12\x16\n\x0e\x61ppstore_token\x18\x02 \x01(\t\"c\n$PodcastSubscriptionTransactionsProto\x12;\n\rsubscriptions\x18\x01 \x03(\x0b\x32$.PodcastSubscriptionTransactionProto*\x9e\x01\n\x12PodcastStatusProto\x12\"\n\x1ePODCAST_STATUS_PROTO_UNDEFINED\x10\x00\x12#\n\x1fPODCAST_STATUS_PROTO_GENERATING\x10\x01\x12\x1e\n\x1aPODCAST_STATUS_PROTO_READY\x10\x02\x12\x1f\n\x1bPODCAST_STATUS_PROTO_FAILED\x10\x03*\x84\x02\n\x1cPodcastVisualTransitionProto\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_UNDEFINED\x10\x00\x12,\n(PODCAST_VISUAL_TRANSITION_PROTO_DISSOLVE\x10\x01\x12)\n%PODCAST_VISUAL_TRANSITION_PROTO_SWIPE\x10\x02\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_BAR_SWIPE\x10\x03\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_PAGE_CURL\x10\x04*n\n\x10PodcastHostProto\x12\x1e\n\x1aPODCAST_HOST_PROTO_UNKNOWN\x10\x00\x12\x1b\n\x17PODCAST_HOST_PROTO_MALE\x10\x01\x12\x1d\n\x19PODCAST_HOST_PROTO_FEMALE\x10\x02*\xd2\x01\n\x1cPodcastSubscriptionTypeProto\x12-\n)PODCAST_SUBSCRIPTION_TYPE_PROTO_UNDEFINED\x10\x00\x12*\n&PODCAST_SUBSCRIPTION_TYPE_PROTO_WEEKLY\x10\x01\x12+\n\'PODCAST_SUBSCRIPTION_TYPE_PROTO_MONTHLY\x10\x02\x12*\n&PODCAST_SUBSCRIPTION_TYPE_PROTO_ANNUAL\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PodcastProto_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._loaded_options = None
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._serialized_options = b'8\001'
  _globals['_YOURPODCASTSSHELFPROTO_THUMBNAILSENTRY']._loaded_options = None
  _globals['_YOURPODCASTSSHELFPROTO_THUMBNAILSENTRY']._serialized_options = b'8\001'
  _globals['_PODCASTSTATUSPROTO']._serialized_start=8050
  _globals['_PODCASTSTATUSPROTO']._serialized_end=8208
  _globals['_PODCASTVISUALTRANSITIONPROTO']._serialized_start=8211
  _globals['_PODCASTVISUALTRANSITIONPROTO']._serialized_end=8471
  _globals['_PODCASTHOSTPROTO']._serialized_start=8473
  _globals['_PODCASTHOSTPROTO']._serialized_end=8583
  _globals['_PODCASTSUBSCRIPTIONTYPEPROTO']._serialized_start=8586
  _globals['_PODCASTSUBSCRIPTIONTYPEPROTO']._serialized_end=8796
  _globals['_PODCASTREQUESTAUTHPROTO']._serialized_start=88
  _globals['_PODCASTREQUESTAUTHPROTO']._serialized_end=248
  _globals['_PODCASTSTREAMAPIREQUESTPROTO']._serialized_start=251
  _globals['_PODCASTSTREAMAPIREQUESTPROTO']._serialized_end=755
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO']._serialized_start=758
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO']._serialized_end=1456
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._serialized_start=1371
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._serialized_end=1446
  _globals['_PODCASTSTREAMAPIRESPONSEDELTAPROTO']._serialized_start=1459
  _globals['_PODCASTSTREAMAPIRESPONSEDELTAPROTO']._serialized_end=1980
  _globals['_CREATEPODCASTREQUESTPROTO']._serialized_start=1982
  _globals['_CREATEPODCASTREQUESTPROTO']._serialized_end=2025
  _globals['_CREATEPODCASTRESPONSEHEADERPROTO']._serialized_start=2027
  _globals['_CREATEPODCASTRESPONSEHEADERPROTO']._serialized_end=2081
  _globals['_CREATEPODCASTRESPONSEDELTAPROTO']._serialized_start=2084
  _globals['_CREATEPODCASTRESPONSEDELTAPROTO']._serialized_end=2244
  _globals['_GENERATEPODCASTREQUESTPROTO']._serialized_start=2247
  _globals['_GENERATEPODCASTREQUESTPROTO']._serialized_end=2394
  _globals['_GENERATEPODCASTFROMPOINTSPROTO']._serialized_start=2396
  _globals['_GENERATEPODCASTFROMPOINTSPROTO']._serialized_end=2467
  _globals['_GENERATEPODCASTFROMSUGGESTIONPROTO']._serialized_start=2469
  _globals['_GENERATEPODCASTFROMSUGGESTIONPROTO']._serialized_end=2544
  _globals['_GENERATEPODCASTRESPONSEHEADERPROTO']._serialized_start=2546
  _globals['_GENERATEPODCASTRESPONSEHEADERPROTO']._serialized_end=2582
  _globals['_GENERATEPODCASTRESPONSEDELTAPROTO']._serialized_start=2584
  _globals['_GENERATEPODCASTRESPONSEDELTAPROTO']._serialized_end=2662
  _globals['_GETPODCASTREQUESTPROTO']._serialized_start=2664
  _globals['_GETPODCASTREQUESTPROTO']._serialized_end=2708
  _globals['_GETPODCASTRESPONSEHEADERPROTO']._serialized_start=2710
  _globals['_GETPODCASTRESPONSEHEADERPROTO']._serialized_end=2773
  _globals['_GETPODCASTRESPONSEDELTAPROTO']._serialized_start=2775
  _globals['_GETPODCASTRESPONSEDELTAPROTO']._serialized_end=2805
  _globals['_GETPODCASTSTORYREQUESTPROTO']._serialized_start=2807
  _globals['_GETPODCASTSTORYREQUESTPROTO']._serialized_end=2854
  _globals['_GETPODCASTSTORYRESPONSEHEADERPROTO']._serialized_start=2856
  _globals['_GETPODCASTSTORYRESPONSEHEADERPROTO']._serialized_end=2892
  _globals['_GETPODCASTSTORYRESPONSEDELTAPROTO']._serialized_start=2895
  _globals['_GETPODCASTSTORYRESPONSEDELTAPROTO']._serialized_end=3024
  _globals['_GETPODCASTSUGGESTIONPOINTSPROTO']._serialized_start=3026
  _globals['_GETPODCASTSUGGESTIONPOINTSPROTO']._serialized_end=3079
  _globals['_GETPODCASTSUGGESTIONPOINTSRESPONSEHEADERPROTO']._serialized_start=3081
  _globals['_GETPODCASTSUGGESTIONPOINTSRESPONSEHEADERPROTO']._serialized_end=3128
  _globals['_GETPODCASTSUGGESTIONPOINTSRESPONSEDELTAPROTO']._serialized_start=3130
  _globals['_GETPODCASTSUGGESTIONPOINTSRESPONSEDELTAPROTO']._serialized_end=3221
  _globals['_REFRESHPODCASTSUGGESTIONSREQUESTPROTO']._serialized_start=3223
  _globals['_REFRESHPODCASTSUGGESTIONSREQUESTPROTO']._serialized_end=3262
  _globals['_REFRESHPODCASTSUGGESTIONSRESPONSEHEADERPROTO']._serialized_start=3264
  _globals['_REFRESHPODCASTSUGGESTIONSRESPONSEHEADERPROTO']._serialized_end=3310
  _globals['_REFRESHPODCASTSUGGESTIONSRESPONSEDELTAPROTO']._serialized_start=3312
  _globals['_REFRESHPODCASTSUGGESTIONSRESPONSEDELTAPROTO']._serialized_end=3357
  _globals['_APPLYPODCASTTRANSACTIONREQUESTPROTO']._serialized_start=3359
  _globals['_APPLYPODCASTTRANSACTIONREQUESTPROTO']._serialized_end=3471
  _globals['_APPLYPODCASTTRANSACTIONRESPONSEHEADERPROTO']._serialized_start=3473
  _globals['_APPLYPODCASTTRANSACTIONRESPONSEHEADERPROTO']._serialized_end=3517
  _globals['_APPLYPODCASTTRANSACTIONRESPONSEDELTAPROTO']._serialized_start=3519
  _globals['_APPLYPODCASTTRANSACTIONRESPONSEDELTAPROTO']._serialized_end=3562
  _globals['_PODCASTPROTO']._serialized_start=3565
  _globals['_PODCASTPROTO']._serialized_end=3911
  _globals['_FIRESTOREPODCASTSUGGESTIONSPROTO']._serialized_start=3914
  _globals['_FIRESTOREPODCASTSUGGESTIONSPROTO']._serialized_end=4155
  _globals['_YOURPODCASTSSHELFPROTO']._serialized_start=4158
  _globals['_YOURPODCASTSSHELFPROTO']._serialized_end=4318
  _globals['_YOURPODCASTSSHELFPROTO_THUMBNAILSENTRY']._serialized_start=4245
  _globals['_YOURPODCASTSSHELFPROTO_THUMBNAILSENTRY']._serialized_end=4318
  _globals['_PODCASTPOINTPROTO']._serialized_start=4320
  _globals['_PODCASTPOINTPROTO']._serialized_end=4410
  _globals['_PODCASTTHUMBNAILPROTO']._serialized_start=4413
  _globals['_PODCASTTHUMBNAILPROTO']._serialized_end=4674
  _globals['_PODCASTAUDIOPROTO']._serialized_start=4676
  _globals['_PODCASTAUDIOPROTO']._serialized_end=4754
  _globals['_PODCASTCARDSPROTO']._serialized_start=4756
  _globals['_PODCASTCARDSPROTO']._serialized_end=4827
  _globals['_PODCASTCARDPROTO']._serialized_start=4830
  _globals['_PODCASTCARDPROTO']._serialized_end=5039
  _globals['_PODCASTERRORPROTO']._serialized_start=5041
  _globals['_PODCASTERRORPROTO']._serialized_end=5077
  _globals['_PODCASTPROMPTANSWERPROTO']._serialized_start=5079
  _globals['_PODCASTPROMPTANSWERPROTO']._serialized_end=5119
  _globals['_PODCASTVISUALSPROTO']._serialized_start=5121
  _globals['_PODCASTVISUALSPROTO']._serialized_end=5180
  _globals['_PODCASTVISUALPROTO']._serialized_start=5183
  _globals['_PODCASTVISUALPROTO']._serialized_end=5349
  _globals['_PODCASTVISUALANIMATIONPROTO']._serialized_start=5351
  _globals['_PODCASTVISUALANIMATIONPROTO']._serialized_end=5445
  _globals['_PODCASTTRANSCRIPTPROTO']._serialized_start=5447
  _globals['_PODCASTTRANSCRIPTPROTO']._serialized_end=5518
  _globals['_PODCASTTRANSCRIPTENTRYPROTO']._serialized_start=5520
  _globals['_PODCASTTRANSCRIPTENTRYPROTO']._serialized_end=5616
  _globals['_PODCASTWORDPROTO']._serialized_start=5618
  _globals['_PODCASTWORDPROTO']._serialized_end=5711
  _globals['_PODCASTKNOWLEDGECARDPROTO']._serialized_start=5713
  _globals['_PODCASTKNOWLEDGECARDPROTO']._serialized_end=5827
  _globals['_PODCASTMULTIPLECHOICECARDPROTO']._serialized_start=5830
  _globals['_PODCASTMULTIPLECHOICECARDPROTO']._serialized_end=6051
  _globals['_PODCASTPOLLCARDPROTO']._serialized_start=6054
  _globals['_PODCASTPOLLCARDPROTO']._serialized_end=6188
  _globals['_PODCASTCARDHEROPROTO']._serialized_start=6190
  _globals['_PODCASTCARDHEROPROTO']._serialized_end=6247
  _globals['_PODCASTMULTIPLECHOICEOPTIONPROTO']._serialized_start=6249
  _globals['_PODCASTMULTIPLECHOICEOPTIONPROTO']._serialized_end=6297
  _globals['_PODCASTPOLLOPTIONPROTO']._serialized_start=6299
  _globals['_PODCASTPOLLOPTIONPROTO']._serialized_end=6337
  _globals['_PODCASTKEYPOINTSPROTO']._serialized_start=6339
  _globals['_PODCASTKEYPOINTSPROTO']._serialized_end=6420
  _globals['_PODCASTFOLLOWUPSPROTO']._serialized_start=6422
  _globals['_PODCASTFOLLOWUPSPROTO']._serialized_end=6502
  _globals['_PODCASTFOLLOWUPPROTO']._serialized_start=6504
  _globals['_PODCASTFOLLOWUPPROTO']._serialized_end=6579
  _globals['_PODCASTKEYPOINTPROTO']._serialized_start=6581
  _globals['_PODCASTKEYPOINTPROTO']._serialized_end=6678
  _globals['_PODCASTSUGGESTIONSPROTO']._serialized_start=6681
  _globals['_PODCASTSUGGESTIONSPROTO']._serialized_end=6868
  _globals['_PODCASTSUGGESTIONSSECTIONPROTO']._serialized_start=6871
  _globals['_PODCASTSUGGESTIONSSECTIONPROTO']._serialized_end=7138
  _globals['_PODCASTQUERYCOMPLETIONSPROTO']._serialized_start=7140
  _globals['_PODCASTQUERYCOMPLETIONSPROTO']._serialized_end=7227
  _globals['_PODCASTQUERYCOMPLETIONPROTO']._serialized_start=7229
  _globals['_PODCASTQUERYCOMPLETIONPROTO']._serialized_end=7273
  _globals['_PODCASTSTORYTHUMBNAILPROTO']._serialized_start=7275
  _globals['_PODCASTSTORYTHUMBNAILPROTO']._serialized_end=7360
  _globals['_PODCASTSTORYHEADERPROTO']._serialized_start=7362
  _globals['_PODCASTSTORYHEADERPROTO']._serialized_end=7402
  _globals['_PODCASTSTORYSLIDEPROTO']._serialized_start=7404
  _globals['_PODCASTSTORYSLIDEPROTO']._serialized_end=7518
  _globals['_PODCASTROUTINEPROTO']._serialized_start=7520
  _globals['_PODCASTROUTINEPROTO']._serialized_end=7588
  _globals['_PODCASTROUTINESEGMENTPROTO']._serialized_start=7590
  _globals['_PODCASTROUTINESEGMENTPROTO']._serialized_end=7694
  _globals['_PODCASTROUTINESTEPPROTO']._serialized_start=7696
  _globals['_PODCASTROUTINESTEPPROTO']._serialized_end=7777
  _globals['_PODCASTAPPSTORETRANSACTIONPROTO']._serialized_start=7779
  _globals['_PODCASTAPPSTORETRANSACTIONPROTO']._serialized_end=7825
  _globals['_PODCASTSUBSCRIPTIONTRANSACTIONPROTO']._serialized_start=7827
  _globals['_PODCASTSUBSCRIPTIONTRANSACTIONPROTO']._serialized_end=7946
  _globals['_PODCASTSUBSCRIPTIONTRANSACTIONSPROTO']._serialized_start=7948
  _globals['_PODCASTSUBSCRIPTIONTRANSACTIONSPROTO']._serialized_end=8047
# @@protoc_insertion_point(module_scope)
