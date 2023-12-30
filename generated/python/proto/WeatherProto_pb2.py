# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WeatherProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12WeatherProto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc1\x03\n\x0cWeatherProto\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bregion_code\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t\x12\x11\n\ttime_zone\x18\x05 \x01(\t\x12\x10\n\x08latitude\x18\x06 \x01(\x01\x12\x11\n\tlongitude\x18\x07 \x01(\x01\x12)\n\tcondition\x18\x08 \x01(\x0e\x32\x16.WeatherConditionProto\x12!\n\x19open_weather_condition_id\x18\t \x01(\x05\x12\x13\n\x0btemperature\x18\n \x01(\x02\x12\x1e\n\x16temperature_feels_like\x18\x0b \x01(\x02\x12\x17\n\x0ftemperature_min\x18\x0c \x01(\x02\x12\x17\n\x0ftemperature_max\x18\r \x01(\x02\x12\x10\n\x08pressure\x18\x0e \x01(\x05\x12\x10\n\x08humidity\x18\x0f \x01(\x05\x12\x12\n\nvisibility\x18\x10 \x01(\x05\x12\x12\n\nwind_speed\x18\x11 \x01(\x02\x12\x14\n\x0cwind_degrees\x18\x12 \x01(\x05*\xec\x03\n\x15WeatherConditionProto\x12\x1d\n\x19WEATHER_CONDITION_UNKNOWN\x10\x00\x12\"\n\x1eWEATHER_CONDITION_THUNDERSTORM\x10\x01\x12\x1d\n\x19WEATHER_CONDITION_DRIZZLE\x10\x02\x12\x1a\n\x16WEATHER_CONDITION_RAIN\x10\x03\x12\x1a\n\x16WEATHER_CONDITION_SNOW\x10\x04\x12\x1a\n\x16WEATHER_CONDITION_MIST\x10\x05\x12\x1b\n\x17WEATHER_CONDITION_SMOKE\x10\x06\x12\x1a\n\x16WEATHER_CONDITION_HAZE\x10\x07\x12\x1a\n\x16WEATHER_CONDITION_DUST\x10\x08\x12\x19\n\x15WEATHER_CONDITION_FOG\x10\t\x12\x1a\n\x16WEATHER_CONDITION_SAND\x10\n\x12\x19\n\x15WEATHER_CONDITION_ASH\x10\x0b\x12\x1c\n\x18WEATHER_CONDITION_SQUALL\x10\x0c\x12\x1d\n\x19WEATHER_CONDITION_TORNADO\x10\r\x12\x1b\n\x17WEATHER_CONDITION_CLEAR\x10\x0e\x12\x1c\n\x18WEATHER_CONDITION_CLOUDS\x10\x0f\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WeatherProto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WEATHERCONDITIONPROTO._serialized_start=508
  _WEATHERCONDITIONPROTO._serialized_end=1000
  _WEATHERPROTO._serialized_start=56
  _WEATHERPROTO._serialized_end=505
# @@protoc_insertion_point(module_scope)
