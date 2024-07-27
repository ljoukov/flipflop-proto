# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: StoredPodcastProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import LogProto_pb2 as LogProto__pb2
import PodcastProto_pb2 as PodcastProto__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18StoredPodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0eLogProto.proto\x1a\x12PodcastProto.proto\"\xec\x05\n\x12StoredPodcastProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\nuser_input\x18\x05 \x01(\x0b\x32\x1c.StoredPodcastUserInputProto\x12<\n\x10suggestion_input\x18\x0f \x01(\x0b\x32\".StoredPodcastSuggestionInputProto\x12\'\n\x05state\x18\x06 \x01(\x0e\x32\x18.StoredPodcastStateProto\x12)\n\x06\x61nswer\x18\x07 \x01(\x0b\x32\x19.PodcastPromptAnswerProto\x12)\n\x06points\x18\x08 \x01(\x0b\x32\x19.StoredPodcastPointsProto\x12%\n\x04plan\x18\t \x01(\x0b\x32\x17.StoredPodcastPlanProto\x12\x31\n\ntranscript\x18\n \x01(\x0b\x32\x1d.StoredPodcastTranscriptProto\x12\'\n\x05\x61udio\x18\x0b \x01(\x0b\x32\x18.StoredPodcastAudioProto\x12+\n\x07visuals\x18\x0c \x01(\x0b\x32\x1a.StoredPodcastVisualsProto\x12\x30\n\nkey_points\x18\r \x01(\x0b\x32\x1c.StoredPodcastKeyPointsProto\x12/\n\tfollowups\x18\x0e \x01(\x0b\x32\x1c.StoredPodcastFollowupsProto\x12\x16\n\x03log\x18\x65 \x01(\x0b\x32\t.LogProtoJ\x04\x08\x64\x10\x65\"@\n\x1bStoredPodcastUserInputProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\x12\x11\n\tpoint_ids\x18\x02 \x03(\t\"\x98\x02\n!StoredPodcastSuggestionInputProto\x12\x1d\n\x15suggestion_section_id\x18\x01 \x01(\t\x12$\n\x1csuggestion_section_reasoning\x18\x02 \x01(\t\x12\x18\n\x10suggestion_title\x18\x03 \x01(\t\x12#\n\x1bsuggestion_thumbnail_prompt\x18\x04 \x01(\t\x12\x18\n\x10suggestion_badge\x18\x05 \x01(\t\x12\x34\n\x11suggestion_points\x18\x06 \x01(\x0b\x32\x19.StoredPodcastPointsProto\x12\x1f\n\x17user_selected_point_ids\x18\x07 \x03(\t\"D\n\x18StoredPodcastPointsProto\x12(\n\x06points\x18\x01 \x03(\x0b\x32\x18.StoredPodcastPointProto\"s\n\x17StoredPodcastPointProto\x12\x10\n\x08point_id\x18\x01 \x01(\t\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x04 \x01(\t\x12\x0f\n\x07outline\x18\x05 \x01(\t\"5\n\x16StoredPodcastPlanProto\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04plan\x18\x02 \x01(\t\"V\n\x1cStoredPodcastTranscriptProto\x12\x36\n\x08sections\x18\x01 \x03(\x0b\x32$.StoredPodcastSectionTranscriptProto\"\x90\x01\n#StoredPodcastSectionTranscriptProto\x12\x34\n\x0csection_type\x18\x01 \x01(\x0e\x32\x1e.StoredPodcastSectionTypeProto\x12\x33\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\".StoredPodcastTranscriptEntryProto\"|\n!StoredPodcastTranscriptEntryProto\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x14\n\x0cstart_millis\x18\x03 \x01(\x05\x12\x12\n\nend_millis\x18\x04 \x01(\x05\"\x8e\x01\n\x19StoredPodcastVisualsProto\x12\x14\n\x0cstyle_prompt\x18\x01 \x01(\t\x12\x18\n\x10thumbnail_prompt\x18\x02 \x01(\t\x12\x15\n\rthumbnail_key\x18\x03 \x01(\t\x12*\n\x07visuals\x18\x04 \x03(\x0b\x32\x19.StoredPodcastVisualProto\"\x90\x01\n\x18StoredPodcastVisualProto\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x05\x12\x14\n\x0cimage_prompt\x18\x02 \x01(\t\x12\x11\n\timage_key\x18\x03 \x01(\t\x12\x31\n\ntransition\x18\x04 \x01(\x0e\x32\x1d.PodcastVisualTransitionProto\"\x81\x01\n\x17StoredPodcastAudioProto\x12\x11\n\taudio_key\x18\x01 \x01(\t\x12\x31\n\x0e\x61udio_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12 \n\x05words\x18\x03 \x03(\x0b\x32\x11.PodcastWordProto\"]\n\x1bStoredPodcastKeyPointsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12/\n\nkey_points\x18\x02 \x03(\x0b\x32\x1b.StoredPodcastKeyPointProto\"\\\n\x1bStoredPodcastFollowupsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12.\n\tfollowups\x18\x02 \x03(\x0b\x32\x1b.StoredPodcastFollowupProto\"d\n\x1aStoredPodcastFollowupProto\x12\x13\n\x0b\x66ollowup_id\x18\x01 \x01(\t\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\r\n\x05\x65moji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"g\n\x1aStoredPodcastKeyPointProto\x12\x14\n\x0ckey_point_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"\xc6\x02\n\x1dStoredPodcastSuggestionsProto\x12\x16\n\x0esuggestions_id\x18\x01 \x01(\t\x12\x32\n\x05state\x18\x02 \x01(\x0e\x32#.StoredPodcastSuggestionsStateProto\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\treasoning\x18\x05 \x01(\t\x12\x0f\n\x07ranking\x18\x06 \x01(\t\x12\x37\n\x08sections\x18\x07 \x03(\x0b\x32%.StoredPodcastSuggestionsSectionProto\x12\x16\n\x03log\x18\x65 \x01(\x0b\x32\t.LogProtoJ\x04\x08\x64\x10\x65\"\xce\x02\n$StoredPodcastSuggestionsSectionProto\x12\x12\n\nsection_id\x18\x01 \x01(\t\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x14\n\x0cstyle_prompt\x18\x04 \x01(\t\x12\x38\n\x11\x62\x61nner_suggestion\x18\x05 \x01(\x0b\x32\x1d.StoredPodcastSuggestionProto\x12\x38\n\x11\x66ooter_suggestion\x18\x06 \x01(\x0b\x32\x1d.StoredPodcastSuggestionProto\x12\x32\n\x06story1\x18\x07 \x01(\x0b\x32\".StoredPodcastStorySuggestionProto\x12\x32\n\x06story2\x18\x08 \x01(\x0b\x32\".StoredPodcastStorySuggestionProto\"\x8b\x01\n\x1cStoredPodcastSuggestionProto\x12\x1c\n\x14suggested_podcast_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x03 \x01(\t\x12\x18\n\x10thumbnail_prompt\x18\x04 \x01(\t\x12\x15\n\rthumbnail_key\x18\x05 \x01(\t\"\x7f\n!StoredPodcastStorySuggestionProto\x12\x1a\n\x12suggested_story_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x18\n\x10thumbnail_prompt\x18\x03 \x01(\t\x12\x15\n\rthumbnail_key\x18\x04 \x01(\t\"\xf0\x02\n\x17StoredPodcastStoryProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x05state\x18\x06 \x01(\x0e\x32\x1d.StoredPodcastStoryStateProto\x12,\n\x05input\x18\x07 \x01(\x0b\x32\x1d.StoredPodcastStoryInputProto\x12.\n\x06slides\x18\x08 \x01(\x0b\x32\x1e.StoredPodcastStorySlidesProto\x12\x16\n\x03log\x18\x64 \x01(\x0b\x32\t.LogProto\"e\n\x1cStoredPodcastStoryInputProto\x12=\n\nsuggestion\x18\x01 \x01(\x0b\x32\'.StoredPodcastStorySuggestionInputProtoH\x00\x42\x06\n\x04type\"\xef\x01\n&StoredPodcastStorySuggestionInputProto\x12\x1d\n\x15suggestion_section_id\x18\x01 \x01(\t\x12$\n\x1csuggestion_section_reasoning\x18\x02 \x01(\t\x12\x18\n\x10suggestion_title\x18\x03 \x01(\t\x12\x1f\n\x17suggestion_style_prompt\x18\x04 \x01(\t\x12#\n\x1bsuggestion_thumbnail_prompt\x18\x05 \x01(\t\x12 \n\x18suggestion_thumbnail_key\x18\x06 \x01(\t\"\x86\x01\n\x1dStoredPodcastStorySlidesProto\x12\x10\n\x08is_ready\x18\x01 \x01(\x08\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\x11\n\tstructure\x18\x03 \x01(\t\x12-\n\x06slides\x18\x04 \x03(\x0b\x32\x1d.StoredPodcastStorySlideProto\"t\n\x1cStoredPodcastStorySlideProto\x12\x10\n\x08slide_id\x18\x01 \x01(\t\x12\x10\n\x08is_ready\x18\x02 \x01(\x08\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x04 \x01(\t\x12\x0c\n\x04text\x18\x05 \x01(\t\"a\n\"StoredPodcastQueryCompletionsProto\x12;\n\x07section\x18\x01 \x03(\x0b\x32*.StoredPodcastQueryCompletionsSectionProto\"j\n)StoredPodcastQueryCompletionsSectionProto\x12=\n\x11query_completions\x18\x01 \x03(\x0b\x32\".StoredPodcastQueryCompletionProto\"2\n!StoredPodcastQueryCompletionProto\x12\r\n\x05query\x18\x01 \x01(\t*\xf8\x01\n\x17StoredPodcastStateProto\x12&\n\"STORED_PODCAST_STATE_PROTO_UNKNOWN\x10\x00\x12$\n STORED_PODCAST_STATE_PROTO_READY\x10\x01\x12*\n&STORED_PODCAST_STATE_PROTO_INPUT_READY\x10\x02\x12\x31\n-STORED_PODCAST_STATE_PROTO_GENERATION_STARTED\x10\x03\x12\x30\n,STORED_PODCAST_STATE_PROTO_GENERATION_FAILED\x10\x04*\xe3\x01\n\x1dStoredPodcastSectionTypeProto\x12-\n)STORED_PODCAST_SECTION_TYPE_PROTO_UNKNOWN\x10\x00\x12\x32\n.STORED_PODCAST_SECTION_TYPE_PROTO_INTRODUCTION\x10\x01\x12-\n)STORED_PODCAST_SECTION_TYPE_PROTO_SECTION\x10\x02\x12\x30\n,STORED_PODCAST_SECTION_TYPE_PROTO_CONCLUSION\x10\x03*\xf6\x01\n\"StoredPodcastSuggestionsStateProto\x12\x34\n0STORED_PODCAST_SUGGESTIONS_STATE_PROTO_UNDEFINED\x10\x00\x12\x35\n1STORED_PODCAST_SUGGESTIONS_STATE_PROTO_GENERATING\x10\x01\x12\x30\n,STORED_PODCAST_SUGGESTIONS_STATE_PROTO_READY\x10\x02\x12\x31\n-STORED_PODCAST_SUGGESTIONS_STATE_PROTO_FAILED\x10\x03*\x8a\x02\n\x1cStoredPodcastStoryStateProto\x12.\n*STORED_PODCAST_STORY_STATE_PROTO_UNDEFINED\x10\x00\x12\x30\n,STORED_PODCAST_STORY_STATE_PROTO_INPUT_READY\x10\x01\x12/\n+STORED_PODCAST_STORY_STATE_PROTO_GENERATING\x10\x02\x12*\n&STORED_PODCAST_STORY_STATE_PROTO_READY\x10\x03\x12+\n\'STORED_PODCAST_STORY_STATE_PROTO_FAILED\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'StoredPodcastProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STOREDPODCASTSTATEPROTO._serialized_start=4820
  _STOREDPODCASTSTATEPROTO._serialized_end=5068
  _STOREDPODCASTSECTIONTYPEPROTO._serialized_start=5071
  _STOREDPODCASTSECTIONTYPEPROTO._serialized_end=5298
  _STOREDPODCASTSUGGESTIONSSTATEPROTO._serialized_start=5301
  _STOREDPODCASTSUGGESTIONSSTATEPROTO._serialized_end=5547
  _STOREDPODCASTSTORYSTATEPROTO._serialized_start=5550
  _STOREDPODCASTSTORYSTATEPROTO._serialized_end=5816
  _STOREDPODCASTPROTO._serialized_start=130
  _STOREDPODCASTPROTO._serialized_end=878
  _STOREDPODCASTUSERINPUTPROTO._serialized_start=880
  _STOREDPODCASTUSERINPUTPROTO._serialized_end=944
  _STOREDPODCASTSUGGESTIONINPUTPROTO._serialized_start=947
  _STOREDPODCASTSUGGESTIONINPUTPROTO._serialized_end=1227
  _STOREDPODCASTPOINTSPROTO._serialized_start=1229
  _STOREDPODCASTPOINTSPROTO._serialized_end=1297
  _STOREDPODCASTPOINTPROTO._serialized_start=1299
  _STOREDPODCASTPOINTPROTO._serialized_end=1414
  _STOREDPODCASTPLANPROTO._serialized_start=1416
  _STOREDPODCASTPLANPROTO._serialized_end=1469
  _STOREDPODCASTTRANSCRIPTPROTO._serialized_start=1471
  _STOREDPODCASTTRANSCRIPTPROTO._serialized_end=1557
  _STOREDPODCASTSECTIONTRANSCRIPTPROTO._serialized_start=1560
  _STOREDPODCASTSECTIONTRANSCRIPTPROTO._serialized_end=1704
  _STOREDPODCASTTRANSCRIPTENTRYPROTO._serialized_start=1706
  _STOREDPODCASTTRANSCRIPTENTRYPROTO._serialized_end=1830
  _STOREDPODCASTVISUALSPROTO._serialized_start=1833
  _STOREDPODCASTVISUALSPROTO._serialized_end=1975
  _STOREDPODCASTVISUALPROTO._serialized_start=1978
  _STOREDPODCASTVISUALPROTO._serialized_end=2122
  _STOREDPODCASTAUDIOPROTO._serialized_start=2125
  _STOREDPODCASTAUDIOPROTO._serialized_end=2254
  _STOREDPODCASTKEYPOINTSPROTO._serialized_start=2256
  _STOREDPODCASTKEYPOINTSPROTO._serialized_end=2349
  _STOREDPODCASTFOLLOWUPSPROTO._serialized_start=2351
  _STOREDPODCASTFOLLOWUPSPROTO._serialized_end=2443
  _STOREDPODCASTFOLLOWUPPROTO._serialized_start=2445
  _STOREDPODCASTFOLLOWUPPROTO._serialized_end=2545
  _STOREDPODCASTKEYPOINTPROTO._serialized_start=2547
  _STOREDPODCASTKEYPOINTPROTO._serialized_end=2650
  _STOREDPODCASTSUGGESTIONSPROTO._serialized_start=2653
  _STOREDPODCASTSUGGESTIONSPROTO._serialized_end=2979
  _STOREDPODCASTSUGGESTIONSSECTIONPROTO._serialized_start=2982
  _STOREDPODCASTSUGGESTIONSSECTIONPROTO._serialized_end=3316
  _STOREDPODCASTSUGGESTIONPROTO._serialized_start=3319
  _STOREDPODCASTSUGGESTIONPROTO._serialized_end=3458
  _STOREDPODCASTSTORYSUGGESTIONPROTO._serialized_start=3460
  _STOREDPODCASTSTORYSUGGESTIONPROTO._serialized_end=3587
  _STOREDPODCASTSTORYPROTO._serialized_start=3590
  _STOREDPODCASTSTORYPROTO._serialized_end=3958
  _STOREDPODCASTSTORYINPUTPROTO._serialized_start=3960
  _STOREDPODCASTSTORYINPUTPROTO._serialized_end=4061
  _STOREDPODCASTSTORYSUGGESTIONINPUTPROTO._serialized_start=4064
  _STOREDPODCASTSTORYSUGGESTIONINPUTPROTO._serialized_end=4303
  _STOREDPODCASTSTORYSLIDESPROTO._serialized_start=4306
  _STOREDPODCASTSTORYSLIDESPROTO._serialized_end=4440
  _STOREDPODCASTSTORYSLIDEPROTO._serialized_start=4442
  _STOREDPODCASTSTORYSLIDEPROTO._serialized_end=4558
  _STOREDPODCASTQUERYCOMPLETIONSPROTO._serialized_start=4560
  _STOREDPODCASTQUERYCOMPLETIONSPROTO._serialized_end=4657
  _STOREDPODCASTQUERYCOMPLETIONSSECTIONPROTO._serialized_start=4659
  _STOREDPODCASTQUERYCOMPLETIONSSECTIONPROTO._serialized_end=4765
  _STOREDPODCASTQUERYCOMPLETIONPROTO._serialized_start=4767
  _STOREDPODCASTQUERYCOMPLETIONPROTO._serialized_end=4817
# @@protoc_insertion_point(module_scope)
