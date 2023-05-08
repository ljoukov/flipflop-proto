# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: StoryProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10StoryProto.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"Q\n\x16GetStoriesRequestProto\x12\x37\n\x13last_modified_after\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x87\x01\n\x17GetStoriesResponseProto\x12\x1c\n\x07stories\x18\x01 \x03(\x0b\x32\x0b.StoryProto\x12\x18\n\x10\x64\x65leted_story_id\x18\x02 \x03(\t\x12\x34\n\x10last_modified_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"4\n\x17\x43reateStoryRequestProto\x12\x19\n\x05\x63\x61rds\x18\x01 \x03(\x0b\x32\n.CardProto\",\n\x18\x43reateStoryResponseProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\"F\n\x17UpdateStoryRequestProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\x12\x19\n\x05\x63\x61rds\x18\x02 \x03(\x0b\x32\n.CardProto\"\x1a\n\x18UpdateStoryResponseProto\"+\n\x17\x44\x65leteStoryRequestProto\x12\x10\n\x08story_id\x18\x01 \x01(\t\"\x1a\n\x18\x44\x65leteStoryResponseProto\"\xe7\x01\n\x14StoryApiRequestProto\x12.\n\x0bget_stories\x18\x01 \x01(\x0b\x32\x17.GetStoriesRequestProtoH\x00\x12\x30\n\x0c\x63reate_story\x18\x02 \x01(\x0b\x32\x18.CreateStoryRequestProtoH\x00\x12\x30\n\x0cupdate_story\x18\x03 \x01(\x0b\x32\x18.UpdateStoryRequestProtoH\x00\x12\x30\n\x0c\x64\x65lete_story\x18\x04 \x01(\x0b\x32\x18.DeleteStoryRequestProtoH\x00\x42\t\n\x07request\"\xf4\x02\n\x15StoryApiResponseProto\x12/\n\x0bget_stories\x18\x01 \x01(\x0b\x32\x18.GetStoriesResponseProtoH\x00\x12\x31\n\x0c\x63reate_story\x18\x02 \x01(\x0b\x32\x19.CreateStoryResponseProtoH\x00\x12\x31\n\x0cupdate_story\x18\x03 \x01(\x0b\x32\x19.UpdateStoryResponseProtoH\x00\x12\x31\n\x0c\x64\x65lete_story\x18\x04 \x01(\x0b\x32\x19.DeleteStoryResponseProtoH\x00\x12\x38\n\tlatencies\x18\x05 \x03(\x0b\x32%.StoryApiResponseProto.LatenciesEntry\x1aK\n\x0eLatenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\x42\n\n\x08response\"m\n\x0eStoryDataProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tauthor_id\x18\x02 \x01(\t\x12\x18\n\x10timestamp_millis\x18\x03 \x01(\x03\x12\"\n\ncards_data\x18\x04 \x03(\x0b\x32\x0e.CardDataProto\"\xe6\x01\n\rCardDataProto\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\tcard_type\x18\x02 \x01(\x0e\x32\x0e.CardTypeProto\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0c\n\x04\x62ody\x18\x04 \x01(\t\x12\x0f\n\x07is_true\x18\x05 \x01(\x08\x12\x0f\n\x07options\x18\x06 \x03(\t\x12\x1c\n\x14\x63orrect_option_index\x18\x07 \x01(\x05\x12\x13\n\x0b\x65xplanation\x18\x08 \x01(\t\x12!\n\timage_ref\x18\t \x01(\x0b\x32\x0e.ImageRefProto\x12\x11\n\thash_tags\x18\n \x03(\t\"[\n\x0cStoriesProto\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x07stories\x18\x02 \x03(\x0b\x32\x0b.StoryProto\"\xd6\x01\n\nStoryProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10last_modified_by\x18\x04 \x01(\t\x12\x34\n\x10last_modified_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05title\x18\x06 \x01(\t\x12\x19\n\x05\x63\x61rds\x18\x07 \x03(\x0b\x32\n.CardProto\";\n\tCardProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\nfront_face\x18\x02 \x01(\x0b\x32\x0e.CardFaceProto\"C\n\rCardFaceProto\x12\x1f\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x0f.CardBlockProto\x12\x11\n\thash_tags\x18\x02 \x03(\t\"\x8b\x03\n\x0e\x43\x61rdBlockProto\x12!\n\x05space\x18\x01 \x01(\x0b\x32\x10.SpaceBlockProtoH\x00\x12!\n\x05image\x18\x02 \x01(\x0b\x32\x10.ImageBlockProtoH\x00\x12\x1f\n\x04text\x18\x03 \x01(\x0b\x32\x0f.TextBlockProtoH\x00\x12\x1f\n\x04\x66lip\x18\x04 \x01(\x0b\x32\x0f.FlipBlockProtoH\x00\x12#\n\x06\x63offee\x18\x05 \x01(\x0b\x32\x11.CoffeeBlockProtoH\x00\x12#\n\x06reveal\x18\x06 \x01(\x0b\x32\x11.RevealBlockProtoH\x00\x12#\n\x06\x63hoice\x18\x07 \x01(\x0b\x32\x11.ChoiceBlockProtoH\x00\x12\'\n\x08question\x18\x08 \x01(\x0b\x32\x13.QuestionBlockProtoH\x00\x12#\n\x06prompt\x18\t \x01(\x0b\x32\x11.PromptBlockProtoH\x00\x12,\n\x0breveal_back\x18\n \x01(\x0b\x32\x15.RevealBackBlockProtoH\x00\x42\x06\n\x04type\" \n\x0fSpaceBlockProto\x12\r\n\x05scale\x18\x01 \x01(\x02\"E\n\rImageRefProto\x12\x16\n\x0cstorage_path\x18\x01 \x01(\tH\x00\x12\x14\n\nimage_data\x18\x02 \x01(\x0cH\x00\x42\x06\n\x04type\"Z\n\x0fImageBlockProto\x12!\n\timage_ref\x18\x01 \x01(\x0b\x32\x0e.ImageRefProto\x12\r\n\x05scale\x18\x02 \x01(\x02\x12\x15\n\rborder_radius\x18\x03 \x01(\x02\"\x93\x01\n\rTextSpanProto\x12\x0c\n\x04text\x18\x01 \x01(\t\x12%\n\x0b\x66ont_weight\x18\x02 \x01(\x0e\x32\x10.FontWeightProto\x12#\n\nfont_style\x18\x03 \x01(\x0e\x32\x0f.FontStyleProto\x12(\n\ndecoration\x18\x04 \x01(\x0e\x32\x14.TextDecorationProto\"\x84\x02\n\x0fStyledTextProto\x12\x1d\n\x05spans\x18\x01 \x03(\x0b\x32\x0e.TextSpanProto\x12!\n\tfont_name\x18\x02 \x01(\x0e\x32\x0e.FontNameProto\x12\x11\n\tfont_size\x18\x03 \x01(\x02\x12\x15\n\rpadding_start\x18\x04 \x01(\x02\x12\x13\n\x0bpadding_end\x18\x05 \x01(\x02\x12\"\n\x05\x61lign\x18\x06 \x01(\x0e\x32\x13.TextAlignmentProto\x12(\n\nwhitespace\x18\x07 \x01(\x0e\x32\x14.TextWhitespaceProto\x12\"\n\x07hyphens\x18\x08 \x01(\x0e\x32\x11.TextHyphensProto\"7\n\x0eTextBlockProto\x12%\n\x0bstyled_text\x18\x01 \x01(\x0b\x32\x10.StyledTextProto\"\x1f\n\x0e\x46lipBlockProto\x12\r\n\x05label\x18\x01 \x01(\t\"Z\n\x10\x43offeeBlockProto\x12\r\n\x05label\x18\x01 \x01(\t\x12\x14\n\x0cstart_offset\x18\x02 \x01(\x02\x12!\n\timage_ref\x18\x03 \x01(\x0b\x32\x0e.ImageRefProto\"P\n\x10RevealBlockProto\x12\r\n\x05scale\x18\x01 \x01(\x02\x12\r\n\x05label\x18\x02 \x01(\t\x12\x1e\n\x04text\x18\x03 \x01(\x0b\x32\x10.StyledTextProto\"J\n\x16\x43hoiceBlockOptionProto\x12\x1e\n\x04text\x18\x01 \x01(\x0b\x32\x10.StyledTextProto\x12\x10\n\x08\x66raction\x18\x02 \x01(\x02\"\xba\x01\n\x10\x43hoiceBlockProto\x12\r\n\x05scale\x18\x01 \x01(\x02\x12(\n\x07options\x18\x02 \x03(\x0b\x32\x17.ChoiceBlockOptionProto\x12\x15\n\rcorrect_index\x18\x03 \x01(\x05\x12+\n\x13\x63orrect_answer_face\x18\x04 \x01(\x0b\x32\x0e.CardFaceProto\x12)\n\x11wrong_answer_face\x18\x05 \x01(\x0b\x32\x0e.CardFaceProto\";\n\x18QuestionBlockOptionProto\x12\r\n\x05label\x18\x01 \x01(\t\x12\x10\n\x08\x66raction\x18\x02 \x01(\x02\"\xbe\x01\n\x12QuestionBlockProto\x12\r\n\x05scale\x18\x01 \x01(\x02\x12*\n\x07options\x18\x02 \x03(\x0b\x32\x19.QuestionBlockOptionProto\x12\x15\n\rcorrect_index\x18\x03 \x01(\x05\x12+\n\x13\x63orrect_answer_face\x18\x04 \x01(\x0b\x32\x0e.CardFaceProto\x12)\n\x11wrong_answer_face\x18\x05 \x01(\x0b\x32\x0e.CardFaceProto\"!\n\x10PromptBlockProto\x12\r\n\x05label\x18\x01 \x01(\t\"H\n\x14RevealBackBlockProto\x12\r\n\x05label\x18\x01 \x01(\t\x12!\n\tback_face\x18\x02 \x01(\x0b\x32\x0e.CardFaceProto*A\n\rCardTypeProto\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06STATIC\x10\x02\x12\x0e\n\nTRUE_FALSE\x10\x03\x12\x07\n\x03\x41\x42\x43\x10\x04*F\n\rFontNameProto\x12\x18\n\x14\x46ONT_NAME_PROTO_TEXT\x10\x00\x12\x1b\n\x17\x46ONT_NAME_PROTO_DISPLAY\x10\x01*K\n\x0f\x46ontWeightProto\x12\x1c\n\x18\x46ONT_WEIGHT_PROTO_NORMAL\x10\x00\x12\x1a\n\x16\x46ONT_WEIGHT_PROTO_BOLD\x10\x01*J\n\x0e\x46ontStyleProto\x12\x1b\n\x17\x46ONT_STYLE_PROTO_NORMAL\x10\x00\x12\x1b\n\x17\x46ONT_STYLE_PROTO_ITALIC\x10\x01*\x82\x01\n\x13TextDecorationProto\x12\x1e\n\x1aTEXT_DECORATION_PROTO_NONE\x10\x00\x12#\n\x1fTEXT_DECORATION_PROTO_UNDERLINE\x10\x01\x12&\n\"TEXT_DECORATION_PROTO_LINE_THROUGH\x10\x02*\x96\x01\n\x12TextAlignmentProto\x12\x1d\n\x19TEXT_ALIGNMENT_PROTO_LEFT\x10\x00\x12\x1f\n\x1bTEXT_ALIGNMENT_PROTO_CENTER\x10\x01\x12\x1e\n\x1aTEXT_ALIGNMENT_PROTO_RIGHT\x10\x02\x12 \n\x1cTEXT_ALIGNMENT_PROTO_JUSTIFY\x10\x03*[\n\x13TextWhitespaceProto\x12 \n\x1cTEXT_WHITESPACE_PROTO_NORMAL\x10\x00\x12\"\n\x1eTEXT_WHITESPACE_PROTO_PRE_WRAP\x10\x01*k\n\x10TextHyphensProto\x12\x1b\n\x17TEXT_HYPHENS_PROTO_NONE\x10\x00\x12\x1d\n\x19TEXT_HYPHENS_PROTO_MANUAL\x10\x01\x12\x1b\n\x17TEXT_HYPHENS_PROTO_AUTO\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'StoryProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STORYAPIRESPONSEPROTO_LATENCIESENTRY._options = None
  _STORYAPIRESPONSEPROTO_LATENCIESENTRY._serialized_options = b'8\001'
  _CARDTYPEPROTO._serialized_start=3872
  _CARDTYPEPROTO._serialized_end=3937
  _FONTNAMEPROTO._serialized_start=3939
  _FONTNAMEPROTO._serialized_end=4009
  _FONTWEIGHTPROTO._serialized_start=4011
  _FONTWEIGHTPROTO._serialized_end=4086
  _FONTSTYLEPROTO._serialized_start=4088
  _FONTSTYLEPROTO._serialized_end=4162
  _TEXTDECORATIONPROTO._serialized_start=4165
  _TEXTDECORATIONPROTO._serialized_end=4295
  _TEXTALIGNMENTPROTO._serialized_start=4298
  _TEXTALIGNMENTPROTO._serialized_end=4448
  _TEXTWHITESPACEPROTO._serialized_start=4450
  _TEXTWHITESPACEPROTO._serialized_end=4541
  _TEXTHYPHENSPROTO._serialized_start=4543
  _TEXTHYPHENSPROTO._serialized_end=4650
  _GETSTORIESREQUESTPROTO._serialized_start=85
  _GETSTORIESREQUESTPROTO._serialized_end=166
  _GETSTORIESRESPONSEPROTO._serialized_start=169
  _GETSTORIESRESPONSEPROTO._serialized_end=304
  _CREATESTORYREQUESTPROTO._serialized_start=306
  _CREATESTORYREQUESTPROTO._serialized_end=358
  _CREATESTORYRESPONSEPROTO._serialized_start=360
  _CREATESTORYRESPONSEPROTO._serialized_end=404
  _UPDATESTORYREQUESTPROTO._serialized_start=406
  _UPDATESTORYREQUESTPROTO._serialized_end=476
  _UPDATESTORYRESPONSEPROTO._serialized_start=478
  _UPDATESTORYRESPONSEPROTO._serialized_end=504
  _DELETESTORYREQUESTPROTO._serialized_start=506
  _DELETESTORYREQUESTPROTO._serialized_end=549
  _DELETESTORYRESPONSEPROTO._serialized_start=551
  _DELETESTORYRESPONSEPROTO._serialized_end=577
  _STORYAPIREQUESTPROTO._serialized_start=580
  _STORYAPIREQUESTPROTO._serialized_end=811
  _STORYAPIRESPONSEPROTO._serialized_start=814
  _STORYAPIRESPONSEPROTO._serialized_end=1186
  _STORYAPIRESPONSEPROTO_LATENCIESENTRY._serialized_start=1099
  _STORYAPIRESPONSEPROTO_LATENCIESENTRY._serialized_end=1174
  _STORYDATAPROTO._serialized_start=1188
  _STORYDATAPROTO._serialized_end=1297
  _CARDDATAPROTO._serialized_start=1300
  _CARDDATAPROTO._serialized_end=1530
  _STORIESPROTO._serialized_start=1532
  _STORIESPROTO._serialized_end=1623
  _STORYPROTO._serialized_start=1626
  _STORYPROTO._serialized_end=1840
  _CARDPROTO._serialized_start=1842
  _CARDPROTO._serialized_end=1901
  _CARDFACEPROTO._serialized_start=1903
  _CARDFACEPROTO._serialized_end=1970
  _CARDBLOCKPROTO._serialized_start=1973
  _CARDBLOCKPROTO._serialized_end=2368
  _SPACEBLOCKPROTO._serialized_start=2370
  _SPACEBLOCKPROTO._serialized_end=2402
  _IMAGEREFPROTO._serialized_start=2404
  _IMAGEREFPROTO._serialized_end=2473
  _IMAGEBLOCKPROTO._serialized_start=2475
  _IMAGEBLOCKPROTO._serialized_end=2565
  _TEXTSPANPROTO._serialized_start=2568
  _TEXTSPANPROTO._serialized_end=2715
  _STYLEDTEXTPROTO._serialized_start=2718
  _STYLEDTEXTPROTO._serialized_end=2978
  _TEXTBLOCKPROTO._serialized_start=2980
  _TEXTBLOCKPROTO._serialized_end=3035
  _FLIPBLOCKPROTO._serialized_start=3037
  _FLIPBLOCKPROTO._serialized_end=3068
  _COFFEEBLOCKPROTO._serialized_start=3070
  _COFFEEBLOCKPROTO._serialized_end=3160
  _REVEALBLOCKPROTO._serialized_start=3162
  _REVEALBLOCKPROTO._serialized_end=3242
  _CHOICEBLOCKOPTIONPROTO._serialized_start=3244
  _CHOICEBLOCKOPTIONPROTO._serialized_end=3318
  _CHOICEBLOCKPROTO._serialized_start=3321
  _CHOICEBLOCKPROTO._serialized_end=3507
  _QUESTIONBLOCKOPTIONPROTO._serialized_start=3509
  _QUESTIONBLOCKOPTIONPROTO._serialized_end=3568
  _QUESTIONBLOCKPROTO._serialized_start=3571
  _QUESTIONBLOCKPROTO._serialized_end=3761
  _PROMPTBLOCKPROTO._serialized_start=3763
  _PROMPTBLOCKPROTO._serialized_end=3796
  _REVEALBACKBLOCKPROTO._serialized_start=3798
  _REVEALBACKBLOCKPROTO._serialized_end=3870
# @@protoc_insertion_point(module_scope)
