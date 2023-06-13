/* eslint-disable */
// @generated by protobuf-ts 2.8.1 with parameter eslint_disable,long_type_string,ts_nocheck
// @generated from protobuf file "ChatProto.proto" (syntax proto3)
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
/**
 * @generated from protobuf message ChatActivityProto
 */
export interface ChatActivityProto {
    /**
     * Machine identifier, LLM-readable, e.g. "compare-and-contrast", "writing-challenge"
     *
     * @generated from protobuf field: string name = 1;
     */
    name: string;
    /**
     * How it should be diplayed to the user
     *
     * @generated from protobuf field: string display_name = 2;
     */
    displayName: string;
    /**
     * @generated from protobuf field: string description_prompt = 3;
     */
    descriptionPrompt: string;
    /**
     * @generated from protobuf field: string action_prompt = 4;
     */
    actionPrompt: string;
}
/**
 * @generated from protobuf message ChatSystemMessageProto
 */
export interface ChatSystemMessageProto {
    /**
     * @generated from protobuf field: string text = 1;
     */
    text: string;
}
/**
 * @generated from protobuf message ChatAssistantMessageProto
 */
export interface ChatAssistantMessageProto {
    /**
     * @generated from protobuf field: string text = 1;
     */
    text: string;
    /**
     * @generated from protobuf field: repeated string activity_name = 2;
     */
    activityName: string[];
}
/**
 * @generated from protobuf message ChatUserMessageProto
 */
export interface ChatUserMessageProto {
    /**
     * Explicitly entered by the user
     *
     * @generated from protobuf field: string text = 1;
     */
    text: string;
    /**
     * User selected one of the activities
     *
     * @generated from protobuf field: string action_name = 2;
     */
    actionName: string;
}
/**
 * @generated from protobuf message ChatMessageProto
 */
