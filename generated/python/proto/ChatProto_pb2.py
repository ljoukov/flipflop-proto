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
import LLMProto_pb2 as LLMProto__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x43hatProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0eLLMProto.proto\"\x9c\x01\n\x13\x43hatApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12\x31\n\rget_chat_bots\x18\x02 \x01(\x0b\x32\x18.GetChatBotsRequestProtoH\x00\x12,\n\nlist_chats\x18\x03 \x01(\x0b\x32\x16.ListChatsRequestProtoH\x00\x42\t\n\x07request\"\xb0\x02\n\x14\x43hatApiResponseProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12\x32\n\rget_chat_bots\x18\x02 \x01(\x0b\x32\x19.GetChatBotsResponseProtoH\x00\x12-\n\nlist_chats\x18\x03 \x01(\x0b\x32\x17.ListChatsResponseProtoH\x00\x12\x37\n\tlatencies\x18\x64 \x03(\x0b\x32$.ChatApiResponseProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\n\n\x08response\"\xa8\x01\n\x19\x43hatStreamApiRequestProto\x12\x19\n\x11\x65ncoded_user_auth\x18\x01 \x01(\t\x12\x39\n\x11post_chat_message\x18\x02 \x01(\x0b\x32\x1c.PostChatMessageRequestProtoH\x00\x12*\n\topen_chat\x18\x03 \x01(\x0b\x32\x15.OpenChatRequestProtoH\x00\x42\t\n\x07request\"\xe6\x02\n ChatStreamApiResponseHeaderProto\x12#\n\x1brefreshed_encoded_user_auth\x18\x01 \x01(\t\x12G\n\x18post_chat_message_header\x18\x02 \x01(\x0b\x32#.PostChatMessageResponseHeaderProtoH\x00\x12\x38\n\x10open_chat_header\x18\x03 \x01(\x0b\x32\x1c.OpenChatResponseHeaderProtoH\x00\x12\x43\n\tlatencies\x18\x64 \x03(\x0b\x32\x30.ChatStreamApiResponseHeaderProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\x08\n\x06header\"i\n\x1f\x43hatStreamApiResponseDeltaProto\x12\x34\n\tassistant\x18\x01 \x01(\x0b\x32\x1f.ChatAssistantMessageDeltaProtoH\x00\x42\x10\n\x0eresponse_delta\";\n\x17GetChatBotsRequestProto\x12 \n\x04type\x18\x01 \x01(\x0e\x32\x12.ChatBotProto.Type\"7\n\x18GetChatBotsResponseProto\x12\x1b\n\x04\x62ots\x18\x01 \x03(\x0b\x32\r.ChatBotProto\"P\n\x15ListChatsRequestProto\x12\x37\n\x13last_modified_after\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"g\n\x10\x43hatSnippetProto\x12\x0f\n\x07\x63hat_id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x34\n\x10last_modified_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"=\n\x16ListChatsResponseProto\x12#\n\x08snippets\x18\x01 \x03(\x0b\x32\x11.ChatSnippetProto\"[\n\x1bPostChatMessageRequestProto\x12\x0f\n\x07\x63hat_id\x18\x01 \x01(\t\x12+\n\x0cuser_message\x18\x02 \x01(\x0b\x32\x15.ChatUserMessageProto\"f\n\"PostChatMessageResponseHeaderProto\x12#\n\x08messages\x18\x01 \x03(\x0b\x32\x11.ChatMessageProto\x12\x1b\n\x13streamed_message_id\x18\x02 \x01(\t\"A\n\x18\x43hatStoryActivityIdProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63tivity_id\x18\x02 \x01(\t\"K\n\x1cOpenChatWithUserMessageProto\x12\x15\n\rglobal_bot_id\x18\x01 \x01(\t\x12\x14\n\x0cuser_message\x18\x02 \x01(\t\"\xcf\x01\n\x14OpenChatRequestProto\x12\x0f\n\x07restart\x18\x01 \x01(\x08\x12\x11\n\x07\x63hat_id\x18\x02 \x01(\tH\x00\x12\x17\n\rglobal_bot_id\x18\x03 \x01(\tH\x00\x12\x36\n\x11story_activity_id\x18\x05 \x01(\x0b\x32\x19.ChatStoryActivityIdProtoH\x00\x12:\n\x11with_user_message\x18\x06 \x01(\x0b\x32\x1d.OpenChatWithUserMessageProtoH\x00\x42\x06\n\x04type\"p\n\x1bOpenChatResponseHeaderProto\x12\x0f\n\x07\x63hat_id\x18\x01 \x01(\t\x12#\n\x08messages\x18\x02 \x03(\x0b\x32\x11.ChatMessageProto\x12\x1b\n\x13streamed_message_id\x18\x03 \x01(\t\"l\n\x1e\x43hatAssistantMessageDeltaProto\x12\x14\n\ntext_delta\x18\x01 \x01(\tH\x00\x12+\n\x08\x61\x63tivity\x18\x02 \x01(\x0b\x32\x17.ChatActivityIntroProtoH\x00\x42\x07\n\x05\x64\x65lta\"\xb8\x02\n\x0c\x43hatBotProto\x12\x0e\n\x06\x62ot_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10last_modified_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12 \n\x04type\x18\x07 \x01(\x0e\x32\x12.ChatBotProto.Type\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x65scription_prompt\x18\x03 \x01(\t\x12(\n\nactivities\x18\x04 \x01(\x0b\x32\x14.ChatActivitiesProto\"4\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\r\n\tSTORY_BOT\x10\x01\x12\x0e\n\nGLOBAL_BOT\x10\x02\"Y\n\x13\x43hatActivitiesProto\x12\x1a\n\x12\x64\x65scription_prompt\x18\x01 \x01(\t\x12&\n\nactivities\x18\x02 \x03(\x0b\x32\x12.ChatActivityProto\"q\n\x11\x43hatActivityProto\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x65scription_prompt\x18\x03 \x01(\t\x12\x15\n\raction_prompt\x18\x04 \x01(\t\"C\n\x16\x43hatActivityIntroProto\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\"[\n\x1e\x43hatAssistantMessageBlockProto\x12\x0c\n\x04text\x18\x01 \x01(\t\x12+\n\nactivities\x18\x02 \x03(\x0b\x32\x17.ChatActivityIntroProto\"q\n\x19\x43hatAssistantMessageProto\x12/\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x1f.ChatAssistantMessageBlockProto\x12#\n\nllm_output\x18\x02 \x01(\x0b\x32\x0f.LLMOutputProto\"I\n\x14\x43hatUserMessageProto\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63tivity_id\x18\x02 \x01(\t\x12\x0e\n\x06\x62ot_id\x18\x03 \x01(\t\"\xb6\x01\n\x10\x43hatMessageProto\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\tassistant\x18\x03 \x01(\x0b\x32\x1a.ChatAssistantMessageProtoH\x00\x12%\n\x04user\x18\x04 \x01(\x0b\x32\x15.ChatUserMessageProtoH\x00\x42\x06\n\x04type\"\xde\x01\n\x10\x43hatSessionProto\x12\x17\n\x0f\x63hat_session_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10last_modified_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08story_id\x18\x04 \x01(\t\x12\x0e\n\x06\x62ot_id\x18\x05 \x01(\t\x12#\n\x08messages\x18\x07 \x03(\x0b\x32\x11.ChatMessageProtoJ\x04\x08\x06\x10\x07\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ChatProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHATAPIRESPONSEPROTO_LATENCIESENTRY._options = None
  _CHATAPIRESPONSEPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._options = None
  _CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _CHATAPIREQUESTPROTO._serialized_start=101
  _CHATAPIREQUESTPROTO._serialized_end=257
  _CHATAPIRESPONSEPROTO._serialized_start=260
  _CHATAPIRESPONSEPROTO._serialized_end=564
  _CHATAPIRESPONSEPROTO_LATENCIESENTRY._serialized_start=477
  _CHATAPIRESPONSEPROTO_LATENCIESENTRY._serialized_end=552
  _CHATSTREAMAPIREQUESTPROTO._serialized_start=567
  _CHATSTREAMAPIREQUESTPROTO._serialized_end=735
  _CHATSTREAMAPIRESPONSEHEADERPROTO._serialized_start=738
  _CHATSTREAMAPIRESPONSEHEADERPROTO._serialized_end=1096
  _CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_start=477
  _CHATSTREAMAPIRESPONSEHEADERPROTO_LATENCIESENTRY._serialized_end=552
  _CHATSTREAMAPIRESPONSEDELTAPROTO._serialized_start=1098
  _CHATSTREAMAPIRESPONSEDELTAPROTO._serialized_end=1203
  _GETCHATBOTSREQUESTPROTO._serialized_start=1205
  _GETCHATBOTSREQUESTPROTO._serialized_end=1264
  _GETCHATBOTSRESPONSEPROTO._serialized_start=1266
  _GETCHATBOTSRESPONSEPROTO._serialized_end=1321
  _LISTCHATSREQUESTPROTO._serialized_start=1323
  _LISTCHATSREQUESTPROTO._serialized_end=1403
  _CHATSNIPPETPROTO._serialized_start=1405
  _CHATSNIPPETPROTO._serialized_end=1508
  _LISTCHATSRESPONSEPROTO._serialized_start=1510
  _LISTCHATSRESPONSEPROTO._serialized_end=1571
  _POSTCHATMESSAGEREQUESTPROTO._serialized_start=1573
  _POSTCHATMESSAGEREQUESTPROTO._serialized_end=1664
  _POSTCHATMESSAGERESPONSEHEADERPROTO._serialized_start=1666
  _POSTCHATMESSAGERESPONSEHEADERPROTO._serialized_end=1768
  _CHATSTORYACTIVITYIDPROTO._serialized_start=1770
  _CHATSTORYACTIVITYIDPROTO._serialized_end=1835
  _OPENCHATWITHUSERMESSAGEPROTO._serialized_start=1837
  _OPENCHATWITHUSERMESSAGEPROTO._serialized_end=1912
  _OPENCHATREQUESTPROTO._serialized_start=1915
  _OPENCHATREQUESTPROTO._serialized_end=2122
  _OPENCHATRESPONSEHEADERPROTO._serialized_start=2124
  _OPENCHATRESPONSEHEADERPROTO._serialized_end=2236
  _CHATASSISTANTMESSAGEDELTAPROTO._serialized_start=2238
  _CHATASSISTANTMESSAGEDELTAPROTO._serialized_end=2346
  _CHATBOTPROTO._serialized_start=2349
  _CHATBOTPROTO._serialized_end=2661
  _CHATBOTPROTO_TYPE._serialized_start=2609
  _CHATBOTPROTO_TYPE._serialized_end=2661
  _CHATACTIVITIESPROTO._serialized_start=2663
  _CHATACTIVITIESPROTO._serialized_end=2752
  _CHATACTIVITYPROTO._serialized_start=2754
  _CHATACTIVITYPROTO._serialized_end=2867
  _CHATACTIVITYINTROPROTO._serialized_start=2869
  _CHATACTIVITYINTROPROTO._serialized_end=2936
  _CHATASSISTANTMESSAGEBLOCKPROTO._serialized_start=2938
  _CHATASSISTANTMESSAGEBLOCKPROTO._serialized_end=3029
  _CHATASSISTANTMESSAGEPROTO._serialized_start=3031
  _CHATASSISTANTMESSAGEPROTO._serialized_end=3144
  _CHATUSERMESSAGEPROTO._serialized_start=3146
  _CHATUSERMESSAGEPROTO._serialized_end=3219
  _CHATMESSAGEPROTO._serialized_start=3222
  _CHATMESSAGEPROTO._serialized_end=3404
  _CHATSESSIONPROTO._serialized_start=3407
  _CHATSESSIONPROTO._serialized_end=3629
# @@protoc_insertion_point(module_scope)
