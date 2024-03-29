/* eslint-disable */
// @generated by protobuf-ts 2.9.1 with parameter eslint_disable,long_type_string,ts_nocheck
// @generated from protobuf file "ReadletProto.proto" (syntax proto3)
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
import { MESSAGE_TYPE } from "@protobuf-ts/runtime";
import { MessageType } from "@protobuf-ts/runtime";
import { ColorTypeProto } from "./ColorProto";
import { Timestamp } from "./google/protobuf/timestamp";
import { Duration } from "./google/protobuf/duration";
/**
 * @generated from protobuf message ReadletApiRequestProto
 */
export interface ReadletApiRequestProto {
    /**
     * @generated from protobuf field: string encoded_user_auth = 1;
     */
    encodedUserAuth: string;
    /**
     * @generated from protobuf oneof: request
     */
    request: {
        oneofKind: "getReadlets";
        /**
         * @generated from protobuf field: GetReadletsRequestProto get_readlets = 2;
         */
        getReadlets: GetReadletsRequestProto;
    } | {
        oneofKind: undefined;
    };
}
/**
 * @generated from protobuf message ReadletApiResponseProto
 */
export interface ReadletApiResponseProto {
    /**
     * If present the token was refreshed and the client should use this new one from now onwards.
     *
     * @generated from protobuf field: string refreshed_encoded_user_auth = 1;
     */
    refreshedEncodedUserAuth: string;
    /**
     * @generated from protobuf oneof: response
     */
    response: {
        oneofKind: "getReadlets";
        /**
         * @generated from protobuf field: GetReadletsResponseProto get_readlets = 2;
         */
        getReadlets: GetReadletsResponseProto;
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
 * @generated from protobuf message GetReadletsRequestProto
 */
export interface GetReadletsRequestProto {
    /**
     * @generated from protobuf field: repeated string category_filter = 1;
     */
    categoryFilter: string[];
}
/**
 * @generated from protobuf message GetReadletsResponseProto
 */
export interface GetReadletsResponseProto {
    /**
     * @generated from protobuf field: repeated ReadletProto readlets = 1;
     */
    readlets: ReadletProto[];
    /**
     * @generated from protobuf field: repeated ReadletCategoryProto available_categories = 2;
     */
    availableCategories: ReadletCategoryProto[];
}
/**
 * @generated from protobuf message ReadletsCacheProto
 */
export interface ReadletsCacheProto {
    /**
     * @generated from protobuf field: google.protobuf.Timestamp created_at = 1;
     */
    createdAt?: Timestamp;
    /**
     * @generated from protobuf field: repeated ReadletProto readlets = 2;
     */
    readlets: ReadletProto[];
}
/**
 * @generated from protobuf message ReadletCategoryProto
 */
export interface ReadletCategoryProto {
    /**
     * @generated from protobuf field: string id = 1;
     */
    id: string;
    /**
     * @generated from protobuf field: string display_name = 2;
     */
    displayName: string;
}
/**
 * @generated from protobuf message ReadletChapterProto
 */
export interface ReadletChapterProto {
    /**
     * @generated from protobuf field: ReadletChapterType type = 1;
     */
    type: ReadletChapterType;
    /**
     * @generated from protobuf field: string title = 2;
     */
    title: string;
    /**
     * @generated from protobuf field: string subtitle = 3;
     */
    subtitle: string;
    /**
     * @generated from protobuf field: string text = 4;
     */
    text: string;
    /**
     * @generated from protobuf field: string audio_path = 5;
     */
    audioPath: string;
    /**
     * @generated from protobuf field: google.protobuf.Duration audio_duration = 6;
     */
    audioDuration?: Duration;
}
/**
 * @generated from protobuf message ReadletProto
 */
export interface ReadletProto {
    /**
     * @generated from protobuf field: string id = 1;
     */
    id: string;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp created_at = 2;
     */
    createdAt?: Timestamp;
    /**
     * @generated from protobuf field: string title = 3;
     */
    title: string;
    /**
     * @generated from protobuf field: string title_emoji = 4;
     */
    titleEmoji: string;
    /**
     * @generated from protobuf field: ColorTypeProto color = 8;
     */
    color: ColorTypeProto;
    /**
     * @generated from protobuf field: string blurb = 5;
     */
    blurb: string;
    /**
     * @generated from protobuf field: repeated string category_ids = 6;
     */
    categoryIds: string[];
    /**
     * @generated from protobuf field: repeated ReadletChapterProto chapters = 7;
     */
    chapters: ReadletChapterProto[];
}
/**
 * @generated from protobuf enum ReadletChapterType
 */
export enum ReadletChapterType {
    /**
     * @generated from protobuf enum value: READLET_CHAPTER_TYPE_UNDEFINED = 0;
     */
    UNDEFINED = 0,
    /**
     * @generated from protobuf enum value: READLET_CHAPTER_TYPE_INTRODUCTION = 1;
     */
    INTRODUCTION = 1,
    /**
     * @generated from protobuf enum value: READLET_CHAPTER_TYPE_REGULAR = 2;
     */
    REGULAR = 2,
    /**
     * @generated from protobuf enum value: READLET_CHAPTER_TYPE_CONCLUSION = 3;
     */
    CONCLUSION = 3
}
// @generated message type with reflection information, may provide speed optimized methods
class ReadletApiRequestProto$Type extends MessageType<ReadletApiRequestProto> {
    constructor() {
        super("ReadletApiRequestProto", [
            { no: 1, name: "encoded_user_auth", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "get_readlets", kind: "message", oneof: "request", T: () => GetReadletsRequestProto }
        ]);
    }
    create(value?: PartialMessage<ReadletApiRequestProto>): ReadletApiRequestProto {
        const message = { encodedUserAuth: "", request: { oneofKind: undefined } };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ReadletApiRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ReadletApiRequestProto): ReadletApiRequestProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string encoded_user_auth */ 1:
                    message.encodedUserAuth = reader.string();
                    break;
                case /* GetReadletsRequestProto get_readlets */ 2:
                    message.request = {
                        oneofKind: "getReadlets",
                        getReadlets: GetReadletsRequestProto.internalBinaryRead(reader, reader.uint32(), options, (message.request as any).getReadlets)
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
    internalBinaryWrite(message: ReadletApiRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string encoded_user_auth = 1; */
        if (message.encodedUserAuth !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.encodedUserAuth);
        /* GetReadletsRequestProto get_readlets = 2; */
        if (message.request.oneofKind === "getReadlets")
            GetReadletsRequestProto.internalBinaryWrite(message.request.getReadlets, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ReadletApiRequestProto
 */
export const ReadletApiRequestProto = new ReadletApiRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ReadletApiResponseProto$Type extends MessageType<ReadletApiResponseProto> {
    constructor() {
        super("ReadletApiResponseProto", [
            { no: 1, name: "refreshed_encoded_user_auth", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "get_readlets", kind: "message", oneof: "response", T: () => GetReadletsResponseProto },
            { no: 100, name: "latencies", kind: "map", K: 9 /*ScalarType.STRING*/, V: { kind: "message", T: () => Duration } }
        ]);
    }
    create(value?: PartialMessage<ReadletApiResponseProto>): ReadletApiResponseProto {
        const message = { refreshedEncodedUserAuth: "", response: { oneofKind: undefined }, latencies: {} };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ReadletApiResponseProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ReadletApiResponseProto): ReadletApiResponseProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string refreshed_encoded_user_auth */ 1:
                    message.refreshedEncodedUserAuth = reader.string();
                    break;
                case /* GetReadletsResponseProto get_readlets */ 2:
                    message.response = {
                        oneofKind: "getReadlets",
                        getReadlets: GetReadletsResponseProto.internalBinaryRead(reader, reader.uint32(), options, (message.response as any).getReadlets)
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
    private binaryReadMap100(map: ReadletApiResponseProto["latencies"], reader: IBinaryReader, options: BinaryReadOptions): void {
        let len = reader.uint32(), end = reader.pos + len, key: keyof ReadletApiResponseProto["latencies"] | undefined, val: ReadletApiResponseProto["latencies"][any] | undefined;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case 1:
                    key = reader.string();
                    break;
                case 2:
                    val = Duration.internalBinaryRead(reader, reader.uint32(), options);
                    break;
                default: throw new globalThis.Error("unknown map entry field for field ReadletApiResponseProto.latencies");
            }
        }
        map[key ?? ""] = val ?? Duration.create();
    }
    internalBinaryWrite(message: ReadletApiResponseProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string refreshed_encoded_user_auth = 1; */
        if (message.refreshedEncodedUserAuth !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.refreshedEncodedUserAuth);
        /* GetReadletsResponseProto get_readlets = 2; */
        if (message.response.oneofKind === "getReadlets")
            GetReadletsResponseProto.internalBinaryWrite(message.response.getReadlets, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* map<string, google.protobuf.Duration> latencies = 100; */
        for (let k of Object.keys(message.latencies)) {
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
 * @generated MessageType for protobuf message ReadletApiResponseProto
 */
export const ReadletApiResponseProto = new ReadletApiResponseProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class GetReadletsRequestProto$Type extends MessageType<GetReadletsRequestProto> {
    constructor() {
        super("GetReadletsRequestProto", [
            { no: 1, name: "category_filter", kind: "scalar", repeat: 2 /*RepeatType.UNPACKED*/, T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<GetReadletsRequestProto>): GetReadletsRequestProto {
        const message = { categoryFilter: [] };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<GetReadletsRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: GetReadletsRequestProto): GetReadletsRequestProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* repeated string category_filter */ 1:
                    message.categoryFilter.push(reader.string());
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
    internalBinaryWrite(message: GetReadletsRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* repeated string category_filter = 1; */
        for (let i = 0; i < message.categoryFilter.length; i++)
            writer.tag(1, WireType.LengthDelimited).string(message.categoryFilter[i]);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message GetReadletsRequestProto
 */
export const GetReadletsRequestProto = new GetReadletsRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class GetReadletsResponseProto$Type extends MessageType<GetReadletsResponseProto> {
    constructor() {
        super("GetReadletsResponseProto", [
            { no: 1, name: "readlets", kind: "message", repeat: 1 /*RepeatType.PACKED*/, T: () => ReadletProto },
            { no: 2, name: "available_categories", kind: "message", repeat: 1 /*RepeatType.PACKED*/, T: () => ReadletCategoryProto }
        ]);
    }
    create(value?: PartialMessage<GetReadletsResponseProto>): GetReadletsResponseProto {
        const message = { readlets: [], availableCategories: [] };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<GetReadletsResponseProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: GetReadletsResponseProto): GetReadletsResponseProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* repeated ReadletProto readlets */ 1:
                    message.readlets.push(ReadletProto.internalBinaryRead(reader, reader.uint32(), options));
                    break;
                case /* repeated ReadletCategoryProto available_categories */ 2:
                    message.availableCategories.push(ReadletCategoryProto.internalBinaryRead(reader, reader.uint32(), options));
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
    internalBinaryWrite(message: GetReadletsResponseProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* repeated ReadletProto readlets = 1; */
        for (let i = 0; i < message.readlets.length; i++)
            ReadletProto.internalBinaryWrite(message.readlets[i], writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        /* repeated ReadletCategoryProto available_categories = 2; */
        for (let i = 0; i < message.availableCategories.length; i++)
            ReadletCategoryProto.internalBinaryWrite(message.availableCategories[i], writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message GetReadletsResponseProto
 */
export const GetReadletsResponseProto = new GetReadletsResponseProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ReadletsCacheProto$Type extends MessageType<ReadletsCacheProto> {
    constructor() {
        super("ReadletsCacheProto", [
            { no: 1, name: "created_at", kind: "message", T: () => Timestamp },
            { no: 2, name: "readlets", kind: "message", repeat: 1 /*RepeatType.PACKED*/, T: () => ReadletProto }
        ]);
    }
    create(value?: PartialMessage<ReadletsCacheProto>): ReadletsCacheProto {
        const message = { readlets: [] };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ReadletsCacheProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ReadletsCacheProto): ReadletsCacheProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* google.protobuf.Timestamp created_at */ 1:
                    message.createdAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.createdAt);
                    break;
                case /* repeated ReadletProto readlets */ 2:
                    message.readlets.push(ReadletProto.internalBinaryRead(reader, reader.uint32(), options));
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
    internalBinaryWrite(message: ReadletsCacheProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* google.protobuf.Timestamp created_at = 1; */
        if (message.createdAt)
            Timestamp.internalBinaryWrite(message.createdAt, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        /* repeated ReadletProto readlets = 2; */
        for (let i = 0; i < message.readlets.length; i++)
            ReadletProto.internalBinaryWrite(message.readlets[i], writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ReadletsCacheProto
 */
export const ReadletsCacheProto = new ReadletsCacheProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ReadletCategoryProto$Type extends MessageType<ReadletCategoryProto> {
    constructor() {
        super("ReadletCategoryProto", [
            { no: 1, name: "id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "display_name", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<ReadletCategoryProto>): ReadletCategoryProto {
        const message = { id: "", displayName: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ReadletCategoryProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ReadletCategoryProto): ReadletCategoryProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string id */ 1:
                    message.id = reader.string();
                    break;
                case /* string display_name */ 2:
                    message.displayName = reader.string();
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
    internalBinaryWrite(message: ReadletCategoryProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string id = 1; */
        if (message.id !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.id);
        /* string display_name = 2; */
        if (message.displayName !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.displayName);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ReadletCategoryProto
 */
export const ReadletCategoryProto = new ReadletCategoryProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ReadletChapterProto$Type extends MessageType<ReadletChapterProto> {
    constructor() {
        super("ReadletChapterProto", [
            { no: 1, name: "type", kind: "enum", T: () => ["ReadletChapterType", ReadletChapterType, "READLET_CHAPTER_TYPE_"] },
            { no: 2, name: "title", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "subtitle", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 4, name: "text", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 5, name: "audio_path", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 6, name: "audio_duration", kind: "message", T: () => Duration }
        ]);
    }
    create(value?: PartialMessage<ReadletChapterProto>): ReadletChapterProto {
        const message = { type: 0, title: "", subtitle: "", text: "", audioPath: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ReadletChapterProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ReadletChapterProto): ReadletChapterProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* ReadletChapterType type */ 1:
                    message.type = reader.int32();
                    break;
                case /* string title */ 2:
                    message.title = reader.string();
                    break;
                case /* string subtitle */ 3:
                    message.subtitle = reader.string();
                    break;
                case /* string text */ 4:
                    message.text = reader.string();
                    break;
                case /* string audio_path */ 5:
                    message.audioPath = reader.string();
                    break;
                case /* google.protobuf.Duration audio_duration */ 6:
                    message.audioDuration = Duration.internalBinaryRead(reader, reader.uint32(), options, message.audioDuration);
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
    internalBinaryWrite(message: ReadletChapterProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* ReadletChapterType type = 1; */
        if (message.type !== 0)
            writer.tag(1, WireType.Varint).int32(message.type);
        /* string title = 2; */
        if (message.title !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.title);
        /* string subtitle = 3; */
        if (message.subtitle !== "")
            writer.tag(3, WireType.LengthDelimited).string(message.subtitle);
        /* string text = 4; */
        if (message.text !== "")
            writer.tag(4, WireType.LengthDelimited).string(message.text);
        /* string audio_path = 5; */
        if (message.audioPath !== "")
            writer.tag(5, WireType.LengthDelimited).string(message.audioPath);
        /* google.protobuf.Duration audio_duration = 6; */
        if (message.audioDuration)
            Duration.internalBinaryWrite(message.audioDuration, writer.tag(6, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ReadletChapterProto
 */
export const ReadletChapterProto = new ReadletChapterProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ReadletProto$Type extends MessageType<ReadletProto> {
    constructor() {
        super("ReadletProto", [
            { no: 1, name: "id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "created_at", kind: "message", T: () => Timestamp },
            { no: 3, name: "title", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 4, name: "title_emoji", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 8, name: "color", kind: "enum", T: () => ["ColorTypeProto", ColorTypeProto, "COLOR_TYPE_PROTO_"] },
            { no: 5, name: "blurb", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 6, name: "category_ids", kind: "scalar", repeat: 2 /*RepeatType.UNPACKED*/, T: 9 /*ScalarType.STRING*/ },
            { no: 7, name: "chapters", kind: "message", repeat: 1 /*RepeatType.PACKED*/, T: () => ReadletChapterProto }
        ]);
    }
    create(value?: PartialMessage<ReadletProto>): ReadletProto {
        const message = { id: "", title: "", titleEmoji: "", color: 0, blurb: "", categoryIds: [], chapters: [] };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ReadletProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ReadletProto): ReadletProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string id */ 1:
                    message.id = reader.string();
                    break;
                case /* google.protobuf.Timestamp created_at */ 2:
                    message.createdAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.createdAt);
                    break;
                case /* string title */ 3:
                    message.title = reader.string();
                    break;
                case /* string title_emoji */ 4:
                    message.titleEmoji = reader.string();
                    break;
                case /* ColorTypeProto color */ 8:
                    message.color = reader.int32();
                    break;
                case /* string blurb */ 5:
                    message.blurb = reader.string();
                    break;
                case /* repeated string category_ids */ 6:
                    message.categoryIds.push(reader.string());
                    break;
                case /* repeated ReadletChapterProto chapters */ 7:
                    message.chapters.push(ReadletChapterProto.internalBinaryRead(reader, reader.uint32(), options));
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
    internalBinaryWrite(message: ReadletProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string id = 1; */
        if (message.id !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.id);
        /* google.protobuf.Timestamp created_at = 2; */
        if (message.createdAt)
            Timestamp.internalBinaryWrite(message.createdAt, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* string title = 3; */
        if (message.title !== "")
            writer.tag(3, WireType.LengthDelimited).string(message.title);
        /* string title_emoji = 4; */
        if (message.titleEmoji !== "")
            writer.tag(4, WireType.LengthDelimited).string(message.titleEmoji);
        /* ColorTypeProto color = 8; */
        if (message.color !== 0)
            writer.tag(8, WireType.Varint).int32(message.color);
        /* string blurb = 5; */
        if (message.blurb !== "")
            writer.tag(5, WireType.LengthDelimited).string(message.blurb);
        /* repeated string category_ids = 6; */
        for (let i = 0; i < message.categoryIds.length; i++)
            writer.tag(6, WireType.LengthDelimited).string(message.categoryIds[i]);
        /* repeated ReadletChapterProto chapters = 7; */
        for (let i = 0; i < message.chapters.length; i++)
            ReadletChapterProto.internalBinaryWrite(message.chapters[i], writer.tag(7, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ReadletProto
 */
export const ReadletProto = new ReadletProto$Type();
