# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RecsProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fRecsProto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8c\x01\n\nEmbedProto\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12#\n\nembed_type\x18\x02 \x01(\x0e\x32\x0f.EmbedTypeProto\x12\x12\n\ninput_hash\x18\x03 \x01(\x0c\x12\x15\n\tembedding\x18\x04 \x03(\x02\x42\x02\x10\x01\"@\n\x0fRecsScoredTopic\x12\x1e\n\x05topic\x18\x01 \x01(\x0e\x32\x0f.RecsTopicProto\x12\r\n\x05score\x18\x02 \x01(\x02\"\xc0\x01\n\x0eStoryRecsProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12\x1a\n\x05\x65mbed\x18\x02 \x01(\x0b\x32\x0b.EmbedProto\x12 \n\x06impact\x18\x03 \x01(\x0e\x32\x10.RecsImpactProto\x12 \n\x06topics\x18\x04 \x03(\x0b\x32\x10.RecsScoredTopic\x12+\n\x0c\x63ontent_type\x18\x05 \x01(\x0e\x32\x15.RecsContentTypeProto\x12\x0f\n\x07quality\x18\x06 \x01(\x02\"f\n\x15StoriesRecsCacheProto\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1d\n\x04recs\x18\x02 \x03(\x0b\x32\x0f.StoryRecsProto*@\n\x0e\x45mbedTypeProto\x12\x16\n\x12\x45MBED_TYPE_UNKNOWN\x10\x00\x12\x16\n\x12\x45MBED_TYPE_ADA_002\x10\x01*\xa9\x03\n\x0eRecsTopicProto\x12\x18\n\x14RECS_TOPIC_UNDEFINED\x10\x00\x12\x13\n\x0fRECS_TOPIC_ARTS\x10\x01\x12\x17\n\x13RECS_TOPIC_BUSINESS\x10\x02\x12\x16\n\x12RECS_TOPIC_CULTURE\x10\x03\x12\x18\n\x14RECS_TOPIC_EDUCATION\x10\x04\x12\x15\n\x11RECS_TOPIC_HEALTH\x10\x05\x12\x16\n\x12RECS_TOPIC_HISTORY\x10\x06\x12\x16\n\x12RECS_TOPIC_HOBBIES\x10\x07\x12\x19\n\x15RECS_TOPIC_HUMANITIES\x10\x08\x12\x1a\n\x16RECS_TOPIC_MATHEMATICS\x10\t\x12\x17\n\x13RECS_TOPIC_LANGUAGE\x10\n\x12\x19\n\x15RECS_TOPIC_PSYCHOLOGY\x10\x0b\x12\x19\n\x15RECS_TOPIC_RECREATION\x10\x0c\x12\x16\n\x12RECS_TOPIC_SCIENCE\x10\r\x12\x1d\n\x19RECS_TOPIC_SOCIAL_STUDIES\x10\x0e\x12\x19\n\x15RECS_TOPIC_TECHNOLOGY\x10\x0f*j\n\x0fRecsImpactProto\x12\x17\n\x13RECS_IMPACT_UNKNOWN\x10\x00\x12\x13\n\x0fRECS_IMPACT_LOW\x10\x01\x12\x13\n\x0fRECS_IMPACT_MED\x10\x02\x12\x14\n\x10RECS_IMPACT_HIGH\x10\x03*\xcd\x01\n\x14RecsContentTypeProto\x12\x1d\n\x19RECS_CONTENT_TYPE_UNKNOWN\x10\x00\x12\x1a\n\x16RECS_CONTENT_TYPE_INFO\x10\x01\x12\x19\n\x15RECS_CONTENT_TYPE_ABC\x10\x02\x12 \n\x1cRECS_CONTENT_TYPE_TRUE_FALSE\x10\x03\x12\x1c\n\x18RECS_CONTENT_TYPE_VOTING\x10\x04\x12\x1f\n\x1bRECS_CONTENT_TYPE_CHALLENGE\x10\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RecsProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMBEDPROTO.fields_by_name['embedding']._options = None
  _EMBEDPROTO.fields_by_name['embedding']._serialized_options = b'\020\001'
  _EMBEDTYPEPROTO._serialized_start=560
  _EMBEDTYPEPROTO._serialized_end=624
  _RECSTOPICPROTO._serialized_start=627
  _RECSTOPICPROTO._serialized_end=1052
  _RECSIMPACTPROTO._serialized_start=1054
  _RECSIMPACTPROTO._serialized_end=1160
  _RECSCONTENTTYPEPROTO._serialized_start=1163
  _RECSCONTENTTYPEPROTO._serialized_end=1368
  _EMBEDPROTO._serialized_start=53
  _EMBEDPROTO._serialized_end=193
  _RECSSCOREDTOPIC._serialized_start=195
  _RECSSCOREDTOPIC._serialized_end=259
  _STORYRECSPROTO._serialized_start=262
  _STORYRECSPROTO._serialized_end=454
  _STORIESRECSCACHEPROTO._serialized_start=456
  _STORIESRECSCACHEPROTO._serialized_end=558
# @@protoc_insertion_point(module_scope)
