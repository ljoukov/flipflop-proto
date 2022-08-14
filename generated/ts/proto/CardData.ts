// @generated by protobuf-ts 2.7.0
// @generated from protobuf file "CardData.proto" (syntax proto3)
// tslint:disable
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
 * @generated from protobuf message StoryData
 */
export interface StoryData {
    /**
     * @generated from protobuf field: string id = 1;
     */
    id: string;
    /**
     * @generated from protobuf field: string createdBy = 2;
     */
    createdBy: string;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp createdAt = 3;
     */
    createdAt?: Timestamp;
    /**
     * @generated from protobuf field: string lastModifiedBy = 4;
     */
    lastModifiedBy: string;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp lastModifiedAt = 5;
     */
    lastModifiedAt?: Timestamp;
    /**
     * @generated from protobuf field: string title = 6;
     */
    title: string;
    /**
     * @generated from protobuf field: repeated CardData cards = 7;
     */
    cards: CardData[];
}
/**
 * @generated from protobuf message CardData
 */
export interface CardData {
    /**
     * @generated from protobuf field: repeated CardBlockData blocks = 1;
     */
    blocks: CardBlockData[];
    /**
     * @generated from protobuf field: repeated string hashTags = 2;
     */
    hashTags: string[];
}
/**
 * @generated from protobuf message CardBlockData
 */
export interface CardBlockData {
    /**
     * @generated from protobuf oneof: type
     */
    type: {
        oneofKind: "space";
        /**
         * @generated from protobuf field: SpaceBlockData space = 1;
         */
        space: SpaceBlockData;
    } | {
        oneofKind: "image";
        /**
         * @generated from protobuf field: ImageBlockData image = 2;
         */
        image: ImageBlockData;
    } | {
        oneofKind: undefined;
    };
}
/**
 * @generated from protobuf message SpaceBlockData
 */
export interface SpaceBlockData {
    /**
     * @generated from protobuf field: float scale = 1;
     */
    scale: number;
}
/**
 * @generated from protobuf message ImageBlockData
 */
