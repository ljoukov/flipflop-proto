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
import LatencyProto_pb2 as LatencyProto__pb2
import LogProto_pb2 as LogProto__pb2
import PodcastProto_pb2 as PodcastProto__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18StoredPodcastProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x12LatencyProto.proto\x1a\x0eLogProto.proto\x1a\x12PodcastProto.proto\"\xd9\x04\n\x12StoredPodcastProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0buser_prompt\x18\x05 \x01(\t\x12\'\n\x05state\x18\x06 \x01(\x0e\x32\x18.StoredPodcastStateProto\x12)\n\x06\x61nswer\x18\x07 \x01(\x0b\x32\x19.PodcastPromptAnswerProto\x12(\n\x06points\x18\x08 \x03(\x0b\x32\x18.StoredPodcastPointProto\x12\x0c\n\x04plan\x18\t \x01(\t\x12\x31\n\ntranscript\x18\n \x01(\x0b\x32\x1d.StoredPodcastTranscriptProto\x12\'\n\x05\x61udio\x18\x0b \x01(\x0b\x32\x18.StoredPodcastAudioProto\x12+\n\x07visuals\x18\x0c \x01(\x0b\x32\x1a.StoredPodcastVisualsProto\x12\x32\n\x0b\x63\x61rds_state\x18\r \x01(\x0e\x32\x1d.StoredPodcastCardsStateProto\x12!\n\x05\x63\x61rds\x18\x0e \x01(\x0b\x32\x12.PodcastCardsProto\x12\"\n\tlatencies\x18\x64 \x01(\x0b\x32\x0f.LatenciesProto\x12\x16\n\x03log\x18\x65 \x01(\x0b\x32\t.LogProto\"\x89\x01\n\x17StoredPodcastPointProto\x12\x10\n\x08point_id\x18\x01 \x01(\t\x12\x10\n\x08selected\x18\x02 \x01(\x08\x12\x11\n\treasoning\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x13\n\x0btitle_emoji\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\"V\n\x1cStoredPodcastTranscriptProto\x12\x36\n\x08sections\x18\x01 \x03(\x0b\x32$.StoredPodcastSectionTranscriptProto\"\x90\x01\n#StoredPodcastSectionTranscriptProto\x12\x34\n\x0csection_type\x18\x01 \x01(\x0e\x32\x1e.StoredPodcastSectionTypeProto\x12\x33\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\".StoredPodcastTranscriptEntryProto\"|\n!StoredPodcastTranscriptEntryProto\x12\x1f\n\x04host\x18\x01 \x01(\x0e\x32\x11.PodcastHostProto\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x14\n\x0cstart_millis\x18\x03 \x01(\x05\x12\x12\n\nend_millis\x18\x04 \x01(\x05\"\x8e\x01\n\x19StoredPodcastVisualsProto\x12\x14\n\x0cstyle_prompt\x18\x01 \x01(\t\x12\x18\n\x10thumbnail_prompt\x18\x02 \x01(\t\x12\x15\n\rthumbnail_key\x18\x03 \x01(\t\x12*\n\x07visuals\x18\x04 \x03(\x0b\x32\x19.StoredPodcastVisualProto\"\x90\x01\n\x18StoredPodcastVisualProto\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x05\x12\x14\n\x0cimage_prompt\x18\x02 \x01(\t\x12\x11\n\timage_key\x18\x03 \x01(\t\x12\x31\n\ntransition\x18\x04 \x01(\x0e\x32\x1d.PodcastVisualTransitionProto\"\x81\x01\n\x17StoredPodcastAudioProto\x12\x11\n\taudio_key\x18\x01 \x01(\t\x12\x31\n\x0e\x61udio_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12 \n\x05words\x18\x03 \x03(\x0b\x32\x11.PodcastWordProto*\xaf\x06\n\x17StoredPodcastStateProto\x12&\n\"STORED_PODCAST_STATE_PROTO_UNKNOWN\x10\x00\x12$\n STORED_PODCAST_STATE_PROTO_READY\x10\x01\x12%\n!STORED_PODCAST_STATE_PROTO_FAILED\x10\x02\x12\x30\n,STORED_PODCAST_STATE_PROTO_GENERATING_ANSWER\x10\n\x12+\n\'STORED_PODCAST_STATE_PROTO_ANSWER_READY\x10\x0b\x12+\n\'STORED_PODCAST_STATE_PROTO_POINTS_READY\x10\x0c\x12.\n*STORED_PODCAST_STATE_PROTO_POINTS_SELECTED\x10\r\x12\x33\n/STORED_PODCAST_STATE_PROTO_GENERATING_THUMBNAIL\x10\x0e\x12.\n*STORED_PODCAST_STATE_PROTO_THUMBNAIL_READY\x10\x0f\x12.\n*STORED_PODCAST_STATE_PROTO_GENERATING_PLAN\x10\x10\x12)\n%STORED_PODCAST_STATE_PROTO_PLAN_READY\x10\x11\x12\x34\n0STORED_PODCAST_STATE_PROTO_GENERATING_TRANSCRIPT\x10\x12\x12/\n+STORED_PODCAST_STATE_PROTO_TRANSCRIPT_READY\x10\x13\x12/\n+STORED_PODCAST_STATE_PROTO_GENERATING_AUDIO\x10\x14\x12*\n&STORED_PODCAST_STATE_PROTO_AUDIO_READY\x10\x15\x12\x31\n-STORED_PODCAST_STATE_PROTO_GENERATING_VISUALS\x10\x16\x12,\n(STORED_PODCAST_STATE_PROTO_VISUALS_READY\x10\x17*\xda\x01\n\x1cStoredPodcastCardsStateProto\x12\x30\n,STORED_PODCAST_CARDS_STATE_PROTO_NOT_STARTED\x10\x00\x12/\n+STORED_PODCAST_CARDS_STATE_PROTO_GENERATING\x10\x01\x12*\n&STORED_PODCAST_CARDS_STATE_PROTO_READY\x10\x02\x12+\n\'STORED_PODCAST_CARDS_STATE_PROTO_FAILED\x10\x03*\xe3\x01\n\x1dStoredPodcastSectionTypeProto\x12-\n)STORED_PODCAST_SECTION_TYPE_PROTO_UNKNOWN\x10\x00\x12\x32\n.STORED_PODCAST_SECTION_TYPE_PROTO_INTRODUCTION\x10\x01\x12-\n)STORED_PODCAST_SECTION_TYPE_PROTO_SECTION\x10\x02\x12\x30\n,STORED_PODCAST_SECTION_TYPE_PROTO_CONCLUSION\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'StoredPodcastProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STOREDPODCASTSTATEPROTO._serialized_start=1679
  _STOREDPODCASTSTATEPROTO._serialized_end=2494
  _STOREDPODCASTCARDSSTATEPROTO._serialized_start=2497
  _STOREDPODCASTCARDSSTATEPROTO._serialized_end=2715
  _STOREDPODCASTSECTIONTYPEPROTO._serialized_start=2718
  _STOREDPODCASTSECTIONTYPEPROTO._serialized_end=2945
  _STOREDPODCASTPROTO._serialized_start=150
  _STOREDPODCASTPROTO._serialized_end=751
  _STOREDPODCASTPOINTPROTO._serialized_start=754
  _STOREDPODCASTPOINTPROTO._serialized_end=891
  _STOREDPODCASTTRANSCRIPTPROTO._serialized_start=893
  _STOREDPODCASTTRANSCRIPTPROTO._serialized_end=979
  _STOREDPODCASTSECTIONTRANSCRIPTPROTO._serialized_start=982
  _STOREDPODCASTSECTIONTRANSCRIPTPROTO._serialized_end=1126
  _STOREDPODCASTTRANSCRIPTENTRYPROTO._serialized_start=1128
  _STOREDPODCASTTRANSCRIPTENTRYPROTO._serialized_end=1252
  _STOREDPODCASTVISUALSPROTO._serialized_start=1255
  _STOREDPODCASTVISUALSPROTO._serialized_end=1397
  _STOREDPODCASTVISUALPROTO._serialized_start=1400
  _STOREDPODCASTVISUALPROTO._serialized_end=1544
  _STOREDPODCASTAUDIOPROTO._serialized_start=1547
  _STOREDPODCASTAUDIOPROTO._serialized_end=1676
# @@protoc_insertion_point(module_scope)