export interface ChatMessageProto {
    /**
     * @generated from protobuf field: google.protobuf.Timestamp created_at = 1;
     */
    createdAt?: Timestamp;
    /**
     * @generated from protobuf oneof: type
     */
    type: {
        oneofKind: "system";
        /**
         * @generated from protobuf field: ChatSystemMessageProto system = 2;
         */
        system: ChatSystemMessageProto;
    } | {
        oneofKind: "assistant";
        /**
         * @generated from protobuf field: ChatAssistantMessageProto assistant = 3;
         */
        assistant: ChatAssistantMessageProto;
    } | {
        oneofKind: "user";
        /**
         * @generated from protobuf field: ChatUserMessageProto user = 4;
         */
        user: ChatUserMessageProto;
    } | {
        oneofKind: undefined;
    };
}
// @generated message type with reflection information, may provide speed optimized methods
class ChatActivityProto$Type extends MessageType<ChatActivityProto> {
    constructor() {
        super("ChatActivityProto", [
            { no: 1, name: "name", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "display_name", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "description_prompt", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 4, name: "action_prompt", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<ChatActivityProto>): ChatActivityProto {
        const message = { name: "", displayName: "", descriptionPrompt: "", actionPrompt: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ChatActivityProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ChatActivityProto): ChatActivityProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string name */ 1:
                    message.name = reader.string();
                    break;
                case /* string display_name */ 2:
                    message.displayName = reader.string();
                    break;
                case /* string description_prompt */ 3:
                    message.descriptionPrompt = reader.string();
                    break;
                case /* string action_prompt */ 4:
                    message.actionPrompt = reader.string();
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
    internalBinaryWrite(message: ChatActivityProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string name = 1; */
        if (message.name !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.name);
        /* string display_name = 2; */
        if (message.displayName !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.displayName);
        /* string description_prompt = 3; */
        if (message.descriptionPrompt !== "")
            writer.tag(3, WireType.LengthDelimited).string(message.descriptionPrompt);
        /* string action_prompt = 4; */
        if (message.actionPrompt !== "")
            writer.tag(4, WireType.LengthDelimited).string(message.actionPrompt);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ChatActivityProto
 */
export const ChatActivityProto = new ChatActivityProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ChatSystemMessageProto$Type extends MessageType<ChatSystemMessageProto> {
    constructor() {
        super("ChatSystemMessageProto", [
            { no: 1, name: "text", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<ChatSystemMessageProto>): ChatSystemMessageProto {
        const message = { text: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ChatSystemMessageProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ChatSystemMessageProto): ChatSystemMessageProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string text */ 1:
                    message.text = reader.string();
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
    internalBinaryWrite(message: ChatSystemMessageProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string text = 1; */
        if (message.text !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.text);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ChatSystemMessageProto
 */
export const ChatSystemMessageProto = new ChatSystemMessageProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ChatAssistantMessageProto$Type extends MessageType<ChatAssistantMessageProto> {
    constructor() {
        super("ChatAssistantMessageProto", [
            { no: 1, name: "text", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "activity_name", kind: "scalar", repeat: 2 /*RepeatType.UNPACKED*/, T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<ChatAssistantMessageProto>): ChatAssistantMessageProto {
        const message = { text: "", activityName: [] };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ChatAssistantMessageProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ChatAssistantMessageProto): ChatAssistantMessageProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string text */ 1:
                    message.text = reader.string();
                    break;
                case /* repeated string activity_name */ 2:
                    message.activityName.push(reader.string());
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
    internalBinaryWrite(message: ChatAssistantMessageProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string text = 1; */
        if (message.text !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.text);
        /* repeated string activity_name = 2; */
        for (let i = 0; i < message.activityName.length; i++)
            writer.tag(2, WireType.LengthDelimited).string(message.activityName[i]);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ChatAssistantMessageProto
 */
export const ChatAssistantMessageProto = new ChatAssistantMessageProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ChatUserMessageProto$Type extends MessageType<ChatUserMessageProto> {
    constructor() {
        super("ChatUserMessageProto", [
            { no: 1, name: "text", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "action_name", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<ChatUserMessageProto>): ChatUserMessageProto {
        const message = { text: "", actionName: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ChatUserMessageProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ChatUserMessageProto): ChatUserMessageProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string text */ 1:
                    message.text = reader.string();
                    break;
                case /* string action_name */ 2:
                    message.actionName = reader.string();
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
    internalBinaryWrite(message: ChatUserMessageProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string text = 1; */
        if (message.text !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.text);
        /* string action_name = 2; */
        if (message.actionName !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.actionName);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ChatUserMessageProto
 */
export const ChatUserMessageProto = new ChatUserMessageProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ChatMessageProto$Type extends MessageType<ChatMessageProto> {
    constructor() {
        super("ChatMessageProto", [
            { no: 1, name: "created_at", kind: "message", T: () => Timestamp },
            { no: 2, name: "system", kind: "message", oneof: "type", T: () => ChatSystemMessageProto },
            { no: 3, name: "assistant", kind: "message", oneof: "type", T: () => ChatAssistantMessageProto },
            { no: 4, name: "user", kind: "message", oneof: "type", T: () => ChatUserMessageProto }
        ]);
    }
    create(value?: PartialMessage<ChatMessageProto>): ChatMessageProto {
        const message = { type: { oneofKind: undefined } };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ChatMessageProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ChatMessageProto): ChatMessageProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* google.protobuf.Timestamp created_at */ 1:
                    message.createdAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.createdAt);
                    break;
                case /* ChatSystemMessageProto system */ 2:
                    message.type = {
                        oneofKind: "system",
                        system: ChatSystemMessageProto.internalBinaryRead(reader, reader.uint32(), options, (message.type as any).system)
                    };
                    break;
                case /* ChatAssistantMessageProto assistant */ 3:
                    message.type = {
                        oneofKind: "assistant",
                        assistant: ChatAssistantMessageProto.internalBinaryRead(reader, reader.uint32(), options, (message.type as any).assistant)
                    };
                    break;
                case /* ChatUserMessageProto user */ 4:
                    message.type = {
                        oneofKind: "user",
                        user: ChatUserMessageProto.internalBinaryRead(reader, reader.uint32(), options, (message.type as any).user)
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
    internalBinaryWrite(message: ChatMessageProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* google.protobuf.Timestamp created_at = 1; */
        if (message.createdAt)
            Timestamp.internalBinaryWrite(message.createdAt, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        /* ChatSystemMessageProto system = 2; */
        if (message.type.oneofKind === "system")
            ChatSystemMessageProto.internalBinaryWrite(message.type.system, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* ChatAssistantMessageProto assistant = 3; */
        if (message.type.oneofKind === "assistant")
            ChatAssistantMessageProto.internalBinaryWrite(message.type.assistant, writer.tag(3, WireType.LengthDelimited).fork(), options).join();
        /* ChatUserMessageProto user = 4; */
        if (message.type.oneofKind === "user")
            ChatUserMessageProto.internalBinaryWrite(message.type.user, writer.tag(4, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ChatMessageProto
 */
export const ChatMessageProto = new ChatMessageProto$Type();
