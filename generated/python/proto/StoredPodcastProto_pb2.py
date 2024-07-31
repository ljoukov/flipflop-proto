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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18StoredPodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0eLogProto.proto\x1a\x12PodcastProto.proto\"\xec\x05\n\x12StoredPodcastProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\nuser_input\x18\x05 \x01(\x0b\x32\x1c.StoredPodcastUserInputProto\x12<\n\x10suggestion_input\x18\x0f \x01(\x0b\x32\".StoredPodcastSuggestionInputProto\x12\'\n\x05state\x18\x06 \x01(\x0e\x32\x18.StoredPodcastStateProto\x12)\n\x06\x61nswer\x18\x07 \x01(\x0b\x32\x19.PodcastPromptAnswerProto\x12)\n\x06points\x18\x08 \x01(\x0b\x32\x19.StoredPodcastPointsProto\x12%\n\x04plan\x18\t \x01(\x0b\x32\x17.StoredPodcastPlanProto\x12\x31\n\ntranscript\x18\n \x01(\x0b\x32\x1d.StoredPodcastTranscriptProto\x12\'\n\x05\x61udio\x18\x0b \x01(\x0b\x32\x18.StoredPodcastAudioProto\x12+\n\x07visuals\x18\x0c \x01(\x0b\x32\x1a.StoredPodcastVisualsProto\x12\x30\n\nkey_points\x18\r \x01(\x0b\x32\x1c.StoredPodcastKeyPointsProto\x12/\n\tfollowups\x18\x0e \x01(\x0b\x32\x1c.StoredPodcastFollowupsProto\x12\x16\n\x03log\x18\x65 \x01(\x0b\x32\t.LogProtoJ\x04\x08\x64\x10\x65\"@\n\x1bStoredPodcastUserInputProto\x12\x0e\n\x06prompt\x18\x01 \x01(\t\x12\x11\n\tpoint_ids\x18\x02 \x03(\t\"\xb3\x02\n!StoredPodcastSuggestionInputProto\x12\x1d\n\x15suggestion_section_id\x18\x01 \x01(\t\x12$\n\x1csuggestion_section_reasoning\x18\x02 \x01(\t\x12\x18\n\x10suggestion_title\x18\x03 \x01(\t\x12#\n\x1bsuggestion_thumbnail_prompt\x18\x04 \x01(\t\x12\x18\n\x10suggestion_badge\x18\x05 \x01(\t\x12\x34\n\x11suggestion_points\x18\x06 \x01(\x0b\x32\x19.StoredPodcastPointsProto\x12:\n\nuser_input\x18\x07 \x01(\x0b\x32&.StoredPodcastSuggestionUserInputProto\":\n%StoredPodcastSuggestionUserInputProto\x12\x11\n\tpoint_ids\x18\x01 \x03(\t\"D\n\x18StoredPodcastPointsProto\x12(\n\x06points\x18\x01 \x03(\x0b\x32\x18.StoredPodcastPointProto\"s\n\x17StoredPodcastPointProto\x12\x10\n\x08point_id\x18\x01 \x01(\t\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x04 \x01(\t\x12\x0f\n\x07outline\x18\x05 \x01(\t\"5\n\x16StoredPodcastPlanProto\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04plan\x18\x02 \x01(\t\"V\n\x1cStoredPodcastTranscriptProto\x12\x36\n\x08sections\x18\x01 \x03(\x0b\x32$.StoredPodcastSectionTranscriptProto\"\x90\x01\n#StoredPodcastSectionTranscriptProto\x12\x34\n\x0csection_type\x18\x01 \x01(\x0e\x32\x1e.StoredPodcastSectionTypeProto\x12\x33\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\".StoredPodcastTranscriptEntryProto\"|\n!StoredPodcastTranscriptEntryProto\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x14\n\x0cstart_millis\x18\x03 \x01(\x05\x12\x12\n\nend_millis\x18\x04 \x01(\x05\"M\n\x17StoredPodcastStyleProto\x12\x32\n\x0bimage_style\x18\x01 \x01(\x0e\x32\x1d.StoredPodcastImageStyleProto\"\xa7\x01\n\x19StoredPodcastVisualsProto\x12\'\n\x05style\x18\x05 \x01(\x0b\x32\x18.StoredPodcastStyleProto\x12\x18\n\x10thumbnail_prompt\x18\x02 \x01(\t\x12\x15\n\rthumbnail_key\x18\x03 \x01(\t\x12*\n\x07visuals\x18\x04 \x03(\x0b\x32\x19.StoredPodcastVisualProtoJ\x04\x08\x01\x10\x02\"\x90\x01\n\x18StoredPodcastVisualProto\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x05\x12\x14\n\x0cimage_prompt\x18\x02 \x01(\t\x12\x11\n\timage_key\x18\x03 \x01(\t\x12\x31\n\ntransition\x18\x04 \x01(\x0e\x32\x1d.PodcastVisualTransitionProto\"\x81\x01\n\x17StoredPodcastAudioProto\x12\x11\n\taudio_key\x18\x01 \x01(\t\x12\x31\n\x0e\x61udio_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12 \n\x05words\x18\x03 \x03(\x0b\x32\x11.PodcastWordProto\"]\n\x1bStoredPodcastKeyPointsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12/\n\nkey_points\x18\x02 \x03(\x0b\x32\x1b.StoredPodcastKeyPointProto\"\\\n\x1bStoredPodcastFollowupsProto\x12\r\n\x05label\x18\x01 \x01(\t\x12.\n\tfollowups\x18\x02 \x03(\x0b\x32\x1b.StoredPodcastFollowupProto\"d\n\x1aStoredPodcastFollowupProto\x12\x13\n\x0b\x66ollowup_id\x18\x01 \x01(\t\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\r\n\x05\x65moji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"g\n\x1aStoredPodcastKeyPointProto\x12\x14\n\x0ckey_point_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x03 \x01(\t\x12\x0f\n\x07outline\x18\x04 \x01(\t\"\xc6\x02\n\x1dStoredPodcastSuggestionsProto\x12\x16\n\x0esuggestions_id\x18\x01 \x01(\t\x12\x32\n\x05state\x18\x02 \x01(\x0e\x32#.StoredPodcastSuggestionsStateProto\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\treasoning\x18\x05 \x01(\t\x12\x0f\n\x07ranking\x18\x06 \x01(\t\x12\x37\n\x08sections\x18\x07 \x03(\x0b\x32%.StoredPodcastSuggestionsSectionProto\x12\x16\n\x03log\x18\x65 \x01(\x0b\x32\t.LogProtoJ\x04\x08\x64\x10\x65\"\xe7\x02\n$StoredPodcastSuggestionsSectionProto\x12\x12\n\nsection_id\x18\x01 \x01(\t\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\'\n\x05style\x18\t \x01(\x0b\x32\x18.StoredPodcastStyleProto\x12\x38\n\x11\x62\x61nner_suggestion\x18\x05 \x01(\x0b\x32\x1d.StoredPodcastSuggestionProto\x12\x38\n\x11\x66ooter_suggestion\x18\x06 \x01(\x0b\x32\x1d.StoredPodcastSuggestionProto\x12\x32\n\x06story1\x18\x07 \x01(\x0b\x32\".StoredPodcastStorySuggestionProto\x12\x32\n\x06story2\x18\x08 \x01(\x0b\x32\".StoredPodcastStorySuggestionProtoJ\x04\x08\x04\x10\x05\"\x8b\x01\n\x1cStoredPodcastSuggestionProto\x12\x1c\n\x14suggested_podcast_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05\x62\x61\x64ge\x18\x03 \x01(\t\x12\x18\n\x10thumbnail_prompt\x18\x04 \x01(\t\x12\x15\n\rthumbnail_key\x18\x05 \x01(\t\"\x7f\n!StoredPodcastStorySuggestionProto\x12\x1a\n\x12suggested_story_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x18\n\x10thumbnail_prompt\x18\x03 \x01(\t\x12\x15\n\rthumbnail_key\x18\x04 \x01(\t\"\xf0\x02\n\x17StoredPodcastStoryProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x05state\x18\x06 \x01(\x0e\x32\x1d.StoredPodcastStoryStateProto\x12,\n\x05input\x18\x07 \x01(\x0b\x32\x1d.StoredPodcastStoryInputProto\x12.\n\x06slides\x18\x08 \x01(\x0b\x32\x1e.StoredPodcastStorySlidesProto\x12\x16\n\x03log\x18\x64 \x01(\x0b\x32\t.LogProto\"e\n\x1cStoredPodcastStoryInputProto\x12=\n\nsuggestion\x18\x01 \x01(\x0b\x32\'.StoredPodcastStorySuggestionInputProtoH\x00\x42\x06\n\x04type\"\x88\x02\n&StoredPodcastStorySuggestionInputProto\x12\x1d\n\x15suggestion_section_id\x18\x01 \x01(\t\x12$\n\x1csuggestion_section_reasoning\x18\x02 \x01(\t\x12\x18\n\x10suggestion_title\x18\x03 \x01(\t\x12\x32\n\x10suggestion_style\x18\x07 \x01(\x0b\x32\x18.StoredPodcastStyleProto\x12#\n\x1bsuggestion_thumbnail_prompt\x18\x05 \x01(\t\x12 \n\x18suggestion_thumbnail_key\x18\x06 \x01(\tJ\x04\x08\x04\x10\x05\"\x86\x01\n\x1dStoredPodcastStorySlidesProto\x12\x10\n\x08is_ready\x18\x01 \x01(\x08\x12\x11\n\treasoning\x18\x02 \x01(\t\x12\x11\n\tstructure\x18\x03 \x01(\t\x12-\n\x06slides\x18\x04 \x03(\x0b\x32\x1d.StoredPodcastStorySlideProto\"t\n\x1cStoredPodcastStorySlideProto\x12\x10\n\x08slide_id\x18\x01 \x01(\t\x12\x10\n\x08is_ready\x18\x02 \x01(\x08\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x04 \x01(\t\x12\x0c\n\x04text\x18\x05 \x01(\t\"a\n\"StoredPodcastQueryCompletionsProto\x12;\n\x07section\x18\x01 \x03(\x0b\x32*.StoredPodcastQueryCompletionsSectionProto\"j\n)StoredPodcastQueryCompletionsSectionProto\x12=\n\x11query_completions\x18\x01 \x03(\x0b\x32\".StoredPodcastQueryCompletionProto\"2\n!StoredPodcastQueryCompletionProto\x12\r\n\x05query\x18\x01 \x01(\t*\x81\x03\n\x17StoredPodcastStateProto\x12&\n\"STORED_PODCAST_STATE_PROTO_UNKNOWN\x10\x00\x12$\n STORED_PODCAST_STATE_PROTO_READY\x10\x01\x12,\n(STORED_PODCAST_STATE_PROTO_USER_PROMPTED\x10\n\x12(\n$STORED_PODCAST_STATE_PROTO_SUGGESTED\x10\x14\x12/\n+STORED_PODCAST_STATE_PROTO_SUGGESTED_POINTS\x10\x15\x12*\n&STORED_PODCAST_STATE_PROTO_INPUT_READY\x10\x02\x12\x31\n-STORED_PODCAST_STATE_PROTO_GENERATION_STARTED\x10\x03\x12\x30\n,STORED_PODCAST_STATE_PROTO_GENERATION_FAILED\x10\x04*\xe3\x01\n\x1dStoredPodcastSectionTypeProto\x12-\n)STORED_PODCAST_SECTION_TYPE_PROTO_UNKNOWN\x10\x00\x12\x32\n.STORED_PODCAST_SECTION_TYPE_PROTO_INTRODUCTION\x10\x01\x12-\n)STORED_PODCAST_SECTION_TYPE_PROTO_SECTION\x10\x02\x12\x30\n,STORED_PODCAST_SECTION_TYPE_PROTO_CONCLUSION\x10\x03*\xa0\x02\n\x1cStoredPodcastImageStyleProto\x12.\n*STORED_PODCAST_IMAGE_STYLE_PROTO_UNDEFINED\x10\x00\x12.\n*STORED_PODCAST_IMAGE_STYLE_PROTO_STORYBOOK\x10\x01\x12\x34\n0STORED_PODCAST_IMAGE_STYLE_PROTO_DIGITAL_ARTWORK\x10\x02\x12\x31\n-STORED_PODCAST_IMAGE_STYLE_PROTO_OIL_PAINTING\x10\x03\x12\x37\n3STORED_PODCAST_IMAGE_STYLE_PROTO_JAPANESE_ANIMATION\x10\x04*\xf6\x01\n\"StoredPodcastSuggestionsStateProto\x12\x34\n0STORED_PODCAST_SUGGESTIONS_STATE_PROTO_UNDEFINED\x10\x00\x12\x35\n1STORED_PODCAST_SUGGESTIONS_STATE_PROTO_GENERATING\x10\x01\x12\x30\n,STORED_PODCAST_SUGGESTIONS_STATE_PROTO_READY\x10\x02\x12\x31\n-STORED_PODCAST_SUGGESTIONS_STATE_PROTO_FAILED\x10\x03*\x8a\x02\n\x1cStoredPodcastStoryStateProto\x12.\n*STORED_PODCAST_STORY_STATE_PROTO_UNDEFINED\x10\x00\x12\x30\n,STORED_PODCAST_STORY_STATE_PROTO_INPUT_READY\x10\x01\x12/\n+STORED_PODCAST_STORY_STATE_PROTO_GENERATING\x10\x02\x12*\n&STORED_PODCAST_STORY_STATE_PROTO_READY\x10\x03\x12+\n\'STORED_PODCAST_STORY_STATE_PROTO_FAILED\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'StoredPodcastProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STOREDPODCASTSTATEPROTO._serialized_start=5061
  _STOREDPODCASTSTATEPROTO._serialized_end=5446
  _STOREDPODCASTSECTIONTYPEPROTO._serialized_start=5449
  _STOREDPODCASTSECTIONTYPEPROTO._serialized_end=5676
  _STOREDPODCASTIMAGESTYLEPROTO._serialized_start=5679
  _STOREDPODCASTIMAGESTYLEPROTO._serialized_end=5967
  _STOREDPODCASTSUGGESTIONSSTATEPROTO._serialized_start=5970
  _STOREDPODCASTSUGGESTIONSSTATEPROTO._serialized_end=6216
  _STOREDPODCASTSTORYSTATEPROTO._serialized_start=6219
  _STOREDPODCASTSTORYSTATEPROTO._serialized_end=6485
  _STOREDPODCASTPROTO._serialized_start=130
  _STOREDPODCASTPROTO._serialized_end=878
  _STOREDPODCASTUSERINPUTPROTO._serialized_start=880
  _STOREDPODCASTUSERINPUTPROTO._serialized_end=944
  _STOREDPODCASTSUGGESTIONINPUTPROTO._serialized_start=947
  _STOREDPODCASTSUGGESTIONINPUTPROTO._serialized_end=1254
  _STOREDPODCASTSUGGESTIONUSERINPUTPROTO._serialized_start=1256
  _STOREDPODCASTSUGGESTIONUSERINPUTPROTO._serialized_end=1314
  _STOREDPODCASTPOINTSPROTO._serialized_start=1316
  _STOREDPODCASTPOINTSPROTO._serialized_end=1384
  _STOREDPODCASTPOINTPROTO._serialized_start=1386
  _STOREDPODCASTPOINTPROTO._serialized_end=1501
  _STOREDPODCASTPLANPROTO._serialized_start=1503
  _STOREDPODCASTPLANPROTO._serialized_end=1556
  _STOREDPODCASTTRANSCRIPTPROTO._serialized_start=1558
  _STOREDPODCASTTRANSCRIPTPROTO._serialized_end=1644
  _STOREDPODCASTSECTIONTRANSCRIPTPROTO._serialized_start=1647
  _STOREDPODCASTSECTIONTRANSCRIPTPROTO._serialized_end=1791
  _STOREDPODCASTTRANSCRIPTENTRYPROTO._serialized_start=1793
  _STOREDPODCASTTRANSCRIPTENTRYPROTO._serialized_end=1917
  _STOREDPODCASTSTYLEPROTO._serialized_start=1919
  _STOREDPODCASTSTYLEPROTO._serialized_end=1996
  _STOREDPODCASTVISUALSPROTO._serialized_start=1999
  _STOREDPODCASTVISUALSPROTO._serialized_end=2166
  _STOREDPODCASTVISUALPROTO._serialized_start=2169
  _STOREDPODCASTVISUALPROTO._serialized_end=2313
  _STOREDPODCASTAUDIOPROTO._serialized_start=2316
  _STOREDPODCASTAUDIOPROTO._serialized_end=2445
  _STOREDPODCASTKEYPOINTSPROTO._serialized_start=2447
  _STOREDPODCASTKEYPOINTSPROTO._serialized_end=2540
  _STOREDPODCASTFOLLOWUPSPROTO._serialized_start=2542
  _STOREDPODCASTFOLLOWUPSPROTO._serialized_end=2634
  _STOREDPODCASTFOLLOWUPPROTO._serialized_start=2636
  _STOREDPODCASTFOLLOWUPPROTO._serialized_end=2736
  _STOREDPODCASTKEYPOINTPROTO._serialized_start=2738
  _STOREDPODCASTKEYPOINTPROTO._serialized_end=2841
  _STOREDPODCASTSUGGESTIONSPROTO._serialized_start=2844
  _STOREDPODCASTSUGGESTIONSPROTO._serialized_end=3170
  _STOREDPODCASTSUGGESTIONSSECTIONPROTO._serialized_start=3173
  _STOREDPODCASTSUGGESTIONSSECTIONPROTO._serialized_end=3532
  _STOREDPODCASTSUGGESTIONPROTO._serialized_start=3535
  _STOREDPODCASTSUGGESTIONPROTO._serialized_end=3674
  _STOREDPODCASTSTORYSUGGESTIONPROTO._serialized_start=3676
  _STOREDPODCASTSTORYSUGGESTIONPROTO._serialized_end=3803
  _STOREDPODCASTSTORYPROTO._serialized_start=3806
  _STOREDPODCASTSTORYPROTO._serialized_end=4174
  _STOREDPODCASTSTORYINPUTPROTO._serialized_start=4176
  _STOREDPODCASTSTORYINPUTPROTO._serialized_end=4277
  _STOREDPODCASTSTORYSUGGESTIONINPUTPROTO._serialized_start=4280
  _STOREDPODCASTSTORYSUGGESTIONINPUTPROTO._serialized_end=4544
  _STOREDPODCASTSTORYSLIDESPROTO._serialized_start=4547
  _STOREDPODCASTSTORYSLIDESPROTO._serialized_end=4681
  _STOREDPODCASTSTORYSLIDEPROTO._serialized_start=4683
  _STOREDPODCASTSTORYSLIDEPROTO._serialized_end=4799
  _STOREDPODCASTQUERYCOMPLETIONSPROTO._serialized_start=4801
  _STOREDPODCASTQUERYCOMPLETIONSPROTO._serialized_end=4898
  _STOREDPODCASTQUERYCOMPLETIONSSECTIONPROTO._serialized_start=4900
  _STOREDPODCASTQUERYCOMPLETIONSSECTIONPROTO._serialized_end=5006
  _STOREDPODCASTQUERYCOMPLETIONPROTO._serialized_start=5008
  _STOREDPODCASTQUERYCOMPLETIONPROTO._serialized_end=5058
# @@protoc_insertion_point(module_scope)
