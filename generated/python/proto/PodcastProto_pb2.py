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


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PodcastProto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"5\n\x15PodcastEpisodeSegment\x12\x0e\n\x06\x64rafts\x18\x01 \x03(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"\xb1\x01\n\x13PodcastEpisodeProto\x12\x12\n\nepisode_id\x18\x01 \x01(\t\x12#\n\x05state\x18\x02 \x01(\x0e\x32\x14.PodcastEpisodeState\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x0c\n\x04refs\x18\x05 \x03(\t\x12\x0c\n\x04plan\x18\x06 \x01(\t\x12(\n\x08segments\x18\x07 \x03(\x0b\x32\x16.PodcastEpisodeSegment\"\xf8\x01\n\x0cPodcastProto\x12\x12\n\npodcast_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x05state\x18\n \x01(\x0e\x32\r.PodcastState\x12\r\n\x05title\x18\x04 \x01(\t\x12\x10\n\x08subtitle\x18\x05 \x01(\t\x12\r\n\x05\x61\x62out\x18\x06 \x01(\t\x12&\n\x08\x65pisodes\x18\x07 \x03(\x0b\x32\x14.PodcastEpisodeProto*\x85\x02\n\x13PodcastEpisodeState\x12!\n\x1dPODCAST_EPISODE_STATE_UNKNOWN\x10\x00\x12)\n%PODCAST_EPISODE_STATE_REFS_INCOMPLETE\x10\x01\x12#\n\x1fPODCAST_EPISODE_STATE_REFS_DONE\x10\x02\x12#\n\x1fPODCAST_EPISODE_STATE_PLAN_DONE\x10\x03\x12-\n)PODCAST_EPISODE_STATE_SEGMENTS_INCOMPLETE\x10\x04\x12\'\n#PODCAST_EPISODE_STATE_SEGMENTS_DONE\x10\x05*B\n\x0cPodcastState\x12\x19\n\x15PODCAST_STATE_UNKNOWN\x10\x00\x12\x17\n\x13PODCAST_STATE_DRAFT\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PodcastProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PODCASTEPISODESTATE._serialized_start=542
  _PODCASTEPISODESTATE._serialized_end=803
  _PODCASTSTATE._serialized_start=805
  _PODCASTSTATE._serialized_end=871
  _PODCASTEPISODESEGMENT._serialized_start=55
  _PODCASTEPISODESEGMENT._serialized_end=108
  _PODCASTEPISODEPROTO._serialized_start=111
  _PODCASTEPISODEPROTO._serialized_end=288
  _PODCASTPROTO._serialized_start=291
  _PODCASTPROTO._serialized_end=539
# @@protoc_insertion_point(module_scope)