export interface ImageBlockData {
    /**
     * @generated from protobuf field: float scale = 1;
     */
    scale: number;
}
// @generated message type with reflection information, may provide speed optimized methods
class StoryData$Type extends MessageType<StoryData> {
    constructor() {
        super("StoryData", [
            { no: 1, name: "id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "createdBy", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "createdAt", kind: "message", T: () => Timestamp },
            { no: 4, name: "lastModifiedBy", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 5, name: "lastModifiedAt", kind: "message", T: () => Timestamp },
            { no: 6, name: "title", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 7, name: "cards", kind: "message", repeat: 1 /*RepeatType.PACKED*/, T: () => CardData }
        ]);
    }
    create(value?: PartialMessage<StoryData>): StoryData {
        const message = { id: "", createdBy: "", lastModifiedBy: "", title: "", cards: [] };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<StoryData>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: StoryData): StoryData {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string id */ 1:
                    message.id = reader.string();
                    break;
                case /* string createdBy */ 2:
                    message.createdBy = reader.string();
                    break;
                case /* google.protobuf.Timestamp createdAt */ 3:
                    message.createdAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.createdAt);
                    break;
                case /* string lastModifiedBy */ 4:
                    message.lastModifiedBy = reader.string();
                    break;
                case /* google.protobuf.Timestamp lastModifiedAt */ 5:
                    message.lastModifiedAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.lastModifiedAt);
                    break;
                case /* string title */ 6:
                    message.title = reader.string();
                    break;
                case /* repeated CardData cards */ 7:
                    message.cards.push(CardData.internalBinaryRead(reader, reader.uint32(), options));
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
    internalBinaryWrite(message: StoryData, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string id = 1; */
        if (message.id !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.id);
        /* string createdBy = 2; */
        if (message.createdBy !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.createdBy);
        /* google.protobuf.Timestamp createdAt = 3; */
        if (message.createdAt)
            Timestamp.internalBinaryWrite(message.createdAt, writer.tag(3, WireType.LengthDelimited).fork(), options).join();
        /* string lastModifiedBy = 4; */
        if (message.lastModifiedBy !== "")
            writer.tag(4, WireType.LengthDelimited).string(message.lastModifiedBy);
        /* google.protobuf.Timestamp lastModifiedAt = 5; */
        if (message.lastModifiedAt)
            Timestamp.internalBinaryWrite(message.lastModifiedAt, writer.tag(5, WireType.LengthDelimited).fork(), options).join();
        /* string title = 6; */
        if (message.title !== "")
            writer.tag(6, WireType.LengthDelimited).string(message.title);
        /* repeated CardData cards = 7; */
        for (let i = 0; i < message.cards.length; i++)
            CardData.internalBinaryWrite(message.cards[i], writer.tag(7, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message StoryData
 */
export const StoryData = new StoryData$Type();
// @generated message type with reflection information, may provide speed optimized methods
class CardData$Type extends MessageType<CardData> {
    constructor() {
        super("CardData", [
            { no: 1, name: "blocks", kind: "message", repeat: 1 /*RepeatType.PACKED*/, T: () => CardBlockData },
            { no: 2, name: "hashTags", kind: "scalar", repeat: 2 /*RepeatType.UNPACKED*/, T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<CardData>): CardData {
        const message = { blocks: [], hashTags: [] };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<CardData>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: CardData): CardData {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* repeated CardBlockData blocks */ 1:
                    message.blocks.push(CardBlockData.internalBinaryRead(reader, reader.uint32(), options));
                    break;
                case /* repeated string hashTags */ 2:
                    message.hashTags.push(reader.string());
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
    internalBinaryWrite(message: CardData, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* repeated CardBlockData blocks = 1; */
        for (let i = 0; i < message.blocks.length; i++)
            CardBlockData.internalBinaryWrite(message.blocks[i], writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        /* repeated string hashTags = 2; */
        for (let i = 0; i < message.hashTags.length; i++)
            writer.tag(2, WireType.LengthDelimited).string(message.hashTags[i]);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message CardData
 */
export const CardData = new CardData$Type();
// @generated message type with reflection information, may provide speed optimized methods
class CardBlockData$Type extends MessageType<CardBlockData> {
    constructor() {
        super("CardBlockData", [
            { no: 1, name: "space", kind: "message", oneof: "type", T: () => SpaceBlockData },
            { no: 2, name: "image", kind: "message", oneof: "type", T: () => ImageBlockData }
        ]);
    }
    create(value?: PartialMessage<CardBlockData>): CardBlockData {
        const message = { type: { oneofKind: undefined } };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<CardBlockData>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: CardBlockData): CardBlockData {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* SpaceBlockData space */ 1:
                    message.type = {
                        oneofKind: "space",
                        space: SpaceBlockData.internalBinaryRead(reader, reader.uint32(), options, (message.type as any).space)
                    };
                    break;
                case /* ImageBlockData image */ 2:
                    message.type = {
                        oneofKind: "image",
                        image: ImageBlockData.internalBinaryRead(reader, reader.uint32(), options, (message.type as any).image)
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
    internalBinaryWrite(message: CardBlockData, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* SpaceBlockData space = 1; */
        if (message.type.oneofKind === "space")
            SpaceBlockData.internalBinaryWrite(message.type.space, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        /* ImageBlockData image = 2; */
        if (message.type.oneofKind === "image")
            ImageBlockData.internalBinaryWrite(message.type.image, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message CardBlockData
 */
export const CardBlockData = new CardBlockData$Type();
// @generated message type with reflection information, may provide speed optimized methods
class SpaceBlockData$Type extends MessageType<SpaceBlockData> {
    constructor() {
        super("SpaceBlockData", [
            { no: 1, name: "scale", kind: "scalar", T: 2 /*ScalarType.FLOAT*/ }
        ]);
    }
    create(value?: PartialMessage<SpaceBlockData>): SpaceBlockData {
        const message = { scale: 0 };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<SpaceBlockData>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: SpaceBlockData): SpaceBlockData {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* float scale */ 1:
                    message.scale = reader.float();
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
    internalBinaryWrite(message: SpaceBlockData, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* float scale = 1; */
        if (message.scale !== 0)
            writer.tag(1, WireType.Bit32).float(message.scale);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message SpaceBlockData
 */
export const SpaceBlockData = new SpaceBlockData$Type();
// @generated message type with reflection information, may provide speed optimized methods
class ImageBlockData$Type extends MessageType<ImageBlockData> {
    constructor() {
        super("ImageBlockData", [
            { no: 1, name: "scale", kind: "scalar", T: 2 /*ScalarType.FLOAT*/ }
        ]);
    }
    create(value?: PartialMessage<ImageBlockData>): ImageBlockData {
        const message = { scale: 0 };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<ImageBlockData>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: ImageBlockData): ImageBlockData {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* float scale */ 1:
                    message.scale = reader.float();
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
    internalBinaryWrite(message: ImageBlockData, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* float scale = 1; */
        if (message.scale !== 0)
            writer.tag(1, WireType.Bit32).float(message.scale);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message ImageBlockData
 */
export const ImageBlockData = new ImageBlockData$Type();
