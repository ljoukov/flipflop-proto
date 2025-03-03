/* eslint-disable */
// @generated by protobuf-ts 2.9.4 with parameter eslint_disable,long_type_string,ts_nocheck
// @generated from protobuf file "ServerProto.proto" (syntax proto3)
// tslint:disable
// @ts-nocheck
import type { BinaryWriteOptions } from "@protobuf-ts/runtime";
import type { IBinaryWriter } from "@protobuf-ts/runtime";
import { WireType } from "@protobuf-ts/runtime";
import type { BinaryReadOptions } from "@protobuf-ts/runtime";
import type { IBinaryReader } from "@protobuf-ts/runtime";
import { UnknownFieldHandler } from "@protobuf-ts/runtime";
import type { PartialMessage } from "@protobuf-ts/runtime";
import { reflectionMergePartial } from "@protobuf-ts/runtime";
import { MessageType } from "@protobuf-ts/runtime";
import { Duration } from "./google/protobuf/duration";
/**
 * @generated from protobuf message ServerApiRequestProto
 */
export interface ServerApiRequestProto {
    /**
     * @generated from protobuf oneof: request
     */
    request: {
        oneofKind: "tts";
        /**
         * @generated from protobuf field: ServerTTSRequestProto tts = 10;
         */
        tts: ServerTTSRequestProto;
    } | {
        oneofKind: undefined;
    };
}
/**
 * @generated from protobuf message ServerApiResponseProto
 */
export interface ServerApiResponseProto {
    /**
     * @generated from protobuf oneof: response
     */
    response: {
        oneofKind: "tts";
        /**
         * @generated from protobuf field: ServerTTSResponseProto tts = 10;
         */
        tts: ServerTTSResponseProto;
    } | {
        oneofKind: undefined;
    };
    /**
     * @generated from protobuf field: map<string, google.protobuf.Duration> latencies = 100;
     */
    latencies: {
        [key: string]: Duration;
    };
}
/**
 * @generated from protobuf message ServerTTSRequestProto
 */
export interface ServerTTSRequestProto {
    /**
     * @generated from protobuf field: repeated ServerTTSSegmentProto segments = 1;
     */
    segments: ServerTTSSegmentProto[];
    /**
     * @generated from protobuf field: float silence_sec = 2;
     */
    silenceSec: number;
    /**
     * @generated from protobuf field: ServerTTSOptionsProto options = 3;
     */
    options?: ServerTTSOptionsProto;
}
/**
 * @generated from protobuf message ServerTTSOptionsProto
 */
export interface ServerTTSOptionsProto {
    /**
     * @generated from protobuf field: bool disable_transcription = 1;
     */
    disableTranscription: boolean;
}
/**
 * @generated from protobuf message ServerTTSSegmentProto
 */
export interface ServerTTSSegmentProto {
    /**
     * @generated from protobuf field: float leading_silence_sec = 1;
     */
    leadingSilenceSec: number;
    /**
     * @generated from protobuf field: float min_duration_sec = 2;
     */
    minDurationSec: number;
    /**
     * @generated from protobuf field: string text = 3;
     */
    text: string;
    /**
     * @generated from protobuf field: ServerTTSVoiceProto voice = 4;
     */
    voice: ServerTTSVoiceProto;
}
/**
 * @generated from protobuf message ServerTTSResponseProto
 */
export interface ServerTTSResponseProto {
    /**
     * @generated from protobuf field: bytes audio = 1;
     */
    audio: Uint8Array;
    /**
     * @generated from protobuf field: ServerAudioMetadataProto audio_metadata = 2;
     */
    audioMetadata?: ServerAudioMetadataProto;
    /**
     * @generated from protobuf field: repeated ServerTTSSegmentTranscriptProto segment_transcripts = 3;
     */
    segmentTranscripts: ServerTTSSegmentTranscriptProto[];
}
/**
 * @generated from protobuf message ServerAudioMetadataProto
 */
export interface ServerAudioMetadataProto {
    /**
     * @generated from protobuf field: float duration_sec = 1;
     */
    durationSec: number;
    /**
     * @generated from protobuf field: int32 sample_rate = 2;
     */
    sampleRate: number;
    /**
     * @generated from protobuf field: int32 num_channels = 3;
     */
    numChannels: number;
}
/**
 * @generated from protobuf message ServerTTSSegmentTranscriptProto
 */
