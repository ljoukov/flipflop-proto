# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: StoredPodcastProto.proto
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
    'StoredPodcastProto.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import LogProto_pb2 as LogProto__pb2
import PodcastProto_pb2 as PodcastProto__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18StoredPodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0eLogProto.proto\x1a\x12PodcastProto.proto\"\xc1\x07\n\x12StoredPodcastProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\nuser_input\x18\x05 \x01(\x0b\x32\x1c.StoredPodcastUserInputProto\x12<\n\x10suggestion_input\x18\x0f \x01(\x0b\x32\".StoredPodcastSuggestionInputProto\x12\'\n\x05state\x18\x06 \x01(\x0e\x32\x18.StoredPodcastStateProto\x12)\n\x06\x61nswer\x18\x07 \x01(\x0b\x32\x19.PodcastPromptAnswerProto\x12)\n\x06points\x18\x08 \x01(\x0b\x32\x19.StoredPodcastPointsProto\x12%\n\x04plan\x18\t \x01(\x0b\x32\x17.StoredPodcastPlanProto\x12\x31\n\ntranscript\x18\n \x01(\x0b\x32\x1d.StoredPodcastTranscriptProto\x12\'\n\x05\x61udio\x18\x0b \x01(\x0b\x32\x18.StoredPodcastAudioProto\x12+\n\x07visuals\x18\x0c \x01(\x0b\x32\x1a.StoredPodcastVisualsProto\x12\x30\n\nkey_points\x18\r \x01(\x0b\x32\x1c.StoredPodcastKeyPointsProto\x12/\n\tfollowups\x18\x0e \x01(\x0b\x32\x1c.StoredPodcastFollowupsProto\x12-\n\x0cpodcast_type\x18\x11 \x01(\x0e\x32\x17.StoredPodcastTypeProto\x12-\n\x08\x65xercise\x18\x12 \x01(\x0b\x32\x1b.StoredPodcastExerciseProto\x12\x16\n\x03log\x18\x65 \x01(\x0b\x32\t.LogProto\x12?\n\x0fllm_request_ids\x18\x66 \x03(\x0b\x32&.StoredPodcastProto.LlmRequestIdsEntry\x1a\x34\n\x12LlmRequestIdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x64\x10\x65\"@\n\x1bStoredPodcastUserInputProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\x12\x11\n\tpoint_ids\x18\x02 \x03(\t\"\xb3\x02\n!StoredPodcastSuggestionInputProto\x12\x1d\n\x15suggestion_section_id\x18\x01 \x01(\t\x12$\n\x1csuggestion_section_reasoning\x18\x02 \x01(\t\x12\x18\n\x10suggestion_title\x18\x03 \x01(\t\x12#\n\x1bsuggestion_thumbnail_prompt\x18\x04 \x01(\t\x12\x18\n\x10suggestion_badge\x18\x05 \x01(\t\x12\x34\n\x11suggestion_points\x18\x06 \x01(\x0b\x32\x19.StoredPodcastPointsProto\x12:\n\nuser_input\x18\x07 \x01(\x0b\x32&.StoredPodcastSuggestionUserInputProto\":\n%StoredPodcastSuggestionUserInputProto\x12\x11\n\tpoint_ids\x18\x01 \x03(\t\"D\n\x18StoredPodcastPointsProto\x12(\n\x06points\x18\x01 \x03(\x0b\x32\x18.StoredPodcastPointProto\"s\n\x17StoredPodcastPointProto\x12\x10\n\x08point_id\x18\x01 \x01(\t\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x04 \x01(\t\x12\x0f\n\x07outline\x18\x05 \x01(\t\"5\n\x16StoredPodcastPlanProto\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04plan\x18\x02 \x01(\t\"V\n\x1cStoredPodcastTranscriptProto\x12\x36\n\x08sections\x18\x01 \x03(\x0b\x32$.StoredPodcastSectionTranscriptProto\"\x90\x01\n#StoredPodcastSectionTranscriptProto\x12\x34\n\x0csection_type\x18\x01 \x01(\x0e\x32\x1e.StoredPodcastSectionTypeProto\x12\x33\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\".StoredPodcastTranscriptEntryProto\"|\n!StoredPodcastTranscriptEntryProto\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x14\n\x0cstart_millis\x18\x03 \x01(\x05\x12\x12\n\nend_millis\x18\x04 \x01(\x05\"M\n\x17StoredPodcastStyleProto\x12\x32\n\x0bimage_style\x18\x01 \x01(\x0e\x32\x1d.StoredPodcastImageStyleProto\"\xa7\x01\n\x19StoredPodcastVisualsProto\x12\'\n\x05style\x18\x05 \x01(\x0b\x32\x18.StoredPodcastStyleProto\x12\x18\n\x10thumbnail_prompt\x18\x02 \x01(\t\x12\x15\n\rthumbnail_key\x18\x03 \x01(\t\x12*\n\x07visuals\x18\x04 \x03(\x0b\x32\x19.StoredPodcastVisualProtoJ\x04\x08\x01\x10\x02\"\x90\x01\n\x18StoredPodcastVisualProto\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x05\x12\x14\n\x0cimage_prompt\x18\x02 \x01(\t\x12\x11\n\timage_key\x18\x03 \x01(\t\x12\x31\n\ntransition\x18\x04 \x01(\x0e\x32\x1d.PodcastVisualTransitionProto\"\x81\x01\n\x17StoredPodcastAudioProto\x12\x11\n\taudio_key\x18\x01 \x01(\t\x12\x31\n\x0e\x61udio_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12 \n\x05words\x18\x03 \x03(\x0b\x32\x11.PodcastWordProto\"]\n\x1bStoredPodcastKeyPointsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12/\n\nkey_points\x18\x02 \x03(\x0b\x32\x1b.StoredPodcastKeyPointProto\"\\\n\x1bStoredPodcastFollowupsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12.\n\tfollowups\x18\x02 \x03(\x0b\x32\x1b.StoredPodcastFollowupProto\"d\n\x1aStoredPodcastFollowupProto\x12\x13\n\x0b\x66ollowup_id\x18\x01 \x01(\t\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\r\n\x05\x65moji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"g\n\x1aStoredPodcastKeyPointProto\x12\x14\n\x0ckey_point_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"\xf3\x02\n\x1dStoredPodcastSuggestionsProto\x12\x16\n\x0esuggestions_id\x18\x01 \x01(\t\x12\x32\n\x05state\x18\x02 \x01(\x0e\x32#.StoredPodcastSuggestionsStateProto\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\treasoning\x18\x05 \x01(\t\x12\x0f\n\x07ranking\x18\x06 \x01(\t\x12\x37\n\x08sections\x18\x07 \x03(\x0b\x32%.StoredPodcastSuggestionsSectionProto\x12+\n\x07routine\x18\x08 \x01(\x0b\x32\x1a.StoredPodcastRoutineProto\x12\x16\n\x03log\x18\x65 \x01(\x0b\x32\t.LogProtoJ\x04\x08\x64\x10\x65\"\xe7\x02\n$StoredPodcastSuggestionsSectionProto\x12\x12\n\nsection_id\x18\x01 \x01(\t\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\'\n\x05style\x18\t \x01(\x0b\x32\x18.StoredPodcastStyleProto\x12\x38\n\x11\x62\x61nner_suggestion\x18\x05 \x01(\x0b\x32\x1d.StoredPodcastSuggestionProto\x12\x38\n\x11\x66ooter_suggestion\x18\x06 \x01(\x0b\x32\x1d.StoredPodcastSuggestionProto\x12\x32\n\x06story1\x18\x07 \x01(\x0b\x32\".StoredPodcastStorySuggestionProto\x12\x32\n\x06story2\x18\x08 \x01(\x0b\x32\".StoredPodcastStorySuggestionProtoJ\x04\x08\x04\x10\x05\"\x8b\x01\n\x1cStoredPodcastSuggestionProto\x12\x1c\n\x14suggested_podcast_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x03 \x01(\t\x12\x18\n\x10thumbnail_prompt\x18\x04 \x01(\t\x12\x15\n\rthumbnail_key\x18\x05 \x01(\t\"\x7f\n!StoredPodcastStorySuggestionProto\x12\x1a\n\x12suggested_story_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x18\n\x10thumbnail_prompt\x18\x03 \x01(\t\x12\x15\n\rthumbnail_key\x18\x04 \x01(\t\"\xf0\x02\n\x17StoredPodcastStoryProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x05state\x18\x06 \x01(\x0e\x32\x1d.StoredPodcastStoryStateProto\x12,\n\x05input\x18\x07 \x01(\x0b\x32\x1d.StoredPodcastStoryInputProto\x12.\n\x06slides\x18\x08 \x01(\x0b\x32\x1e.StoredPodcastStorySlidesProto\x12\x16\n\x03log\x18\x64 \x01(\x0b\x32\t.LogProto\"e\n\x1cStoredPodcastStoryInputProto\x12=\n\nsuggestion\x18\x01 \x01(\x0b\x32\'.StoredPodcastStorySuggestionInputProtoH\x00\x42\x06\n\x04type\"\x88\x02\n&StoredPodcastStorySuggestionInputProto\x12\x1d\n\x15suggestion_section_id\x18\x01 \x01(\t\x12$\n\x1csuggestion_section_reasoning\x18\x02 \x01(\t\x12\x18\n\x10suggestion_title\x18\x03 \x01(\t\x12\x32\n\x10suggestion_style\x18\x07 \x01(\x0b\x32\x18.StoredPodcastStyleProto\x12#\n\x1bsuggestion_thumbnail_prompt\x18\x05 \x01(\t\x12 \n\x18suggestion_thumbnail_key\x18\x06 \x01(\tJ\x04\x08\x04\x10\x05\"\x86\x01\n\x1dStoredPodcastStorySlidesProto\x12\x10\n\x08is_ready\x18\x01 \x01(\x08\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\x11\n\tstructure\x18\x03 \x01(\t\x12-\n\x06slides\x18\x04 \x03(\x0b\x32\x1d.StoredPodcastStorySlideProto\"\x8d\x01\n\x1cStoredPodcastStorySlideProto\x12\x10\n\x08slide_id\x18\x01 \x01(\t\x12\x15\n\ris_text_ready\x18\x02 \x01(\x08\x12\r\n\x05title\x18\x03 \x01(\t\x12\x14\n\x0cimage_prompt\x18\x04 \x01(\t\x12\x0c\n\x04text\x18\x05 \x01(\t\x12\x11\n\timage_key\x18\x06 \x01(\t\"\xa0\x01\n\x19StoredPodcastRoutineProto\x12\x12\n\nroutine_id\x18\x04 \x01(\t\x12\x11\n\treasoning\x18\x01 \x01(\t\x12\x33\n\x08segments\x18\x02 \x03(\x0b\x32!.StoredPodcastRoutineSegmentProto\x12\'\n\x05style\x18\x03 \x01(\x0b\x32\x18.StoredPodcastStyleProto\"\x9e\x01\n StoredPodcastRoutineSegmentProto\x12\x12\n\nsegment_id\x18\x01 \x01(\t\x12\x15\n\rsegment_label\x18\x05 \x01(\t\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12-\n\x05steps\x18\x04 \x03(\x0b\x32\x1e.StoredPodcastRoutineStepProto\"\xa8\x01\n\x1dStoredPodcastRoutineStepProto\x12\x0f\n\x07step_id\x18\x06 \x01(\t\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.StoredPodcastTypeProto\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07outline\x18\x03 \x01(\t\x12\x18\n\x10thumbnail_prompt\x18\x04 \x01(\t\x12\x15\n\rthumbnail_key\x18\x05 \x01(\t\"\x95\x02\n\x1aStoredPodcastExerciseProto\x12-\n\x04plan\x18\x01 \x01(\x0b\x32\x1f.StoredPodcastExercisePlanProto\x12\x32\n\x06warmup\x18\x02 \x01(\x0b\x32\".StoredPodcastExerciseSectionProto\x12\x35\n\texercises\x18\x03 \x03(\x0b\x32\".StoredPodcastExerciseSectionProto\x12\x34\n\x08\x63ooldown\x18\x04 \x01(\x0b\x32\".StoredPodcastExerciseSectionProto\x12\'\n\x05style\x18\x05 \x01(\x0b\x32\x18.StoredPodcastStyleProto\"\xa1\x01\n\x1eStoredPodcastExercisePlanProto\x12\r\n\x05title\x18\x01 \x01(\t\x12\r\n\x05ideas\x18\x02 \x01(\t\x12\x11\n\treasoning\x18\x03 \x01(\t\x12\x19\n\x11selected_category\x18\x04 \x01(\t\x12\x0e\n\x06warmup\x18\x05 \x01(\t\x12\x11\n\texercises\x18\x06 \x03(\t\x12\x10\n\x08\x63ooldown\x18\x07 \x01(\t\"\xb3\x01\n!StoredPodcastExerciseSectionProto\x12\x34\n\x08segments\x18\x01 \x03(\x0b\x32\".StoredPodcastExerciseSegmentProto\x12@\n\nbackground\x18\x02 \x01(\x0b\x32,.StoredPodcastExerciseSectionBackgroundProto\x12\x16\n\x0ellm_request_id\x18\x64 \x01(\t\"\xd6\x01\n!StoredPodcastExerciseSegmentProto\x12;\n\x0fspoken_segments\x18\x01 \x01(\x0b\x32 .StoredPodcastSpokenSegmentProtoH\x00\x12\x35\n\x04reps\x18\x02 \x01(\x0b\x32%.StoredPodcastExerciseVisualRepsProtoH\x00\x12\x35\n\x04text\x18\x03 \x01(\x0b\x32%.StoredPodcastExerciseVisualTextProtoH\x00\x42\x06\n\x04type\"V\n+StoredPodcastExerciseSectionBackgroundProto\x12\x14\n\x0cimage_prompt\x18\x01 \x01(\t\x12\x11\n\timage_key\x18\x02 \x01(\t\"\x92\x01\n\x1fStoredPodcastSpokenSegmentProto\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x30\n\rleading_pause\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0cmin_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\"5\n$StoredPodcastExerciseVisualTextProto\x12\r\n\x05title\x18\x01 \x01(\t\"\xae\x01\n$StoredPodcastExerciseVisualRepsProto\x12=\n\x06marker\x18\x01 \x01(\x0b\x32+.StoredPodcastExerciseVisualRepsMarkerProtoH\x00\x12?\n\x07\x63ounter\x18\x02 \x01(\x0b\x32,.StoredPodcastExerciseVisualRepsCounterProtoH\x00\x42\x06\n\x04type\"\xb7\x01\n*StoredPodcastExerciseVisualRepsMarkerProto\x12>\n\x04type\x18\x01 \x01(\x0e\x32\x30.StoredPodcastExerciseVisualRepsMarkerProto.Type\x12\x11\n\trep_total\x18\x02 \x01(\x05\"6\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\t\n\x05START\x10\x01\x12\x07\n\x03\x45ND\x10\x02\x12\x0b\n\x07\x43OUNTER\x10\x03\"T\n+StoredPodcastExerciseVisualRepsCounterProto\x12\x12\n\nrep_number\x18\x02 \x01(\x05\x12\x11\n\trep_total\x18\x03 \x01(\x05*\x81\x03\n\x17StoredPodcastStateProto\x12&\n\"STORED_PODCAST_STATE_PROTO_UNKNOWN\x10\x00\x12$\n STORED_PODCAST_STATE_PROTO_READY\x10\x01\x12,\n(STORED_PODCAST_STATE_PROTO_USER_PROMPTED\x10\n\x12(\n$STORED_PODCAST_STATE_PROTO_SUGGESTED\x10\x14\x12/\n+STORED_PODCAST_STATE_PROTO_SUGGESTED_POINTS\x10\x15\x12*\n&STORED_PODCAST_STATE_PROTO_INPUT_READY\x10\x02\x12\x31\n-STORED_PODCAST_STATE_PROTO_GENERATION_STARTED\x10\x03\x12\x30\n,STORED_PODCAST_STATE_PROTO_GENERATION_FAILED\x10\x04*\xe3\x01\n\x1dStoredPodcastSectionTypeProto\x12-\n)STORED_PODCAST_SECTION_TYPE_PROTO_UNKNOWN\x10\x00\x12\x32\n.STORED_PODCAST_SECTION_TYPE_PROTO_INTRODUCTION\x10\x01\x12-\n)STORED_PODCAST_SECTION_TYPE_PROTO_SECTION\x10\x02\x12\x30\n,STORED_PODCAST_SECTION_TYPE_PROTO_CONCLUSION\x10\x03*\xa0\x02\n\x1cStoredPodcastImageStyleProto\x12.\n*STORED_PODCAST_IMAGE_STYLE_PROTO_UNDEFINED\x10\x00\x12.\n*STORED_PODCAST_IMAGE_STYLE_PROTO_STORYBOOK\x10\x01\x12\x34\n0STORED_PODCAST_IMAGE_STYLE_PROTO_DIGITAL_ARTWORK\x10\x02\x12\x31\n-STORED_PODCAST_IMAGE_STYLE_PROTO_OIL_PAINTING\x10\x03\x12\x37\n3STORED_PODCAST_IMAGE_STYLE_PROTO_JAPANESE_ANIMATION\x10\x04*\xf6\x01\n\"StoredPodcastSuggestionsStateProto\x12\x34\n0STORED_PODCAST_SUGGESTIONS_STATE_PROTO_UNDEFINED\x10\x00\x12\x35\n1STORED_PODCAST_SUGGESTIONS_STATE_PROTO_GENERATING\x10\x01\x12\x30\n,STORED_PODCAST_SUGGESTIONS_STATE_PROTO_READY\x10\x02\x12\x31\n-STORED_PODCAST_SUGGESTIONS_STATE_PROTO_FAILED\x10\x03*\x8a\x02\n\x1cStoredPodcastStoryStateProto\x12.\n*STORED_PODCAST_STORY_STATE_PROTO_UNDEFINED\x10\x00\x12\x30\n,STORED_PODCAST_STORY_STATE_PROTO_INPUT_READY\x10\x01\x12/\n+STORED_PODCAST_STORY_STATE_PROTO_GENERATING\x10\x02\x12*\n&STORED_PODCAST_STORY_STATE_PROTO_READY\x10\x03\x12+\n\'STORED_PODCAST_STORY_STATE_PROTO_FAILED\x10\x04*\xbc\x01\n\x16StoredPodcastTypeProto\x12\'\n#STORED_PODCAST_TYPE_PROTO_UNDEFINED\x10\x00\x12\'\n#STORED_PODCAST_TYPE_PROTO_EXPLAINER\x10\x01\x12&\n\"STORED_PODCAST_TYPE_PROTO_EXERCISE\x10\x02\x12(\n$STORED_PODCAST_TYPE_PROTO_MEDITATION\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'StoredPodcastProto_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STOREDPODCASTPROTO_LLMREQUESTIDSENTRY']._loaded_options = None
  _globals['_STOREDPODCASTPROTO_LLMREQUESTIDSENTRY']._serialized_options = b'8\001'
  _globals['_STOREDPODCASTSTATEPROTO']._serialized_start=7165
  _globals['_STOREDPODCASTSTATEPROTO']._serialized_end=7550
  _globals['_STOREDPODCASTSECTIONTYPEPROTO']._serialized_start=7553
  _globals['_STOREDPODCASTSECTIONTYPEPROTO']._serialized_end=7780
  _globals['_STOREDPODCASTIMAGESTYLEPROTO']._serialized_start=7783
  _globals['_STOREDPODCASTIMAGESTYLEPROTO']._serialized_end=8071
  _globals['_STOREDPODCASTSUGGESTIONSSTATEPROTO']._serialized_start=8074
  _globals['_STOREDPODCASTSUGGESTIONSSTATEPROTO']._serialized_end=8320
  _globals['_STOREDPODCASTSTORYSTATEPROTO']._serialized_start=8323
  _globals['_STOREDPODCASTSTORYSTATEPROTO']._serialized_end=8589
  _globals['_STOREDPODCASTTYPEPROTO']._serialized_start=8592
  _globals['_STOREDPODCASTTYPEPROTO']._serialized_end=8780
  _globals['_STOREDPODCASTPROTO']._serialized_start=130
  _globals['_STOREDPODCASTPROTO']._serialized_end=1091
  _globals['_STOREDPODCASTPROTO_LLMREQUESTIDSENTRY']._serialized_start=1033
  _globals['_STOREDPODCASTPROTO_LLMREQUESTIDSENTRY']._serialized_end=1085
  _globals['_STOREDPODCASTUSERINPUTPROTO']._serialized_start=1093
  _globals['_STOREDPODCASTUSERINPUTPROTO']._serialized_end=1157
  _globals['_STOREDPODCASTSUGGESTIONINPUTPROTO']._serialized_start=1160
  _globals['_STOREDPODCASTSUGGESTIONINPUTPROTO']._serialized_end=1467
  _globals['_STOREDPODCASTSUGGESTIONUSERINPUTPROTO']._serialized_start=1469
  _globals['_STOREDPODCASTSUGGESTIONUSERINPUTPROTO']._serialized_end=1527
  _globals['_STOREDPODCASTPOINTSPROTO']._serialized_start=1529
  _globals['_STOREDPODCASTPOINTSPROTO']._serialized_end=1597
  _globals['_STOREDPODCASTPOINTPROTO']._serialized_start=1599
  _globals['_STOREDPODCASTPOINTPROTO']._serialized_end=1714
  _globals['_STOREDPODCASTPLANPROTO']._serialized_start=1716
  _globals['_STOREDPODCASTPLANPROTO']._serialized_end=1769
  _globals['_STOREDPODCASTTRANSCRIPTPROTO']._serialized_start=1771
  _globals['_STOREDPODCASTTRANSCRIPTPROTO']._serialized_end=1857
  _globals['_STOREDPODCASTSECTIONTRANSCRIPTPROTO']._serialized_start=1860
  _globals['_STOREDPODCASTSECTIONTRANSCRIPTPROTO']._serialized_end=2004
  _globals['_STOREDPODCASTTRANSCRIPTENTRYPROTO']._serialized_start=2006
  _globals['_STOREDPODCASTTRANSCRIPTENTRYPROTO']._serialized_end=2130
  _globals['_STOREDPODCASTSTYLEPROTO']._serialized_start=2132
  _globals['_STOREDPODCASTSTYLEPROTO']._serialized_end=2209
  _globals['_STOREDPODCASTVISUALSPROTO']._serialized_start=2212
  _globals['_STOREDPODCASTVISUALSPROTO']._serialized_end=2379
  _globals['_STOREDPODCASTVISUALPROTO']._serialized_start=2382
  _globals['_STOREDPODCASTVISUALPROTO']._serialized_end=2526
  _globals['_STOREDPODCASTAUDIOPROTO']._serialized_start=2529
  _globals['_STOREDPODCASTAUDIOPROTO']._serialized_end=2658
  _globals['_STOREDPODCASTKEYPOINTSPROTO']._serialized_start=2660
  _globals['_STOREDPODCASTKEYPOINTSPROTO']._serialized_end=2753
  _globals['_STOREDPODCASTFOLLOWUPSPROTO']._serialized_start=2755
  _globals['_STOREDPODCASTFOLLOWUPSPROTO']._serialized_end=2847
  _globals['_STOREDPODCASTFOLLOWUPPROTO']._serialized_start=2849
  _globals['_STOREDPODCASTFOLLOWUPPROTO']._serialized_end=2949
  _globals['_STOREDPODCASTKEYPOINTPROTO']._serialized_start=2951
  _globals['_STOREDPODCASTKEYPOINTPROTO']._serialized_end=3054
  _globals['_STOREDPODCASTSUGGESTIONSPROTO']._serialized_start=3057
  _globals['_STOREDPODCASTSUGGESTIONSPROTO']._serialized_end=3428
  _globals['_STOREDPODCASTSUGGESTIONSSECTIONPROTO']._serialized_start=3431
  _globals['_STOREDPODCASTSUGGESTIONSSECTIONPROTO']._serialized_end=3790
  _globals['_STOREDPODCASTSUGGESTIONPROTO']._serialized_start=3793
  _globals['_STOREDPODCASTSUGGESTIONPROTO']._serialized_end=3932
  _globals['_STOREDPODCASTSTORYSUGGESTIONPROTO']._serialized_start=3934
  _globals['_STOREDPODCASTSTORYSUGGESTIONPROTO']._serialized_end=4061
  _globals['_STOREDPODCASTSTORYPROTO']._serialized_start=4064
  _globals['_STOREDPODCASTSTORYPROTO']._serialized_end=4432
  _globals['_STOREDPODCASTSTORYINPUTPROTO']._serialized_start=4434
  _globals['_STOREDPODCASTSTORYINPUTPROTO']._serialized_end=4535
  _globals['_STOREDPODCASTSTORYSUGGESTIONINPUTPROTO']._serialized_start=4538
  _globals['_STOREDPODCASTSTORYSUGGESTIONINPUTPROTO']._serialized_end=4802
  _globals['_STOREDPODCASTSTORYSLIDESPROTO']._serialized_start=4805
  _globals['_STOREDPODCASTSTORYSLIDESPROTO']._serialized_end=4939
  _globals['_STOREDPODCASTSTORYSLIDEPROTO']._serialized_start=4942
  _globals['_STOREDPODCASTSTORYSLIDEPROTO']._serialized_end=5083
  _globals['_STOREDPODCASTROUTINEPROTO']._serialized_start=5086
  _globals['_STOREDPODCASTROUTINEPROTO']._serialized_end=5246
  _globals['_STOREDPODCASTROUTINESEGMENTPROTO']._serialized_start=5249
  _globals['_STOREDPODCASTROUTINESEGMENTPROTO']._serialized_end=5407
  _globals['_STOREDPODCASTROUTINESTEPPROTO']._serialized_start=5410
  _globals['_STOREDPODCASTROUTINESTEPPROTO']._serialized_end=5578
  _globals['_STOREDPODCASTEXERCISEPROTO']._serialized_start=5581
  _globals['_STOREDPODCASTEXERCISEPROTO']._serialized_end=5858
  _globals['_STOREDPODCASTEXERCISEPLANPROTO']._serialized_start=5861
  _globals['_STOREDPODCASTEXERCISEPLANPROTO']._serialized_end=6022
  _globals['_STOREDPODCASTEXERCISESECTIONPROTO']._serialized_start=6025
  _globals['_STOREDPODCASTEXERCISESECTIONPROTO']._serialized_end=6204
  _globals['_STOREDPODCASTEXERCISESEGMENTPROTO']._serialized_start=6207
  _globals['_STOREDPODCASTEXERCISESEGMENTPROTO']._serialized_end=6421
  _globals['_STOREDPODCASTEXERCISESECTIONBACKGROUNDPROTO']._serialized_start=6423
  _globals['_STOREDPODCASTEXERCISESECTIONBACKGROUNDPROTO']._serialized_end=6509
  _globals['_STOREDPODCASTSPOKENSEGMENTPROTO']._serialized_start=6512
  _globals['_STOREDPODCASTSPOKENSEGMENTPROTO']._serialized_end=6658
  _globals['_STOREDPODCASTEXERCISEVISUALTEXTPROTO']._serialized_start=6660
  _globals['_STOREDPODCASTEXERCISEVISUALTEXTPROTO']._serialized_end=6713
  _globals['_STOREDPODCASTEXERCISEVISUALREPSPROTO']._serialized_start=6716
  _globals['_STOREDPODCASTEXERCISEVISUALREPSPROTO']._serialized_end=6890
  _globals['_STOREDPODCASTEXERCISEVISUALREPSMARKERPROTO']._serialized_start=6893
  _globals['_STOREDPODCASTEXERCISEVISUALREPSMARKERPROTO']._serialized_end=7076
  _globals['_STOREDPODCASTEXERCISEVISUALREPSMARKERPROTO_TYPE']._serialized_start=7022
  _globals['_STOREDPODCASTEXERCISEVISUALREPSMARKERPROTO_TYPE']._serialized_end=7076
  _globals['_STOREDPODCASTEXERCISEVISUALREPSCOUNTERPROTO']._serialized_start=7078
  _globals['_STOREDPODCASTEXERCISEVISUALREPSCOUNTERPROTO']._serialized_end=7162
# @@protoc_insertion_point(module_scope)
