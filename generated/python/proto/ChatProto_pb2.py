# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ChatProto.proto
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
    'ChatProto.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x43hatProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x93\x01\n\x13\x43hatApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12,\n\nlist_chats\x18\x02 \x01(\x0b\x32\x16.ListChatsRequestProtoH\x00\x12(\n\x08get_chat\x18\x03 \x01(\x0b\x32\x14.GetChatRequestProtoH\x00\x42\t\n\x07request\"\xa7\x02\n\x14\x43hatApiResponseProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12-\n\nlist_chats\x18\x02 \x01(\x0b\x32\x17.ListChatsResponseProtoH\x00\x12)\n\x08get_chat\x18\x03 \x01(\x0b\x32\x15.GetChatResponseProtoH\x00\x12\x37\n\tlatencies\x18\x64 \x03(\x0b\x32$.ChatApiResponseProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\n\n\x08response\"m\n\x19\x43hatStreamApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12*\n\topen_chat\x18\x02 \x01(\x0b\x32\x15.OpenChatRequestProtoH\x00\x42\t\n\x07request\"\x9d\x02\n ChatStreamApiResponseHeaderProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12\x38\n\x10open_chat_header\x18\x02 \x01(\x0b\x32\x1c.OpenChatResponseHeaderProtoH\x00\x12\x43\n\tlatencies\x18\x64 \x03(\x0b\x32\x30.ChatStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\x08\n\x06header\"i\n\x1f\x43hatStreamApiResponseDeltaProto\x12\x34\n\tassistant\x18\x01 \x01(\x0b\x32\x1f.ChatAssistantMessageDeltaProtoH\x00\x42\x10\n\x0eresponse_delta\"P\n\x15ListChatsRequestProto\x12\x37\n\x13last_modified_after\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"=\n\x16ListChatsResponseProto\x12#\n\x08snippets\x18\x01 \x03(\x0b\x32\x11.ChatSnippetProto\"o\n\x10\x43hatSnippetProto\x12\x17\n\x0flast_message_id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x34\n\x10last_modified_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\".\n\x13GetChatRequestProto\x12\x17\n\x0flast_message_id\x18\x01 \x01(\t\";\n\x14GetChatResponseProto\x12#\n\x08messages\x18\x01 \x03(\x0b\x32\x11.ChatMessageProto\"\x8a\x01\n\x14OpenChatRequestProto\x12.\n\rwith_solo_bot\x18\x01 \x01(\x0e\x32\x15.ChatSoloBotTypeProtoH\x00\x12:\n\x11with_user_message\x18\x02 \x01(\x0b\x32\x1d.OpenChatWithUserMessageProtoH\x00\x42\x06\n\x04type\"\xcc\x01\n\x1bOpenChatResponseHeaderProto\x12#\n\x08messages\x18\x01 \x03(\x0b\x32\x11.ChatMessageProto\x12\x1b\n\x13streamed_message_id\x18\x02 \x01(\t\x12*\n\"streamed_message_parent_message_id\x18\x03 \x01(\t\x12?\n\x1bstreamed_message_created_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"f\n\x1cOpenChatWithUserMessageProto\x12\x19\n\x11parent_message_id\x18\x01 \x01(\t\x12+\n\x0cuser_message\x18\x02 \x01(\x0b\x32\x15.ChatUserMessageProto\"\xd1\x01\n\x10\x43hatMessageProto\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x19\n\x11parent_message_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\tassistant\x18\x04 \x01(\x0b\x32\x1a.ChatAssistantMessageProtoH\x00\x12%\n\x04user\x18\x05 \x01(\x0b\x32\x15.ChatUserMessageProtoH\x00\x42\x06\n\x04type\"l\n\x1e\x43hatAssistantMessageDeltaProto\x12\x14\n\ntext_delta\x18\x01 \x01(\tH\x00\x12+\n\x08\x61\x63tivity\x18\x02 \x01(\x0b\x32\x17.ChatActivityIntroProtoH\x00\x42\x07\n\x05\x64\x65lta\"L\n\x19\x43hatAssistantMessageProto\x12/\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x1f.ChatAssistantMessageBlockProto\"[\n\x1e\x43hatAssistantMessageBlockProto\x12\x0c\n\x04text\x18\x01 \x01(\t\x12+\n\nactivities\x18\x02 \x03(\x0b\x32\x17.ChatActivityIntroProto\"C\n\x16\x43hatActivityIntroProto\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\"\x85\x01\n\x14\x43hatUserMessageProto\x12-\n\ntext_input\x18\x01 \x01(\x0b\x32\x17.ChatUserTextInputProtoH\x00\x12\x35\n\x0e\x61\x63tivity_input\x18\x02 \x01(\x0b\x32\x1b.ChatUserActivityInputProtoH\x00\x42\x07\n\x05input\"U\n\x16\x43hatUserTextInputProto\x12-\n\rresponse_type\x18\x01 \x01(\x0e\x32\x16.ChatResponseTypeProto\x12\x0c\n\x04text\x18\x02 \x01(\t\"C\n\x1a\x43hatUserActivityInputProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63tivity_id\x18\x02 \x01(\t*\x8f\x01\n\x14\x43hatSoloBotTypeProto\x12&\n\"CHAT_SOLO_BOT_TYPE_PROTO_UNDEFINED\x10\x00\x12%\n!CHAT_SOLO_BOT_TYPE_PROTO_GREETING\x10\x01\x12(\n$CHAT_SOLO_BOT_TYPE_PROTO_AFFIRMATION\x10\x02*\xd8\x01\n\x15\x43hatResponseTypeProto\x12&\n\"CHAT_RESPONSE_TYPE_PROTO_UNDEFINED\x10\x00\x12\"\n\x1e\x43HAT_RESPONSE_TYPE_PROTO_SHORT\x10\x01\x12#\n\x1f\x43HAT_RESPONSE_TYPE_PROTO_REASON\x10\x02\x12%\n!CHAT_RESPONSE_TYPE_PROTO_SIMPLIFY\x10\x03\x12\'\n#CHAT_RESPONSE_TYPE_PROTO_BRAINSTORM\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ChatProto_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHATAPIRESPONSEPROTO_LATENCIESENTRY']._loaded_options = None
  _globals['_CHATAPIRESPONSEPROTO_LATENCIESENTRY']._serialized_options = b'8\001'
  _globals['_CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._loaded_options = None
  _globals['_CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._serialized_options = b'8\001'
  _globals['_CHATSOLOBOTTYPEPROTO']._serialized_start=2712
  _globals['_CHATSOLOBOTTYPEPROTO']._serialized_end=2855
  _globals['_CHATRESPONSETYPEPROTO']._serialized_start=2858
  _globals['_CHATRESPONSETYPEPROTO']._serialized_end=3074
  _globals['_CHATAPIREQUESTPROTO']._serialized_start=85
  _globals['_CHATAPIREQUESTPROTO']._serialized_end=232
  _globals['_CHATAPIRESPONSEPROTO']._serialized_start=235
  _globals['_CHATAPIRESPONSEPROTO']._serialized_end=530
  _globals['_CHATAPIRESPONSEPROTO_LATENCIESENTRY']._serialized_start=443
  _globals['_CHATAPIRESPONSEPROTO_LATENCIESENTRY']._serialized_end=518
  _globals['_CHATSTREAMAPIREQUESTPROTO']._serialized_start=532
  _globals['_CHATSTREAMAPIREQUESTPROTO']._serialized_end=641
  _globals['_CHATSTREAMAPIRESPONSEHEADERPROTO']._serialized_start=644
  _globals['_CHATSTREAMAPIRESPONSEHEADERPROTO']._serialized_end=929
  _globals['_CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._serialized_start=443
  _globals['_CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY']._serialized_end=518
  _globals['_CHATSTREAMAPIRESPONSEDELTAPROTO']._serialized_start=931
  _globals['_CHATSTREAMAPIRESPONSEDELTAPROTO']._serialized_end=1036
  _globals['_LISTCHATSREQUESTPROTO']._serialized_start=1038
  _globals['_LISTCHATSREQUESTPROTO']._serialized_end=1118
  _globals['_LISTCHATSRESPONSEPROTO']._serialized_start=1120
  _globals['_LISTCHATSRESPONSEPROTO']._serialized_end=1181
  _globals['_CHATSNIPPETPROTO']._serialized_start=1183
  _globals['_CHATSNIPPETPROTO']._serialized_end=1294
  _globals['_GETCHATREQUESTPROTO']._serialized_start=1296
  _globals['_GETCHATREQUESTPROTO']._serialized_end=1342
  _globals['_GETCHATRESPONSEPROTO']._serialized_start=1344
  _globals['_GETCHATRESPONSEPROTO']._serialized_end=1403
  _globals['_OPENCHATREQUESTPROTO']._serialized_start=1406
  _globals['_OPENCHATREQUESTPROTO']._serialized_end=1544
  _globals['_OPENCHATRESPONSEHEADERPROTO']._serialized_start=1547
  _globals['_OPENCHATRESPONSEHEADERPROTO']._serialized_end=1751
  _globals['_OPENCHATWITHUSERMESSAGEPROTO']._serialized_start=1753
  _globals['_OPENCHATWITHUSERMESSAGEPROTO']._serialized_end=1855
  _globals['_CHATMESSAGEPROTO']._serialized_start=1858
  _globals['_CHATMESSAGEPROTO']._serialized_end=2067
  _globals['_CHATASSISTANTMESSAGEDELTAPROTO']._serialized_start=2069
  _globals['_CHATASSISTANTMESSAGEDELTAPROTO']._serialized_end=2177
  _globals['_CHATASSISTANTMESSAGEPROTO']._serialized_start=2179
  _globals['_CHATASSISTANTMESSAGEPROTO']._serialized_end=2255
  _globals['_CHATASSISTANTMESSAGEBLOCKPROTO']._serialized_start=2257
  _globals['_CHATASSISTANTMESSAGEBLOCKPROTO']._serialized_end=2348
  _globals['_CHATACTIVITYINTROPROTO']._serialized_start=2350
  _globals['_CHATACTIVITYINTROPROTO']._serialized_end=2417
  _globals['_CHATUSERMESSAGEPROTO']._serialized_start=2420
  _globals['_CHATUSERMESSAGEPROTO']._serialized_end=2553
  _globals['_CHATUSERTEXTINPUTPROTO']._serialized_start=2555
  _globals['_CHATUSERTEXTINPUTPROTO']._serialized_end=2640
  _globals['_CHATUSERACTIVITYINPUTPROTO']._serialized_start=2642
  _globals['_CHATUSERACTIVITYINPUTPROTO']._serialized_end=2709
# @@protoc_insertion_point(module_scope)
