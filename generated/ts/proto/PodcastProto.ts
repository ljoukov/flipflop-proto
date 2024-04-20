/* eslint-disable */
// @generated by protobuf-ts 2.9.1 with parameter eslint_disable,long_type_string,ts_nocheck
// @generated from protobuf file "PodcastProto.proto" (syntax proto3)
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
import { Timestamp } from "./google/protobuf/timestamp";
import { Duration } from "./google/protobuf/duration";
/**
 * @generated from protobuf message PodcastStreamApiRequestProto
 */
export interface PodcastStreamApiRequestProto {
    /**
     * @generated from protobuf field: string encoded_user_auth = 1;
     */
    encodedUserAuth: string;
    /**
     * @generated from protobuf oneof: request
     */
    request: {
        oneofKind: "createPlan";
        /**
         * @generated from protobuf field: CreatePodcastPlanRequestProto create_plan = 2;
         */
        createPlan: CreatePodcastPlanRequestProto;
    } | {
        oneofKind: undefined;
    };
}
/**
 * @generated from protobuf message PodcastStreamApiResponseHeaderProto
 */
export interface PodcastStreamApiResponseHeaderProto {
    /**
     * If present the token was refreshed and the client should use this new one
     * from now onwards.
     *
     * @generated from protobuf field: string refreshed_encoded_user_auth = 1;
     */
    refreshedEncodedUserAuth: string;
    /**
     * @generated from protobuf oneof: header
     */
    header: {
        oneofKind: "createPlanHeader";
        /**
         * @generated from protobuf field: CreatePodcastPlanResponseHeaderProto create_plan_header = 2;
         */
        createPlanHeader: CreatePodcastPlanResponseHeaderProto;
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
 * @generated from protobuf message PodcastStreamApiResponseDeltaProto
 */
export interface PodcastStreamApiResponseDeltaProto {
    /**
     * @generated from protobuf oneof: response_delta
     */
    responseDelta: {
        oneofKind: "createPlanDelta";
        /**
         * @generated from protobuf field: CreatePodcastPlanResponseDeltaProto create_plan_delta = 1;
         */
        createPlanDelta: CreatePodcastPlanResponseDeltaProto;
    } | {
        oneofKind: undefined;
    };
}
/**
 * @generated from protobuf message CreatePodcastPlanRequestProto
 */
export interface CreatePodcastPlanRequestProto {
    /**
     * @generated from protobuf field: string prompt = 1;
     */
    prompt: string;
}
/**
 * @generated from protobuf message CreatePodcastPlanResponseHeaderProto
 */
export interface CreatePodcastPlanResponseHeaderProto {
}
/**
 * @generated from protobuf message CreatePodcastPlanResponseDeltaProto
 */
export interface CreatePodcastPlanResponseDeltaProto {
    /**
     * @generated from protobuf oneof: type
     */
    type: {
        oneofKind: "separator";
        /**
         * @generated from protobuf field: bool separator = 1;
         */
        separator: boolean;
    } | {
        oneofKind: "errorNoTopic";
        /**
         * This is the last delta message
         *
         * @generated from protobuf field: bool error_no_topic = 2;
         */
        errorNoTopic: boolean;
    } | {
        oneofKind: "planDelta";
        /**
         * IDs start at 10
         *
         * @generated from protobuf field: PodcastPlanProto plan_delta = 10;
         */
        planDelta: PodcastPlanProto;
    } | {
        oneofKind: undefined;
    };
}
/**
 * @generated from protobuf message PodcastPlanProto
 */
export interface PodcastPlanProto {
    /**
     * @generated from protobuf field: string id = 1;
     */
    id: string;
    /**
     * @generated from protobuf field: string created_by = 2;
     */
    createdBy: string;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp created_at = 3;
     */
    createdAt?: Timestamp;
    /**
     * ID starts at 10
     *
     * @generated from protobuf field: string title = 10;
     */
    title: string;
    /**
     * @generated from protobuf field: string title_emoji = 11;
     */
    titleEmoji: string;
    /**
     * @generated from protobuf field: string hook = 12;
     */
    hook: string;
    /**
     * @generated from protobuf field: repeated string segments = 13;
     */
    segments: string[];
}
// @generated message type with reflection information, may provide speed optimized methods
class PodcastStreamApiRequestProto$Type extends MessageType<PodcastStreamApiRequestProto> {
    constructor() {
        super("PodcastStreamApiRequestProto", [
            { no: 1, name: "encoded_user_auth", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "create_plan", kind: "message", oneof: "request", T: () => CreatePodcastPlanRequestProto }
        ]);
    }
    create(value?: PartialMessage<PodcastStreamApiRequestProto>): PodcastStreamApiRequestProto {
        const message = { encodedUserAuth: "", request: { oneofKind: undefined } };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<PodcastStreamApiRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: PodcastStreamApiRequestProto): PodcastStreamApiRequestProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string encoded_user_auth */ 1:
                    message.encodedUserAuth = reader.string();
                    break;
                case /* CreatePodcastPlanRequestProto create_plan */ 2:
                    message.request = {
                        oneofKind: "createPlan",
                        createPlan: CreatePodcastPlanRequestProto.internalBinaryRead(reader, reader.uint32(), options, (message.request as any).createPlan)
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
    internalBinaryWrite(message: PodcastStreamApiRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string encoded_user_auth = 1; */
        if (message.encodedUserAuth !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.encodedUserAuth);
        /* CreatePodcastPlanRequestProto create_plan = 2; */
        if (message.request.oneofKind === "createPlan")
            CreatePodcastPlanRequestProto.internalBinaryWrite(message.request.createPlan, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message PodcastStreamApiRequestProto
 */
export const PodcastStreamApiRequestProto = new PodcastStreamApiRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class PodcastStreamApiResponseHeaderProto$Type extends MessageType<PodcastStreamApiResponseHeaderProto> {
    constructor() {
        super("PodcastStreamApiResponseHeaderProto", [
            { no: 1, name: "refreshed_encoded_user_auth", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "create_plan_header", kind: "message", oneof: "header", T: () => CreatePodcastPlanResponseHeaderProto },
            { no: 100, name: "latencies", kind: "map", K: 9 /*ScalarType.STRING*/, V: { kind: "message", T: () => Duration } }
        ]);
    }
    create(value?: PartialMessage<PodcastStreamApiResponseHeaderProto>): PodcastStreamApiResponseHeaderProto {
        const message = { refreshedEncodedUserAuth: "", header: { oneofKind: undefined }, latencies: {} };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<PodcastStreamApiResponseHeaderProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: PodcastStreamApiResponseHeaderProto): PodcastStreamApiResponseHeaderProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string refreshed_encoded_user_auth */ 1:
                    message.refreshedEncodedUserAuth = reader.string();
                    break;
                case /* CreatePodcastPlanResponseHeaderProto create_plan_header */ 2:
                    message.header = {
                        oneofKind: "createPlanHeader",
                        createPlanHeader: CreatePodcastPlanResponseHeaderProto.internalBinaryRead(reader, reader.uint32(), options, (message.header as any).createPlanHeader)
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
    private binaryReadMap100(map: PodcastStreamApiResponseHeaderProto["latencies"], reader: IBinaryReader, options: BinaryReadOptions): void {
        let len = reader.uint32(), end = reader.pos + len, key: keyof PodcastStreamApiResponseHeaderProto["latencies"] | undefined, val: PodcastStreamApiResponseHeaderProto["latencies"][any] | undefined;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case 1:
                    key = reader.string();
                    break;
                case 2:
                    val = Duration.internalBinaryRead(reader, reader.uint32(), options);
                    break;
                default: throw new globalThis.Error("unknown map entry field for field PodcastStreamApiResponseHeaderProto.latencies");
            }
        }
        map[key ?? ""] = val ?? Duration.create();
    }
    internalBinaryWrite(message: PodcastStreamApiResponseHeaderProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string refreshed_encoded_user_auth = 1; */
        if (message.refreshedEncodedUserAuth !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.refreshedEncodedUserAuth);
        /* CreatePodcastPlanResponseHeaderProto create_plan_header = 2; */
        if (message.header.oneofKind === "createPlanHeader")
            CreatePodcastPlanResponseHeaderProto.internalBinaryWrite(message.header.createPlanHeader, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
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
 * @generated MessageType for protobuf message PodcastStreamApiResponseHeaderProto
 */
export const PodcastStreamApiResponseHeaderProto = new PodcastStreamApiResponseHeaderProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class PodcastStreamApiResponseDeltaProto$Type extends MessageType<PodcastStreamApiResponseDeltaProto> {
    constructor() {
        super("PodcastStreamApiResponseDeltaProto", [
            { no: 1, name: "create_plan_delta", kind: "message", oneof: "responseDelta", T: () => CreatePodcastPlanResponseDeltaProto }
        ]);
    }
    create(value?: PartialMessage<PodcastStreamApiResponseDeltaProto>): PodcastStreamApiResponseDeltaProto {
        const message = { responseDelta: { oneofKind: undefined } };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<PodcastStreamApiResponseDeltaProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: PodcastStreamApiResponseDeltaProto): PodcastStreamApiResponseDeltaProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* CreatePodcastPlanResponseDeltaProto create_plan_delta */ 1:
                    message.responseDelta = {
                        oneofKind: "createPlanDelta",
                        createPlanDelta: CreatePodcastPlanResponseDeltaProto.internalBinaryRead(reader, reader.uint32(), options, (message.responseDelta as any).createPlanDelta)
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
    internalBinaryWrite(message: PodcastStreamApiResponseDeltaProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* CreatePodcastPlanResponseDeltaProto create_plan_delta = 1; */
        if (message.responseDelta.oneofKind === "createPlanDelta")
            CreatePodcastPlanResponseDeltaProto.internalBinaryWrite(message.responseDelta.createPlanDelta, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message PodcastStreamApiResponseDeltaProto
 */
export const PodcastStreamApiResponseDeltaProto = new PodcastStreamApiResponseDeltaProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class CreatePodcastPlanRequestProto$Type extends MessageType<CreatePodcastPlanRequestProto> {
    constructor() {
        super("CreatePodcastPlanRequestProto", [
            { no: 1, name: "prompt", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<CreatePodcastPlanRequestProto>): CreatePodcastPlanRequestProto {
        const message = { prompt: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<CreatePodcastPlanRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: CreatePodcastPlanRequestProto): CreatePodcastPlanRequestProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string prompt */ 1:
                    message.prompt = reader.string();
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
    internalBinaryWrite(message: CreatePodcastPlanRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string prompt = 1; */
        if (message.prompt !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.prompt);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message CreatePodcastPlanRequestProto
 */
export const CreatePodcastPlanRequestProto = new CreatePodcastPlanRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class CreatePodcastPlanResponseHeaderProto$Type extends MessageType<CreatePodcastPlanResponseHeaderProto> {
    constructor() {
        super("CreatePodcastPlanResponseHeaderProto", []);
    }
    create(value?: PartialMessage<CreatePodcastPlanResponseHeaderProto>): CreatePodcastPlanResponseHeaderProto {
        const message = {};
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<CreatePodcastPlanResponseHeaderProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: CreatePodcastPlanResponseHeaderProto): CreatePodcastPlanResponseHeaderProto {
        return target ?? this.create();
    }
    internalBinaryWrite(message: CreatePodcastPlanResponseHeaderProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message CreatePodcastPlanResponseHeaderProto
 */
export const CreatePodcastPlanResponseHeaderProto = new CreatePodcastPlanResponseHeaderProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class CreatePodcastPlanResponseDeltaProto$Type extends MessageType<CreatePodcastPlanResponseDeltaProto> {
    constructor() {
        super("CreatePodcastPlanResponseDeltaProto", [
            { no: 1, name: "separator", kind: "scalar", oneof: "type", T: 8 /*ScalarType.BOOL*/ },
            { no: 2, name: "error_no_topic", kind: "scalar", oneof: "type", T: 8 /*ScalarType.BOOL*/ },
            { no: 10, name: "plan_delta", kind: "message", oneof: "type", T: () => PodcastPlanProto }
        ]);
    }
    create(value?: PartialMessage<CreatePodcastPlanResponseDeltaProto>): CreatePodcastPlanResponseDeltaProto {
        const message = { type: { oneofKind: undefined } };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<CreatePodcastPlanResponseDeltaProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: CreatePodcastPlanResponseDeltaProto): CreatePodcastPlanResponseDeltaProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* bool separator */ 1:
                    message.type = {
                        oneofKind: "separator",
                        separator: reader.bool()
                    };
                    break;
                case /* bool error_no_topic */ 2:
                    message.type = {
                        oneofKind: "errorNoTopic",
                        errorNoTopic: reader.bool()
                    };
                    break;
                case /* PodcastPlanProto plan_delta */ 10:
                    message.type = {
                        oneofKind: "planDelta",
                        planDelta: PodcastPlanProto.internalBinaryRead(reader, reader.uint32(), options, (message.type as any).planDelta)
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
    internalBinaryWrite(message: CreatePodcastPlanResponseDeltaProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* bool separator = 1; */
        if (message.type.oneofKind === "separator")
            writer.tag(1, WireType.Varint).bool(message.type.separator);
        /* bool error_no_topic = 2; */
        if (message.type.oneofKind === "errorNoTopic")
            writer.tag(2, WireType.Varint).bool(message.type.errorNoTopic);
        /* PodcastPlanProto plan_delta = 10; */
        if (message.type.oneofKind === "planDelta")
            PodcastPlanProto.internalBinaryWrite(message.type.planDelta, writer.tag(10, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message CreatePodcastPlanResponseDeltaProto
 */
export const CreatePodcastPlanResponseDeltaProto = new CreatePodcastPlanResponseDeltaProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class PodcastPlanProto$Type extends MessageType<PodcastPlanProto> {
    constructor() {
        super("PodcastPlanProto", [
            { no: 1, name: "id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "created_by", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "created_at", kind: "message", T: () => Timestamp },
            { no: 10, name: "title", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 11, name: "title_emoji", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 12, name: "hook", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 13, name: "segments", kind: "scalar", repeat: 2 /*RepeatType.UNPACKED*/, T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<PodcastPlanProto>): PodcastPlanProto {
        const message = { id: "", createdBy: "", title: "", titleEmoji: "", hook: "", segments: [] };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<PodcastPlanProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: PodcastPlanProto): PodcastPlanProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string id */ 1:
                    message.id = reader.string();
                    break;
                case /* string created_by */ 2:
                    message.createdBy = reader.string();
                    break;
                case /* google.protobuf.Timestamp created_at */ 3:
                    message.createdAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.createdAt);
                    break;
                case /* string title */ 10:
                    message.title = reader.string();
                    break;
                case /* string title_emoji */ 11:
                    message.titleEmoji = reader.string();
                    break;
                case /* string hook */ 12:
                    message.hook = reader.string();
                    break;
                case /* repeated string segments */ 13:
                    message.segments.push(reader.string());
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
    internalBinaryWrite(message: PodcastPlanProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string id = 1; */
        if (message.id !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.id);
        /* string created_by = 2; */
        if (message.createdBy !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.createdBy);
        /* google.protobuf.Timestamp created_at = 3; */
        if (message.createdAt)
            Timestamp.internalBinaryWrite(message.createdAt, writer.tag(3, WireType.LengthDelimited).fork(), options).join();
        /* string title = 10; */
        if (message.title !== "")
            writer.tag(10, WireType.LengthDelimited).string(message.title);
        /* string title_emoji = 11; */
        if (message.titleEmoji !== "")
            writer.tag(11, WireType.LengthDelimited).string(message.titleEmoji);
        /* string hook = 12; */
        if (message.hook !== "")
            writer.tag(12, WireType.LengthDelimited).string(message.hook);
        /* repeated string segments = 13; */
        for (let i = 0; i < message.segments.length; i++)
            writer.tag(13, WireType.LengthDelimited).string(message.segments[i]);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message PodcastPlanProto
 */
export const PodcastPlanProto = new PodcastPlanProto$Type();
