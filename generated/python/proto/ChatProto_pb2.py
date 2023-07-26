# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ChatProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x43hatProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd7\x01\n\x13\x43hatApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12\x31\n\rget_chat_bots\x18\x02 \x01(\x0b\x32\x18.GetChatBotsRequestProtoH\x00\x12,\n\nlist_chats\x18\x03 \x01(\x0b\x32\x16.ListChatsRequestProtoH\x00\x12\x39\n\x11get_chat_messages\x18\x04 \x01(\x0b\x32\x1c.GetChatMessagesRequestProtoH\x00\x42\t\n\x07request\"\xec\x02\n\x14\x43hatApiResponseProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12\x32\n\rget_chat_bots\x18\x02 \x01(\x0b\x32\x19.GetChatBotsResponseProtoH\x00\x12-\n\nlist_chats\x18\x03 \x01(\x0b\x32\x17.ListChatsResponseProtoH\x00\x12:\n\x11get_chat_messages\x18\x04 \x01(\x0b\x32\x1d.GetChatMessagesResponseProtoH\x00\x12\x37\n\tlatencies\x18\x64 \x03(\x0b\x32$.ChatApiResponseProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\n\n\x08response\"\xa8\x01\n\x19\x43hatStreamApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12\x39\n\x11post_chat_message\x18\x02 \x01(\x0b\x32\x1c.PostChatMessageRequestProtoH\x00\x12*\n\topen_chat\x18\x03 \x01(\x0b\x32\x15.OpenChatRequestProtoH\x00\x42\t\n\x07request\"\xe8\x02\n ChatStreamApiResponseHeaderProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12G\n\x18post_chat_message_header\x18\x02 \x01(\x0b\x32#.PostChatMessageResponseHeaderProtoH\x00\x12\x38\n\x10open_chat_header\x18\x03 \x01(\x0b\x32\x1c.OpenChatResponseHeaderProtoH\x00\x12\x43\n\tlatencies\x18\x64 \x03(\x0b\x32\x30.ChatStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\n\n\x08response\";\n\x17GetChatBotsRequestProto\x12 \n\x04type\x18\x01 \x01(\x0e\x32\x12.ChatBotProto.Type\"7\n\x18GetChatBotsResponseProto\x12\x1b\n\x04\x62ots\x18\x01 \x03(\x0b\x32\r.ChatBotProto\"\x17\n\x15ListChatsRequestProto\"1\n\x10\x43hatSnippetProto\x12\x0f\n\x07\x63hat_id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"=\n\x16ListChatsResponseProto\x12#\n\x08snippets\x18\x01 \x03(\x0b\x32\x11.ChatSnippetProto\".\n\x1bGetChatMessagesRequestProto\x12\x0f\n\x07\x63hat_id\x18\x01 \x01(\t\"C\n\x1cGetChatMessagesResponseProto\x12#\n\x08messages\x18\x01 \x03(\x0b\x32\x11.ChatMessageProto\".\n\x1bPostChatMessageRequestProto\x12\x0f\n\x07\x63hat_id\x18\x01 \x01(\t\"$\n\"PostChatMessageResponseHeaderProto\"7\n\x14OpenChatRequestProto\x12\x0e\n\x06\x62ot_id\x18\x01 \x01(\t\x12\x0f\n\x07restart\x18\x02 \x01(\x08\"]\n\x1bOpenChatResponseHeaderProto\x12#\n\x08messages\x18\x01 \x03(\x0b\x32\x11.ChatMessageProto\x12\x19\n\x11response_streamed\x18\x02 \x01(\x08\"[\n#ChatAssistantMessageBlockDeltaProto\x12\x14\n\ntext_delta\x18\x01 \x01(\tH\x00\x12\x15\n\x0b\x61\x63tivity_id\x18\x02 \x01(\tH\x00\x42\x07\n\x05\x64\x65lta\"\xb8\x02\n\x0c\x43hatBotProto\x12\x0e\n\x06\x62ot_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10last_modified_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12 \n\x04type\x18\x07 \x01(\x0e\x32\x12.ChatBotProto.Type\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x65scription_prompt\x18\x03 \x01(\t\x12(\n\nactivities\x18\x04 \x01(\x0b\x32\x14.ChatActivitiesProto\"4\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\r\n\tSTORY_BOT\x10\x01\x12\x0e\n\nGLOBAL_BOT\x10\x02\"Y\n\x13\x43hatActivitiesProto\x12\x1a\n\x12\x64\x65scription_prompt\x18\x01 \x01(\t\x12&\n\nactivities\x18\x02 \x03(\x0b\x32\x12.ChatActivityProto\"q\n\x11\x43hatActivityProto\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x65scription_prompt\x18\x03 \x01(\t\x12\x15\n\raction_prompt\x18\x04 \x01(\t\"D\n\x1e\x43hatAssistantMessageBlockProto\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63tivity_ids\x18\x03 \x03(\t\"L\n\x19\x43hatAssistantMessageProto\x12/\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x1f.ChatAssistantMessageBlockProto\"9\n\x14\x43hatUserMessageProto\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63tivity_id\x18\x02 \x01(\t\"\xb6\x01\n\x10\x43hatMessageProto\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\tassistant\x18\x03 \x01(\x0b\x32\x1a.ChatAssistantMessageProtoH\x00\x12%\n\x04user\x18\x04 \x01(\x0b\x32\x15.ChatUserMessageProtoH\x00\x42\x06\n\x04type\"\xde\x01\n\x10\x43hatSessionProto\x12\x17\n\x0f\x63hat_session_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10last_modified_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08story_id\x18\x04 \x01(\t\x12\x0e\n\x06\x62ot_id\x18\x05 \x01(\t\x12#\n\x08messages\x18\x07 \x03(\x0b\x32\x11.ChatMessageProtoJ\x04\x08\x06\x10\x07\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ChatProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHATAPIRESPONSEPROTO_LATENCIESENTRY._options = None
  _CHATAPIRESPONSEPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._options = None
  _CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _CHATAPIREQUESTPROTO._serialized_start=85
  _CHATAPIREQUESTPROTO._serialized_end=300
  _CHATAPIRESPONSEPROTO._serialized_start=303
  _CHATAPIRESPONSEPROTO._serialized_end=667
  _CHATAPIRESPONSEPROTO_LATENCIESENTRY._serialized_start=580
  _CHATAPIRESPONSEPROTO_LATENCIESENTRY._serialized_end=655
  _CHATSTREAMAPIREQUESTPROTO._serialized_start=670
  _CHATSTREAMAPIREQUESTPROTO._serialized_end=838
  _CHATSTREAMAPIRESPONSEHEADERPROTO._serialized_start=841
  _CHATSTREAMAPIRESPONSEHEADERPROTO._serialized_end=1201
  _CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_start=580
  _CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_end=655
  _GETCHATBOTSREQUESTPROTO._serialized_start=1203
  _GETCHATBOTSREQUESTPROTO._serialized_end=1262
  _GETCHATBOTSRESPONSEPROTO._serialized_start=1264
  _GETCHATBOTSRESPONSEPROTO._serialized_end=1319
  _LISTCHATSREQUESTPROTO._serialized_start=1321
  _LISTCHATSREQUESTPROTO._serialized_end=1344
  _CHATSNIPPETPROTO._serialized_start=1346
  _CHATSNIPPETPROTO._serialized_end=1395
  _LISTCHATSRESPONSEPROTO._serialized_start=1397
  _LISTCHATSRESPONSEPROTO._serialized_end=1458
  _GETCHATMESSAGESREQUESTPROTO._serialized_start=1460
  _GETCHATMESSAGESREQUESTPROTO._serialized_end=1506
  _GETCHATMESSAGESRESPONSEPROTO._serialized_start=1508
  _GETCHATMESSAGESRESPONSEPROTO._serialized_end=1575
  _POSTCHATMESSAGEREQUESTPROTO._serialized_start=1577
  _POSTCHATMESSAGEREQUESTPROTO._serialized_end=1623
  _POSTCHATMESSAGERESPONSEHEADERPROTO._serialized_start=1625
  _POSTCHATMESSAGERESPONSEHEADERPROTO._serialized_end=1661
  _OPENCHATREQUESTPROTO._serialized_start=1663
  _OPENCHATREQUESTPROTO._serialized_end=1718
  _OPENCHATRESPONSEHEADERPROTO._serialized_start=1720
  _OPENCHATRESPONSEHEADERPROTO._serialized_end=1813
  _CHATASSISTANTMESSAGEBLOCKDELTAPROTO._serialized_start=1815
  _CHATASSISTANTMESSAGEBLOCKDELTAPROTO._serialized_end=1906
  _CHATBOTPROTO._serialized_start=1909
  _CHATBOTPROTO._serialized_end=2221
  _CHATBOTPROTO_TYPE._serialized_start=2169
  _CHATBOTPROTO_TYPE._serialized_end=2221
  _CHATACTIVITIESPROTO._serialized_start=2223
  _CHATACTIVITIESPROTO._serialized_end=2312
  _CHATACTIVITYPROTO._serialized_start=2314
  _CHATACTIVITYPROTO._serialized_end=2427
  _CHATASSISTANTMESSAGEBLOCKPROTO._serialized_start=2429
  _CHATASSISTANTMESSAGEBLOCKPROTO._serialized_end=2497
  _CHATASSISTANTMESSAGEPROTO._serialized_start=2499
  _CHATASSISTANTMESSAGEPROTO._serialized_end=2575
  _CHATUSERMESSAGEPROTO._serialized_start=2577
  _CHATUSERMESSAGEPROTO._serialized_end=2634
  _CHATMESSAGEPROTO._serialized_start=2637
  _CHATMESSAGEPROTO._serialized_end=2819
  _CHATSESSIONPROTO._serialized_start=2822
  _CHATSESSIONPROTO._serialized_end=3044
# @@protoc_insertion_point(module_scope)
