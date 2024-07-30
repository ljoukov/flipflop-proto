/* eslint-disable */
// @generated by protobuf-ts 2.9.1 with parameter eslint_disable,long_type_string,ts_nocheck
// @generated from protobuf file "TaskProto.proto" (syntax proto3)
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
 * @generated from protobuf message TaskProto
 */
export interface TaskProto {
    /**
     * @generated from protobuf field: string task_id = 1;
     */
    taskId: string;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp created_at = 2;
     */
    createdAt?: Timestamp;
    /**
     * @generated from protobuf oneof: type
     */
    type: {
        oneofKind: "generatePodcast";
        /**
         * @generated from protobuf field: GeneratePodcastTaskProto generate_podcast = 10;
         */
        generatePodcast: GeneratePodcastTaskProto;
    } | {
        oneofKind: "generateSuggestions";
        /**
         * @generated from protobuf field: GeneratePodcastSuggestionsTaskProto generate_suggestions = 11;
         */
        generateSuggestions: GeneratePodcastSuggestionsTaskProto;
    } | {
        oneofKind: undefined;
    };
}
/**
 * @generated from protobuf message GeneratePodcastTaskProto
 */
export interface GeneratePodcastTaskProto {
    /**
     * @generated from protobuf field: string user_id = 1;
     */
    userId: string;
    /**
     * @generated from protobuf field: string podcast_id = 2;
     */
    podcastId: string;
    /**
     * @generated from protobuf field: repeated string point_ids = 3;
     */
    pointIds: string[];
}
/**
 * @generated from protobuf message GeneratePodcastSuggestionsTaskProto
 */
export interface GeneratePodcastSuggestionsTaskProto {
    /**
     * @generated from protobuf field: string user_id = 1;
     */
    userId: string;
}
// @generated message type with reflection information, may provide speed optimized methods
class TaskProto$Type extends MessageType<TaskProto> {
    constructor() {
        super("TaskProto", [
            { no: 1, name: "task_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "created_at", kind: "message", T: () => Timestamp },
            { no: 10, name: "generate_podcast", kind: "message", oneof: "type", T: () => GeneratePodcastTaskProto },
            { no: 11, name: "generate_suggestions", kind: "message", oneof: "type", T: () => GeneratePodcastSuggestionsTaskProto }
        ]);
    }
    create(value?: PartialMessage<TaskProto>): TaskProto {
        const message = { taskId: "", type: { oneofKind: undefined } };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<TaskProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: TaskProto): TaskProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string task_id */ 1:
                    message.taskId = reader.string();
                    break;
                case /* google.protobuf.Timestamp created_at */ 2:
                    message.createdAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.createdAt);
                    break;
                case /* GeneratePodcastTaskProto generate_podcast */ 10:
                    message.type = {
                        oneofKind: "generatePodcast",
                        generatePodcast: GeneratePodcastTaskProto.internalBinaryRead(reader, reader.uint32(), options, (message.type as any).generatePodcast)
                    };
                    break;
                case /* GeneratePodcastSuggestionsTaskProto generate_suggestions */ 11:
                    message.type = {
                        oneofKind: "generateSuggestions",
                        generateSuggestions: GeneratePodcastSuggestionsTaskProto.internalBinaryRead(reader, reader.uint32(), options, (message.type as any).generateSuggestions)
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
    internalBinaryWrite(message: TaskProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string task_id = 1; */
        if (message.taskId !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.taskId);
        /* google.protobuf.Timestamp created_at = 2; */
        if (message.createdAt)
            Timestamp.internalBinaryWrite(message.createdAt, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* GeneratePodcastTaskProto generate_podcast = 10; */
        if (message.type.oneofKind === "generatePodcast")
            GeneratePodcastTaskProto.internalBinaryWrite(message.type.generatePodcast, writer.tag(10, WireType.LengthDelimited).fork(), options).join();
        /* GeneratePodcastSuggestionsTaskProto generate_suggestions = 11; */
        if (message.type.oneofKind === "generateSuggestions")
            GeneratePodcastSuggestionsTaskProto.internalBinaryWrite(message.type.generateSuggestions, writer.tag(11, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message TaskProto
 */
export const TaskProto = new TaskProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class GeneratePodcastTaskProto$Type extends MessageType<GeneratePodcastTaskProto> {
    constructor() {
        super("GeneratePodcastTaskProto", [
            { no: 1, name: "user_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "podcast_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "point_ids", kind: "scalar", repeat: 2 /*RepeatType.UNPACKED*/, T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<GeneratePodcastTaskProto>): GeneratePodcastTaskProto {
        const message = { userId: "", podcastId: "", pointIds: [] };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<GeneratePodcastTaskProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: GeneratePodcastTaskProto): GeneratePodcastTaskProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string user_id */ 1:
                    message.userId = reader.string();
                    break;
                case /* string podcast_id */ 2:
                    message.podcastId = reader.string();
                    break;
                case /* repeated string point_ids */ 3:
                    message.pointIds.push(reader.string());
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
    internalBinaryWrite(message: GeneratePodcastTaskProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string user_id = 1; */
        if (message.userId !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.userId);
        /* string podcast_id = 2; */
        if (message.podcastId !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.podcastId);
        /* repeated string point_ids = 3; */
        for (let i = 0; i < message.pointIds.length; i++)
            writer.tag(3, WireType.LengthDelimited).string(message.pointIds[i]);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message GeneratePodcastTaskProto
 */
export const GeneratePodcastTaskProto = new GeneratePodcastTaskProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class GeneratePodcastSuggestionsTaskProto$Type extends MessageType<GeneratePodcastSuggestionsTaskProto> {
    constructor() {
        super("GeneratePodcastSuggestionsTaskProto", [
            { no: 1, name: "user_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<GeneratePodcastSuggestionsTaskProto>): GeneratePodcastSuggestionsTaskProto {
        const message = { userId: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<GeneratePodcastSuggestionsTaskProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: GeneratePodcastSuggestionsTaskProto): GeneratePodcastSuggestionsTaskProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string user_id */ 1:
                    message.userId = reader.string();
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
    internalBinaryWrite(message: GeneratePodcastSuggestionsTaskProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string user_id = 1; */
        if (message.userId !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.userId);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message GeneratePodcastSuggestionsTaskProto
 */
export const GeneratePodcastSuggestionsTaskProto = new GeneratePodcastSuggestionsTaskProto$Type();