export interface ServerTTSSegmentTranscriptProto {
    /**
     * @generated from protobuf field: float offset_sec = 1;
     */
    offsetSec: number;
    /**
     * @generated from protobuf field: float duration_sec = 2;
     */
    durationSec: number;
    /**
     * @generated from protobuf field: ServerTranscriptProto transcript = 3;
     */
    transcript?: ServerTranscriptProto;
}
/**
 * @generated from protobuf message ServerTranscriptProto
 */
export interface ServerTranscriptProto {
    /**
     * @generated from protobuf field: string text = 1;
     */
    text: string;
    /**
     * @generated from protobuf field: repeated ServerTranscriptWordProto words = 2;
     */
    words: ServerTranscriptWordProto[];
}
/**
 * @generated from protobuf message ServerTranscriptWordProto
 */
export interface ServerTranscriptWordProto {
    /**
     * @generated from protobuf field: string word = 1;
     */
    word: string;
    /**
     * @generated from protobuf field: float start_sec = 2;
     */
    startSec: number;
    /**
     * @generated from protobuf field: float end_sec = 3;
     */
    endSec: number;
}
/**
 * @generated from protobuf enum ServerTTSVoiceProto
 */
export enum ServerTTSVoiceProto {
    /**
     * @generated from protobuf enum value: SERVER_TTS_VOICE_PROTO_UNDEFINED = 0;
     */
    SERVER_TTS_VOICE_PROTO_UNDEFINED = 0,
    /**
     * @generated from protobuf enum value: SERVER_TTS_VOICE_PROTO_ALLOY = 1;
     */
    SERVER_TTS_VOICE_PROTO_ALLOY = 1,
    /**
     * @generated from protobuf enum value: SERVER_TTS_VOICE_PROTO_ECHO = 2;
     */
    SERVER_TTS_VOICE_PROTO_ECHO = 2,
    /**
     * @generated from protobuf enum value: SERVER_TTS_VOICE_PROTO_FABLE = 3;
     */
    SERVER_TTS_VOICE_PROTO_FABLE = 3,
    /**
     * @generated from protobuf enum value: SERVER_TTS_VOICE_PROTO_ONYX = 4;
     */
    SERVER_TTS_VOICE_PROTO_ONYX = 4,
    /**
     * @generated from protobuf enum value: SERVER_TTS_VOICE_PROTO_NOVA = 5;
     */
    SERVER_TTS_VOICE_PROTO_NOVA = 5,
    /**
     * @generated from protobuf enum value: SERVER_TTS_VOICE_PROTO_SHIMMER = 6;
     */
    SERVER_TTS_VOICE_PROTO_SHIMMER = 6,
    /**
     * @generated from protobuf enum value: SERVER_TTS_VOICE_PROTO_MEDITATION = 7;
     */
    SERVER_TTS_VOICE_PROTO_MEDITATION = 7,
    /**
     * @generated from protobuf enum value: SERVER_TTS_VOICE_PROTO_JOURNEY_D_MALE = 8;
     */
    SERVER_TTS_VOICE_PROTO_JOURNEY_D_MALE = 8,
    /**
     * @generated from protobuf enum value: SERVER_TTS_VOICE_PROTO_JOURNEY_F_FEMALE = 9;
     */
    SERVER_TTS_VOICE_PROTO_JOURNEY_F_FEMALE = 9,
    /**
     * @generated from protobuf enum value: SERVER_TTS_VOICE_PROTO_JOURNEY_O_FEMALE = 10;
     */
    SERVER_TTS_VOICE_PROTO_JOURNEY_O_FEMALE = 10
}
// @generated message type with reflection information, may provide speed optimized methods
class ServerApiRequestProto$Type extends MessageType<ServerApiRequestProto> {
    constructor() {
        super("ServerApiRequestProto", [
            { no: 10, name: "tts", kind: "message", oneof: "request", T: () => ServerTTSRequestProto }
        ]);
    }
    create(value?: PartialMessage<ServerApiRequestProto>): ServerApiRequestProto {
        const message = globalThis.Object.create((this.messagePrototype!));
        message.request = { oneofKind: undefined };
        if (value !== undefined)
            reflectionMergePartial<ServerApiRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ServerApiRequestProto): ServerApiRequestProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* ServerTTSRequestProto tts */ 10:
                    message.request = {
                        oneofKind: "tts",
                        tts: ServerTTSRequestProto.internalBinaryRead(reader, reader.uint32(), options, (message.request as any).tts)
                    };
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: ServerApiRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* ServerTTSRequestProto tts = 10; */
        if (message.request.oneofKind === "tts")
            ServerTTSRequestProto.internalBinaryWrite(message.request.tts, writer.tag(10, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ServerApiRequestProto
 */
export const ServerApiRequestProto = new ServerApiRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ServerApiResponseProto$Type extends MessageType<ServerApiResponseProto> {
    constructor() {
        super("ServerApiResponseProto", [
            { no: 10, name: "tts", kind: "message", oneof: "response", T: () => ServerTTSResponseProto },
            { no: 100, name: "latencies", kind: "map", K: 9 /*ScalarType.STRING*/, V: { kind: "message", T: () => Duration } }
        ]);
    }
    create(value?: PartialMessage<ServerApiResponseProto>): ServerApiResponseProto {
        const message = globalThis.Object.create((this.messagePrototype!));
        message.response = { oneofKind: undefined };
        message.latencies = {};
        if (value !== undefined)
            reflectionMergePartial<ServerApiResponseProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ServerApiResponseProto): ServerApiResponseProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* ServerTTSResponseProto tts */ 10:
                    message.response = {
                        oneofKind: "tts",
                        tts: ServerTTSResponseProto.internalBinaryRead(reader, reader.uint32(), options, (message.response as any).tts)
                    };
                    break;
                case /* map<string, google.protobuf.Duration> latencies */ 100:
                    this.binaryReadMap100(message.latencies, reader, options);
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    private binaryReadMap100(map: ServerApiResponseProto["latencies"], reader: IBinaryReader, options: BinaryReadOptions): void {
        let len = reader.uint32(), end = reader.pos + len, key: keyof ServerApiResponseProto["latencies"] | undefined, val: ServerApiResponseProto["latencies"][any] | undefined;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case 1:
                    key = reader.string();
                    break;
                case 2:
                    val = Duration.internalBinaryRead(reader, reader.uint32(), options);
                    break;
                default: throw new globalThis.Error("unknown map entry field for field ServerApiResponseProto.latencies");
            }
        }
        map[key ?? ""] = val ?? Duration.create();
    }
    internalBinaryWrite(message: ServerApiResponseProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* ServerTTSResponseProto tts = 10; */
        if (message.response.oneofKind === "tts")
            ServerTTSResponseProto.internalBinaryWrite(message.response.tts, writer.tag(10, WireType.LengthDelimited).fork(), options).join();
        /* map<string, google.protobuf.Duration> latencies = 100; */
        for (let k of globalThis.Object.keys(message.latencies)) {
            writer.tag(100, WireType.LengthDelimited).fork().tag(1, WireType.LengthDelimited).string(k);
            writer.tag(2, WireType.LengthDelimited).fork();
            Duration.internalBinaryWrite(message.latencies[k], writer, options);
            writer.join().join();
        }
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ServerApiResponseProto
 */
export const ServerApiResponseProto = new ServerApiResponseProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ServerTTSRequestProto$Type extends MessageType<ServerTTSRequestProto> {
    constructor() {
        super("ServerTTSRequestProto", [
            { no: 1, name: "segments", kind: "message", repeat: 1 /*RepeatType.PACKED*/, T: () => ServerTTSSegmentProto },
            { no: 2, name: "silence_sec", kind: "scalar", T: 2 /*ScalarType.FLOAT*/ },
            { no: 3, name: "options", kind: "message", T: () => ServerTTSOptionsProto }
        ]);
    }
    create(value?: PartialMessage<ServerTTSRequestProto>): ServerTTSRequestProto {
        const message = globalThis.Object.create((this.messagePrototype!));
        message.segments = [];
        message.silenceSec = 0;
        if (value !== undefined)
            reflectionMergePartial<ServerTTSRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ServerTTSRequestProto): ServerTTSRequestProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* repeated ServerTTSSegmentProto segments */ 1:
                    message.segments.push(ServerTTSSegmentProto.internalBinaryRead(reader, reader.uint32(), options));
                    break;
                case /* float silence_sec */ 2:
                    message.silenceSec = reader.float();
                    break;
                case /* ServerTTSOptionsProto options */ 3:
                    message.options = ServerTTSOptionsProto.internalBinaryRead(reader, reader.uint32(), options, message.options);
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: ServerTTSRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* repeated ServerTTSSegmentProto segments = 1; */
        for (let i = 0; i < message.segments.length; i++)
            ServerTTSSegmentProto.internalBinaryWrite(message.segments[i], writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        /* float silence_sec = 2; */
        if (message.silenceSec !== 0)
            writer.tag(2, WireType.Bit32).float(message.silenceSec);
        /* ServerTTSOptionsProto options = 3; */
        if (message.options)
            ServerTTSOptionsProto.internalBinaryWrite(message.options, writer.tag(3, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ServerTTSRequestProto
 */
export const ServerTTSRequestProto = new ServerTTSRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ServerTTSOptionsProto$Type extends MessageType<ServerTTSOptionsProto> {
    constructor() {
        super("ServerTTSOptionsProto", [
            { no: 1, name: "disable_transcription", kind: "scalar", T: 8 /*ScalarType.BOOL*/ }
        ]);
    }
    create(value?: PartialMessage<ServerTTSOptionsProto>): ServerTTSOptionsProto {
        const message = globalThis.Object.create((this.messagePrototype!));
        message.disableTranscription = false;
        if (value !== undefined)
            reflectionMergePartial<ServerTTSOptionsProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ServerTTSOptionsProto): ServerTTSOptionsProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* bool disable_transcription */ 1:
                    message.disableTranscription = reader.bool();
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: ServerTTSOptionsProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* bool disable_transcription = 1; */
        if (message.disableTranscription !== false)
            writer.tag(1, WireType.Varint).bool(message.disableTranscription);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ServerTTSOptionsProto
 */
export const ServerTTSOptionsProto = new ServerTTSOptionsProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ServerTTSSegmentProto$Type extends MessageType<ServerTTSSegmentProto> {
    constructor() {
        super("ServerTTSSegmentProto", [
            { no: 1, name: "leading_silence_sec", kind: "scalar", T: 2 /*ScalarType.FLOAT*/ },
            { no: 2, name: "min_duration_sec", kind: "scalar", T: 2 /*ScalarType.FLOAT*/ },
            { no: 3, name: "text", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 4, name: "voice", kind: "enum", T: () => ["ServerTTSVoiceProto", ServerTTSVoiceProto] }
        ]);
    }
    create(value?: PartialMessage<ServerTTSSegmentProto>): ServerTTSSegmentProto {
        const message = globalThis.Object.create((this.messagePrototype!));
        message.leadingSilenceSec = 0;
        message.minDurationSec = 0;
        message.text = "";
        message.voice = 0;
        if (value !== undefined)
            reflectionMergePartial<ServerTTSSegmentProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ServerTTSSegmentProto): ServerTTSSegmentProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* float leading_silence_sec */ 1:
                    message.leadingSilenceSec = reader.float();
                    break;
                case /* float min_duration_sec */ 2:
                    message.minDurationSec = reader.float();
                    break;
                case /* string text */ 3:
                    message.text = reader.string();
                    break;
                case /* ServerTTSVoiceProto voice */ 4:
                    message.voice = reader.int32();
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: ServerTTSSegmentProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* float leading_silence_sec = 1; */
        if (message.leadingSilenceSec !== 0)
            writer.tag(1, WireType.Bit32).float(message.leadingSilenceSec);
        /* float min_duration_sec = 2; */
        if (message.minDurationSec !== 0)
            writer.tag(2, WireType.Bit32).float(message.minDurationSec);
        /* string text = 3; */
        if (message.text !== "")
            writer.tag(3, WireType.LengthDelimited).string(message.text);
        /* ServerTTSVoiceProto voice = 4; */
        if (message.voice !== 0)
            writer.tag(4, WireType.Varint).int32(message.voice);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ServerTTSSegmentProto
 */
export const ServerTTSSegmentProto = new ServerTTSSegmentProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ServerTTSResponseProto$Type extends MessageType<ServerTTSResponseProto> {
    constructor() {
        super("ServerTTSResponseProto", [
            { no: 1, name: "audio", kind: "scalar", T: 12 /*ScalarType.BYTES*/ },
            { no: 2, name: "audio_metadata", kind: "message", T: () => ServerAudioMetadataProto },
            { no: 3, name: "segment_transcripts", kind: "message", repeat: 1 /*RepeatType.PACKED*/, T: () => ServerTTSSegmentTranscriptProto }
        ]);
    }
    create(value?: PartialMessage<ServerTTSResponseProto>): ServerTTSResponseProto {
        const message = globalThis.Object.create((this.messagePrototype!));
        message.audio = new Uint8Array(0);
        message.segmentTranscripts = [];
        if (value !== undefined)
            reflectionMergePartial<ServerTTSResponseProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ServerTTSResponseProto): ServerTTSResponseProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* bytes audio */ 1:
                    message.audio = reader.bytes();
                    break;
                case /* ServerAudioMetadataProto audio_metadata */ 2:
                    message.audioMetadata = ServerAudioMetadataProto.internalBinaryRead(reader, reader.uint32(), options, message.audioMetadata);
                    break;
                case /* repeated ServerTTSSegmentTranscriptProto segment_transcripts */ 3:
                    message.segmentTranscripts.push(ServerTTSSegmentTranscriptProto.internalBinaryRead(reader, reader.uint32(), options));
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: ServerTTSResponseProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* bytes audio = 1; */
        if (message.audio.length)
            writer.tag(1, WireType.LengthDelimited).bytes(message.audio);
        /* ServerAudioMetadataProto audio_metadata = 2; */
        if (message.audioMetadata)
            ServerAudioMetadataProto.internalBinaryWrite(message.audioMetadata, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* repeated ServerTTSSegmentTranscriptProto segment_transcripts = 3; */
        for (let i = 0; i < message.segmentTranscripts.length; i++)
            ServerTTSSegmentTranscriptProto.internalBinaryWrite(message.segmentTranscripts[i], writer.tag(3, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ServerTTSResponseProto
 */
export const ServerTTSResponseProto = new ServerTTSResponseProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ServerAudioMetadataProto$Type extends MessageType<ServerAudioMetadataProto> {
    constructor() {
        super("ServerAudioMetadataProto", [
            { no: 1, name: "duration_sec", kind: "scalar", T: 2 /*ScalarType.FLOAT*/ },
            { no: 2, name: "sample_rate", kind: "scalar", T: 5 /*ScalarType.INT32*/ },
            { no: 3, name: "num_channels", kind: "scalar", T: 5 /*ScalarType.INT32*/ }
        ]);
    }
    create(value?: PartialMessage<ServerAudioMetadataProto>): ServerAudioMetadataProto {
        const message = globalThis.Object.create((this.messagePrototype!));
        message.durationSec = 0;
        message.sampleRate = 0;
        message.numChannels = 0;
        if (value !== undefined)
            reflectionMergePartial<ServerAudioMetadataProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ServerAudioMetadataProto): ServerAudioMetadataProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* float duration_sec */ 1:
                    message.durationSec = reader.float();
                    break;
                case /* int32 sample_rate */ 2:
                    message.sampleRate = reader.int32();
                    break;
                case /* int32 num_channels */ 3:
                    message.numChannels = reader.int32();
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: ServerAudioMetadataProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* float duration_sec = 1; */
        if (message.durationSec !== 0)
            writer.tag(1, WireType.Bit32).float(message.durationSec);
        /* int32 sample_rate = 2; */
        if (message.sampleRate !== 0)
            writer.tag(2, WireType.Varint).int32(message.sampleRate);
        /* int32 num_channels = 3; */
        if (message.numChannels !== 0)
            writer.tag(3, WireType.Varint).int32(message.numChannels);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ServerAudioMetadataProto
 */
export const ServerAudioMetadataProto = new ServerAudioMetadataProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ServerTTSSegmentTranscriptProto$Type extends MessageType<ServerTTSSegmentTranscriptProto> {
    constructor() {
        super("ServerTTSSegmentTranscriptProto", [
            { no: 1, name: "offset_sec", kind: "scalar", T: 2 /*ScalarType.FLOAT*/ },
            { no: 2, name: "duration_sec", kind: "scalar", T: 2 /*ScalarType.FLOAT*/ },
            { no: 3, name: "transcript", kind: "message", T: () => ServerTranscriptProto }
        ]);
    }
    create(value?: PartialMessage<ServerTTSSegmentTranscriptProto>): ServerTTSSegmentTranscriptProto {
        const message = globalThis.Object.create((this.messagePrototype!));
        message.offsetSec = 0;
        message.durationSec = 0;
        if (value !== undefined)
            reflectionMergePartial<ServerTTSSegmentTranscriptProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ServerTTSSegmentTranscriptProto): ServerTTSSegmentTranscriptProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* float offset_sec */ 1:
                    message.offsetSec = reader.float();
                    break;
                case /* float duration_sec */ 2:
                    message.durationSec = reader.float();
                    break;
                case /* ServerTranscriptProto transcript */ 3:
                    message.transcript = ServerTranscriptProto.internalBinaryRead(reader, reader.uint32(), options, message.transcript);
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: ServerTTSSegmentTranscriptProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* float offset_sec = 1; */
        if (message.offsetSec !== 0)
            writer.tag(1, WireType.Bit32).float(message.offsetSec);
        /* float duration_sec = 2; */
        if (message.durationSec !== 0)
            writer.tag(2, WireType.Bit32).float(message.durationSec);
        /* ServerTranscriptProto transcript = 3; */
        if (message.transcript)
            ServerTranscriptProto.internalBinaryWrite(message.transcript, writer.tag(3, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ServerTTSSegmentTranscriptProto
 */
export const ServerTTSSegmentTranscriptProto = new ServerTTSSegmentTranscriptProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ServerTranscriptProto$Type extends MessageType<ServerTranscriptProto> {
    constructor() {
        super("ServerTranscriptProto", [
            { no: 1, name: "text", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "words", kind: "message", repeat: 1 /*RepeatType.PACKED*/, T: () => ServerTranscriptWordProto }
        ]);
    }
    create(value?: PartialMessage<ServerTranscriptProto>): ServerTranscriptProto {
        const message = globalThis.Object.create((this.messagePrototype!));
        message.text = "";
        message.words = [];
        if (value !== undefined)
            reflectionMergePartial<ServerTranscriptProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ServerTranscriptProto): ServerTranscriptProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string text */ 1:
                    message.text = reader.string();
                    break;
                case /* repeated ServerTranscriptWordProto words */ 2:
                    message.words.push(ServerTranscriptWordProto.internalBinaryRead(reader, reader.uint32(), options));
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: ServerTranscriptProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string text = 1; */
        if (message.text !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.text);
        /* repeated ServerTranscriptWordProto words = 2; */
        for (let i = 0; i < message.words.length; i++)
            ServerTranscriptWordProto.internalBinaryWrite(message.words[i], writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ServerTranscriptProto
 */
export const ServerTranscriptProto = new ServerTranscriptProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ServerTranscriptWordProto$Type extends MessageType<ServerTranscriptWordProto> {
    constructor() {
        super("ServerTranscriptWordProto", [
            { no: 1, name: "word", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "start_sec", kind: "scalar", T: 2 /*ScalarType.FLOAT*/ },
            { no: 3, name: "end_sec", kind: "scalar", T: 2 /*ScalarType.FLOAT*/ }
        ]);
    }
    create(value?: PartialMessage<ServerTranscriptWordProto>): ServerTranscriptWordProto {
        const message = globalThis.Object.create((this.messagePrototype!));
        message.word = "";
        message.startSec = 0;
        message.endSec = 0;
        if (value !== undefined)
            reflectionMergePartial<ServerTranscriptWordProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ServerTranscriptWordProto): ServerTranscriptWordProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string word */ 1:
                    message.word = reader.string();
                    break;
                case /* float start_sec */ 2:
                    message.startSec = reader.float();
                    break;
                case /* float end_sec */ 3:
                    message.endSec = reader.float();
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: ServerTranscriptWordProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string word = 1; */
        if (message.word !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.word);
        /* float start_sec = 2; */
        if (message.startSec !== 0)
            writer.tag(2, WireType.Bit32).float(message.startSec);
        /* float end_sec = 3; */
        if (message.endSec !== 0)
            writer.tag(3, WireType.Bit32).float(message.endSec);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ServerTranscriptWordProto
 */
export const ServerTranscriptWordProto = new ServerTranscriptWordProto$Type();
