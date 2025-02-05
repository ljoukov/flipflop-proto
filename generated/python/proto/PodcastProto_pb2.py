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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xab\x01\n\x17PodcastRequestAuthProto\x12\x19\n\x11\x66irebase_id_token\x18\x01 \x01(\t\x12\x16\n\x0e\x61ppcheck_token\x18\x02 \x01(\t\x12\x14\n\x0cis_anonomous\x18\x03 \x01(\x08\x12G\n\x1d\x61ppstore_current_entitlements\x18\x04 \x03(\x0b\x32 .PodcastAppStoreTransactionProto\"h\n\x1ePodcastSubscriptionStatusProto\x12\x15\n\ris_subscriber\x18\x01 \x01(\x08\x12/\n\x06source\x18\x02 \x01(\x0e\x32\x1f.PodcastSubscriptionSourceProto\"\xc3\x04\n\x1cPodcastStreamApiRequestProto\x12.\n\x0crequest_auth\x18\x01 \x01(\x0b\x32\x18.PodcastRequestAuthProto\x12,\n\x06\x63reate\x18\n \x01(\x0b\x32\x1a.CreatePodcastRequestProtoH\x00\x12\x30\n\x08generate\x18\x0b \x01(\x0b\x32\x1c.GeneratePodcastRequestProtoH\x00\x12*\n\x07podcast\x18\x0c \x01(\x0b\x32\x17.GetPodcastRequestProtoH\x00\x12-\n\x05story\x18\r \x01(\x0b\x32\x1c.GetPodcastStoryRequestProtoH\x00\x12\x44\n\x11suggestion_points\x18\x0e \x01(\x0b\x32\'.GetPodcastSuggestionPointsRequestProtoH\x00\x12@\n\x0f\x66ollowup_points\x18\x11 \x01(\x0b\x32%.GetPodcastFollowupPointsRequestProtoH\x00\x12+\n\x04home\x18\x0f \x01(\x0b\x32\x1b.GetPodcastHomeRequestProtoH\x00\x12\x34\n\x0e\x64\x65lete_account\x18\x10 \x01(\x0b\x32\x1a.DeleteAccountRequestProtoH\x00\x12\x42\n\x10onboarding_input\x18\x12 \x01(\x0b\x32&.GetPodcastOnboardingInputRequestProtoH\x00\x42\t\n\x07request\"\xa5\x06\n#PodcastStreamApiResponseHeaderProto\x12:\n\rcreate_header\x18\n \x01(\x0b\x32!.CreatePodcastResponseHeaderProtoH\x00\x12>\n\x0fgenerate_header\x18\x0b \x01(\x0b\x32#.GeneratePodcastResponseHeaderProtoH\x00\x12\x38\n\x0epodcast_header\x18\x0c \x01(\x0b\x32\x1e.GetPodcastResponseHeaderProtoH\x00\x12;\n\x0cstory_header\x18\r \x01(\x0b\x32#.GetPodcastStoryResponseHeaderProtoH\x00\x12R\n\x18suggestion_points_header\x18\x0e \x01(\x0b\x32..GetPodcastSuggestionPointsResponseHeaderProtoH\x00\x12N\n\x16\x66ollowup_points_header\x18\x11 \x01(\x0b\x32,.GetPodcastFollowupPointsResponseHeaderProtoH\x00\x12\x39\n\x0bhome_header\x18\x0f \x01(\x0b\x32\".GetPodcastHomeResponseHeaderProtoH\x00\x12\x42\n\x15\x64\x65lete_account_header\x18\x10 \x01(\x0b\x32!.DeleteAccountResponseHeaderProtoH\x00\x12I\n\x10onboarding_input\x18\x12 \x01(\x0b\x32-.GetPodcastOnboardingInputResponseHeaderProtoH\x00\x12\x46\n\tlatencies\x18\x64 \x03(\x0b\x32\x33.PodcastStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\x08\n\x06header\"\x8c\x05\n\"PodcastStreamApiResponseDeltaProto\x12\x38\n\x0c\x63reate_delta\x18\n \x01(\x0b\x32 .CreatePodcastResponseDeltaProtoH\x00\x12<\n\x0egenerate_delta\x18\x0b \x01(\x0b\x32\".GeneratePodcastResponseDeltaProtoH\x00\x12\x36\n\rpodcast_delta\x18\x0c \x01(\x0b\x32\x1d.GetPodcastResponseDeltaProtoH\x00\x12\x39\n\x0bstory_delta\x18\r \x01(\x0b\x32\".GetPodcastStoryResponseDeltaProtoH\x00\x12P\n\x17suggestion_points_delta\x18\x0e \x01(\x0b\x32-.GetPodcastSuggestionPointsResponseDeltaProtoH\x00\x12L\n\x15\x66ollowup_points_delta\x18\x11 \x01(\x0b\x32+.GetPodcastFollowupPointsResponseDeltaProtoH\x00\x12\x37\n\nhome_delta\x18\x0f \x01(\x0b\x32!.GetPodcastHomeResponseDeltaProtoH\x00\x12@\n\x14\x64\x65lete_account_delta\x18\x10 \x01(\x0b\x32 .DeleteAccountResponseDeltaProtoH\x00\x12N\n\x16onboarding_input_delta\x18\x12 \x01(\x0b\x32,.GetPodcastOnboardingInputResponseDeltaProtoH\x00\x42\x10\n\x0eresponse_delta\"+\n\x19\x43reatePodcastRequestProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"6\n CreatePodcastResponseHeaderProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"\xa0\x01\n\x1f\x43reatePodcastResponseDeltaProto\x12#\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x12.PodcastErrorProtoH\x00\x12+\n\x06\x61nswer\x18\x02 \x01(\x0b\x32\x19.PodcastPromptAnswerProtoH\x00\x12#\n\x05point\x18\x03 \x01(\x0b\x32\x12.PodcastPointProtoH\x00\x42\x06\n\x04type\"\x93\x01\n\x1bGeneratePodcastRequestProto\x12\x31\n\x06points\x18\x01 \x01(\x0b\x32\x1f.GeneratePodcastFromPointsProtoH\x00\x12\x39\n\nsuggestion\x18\x02 \x01(\x0b\x32#.GeneratePodcastFromSuggestionProtoH\x00\x42\x06\n\x04type\"G\n\x1eGeneratePodcastFromPointsProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x11\n\tpoint_ids\x18\x02 \x03(\t\"K\n\"GeneratePodcastFromSuggestionProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x11\n\tpoint_ids\x18\x02 \x03(\t\"$\n\"GeneratePodcastResponseHeaderProto\"N\n!GeneratePodcastResponseDeltaProto\x12!\n\x04\x63\x61rd\x18\x01 \x01(\x0b\x32\x11.PodcastCardProtoH\x00\x42\x06\n\x04type\",\n\x16GetPodcastRequestProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"b\n\x1dGetPodcastResponseHeaderProto\x12\x1e\n\x07podcast\x18\x01 \x01(\x0b\x32\r.PodcastProto\x12!\n\x05\x63\x61rds\x18\x02 \x01(\x0b\x32\x12.PodcastCardsProto\"\x1e\n\x1cGetPodcastResponseDeltaProto\"/\n\x1bGetPodcastStoryRequestProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\"$\n\"GetPodcastStoryResponseHeaderProto\"\x81\x01\n!GetPodcastStoryResponseDeltaProto\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x18.PodcastStoryHeaderProtoH\x00\x12(\n\x05slide\x18\x02 \x01(\x0b\x32\x17.PodcastStorySlideProtoH\x00\x42\x06\n\x04type\"<\n&GetPodcastSuggestionPointsRequestProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\"/\n-GetPodcastSuggestionPointsResponseHeaderProto\"[\n,GetPodcastSuggestionPointsResponseDeltaProto\x12#\n\x05point\x18\x01 \x01(\x0b\x32\x12.PodcastPointProtoH\x00\x42\x06\n\x04type\"^\n$GetPodcastFollowupPointsRequestProto\x12\x19\n\x11source_podcast_id\x18\x01 \x01(\t\x12\x1b\n\x13\x66ollowup_podcast_id\x18\x02 \x01(\t\"-\n+GetPodcastFollowupPointsResponseHeaderProto\"Y\n*GetPodcastFollowupPointsResponseDeltaProto\x12#\n\x05point\x18\x01 \x01(\x0b\x32\x12.PodcastPointProtoH\x00\x42\x06\n\x04type\"T\n\x1aGetPodcastHomeRequestProto\x12\x36\n\x10onboarding_input\x18\x01 \x01(\x0b\x32\x1c.PodcastOnboardingInputProto\"\xa2\x01\n!GetPodcastHomeResponseHeaderProto\x12<\n\x13subscription_status\x18\x01 \x01(\x0b\x32\x1f.PodcastSubscriptionStatusProto\x12\"\n\x1a\x66irestore_suggestions_path\x18\x02 \x01(\t\x12\x1b\n\x13onboarding_required\x18\x03 \x01(\x08\"\"\n GetPodcastHomeResponseDeltaProto\"\x1b\n\x19\x44\x65leteAccountRequestProto\"\"\n DeleteAccountResponseHeaderProto\"!\n\x1f\x44\x65leteAccountResponseDeltaProto\"\'\n%GetPodcastOnboardingInputRequestProto\"f\n,GetPodcastOnboardingInputResponseHeaderProto\x12\x36\n\x10onboarding_input\x18\x01 \x01(\x0b\x32\x1c.PodcastOnboardingInputProto\"-\n+GetPodcastOnboardingInputResponseDeltaProto\"\x87\x03\n\x0cPodcastProto\x12.\n\nupdated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\tthumbnail\x18\x02 \x01(\x0b\x32\x16.PodcastThumbnailProto\x12!\n\x05\x61udio\x18\x03 \x01(\x0b\x32\x12.PodcastAudioProto\x12%\n\x07visuals\x18\x04 \x01(\x0b\x32\x14.PodcastVisualsProto\x12+\n\ntranscript\x18\x05 \x01(\x0b\x32\x17.PodcastTranscriptProto\x12!\n\x05\x63\x61rds\x18\x06 \x01(\x0b\x32\x12.PodcastCardsProto\x12*\n\nkey_points\x18\x07 \x01(\x0b\x32\x16.PodcastKeyPointsProto\x12)\n\tfollowups\x18\x08 \x01(\x0b\x32\x16.PodcastFollowupsProto\x12+\n\ncompletion\x18\t \x01(\x0b\x32\x17.PodcastCompletionProto\"\x8a\x02\n FirestorePodcastSuggestionsProto\x12.\n\nupdated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x13your_podcasts_shelf\x18\x02 \x01(\x0b\x32\x17.YourPodcastsShelfProto\x12-\n\x0bsuggestions\x18\x03 \x01(\x0b\x32\x18.PodcastSuggestionsProto\x12Q\n new_suggestions_generation_state\x18\x04 \x01(\x0b\x32\'.PodcastSuggestionsGenerationStateProto\"\xa0\x01\n\x16YourPodcastsShelfProto\x12;\n\nthumbnails\x18\x01 \x03(\x0b\x32\'.YourPodcastsShelfProto.ThumbnailsEntry\x1aI\n\x0fThumbnailsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.PodcastThumbnailProto:\x02\x38\x01\"Z\n\x11PodcastPointProto\x12\x10\n\x08point_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"\xb4\x02\n\x15PodcastThumbnailProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12#\n\x06status\x18\x02 \x01(\x0e\x32\x13.PodcastStatusProto\x12\x16\n\x0e\x64isplay_status\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x12\n\nlong_title\x18\t \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\n \x03(\t\x12\x1f\n\x04type\x18\x0b \x01(\x0e\x32\x11.PodcastTypeProto\x12\x0c\n\x04path\x18\x06 \x01(\t\x12+\n\x08\x64uration\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"N\n\x11PodcastAudioProto\x12\x0c\n\x04path\x18\x01 \x01(\t\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"G\n\x11PodcastCardsProto\x12\x10\n\x08is_ready\x18\x01 \x01(\x08\x12 \n\x05\x63\x61rds\x18\x02 \x03(\x0b\x32\x11.PodcastCardProto\"\xd1\x01\n\x10PodcastCardProto\x12\x0f\n\x07\x63\x61rd_id\x18\x01 \x01(\t\x12\x10\n\x08is_ready\x18\x02 \x01(\x08\x12/\n\tknowledge\x18\n \x01(\x0b\x32\x1a.PodcastKnowledgeCardProtoH\x00\x12:\n\x0fmultiple_choice\x18\x0b \x01(\x0b\x32\x1f.PodcastMultipleChoiceCardProtoH\x00\x12%\n\x04poll\x18\x0c \x01(\x0b\x32\x15.PodcastPollCardProtoH\x00\x42\x06\n\x04type\"$\n\x11PodcastErrorProto\x12\x0f\n\x07message\x18\x01 \x01(\t\"(\n\x18PodcastPromptAnswerProto\x12\x0c\n\x04text\x18\x01 \x01(\t\";\n\x13PodcastVisualsProto\x12$\n\x07visuals\x18\x01 \x03(\x0b\x32\x13.PodcastVisualProto\"\xa6\x01\n\x12PodcastVisualProto\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x05\x12\x12\n\nimage_path\x18\x02 \x01(\t\x12/\n\tanimation\x18\x04 \x01(\x0b\x32\x1c.PodcastVisualAnimationProto\x12\x31\n\ntransition\x18\x03 \x01(\x0e\x32\x1d.PodcastVisualTransitionProto\"^\n\x1bPodcastVisualAnimationProto\x12\x17\n\x0f\x64uration_millis\x18\x01 \x01(\x05\x12\x13\n\x0bstart_scale\x18\x02 \x01(\x02\x12\x11\n\tend_scale\x18\x03 \x01(\x02\"G\n\x16PodcastTranscriptProto\x12-\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1c.PodcastTranscriptEntryProto\"`\n\x1bPodcastTranscriptEntryProto\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12 \n\x05words\x18\x02 \x03(\x0b\x32\x11.PodcastWordProto\"]\n\x10PodcastWordProto\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x14\n\x0cstart_millis\x18\x02 \x01(\x05\x12\x12\n\nend_millis\x18\x03 \x01(\x05\x12\x11\n\tseparator\x18\x04 \x01(\t\"r\n\x19PodcastKnowledgeCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x13\n\x0b\x65xplanation\x18\x04 \x01(\t\"\xdd\x01\n\x1ePodcastMultipleChoiceCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x10\n\x08question\x18\x03 \x01(\t\x12\x32\n\x07options\x18\x04 \x03(\x0b\x32!.PodcastMultipleChoiceOptionProto\x12\x1d\n\x15\x63orrect_answer_number\x18\x05 \x01(\x05\x12\r\n\x05hints\x18\x06 \x03(\t\x12\x13\n\x0b\x65xplanation\x18\x07 \x01(\t\"\x86\x01\n\x14PodcastPollCardProto\x12\r\n\x05title\x18\x01 \x01(\t\x12#\n\x04hero\x18\x02 \x01(\x0b\x32\x15.PodcastCardHeroProto\x12\x10\n\x08question\x18\x03 \x01(\t\x12(\n\x07options\x18\x04 \x03(\x0b\x32\x17.PodcastPollOptionProto\"9\n\x14PodcastCardHeroProto\x12\r\n\x05\x65moji\x18\x01 \x01(\t\x12\x12\n\nlottie_url\x18\x02 \x01(\t\"0\n PodcastMultipleChoiceOptionProto\x12\x0c\n\x04text\x18\x01 \x01(\t\"&\n\x16PodcastPollOptionProto\x12\x0c\n\x04text\x18\x01 \x01(\t\"Q\n\x15PodcastKeyPointsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12)\n\nkey_points\x18\x02 \x03(\x0b\x32\x15.PodcastKeyPointProto\"P\n\x15PodcastFollowupsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12(\n\tfollowups\x18\x02 \x03(\x0b\x32\x15.PodcastFollowupProto\"S\n\x14PodcastFollowupProto\x12\x1b\n\x13\x66ollowup_podcast_id\x18\x01 \x01(\t\x12\r\n\x05\x65moji\x18\x02 \x01(\t\x12\x0f\n\x07outline\x18\x03 \x01(\t\"a\n\x14PodcastKeyPointProto\x12\x14\n\x0ckey_point_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"b\n\x16PodcastCompletionProto\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\x15\n\rencouragement\x18\x02 \x01(\t\x12\r\n\x05\x65moji\x18\x03 \x01(\t\x12\x12\n\nlottie_url\x18\x04 \x01(\t\"\xbb\x01\n\x17PodcastSuggestionsProto\x12\x16\n\x0esuggestions_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x08sections\x18\x03 \x03(\x0b\x32\x1f.PodcastSuggestionsSectionProto\x12%\n\x07routine\x18\x04 \x01(\x0b\x32\x14.PodcastRoutineProto\"\xb5\x01\n&PodcastSuggestionsGenerationStateProto\x12\x16\n\x0esuggestions_id\x18\x01 \x01(\t\x12.\n\nupdated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x05state\x18\x03 \x01(\x0e\x32\x1d.PodcastSuggestionsStateProto\x12\x15\n\rdisplay_state\x18\x04 \x01(\t\"\x8b\x02\n\x1ePodcastSuggestionsSectionProto\x12\x12\n\nsection_id\x18\x01 \x01(\t\x12\x15\n\rsection_title\x18\x02 \x01(\t\x12\x31\n\x11\x62\x61nner_suggestion\x18\x03 \x01(\x0b\x32\x16.PodcastThumbnailProto\x12\x31\n\x11\x66ooter_suggestion\x18\x04 \x01(\x0b\x32\x16.PodcastThumbnailProto\x12+\n\x06story1\x18\x05 \x01(\x0b\x32\x1b.PodcastStoryThumbnailProto\x12+\n\x06story2\x18\x06 \x01(\x0b\x32\x1b.PodcastStoryThumbnailProto\"U\n\x1aPodcastStoryThumbnailProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x16\n\x0ethumbnail_path\x18\x03 \x01(\t\"(\n\x17PodcastStoryHeaderProto\x12\r\n\x05\x62\x61\x64ge\x18\x01 \x01(\t\"r\n\x16PodcastStorySlideProto\x12\x10\n\x08slide_id\x18\x01 \x01(\t\x12\x15\n\ris_text_ready\x18\x02 \x01(\x08\x12\r\n\x05title\x18\x03 \x01(\t\x12\x12\n\nimage_path\x18\x04 \x01(\t\x12\x0c\n\x04text\x18\x05 \x01(\t\"g\n\x13PodcastRoutineProto\x12\x12\n\nroutine_id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12-\n\x08segments\x18\x01 \x03(\x0b\x32\x1b.PodcastRoutineSegmentProto\"h\n\x1aPodcastRoutineSegmentProto\x12\x12\n\nsegment_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\'\n\x05steps\x18\x03 \x03(\x0b\x32\x18.PodcastRoutineStepProto\"\\\n\x17PodcastRoutineStepProto\x12)\n\tthumbnail\x18\x05 \x01(\x0b\x32\x16.PodcastThumbnailProtoJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05\"T\n\x1fPodcastAppStoreTransactionProto\x12\x17\n\x0ftransaction_jws\x18\x01 \x01(\t\x12\x18\n\x10renewal_info_jws\x18\x02 \x01(\t\"\xba\x01\n\x18PodcastUserProgressProto\x12H\n\x10routine_progress\x18\x01 \x03(\x0b\x32..PodcastUserProgressProto.RoutineProgressEntry\x1aT\n\x14RoutineProgressEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.PodcastRoutineProgressProto:\x02\x38\x01\"\xbb\x01\n\x1bPodcastRoutineProgressProto\x12\x45\n\rstep_progress\x18\x01 \x03(\x0b\x32..PodcastRoutineProgressProto.StepProgressEntry\x1aU\n\x11StepProgressEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .PodcastRoutineStepProgressProto:\x02\x38\x01\"f\n\x1fPodcastRoutineStepProgressProto\x12\x30\n\x0c\x63ompleted_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tcompleted\x18\x02 \x01(\x08\"\x81\x01\n\x1bPodcastOnboardingInputProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08goal_ids\x18\x02 \x03(\t\x12\x1a\n\x12learning_style_ids\x18\x03 \x03(\t\x12\x14\n\x0cinterest_ids\x18\x04 \x03(\t\x12\x10\n\x08voice_id\x18\x05 \x01(\t\"\x93\x01\n\x1eOnDeviceStoredUserDetailsProto\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12<\n\x13subscription_source\x18\x02 \x01(\x0e\x32\x1f.PodcastSubscriptionSourceProto\x12\"\n\x1a\x66irestore_suggestions_path\x18\x03 \x01(\t\"\xa3\x02\n\x1cPodcastOnboardingConfigProto\x12\x38\n\x0cgoals_config\x18\x01 \x01(\x0b\x32\".PodcastOnboardingGoalsConfigProto\x12K\n\x16learning_styles_config\x18\x02 \x01(\x0b\x32+.PodcastOnboardingLearningStylesConfigProto\x12@\n\x10interests_config\x18\x03 \x01(\x0b\x32&.PodcastOnboardingInterestsConfigProto\x12:\n\rvoices_config\x18\x04 \x01(\x0b\x32#.PodcastOnboardingVoicesConfigProto\"\x84\x01\n!PodcastOnboardingGoalsConfigProto\x12\x12\n\npage_title\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08subtitle\x18\x03 \x01(\t\x12*\n\x05goals\x18\x04 \x03(\x0b\x32\x1b.PodcastOnboardingGoalProto\"\xa0\x01\n*PodcastOnboardingLearningStylesConfigProto\x12\x12\n\npage_title\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08subtitle\x18\x03 \x01(\t\x12=\n\x0flearning_styles\x18\x04 \x03(\x0b\x32$.PodcastOnboardingLearningStyleProto\"\x9b\x01\n%PodcastOnboardingInterestsConfigProto\x12\x12\n\npage_title\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08subtitle\x18\x03 \x01(\t\x12=\n\x0finterest_groups\x18\x04 \x03(\x0b\x32$.PodcastOnboardingInterestGroupProto\"\x87\x01\n\"PodcastOnboardingVoicesConfigProto\x12\x12\n\npage_title\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08subtitle\x18\x03 \x01(\t\x12,\n\x06voices\x18\x04 \x03(\x0b\x32\x1c.PodcastOnboardingVoiceProto\"t\n#PodcastOnboardingInterestGroupProto\x12\x19\n\x11interest_group_id\x18\x01 \x01(\t\x12\x32\n\tinterests\x18\x02 \x03(\x0b\x32\x1f.PodcastOnboardingInterestProto\"K\n\x1aPodcastOnboardingGoalProto\x12\x0f\n\x07goal_id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\r\n\x05\x65moji\x18\x03 \x01(\t\"p\n#PodcastOnboardingLearningStyleProto\x12\x19\n\x11learning_style_id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x10\n\x08subtitle\x18\x03 \x01(\t\x12\r\n\x05\x65moji\x18\x04 \x01(\t\"S\n\x1ePodcastOnboardingInterestProto\x12\x13\n\x0binterest_id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\r\n\x05\x65moji\x18\x03 \x01(\t\"f\n\x1bPodcastOnboardingVoiceProto\x12\x10\n\x08voice_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08subtitle\x18\x03 \x01(\t\x12\x14\n\x0csample_paths\x18\x04 \x03(\t*\xcb\x01\n\x1ePodcastSubscriptionSourceProto\x12/\n+PODCAST_SUBSCRIPTION_SOURCE_PROTO_UNDEFINED\x10\x00\x12;\n7PODCAST_SUBSCRIPTION_SOURCE_PROTO_PLATFORM_SUBSCRIPTION\x10\x01\x12;\n7PODCAST_SUBSCRIPTION_SOURCE_PROTO_EXTERNAL_SUBSCRIPTION\x10\x02*\x9e\x01\n\x12PodcastStatusProto\x12\"\n\x1ePODCAST_STATUS_PROTO_UNDEFINED\x10\x00\x12#\n\x1fPODCAST_STATUS_PROTO_GENERATING\x10\x01\x12\x1e\n\x1aPODCAST_STATUS_PROTO_READY\x10\x02\x12\x1f\n\x1bPODCAST_STATUS_PROTO_FAILED\x10\x03*\x9a\x01\n\x10PodcastTypeProto\x12 \n\x1cPODCAST_TYPE_PROTO_UNDEFINED\x10\x00\x12 \n\x1cPODCAST_TYPE_PROTO_EXPLAINER\x10\x01\x12\x1f\n\x1bPODCAST_TYPE_PROTO_EXERCISE\x10\x02\x12!\n\x1dPODCAST_TYPE_PROTO_MEDITATION\x10\x03*\x84\x02\n\x1cPodcastVisualTransitionProto\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_UNDEFINED\x10\x00\x12,\n(PODCAST_VISUAL_TRANSITION_PROTO_DISSOLVE\x10\x01\x12)\n%PODCAST_VISUAL_TRANSITION_PROTO_SWIPE\x10\x02\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_BAR_SWIPE\x10\x03\x12-\n)PODCAST_VISUAL_TRANSITION_PROTO_PAGE_CURL\x10\x04*n\n\x10PodcastHostProto\x12\x1e\n\x1aPODCAST_HOST_PROTO_UNKNOWN\x10\x00\x12\x1b\n\x17PODCAST_HOST_PROTO_MALE\x10\x01\x12\x1d\n\x19PODCAST_HOST_PROTO_FEMALE\x10\x02*\xd4\x01\n\x1cPodcastSuggestionsStateProto\x12-\n)PODCAST_SUGGESTIONS_STATE_PROTO_UNDEFINED\x10\x00\x12.\n*PODCAST_SUGGESTIONS_STATE_PROTO_GENERATING\x10\x01\x12)\n%PODCAST_SUGGESTIONS_STATE_PROTO_READY\x10\x02\x12*\n&PODCAST_SUGGESTIONS_STATE_PROTO_FAILED\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PodcastProto_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._loaded_options = None
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._serialized_options = b'8\001'
  _globals['_YOURPODCASTSSHELFPROTO_THUMBNAILSENTRY']._loaded_options = None
  _globals['_YOURPODCASTSSHELFPROTO_THUMBNAILSENTRY']._serialized_options = b'8\001'
  _globals['_PODCASTUSERPROGRESSPROTO_ROUTINEPROGRESSENTRY']._loaded_options = None
  _globals['_PODCASTUSERPROGRESSPROTO_ROUTINEPROGRESSENTRY']._serialized_options = b'8\001'
  _globals['_PODCASTROUTINEPROGRESSPROTO_STEPPROGRESSENTRY']._loaded_options = None
  _globals['_PODCASTROUTINEPROGRESSPROTO_STEPPROGRESSENTRY']._serialized_options = b'8\001'
  _globals['_PODCASTSUBSCRIPTIONSOURCEPROTO']._serialized_start=11281
  _globals['_PODCASTSUBSCRIPTIONSOURCEPROTO']._serialized_end=11484
  _globals['_PODCASTSTATUSPROTO']._serialized_start=11487
  _globals['_PODCASTSTATUSPROTO']._serialized_end=11645
  _globals['_PODCASTTYPEPROTO']._serialized_start=11648
  _globals['_PODCASTTYPEPROTO']._serialized_end=11802
  _globals['_PODCASTVISUALTRANSITIONPROTO']._serialized_start=11805
  _globals['_PODCASTVISUALTRANSITIONPROTO']._serialized_end=12065
  _globals['_PODCASTHOSTPROTO']._serialized_start=12067
  _globals['_PODCASTHOSTPROTO']._serialized_end=12177
  _globals['_PODCASTSUGGESTIONSSTATEPROTO']._serialized_start=12180
  _globals['_PODCASTSUGGESTIONSSTATEPROTO']._serialized_end=12392
  _globals['_PODCASTREQUESTAUTHPROTO']._serialized_start=88
  _globals['_PODCASTREQUESTAUTHPROTO']._serialized_end=259
  _globals['_PODCASTSUBSCRIPTIONSTATUSPROTO']._serialized_start=261
  _globals['_PODCASTSUBSCRIPTIONSTATUSPROTO']._serialized_end=365
  _globals['_PODCASTSTREAMAPIREQUESTPROTO']._serialized_start=368
  _globals['_PODCASTSTREAMAPIREQUESTPROTO']._serialized_end=947
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO']._serialized_start=950
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO']._serialized_end=1755
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._serialized_start=1670
  _globals['_PODCASTSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._serialized_end=1745
  _globals['_PODCASTSTREAMAPIRESPONSEDELTAPROTO']._serialized_start=1758
  _globals['_PODCASTSTREAMAPIRESPONSEDELTAPROTO']._serialized_end=2410
  _globals['_CREATEPODCASTREQUESTPROTO']._serialized_start=2412
  _globals['_CREATEPODCASTREQUESTPROTO']._serialized_end=2455
  _globals['_CREATEPODCASTRESPONSEHEADERPROTO']._serialized_start=2457
  _globals['_CREATEPODCASTRESPONSEHEADERPROTO']._serialized_end=2511
  _globals['_CREATEPODCASTRESPONSEDELTAPROTO']._serialized_start=2514
  _globals['_CREATEPODCASTRESPONSEDELTAPROTO']._serialized_end=2674
  _globals['_GENERATEPODCASTREQUESTPROTO']._serialized_start=2677
  _globals['_GENERATEPODCASTREQUESTPROTO']._serialized_end=2824
  _globals['_GENERATEPODCASTFROMPOINTSPROTO']._serialized_start=2826
  _globals['_GENERATEPODCASTFROMPOINTSPROTO']._serialized_end=2897
  _globals['_GENERATEPODCASTFROMSUGGESTIONPROTO']._serialized_start=2899
  _globals['_GENERATEPODCASTFROMSUGGESTIONPROTO']._serialized_end=2974
  _globals['_GENERATEPODCASTRESPONSEHEADERPROTO']._serialized_start=2976
  _globals['_GENERATEPODCASTRESPONSEHEADERPROTO']._serialized_end=3012
  _globals['_GENERATEPODCASTRESPONSEDELTAPROTO']._serialized_start=3014
  _globals['_GENERATEPODCASTRESPONSEDELTAPROTO']._serialized_end=3092
  _globals['_GETPODCASTREQUESTPROTO']._serialized_start=3094
  _globals['_GETPODCASTREQUESTPROTO']._serialized_end=3138
  _globals['_GETPODCASTRESPONSEHEADERPROTO']._serialized_start=3140
  _globals['_GETPODCASTRESPONSEHEADERPROTO']._serialized_end=3238
  _globals['_GETPODCASTRESPONSEDELTAPROTO']._serialized_start=3240
  _globals['_GETPODCASTRESPONSEDELTAPROTO']._serialized_end=3270
  _globals['_GETPODCASTSTORYREQUESTPROTO']._serialized_start=3272
  _globals['_GETPODCASTSTORYREQUESTPROTO']._serialized_end=3319
  _globals['_GETPODCASTSTORYRESPONSEHEADERPROTO']._serialized_start=3321
  _globals['_GETPODCASTSTORYRESPONSEHEADERPROTO']._serialized_end=3357
  _globals['_GETPODCASTSTORYRESPONSEDELTAPROTO']._serialized_start=3360
  _globals['_GETPODCASTSTORYRESPONSEDELTAPROTO']._serialized_end=3489
  _globals['_GETPODCASTSUGGESTIONPOINTSREQUESTPROTO']._serialized_start=3491
  _globals['_GETPODCASTSUGGESTIONPOINTSREQUESTPROTO']._serialized_end=3551
  _globals['_GETPODCASTSUGGESTIONPOINTSRESPONSEHEADERPROTO']._serialized_start=3553
  _globals['_GETPODCASTSUGGESTIONPOINTSRESPONSEHEADERPROTO']._serialized_end=3600
  _globals['_GETPODCASTSUGGESTIONPOINTSRESPONSEDELTAPROTO']._serialized_start=3602
  _globals['_GETPODCASTSUGGESTIONPOINTSRESPONSEDELTAPROTO']._serialized_end=3693
  _globals['_GETPODCASTFOLLOWUPPOINTSREQUESTPROTO']._serialized_start=3695
  _globals['_GETPODCASTFOLLOWUPPOINTSREQUESTPROTO']._serialized_end=3789
  _globals['_GETPODCASTFOLLOWUPPOINTSRESPONSEHEADERPROTO']._serialized_start=3791
  _globals['_GETPODCASTFOLLOWUPPOINTSRESPONSEHEADERPROTO']._serialized_end=3836
  _globals['_GETPODCASTFOLLOWUPPOINTSRESPONSEDELTAPROTO']._serialized_start=3838
  _globals['_GETPODCASTFOLLOWUPPOINTSRESPONSEDELTAPROTO']._serialized_end=3927
  _globals['_GETPODCASTHOMEREQUESTPROTO']._serialized_start=3929
  _globals['_GETPODCASTHOMEREQUESTPROTO']._serialized_end=4013
  _globals['_GETPODCASTHOMERESPONSEHEADERPROTO']._serialized_start=4016
  _globals['_GETPODCASTHOMERESPONSEHEADERPROTO']._serialized_end=4178
  _globals['_GETPODCASTHOMERESPONSEDELTAPROTO']._serialized_start=4180
  _globals['_GETPODCASTHOMERESPONSEDELTAPROTO']._serialized_end=4214
  _globals['_DELETEACCOUNTREQUESTPROTO']._serialized_start=4216
  _globals['_DELETEACCOUNTREQUESTPROTO']._serialized_end=4243
  _globals['_DELETEACCOUNTRESPONSEHEADERPROTO']._serialized_start=4245
  _globals['_DELETEACCOUNTRESPONSEHEADERPROTO']._serialized_end=4279
  _globals['_DELETEACCOUNTRESPONSEDELTAPROTO']._serialized_start=4281
  _globals['_DELETEACCOUNTRESPONSEDELTAPROTO']._serialized_end=4314
  _globals['_GETPODCASTONBOARDINGINPUTREQUESTPROTO']._serialized_start=4316
  _globals['_GETPODCASTONBOARDINGINPUTREQUESTPROTO']._serialized_end=4355
  _globals['_GETPODCASTONBOARDINGINPUTRESPONSEHEADERPROTO']._serialized_start=4357
  _globals['_GETPODCASTONBOARDINGINPUTRESPONSEHEADERPROTO']._serialized_end=4459
  _globals['_GETPODCASTONBOARDINGINPUTRESPONSEDELTAPROTO']._serialized_start=4461
  _globals['_GETPODCASTONBOARDINGINPUTRESPONSEDELTAPROTO']._serialized_end=4506
  _globals['_PODCASTPROTO']._serialized_start=4509
  _globals['_PODCASTPROTO']._serialized_end=4900
  _globals['_FIRESTOREPODCASTSUGGESTIONSPROTO']._serialized_start=4903
  _globals['_FIRESTOREPODCASTSUGGESTIONSPROTO']._serialized_end=5169
  _globals['_YOURPODCASTSSHELFPROTO']._serialized_start=5172
  _globals['_YOURPODCASTSSHELFPROTO']._serialized_end=5332
  _globals['_YOURPODCASTSSHELFPROTO_THUMBNAILSENTRY']._serialized_start=5259
  _globals['_YOURPODCASTSSHELFPROTO_THUMBNAILSENTRY']._serialized_end=5332
  _globals['_PODCASTPOINTPROTO']._serialized_start=5334
  _globals['_PODCASTPOINTPROTO']._serialized_end=5424
  _globals['_PODCASTTHUMBNAILPROTO']._serialized_start=5427
  _globals['_PODCASTTHUMBNAILPROTO']._serialized_end=5735
  _globals['_PODCASTAUDIOPROTO']._serialized_start=5737
  _globals['_PODCASTAUDIOPROTO']._serialized_end=5815
  _globals['_PODCASTCARDSPROTO']._serialized_start=5817
  _globals['_PODCASTCARDSPROTO']._serialized_end=5888
  _globals['_PODCASTCARDPROTO']._serialized_start=5891
  _globals['_PODCASTCARDPROTO']._serialized_end=6100
  _globals['_PODCASTERRORPROTO']._serialized_start=6102
  _globals['_PODCASTERRORPROTO']._serialized_end=6138
  _globals['_PODCASTPROMPTANSWERPROTO']._serialized_start=6140
  _globals['_PODCASTPROMPTANSWERPROTO']._serialized_end=6180
  _globals['_PODCASTVISUALSPROTO']._serialized_start=6182
  _globals['_PODCASTVISUALSPROTO']._serialized_end=6241
  _globals['_PODCASTVISUALPROTO']._serialized_start=6244
  _globals['_PODCASTVISUALPROTO']._serialized_end=6410
  _globals['_PODCASTVISUALANIMATIONPROTO']._serialized_start=6412
  _globals['_PODCASTVISUALANIMATIONPROTO']._serialized_end=6506
  _globals['_PODCASTTRANSCRIPTPROTO']._serialized_start=6508
  _globals['_PODCASTTRANSCRIPTPROTO']._serialized_end=6579
  _globals['_PODCASTTRANSCRIPTENTRYPROTO']._serialized_start=6581
  _globals['_PODCASTTRANSCRIPTENTRYPROTO']._serialized_end=6677
  _globals['_PODCASTWORDPROTO']._serialized_start=6679
  _globals['_PODCASTWORDPROTO']._serialized_end=6772
  _globals['_PODCASTKNOWLEDGECARDPROTO']._serialized_start=6774
  _globals['_PODCASTKNOWLEDGECARDPROTO']._serialized_end=6888
  _globals['_PODCASTMULTIPLECHOICECARDPROTO']._serialized_start=6891
  _globals['_PODCASTMULTIPLECHOICECARDPROTO']._serialized_end=7112
  _globals['_PODCASTPOLLCARDPROTO']._serialized_start=7115
  _globals['_PODCASTPOLLCARDPROTO']._serialized_end=7249
  _globals['_PODCASTCARDHEROPROTO']._serialized_start=7251
  _globals['_PODCASTCARDHEROPROTO']._serialized_end=7308
  _globals['_PODCASTMULTIPLECHOICEOPTIONPROTO']._serialized_start=7310
  _globals['_PODCASTMULTIPLECHOICEOPTIONPROTO']._serialized_end=7358
  _globals['_PODCASTPOLLOPTIONPROTO']._serialized_start=7360
  _globals['_PODCASTPOLLOPTIONPROTO']._serialized_end=7398
  _globals['_PODCASTKEYPOINTSPROTO']._serialized_start=7400
  _globals['_PODCASTKEYPOINTSPROTO']._serialized_end=7481
  _globals['_PODCASTFOLLOWUPSPROTO']._serialized_start=7483
  _globals['_PODCASTFOLLOWUPSPROTO']._serialized_end=7563
  _globals['_PODCASTFOLLOWUPPROTO']._serialized_start=7565
  _globals['_PODCASTFOLLOWUPPROTO']._serialized_end=7648
  _globals['_PODCASTKEYPOINTPROTO']._serialized_start=7650
  _globals['_PODCASTKEYPOINTPROTO']._serialized_end=7747
  _globals['_PODCASTCOMPLETIONPROTO']._serialized_start=7749
  _globals['_PODCASTCOMPLETIONPROTO']._serialized_end=7847
  _globals['_PODCASTSUGGESTIONSPROTO']._serialized_start=7850
  _globals['_PODCASTSUGGESTIONSPROTO']._serialized_end=8037
  _globals['_PODCASTSUGGESTIONSGENERATIONSTATEPROTO']._serialized_start=8040
  _globals['_PODCASTSUGGESTIONSGENERATIONSTATEPROTO']._serialized_end=8221
  _globals['_PODCASTSUGGESTIONSSECTIONPROTO']._serialized_start=8224
  _globals['_PODCASTSUGGESTIONSSECTIONPROTO']._serialized_end=8491
  _globals['_PODCASTSTORYTHUMBNAILPROTO']._serialized_start=8493
  _globals['_PODCASTSTORYTHUMBNAILPROTO']._serialized_end=8578
  _globals['_PODCASTSTORYHEADERPROTO']._serialized_start=8580
  _globals['_PODCASTSTORYHEADERPROTO']._serialized_end=8620
  _globals['_PODCASTSTORYSLIDEPROTO']._serialized_start=8622
  _globals['_PODCASTSTORYSLIDEPROTO']._serialized_end=8736
  _globals['_PODCASTROUTINEPROTO']._serialized_start=8738
  _globals['_PODCASTROUTINEPROTO']._serialized_end=8841
  _globals['_PODCASTROUTINESEGMENTPROTO']._serialized_start=8843
  _globals['_PODCASTROUTINESEGMENTPROTO']._serialized_end=8947
  _globals['_PODCASTROUTINESTEPPROTO']._serialized_start=8949
  _globals['_PODCASTROUTINESTEPPROTO']._serialized_end=9041
  _globals['_PODCASTAPPSTORETRANSACTIONPROTO']._serialized_start=9043
  _globals['_PODCASTAPPSTORETRANSACTIONPROTO']._serialized_end=9127
  _globals['_PODCASTUSERPROGRESSPROTO']._serialized_start=9130
  _globals['_PODCASTUSERPROGRESSPROTO']._serialized_end=9316
  _globals['_PODCASTUSERPROGRESSPROTO_ROUTINEPROGRESSENTRY']._serialized_start=9232
  _globals['_PODCASTUSERPROGRESSPROTO_ROUTINEPROGRESSENTRY']._serialized_end=9316
  _globals['_PODCASTROUTINEPROGRESSPROTO']._serialized_start=9319
  _globals['_PODCASTROUTINEPROGRESSPROTO']._serialized_end=9506
  _globals['_PODCASTROUTINEPROGRESSPROTO_STEPPROGRESSENTRY']._serialized_start=9421
  _globals['_PODCASTROUTINEPROGRESSPROTO_STEPPROGRESSENTRY']._serialized_end=9506
  _globals['_PODCASTROUTINESTEPPROGRESSPROTO']._serialized_start=9508
  _globals['_PODCASTROUTINESTEPPROGRESSPROTO']._serialized_end=9610
  _globals['_PODCASTONBOARDINGINPUTPROTO']._serialized_start=9613
  _globals['_PODCASTONBOARDINGINPUTPROTO']._serialized_end=9742
  _globals['_ONDEVICESTOREDUSERDETAILSPROTO']._serialized_start=9745
  _globals['_ONDEVICESTOREDUSERDETAILSPROTO']._serialized_end=9892
  _globals['_PODCASTONBOARDINGCONFIGPROTO']._serialized_start=9895
  _globals['_PODCASTONBOARDINGCONFIGPROTO']._serialized_end=10186
  _globals['_PODCASTONBOARDINGGOALSCONFIGPROTO']._serialized_start=10189
  _globals['_PODCASTONBOARDINGGOALSCONFIGPROTO']._serialized_end=10321
  _globals['_PODCASTONBOARDINGLEARNINGSTYLESCONFIGPROTO']._serialized_start=10324
  _globals['_PODCASTONBOARDINGLEARNINGSTYLESCONFIGPROTO']._serialized_end=10484
  _globals['_PODCASTONBOARDINGINTERESTSCONFIGPROTO']._serialized_start=10487
  _globals['_PODCASTONBOARDINGINTERESTSCONFIGPROTO']._serialized_end=10642
  _globals['_PODCASTONBOARDINGVOICESCONFIGPROTO']._serialized_start=10645
  _globals['_PODCASTONBOARDINGVOICESCONFIGPROTO']._serialized_end=10780
  _globals['_PODCASTONBOARDINGINTERESTGROUPPROTO']._serialized_start=10782
  _globals['_PODCASTONBOARDINGINTERESTGROUPPROTO']._serialized_end=10898
  _globals['_PODCASTONBOARDINGGOALPROTO']._serialized_start=10900
  _globals['_PODCASTONBOARDINGGOALPROTO']._serialized_end=10975
  _globals['_PODCASTONBOARDINGLEARNINGSTYLEPROTO']._serialized_start=10977
  _globals['_PODCASTONBOARDINGLEARNINGSTYLEPROTO']._serialized_end=11089
  _globals['_PODCASTONBOARDINGINTERESTPROTO']._serialized_start=11091
  _globals['_PODCASTONBOARDINGINTERESTPROTO']._serialized_end=11174
  _globals['_PODCASTONBOARDINGVOICEPROTO']._serialized_start=11176
  _globals['_PODCASTONBOARDINGVOICEPROTO']._serialized_end=11278
# @@protoc_insertion_point(module_scope)
