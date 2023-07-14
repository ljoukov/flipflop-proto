/* eslint-disable */
// @generated by protobuf-ts 2.8.1 with parameter eslint_disable,long_type_string,ts_nocheck
// @generated from protobuf file "UserDataProto.proto" (syntax proto3)
// tslint:disable
// @ts-nocheck
import { WireType } from "@protobuf-ts/runtime";
import type { BinaryWriteOptions } from "@protobuf-ts/runtime";
import type { IBinaryWriter } from "@protobuf-ts/runtime";
import { UnknownFieldHandler } from "@protobuf-ts/runtime";
import type { BinaryReadOptions } from "@protobuf-ts/runtime";
import type { IBinaryReader } from "@protobuf-ts/runtime";
import type { PartialMessage } from "@protobuf-ts/runtime";
import { reflectionMergePartial } from "@protobuf-ts/runtime";
import { MESSAGE_TYPE } from "@protobuf-ts/runtime";
import { MessageType } from "@protobuf-ts/runtime";
import { Timestamp } from "./google/protobuf/timestamp";
import { Duration } from "./google/protobuf/duration";
/**
 * @generated from protobuf message GetUserDataRequestProto
 */
export interface GetUserDataRequestProto {
}
/**
 * @generated from protobuf message GetUserDataResponseProto
 */
export interface GetUserDataResponseProto {
    /**
     * @generated from protobuf field: UserDataProto user_data = 1;
     */
    userData?: UserDataProto;
}
/**
 * @generated from protobuf message UpdateUserDataRequestProto
 */
export interface UpdateUserDataRequestProto {
    /**
     * @generated from protobuf field: UserDataProto user_data = 1;
     */
    userData?: UserDataProto;
}
/**
 * @generated from protobuf message UpdateUserDataResponseProto
 */
export interface UpdateUserDataResponseProto {
    /**
     * @generated from protobuf field: UserDataProto user_data = 1;
     */
    userData?: UserDataProto;
}
/**
 * @generated from protobuf message UserApiRequestProto
 */
export interface UserApiRequestProto {
    /**
     * @generated from protobuf field: string encoded_user_auth = 1;
     */
    encodedUserAuth: string;
    /**
     * @generated from protobuf oneof: request
     */
    request: {
        oneofKind: "getUserData";
        /**
         * @generated from protobuf field: GetUserDataRequestProto get_user_data = 2;
         */
        getUserData: GetUserDataRequestProto;
    } | {
        oneofKind: "updateUserData";
        /**
         * @generated from protobuf field: UpdateUserDataRequestProto update_user_data = 3;
         */
        updateUserData: UpdateUserDataRequestProto;
    } | {
        oneofKind: undefined;
    };
}
/**
 * @generated from protobuf message UserApiResponseProto
 */
export interface UserApiResponseProto {
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
        oneofKind: "getUserData";
        /**
         * @generated from protobuf field: GetUserDataResponseProto get_user_data = 2;
         */
        getUserData: GetUserDataResponseProto;
    } | {
        oneofKind: "updateUserData";
        /**
         * @generated from protobuf field: UpdateUserDataResponseProto update_user_data = 3;
         */
        updateUserData: UpdateUserDataResponseProto;
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
 * @generated from protobuf message CardUserDataProto
 */
export interface CardUserDataProto {
    /**
     * @generated from protobuf field: string card_id = 1;
     */
    cardId: string;
    /**
     * For cards with "prompt" block.
     *
     * @generated from protobuf field: optional string prompt_response = 3;
     */
    promptResponse?: string;
}
/**
 * @generated from protobuf message StoryUserDataProto
 */
export interface StoryUserDataProto {
    /**
     * @generated from protobuf field: string story_id = 1;
     */
    storyId: string;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp last_modified_at = 2;
     */
    lastModifiedAt?: Timestamp;
    /**
     * @generated from protobuf field: bool liked = 3;
     */
    liked: boolean;
}
/**
 * @generated from protobuf message UserDataProto
 */
export interface UserDataProto {
    /**
     * @generated from protobuf field: string user_id = 3;
     */
    userId: string;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp created_at = 4;
     */
    createdAt?: Timestamp;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp last_modified_at = 2;
     */
    lastModifiedAt?: Timestamp;
    /**
     * @generated from protobuf field: repeated StoryUserDataProto stories_data = 1;
     */
    storiesData: StoryUserDataProto[];
}
// @generated message type with reflection information, may provide speed optimized methods
class GetUserDataRequestProto$Type extends MessageType<GetUserDataRequestProto> {
    constructor() {
        super("GetUserDataRequestProto", []);
    }
    create(value?: PartialMessage<GetUserDataRequestProto>): GetUserDataRequestProto {
        const message = {};
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<GetUserDataRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: GetUserDataRequestProto): GetUserDataRequestProto {
        return target ?? this.create();
    }
    internalBinaryWrite(message: GetUserDataRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message GetUserDataRequestProto
 */
export const GetUserDataRequestProto = new GetUserDataRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class GetUserDataResponseProto$Type extends MessageType<GetUserDataResponseProto> {
    constructor() {
        super("GetUserDataResponseProto", [
            { no: 1, name: "user_data", kind: "message", T: () => UserDataProto }
        ]);
    }
    create(value?: PartialMessage<GetUserDataResponseProto>): GetUserDataResponseProto {
        const message = {};
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<GetUserDataResponseProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: GetUserDataResponseProto): GetUserDataResponseProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* UserDataProto user_data */ 1:
                    message.userData = UserDataProto.internalBinaryRead(reader, reader.uint32(), options, message.userData);
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
    internalBinaryWrite(message: GetUserDataResponseProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* UserDataProto user_data = 1; */
        if (message.userData)
            UserDataProto.internalBinaryWrite(message.userData, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message GetUserDataResponseProto
 */
export const GetUserDataResponseProto = new GetUserDataResponseProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class UpdateUserDataRequestProto$Type extends MessageType<UpdateUserDataRequestProto> {
    constructor() {
        super("UpdateUserDataRequestProto", [
            { no: 1, name: "user_data", kind: "message", T: () => UserDataProto }
        ]);
    }
    create(value?: PartialMessage<UpdateUserDataRequestProto>): UpdateUserDataRequestProto {
        const message = {};
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<UpdateUserDataRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: UpdateUserDataRequestProto): UpdateUserDataRequestProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* UserDataProto user_data */ 1:
                    message.userData = UserDataProto.internalBinaryRead(reader, reader.uint32(), options, message.userData);
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
    internalBinaryWrite(message: UpdateUserDataRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* UserDataProto user_data = 1; */
        if (message.userData)
            UserDataProto.internalBinaryWrite(message.userData, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message UpdateUserDataRequestProto
 */
export const UpdateUserDataRequestProto = new UpdateUserDataRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class UpdateUserDataResponseProto$Type extends MessageType<UpdateUserDataResponseProto> {
    constructor() {
        super("UpdateUserDataResponseProto", [
            { no: 1, name: "user_data", kind: "message", T: () => UserDataProto }
        ]);
    }
    create(value?: PartialMessage<UpdateUserDataResponseProto>): UpdateUserDataResponseProto {
        const message = {};
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<UpdateUserDataResponseProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: UpdateUserDataResponseProto): UpdateUserDataResponseProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* UserDataProto user_data */ 1:
                    message.userData = UserDataProto.internalBinaryRead(reader, reader.uint32(), options, message.userData);
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
    internalBinaryWrite(message: UpdateUserDataResponseProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* UserDataProto user_data = 1; */
        if (message.userData)
            UserDataProto.internalBinaryWrite(message.userData, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message UpdateUserDataResponseProto
 */
export const UpdateUserDataResponseProto = new UpdateUserDataResponseProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class UserApiRequestProto$Type extends MessageType<UserApiRequestProto> {
    constructor() {
        super("UserApiRequestProto", [
            { no: 1, name: "encoded_user_auth", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "get_user_data", kind: "message", oneof: "request", T: () => GetUserDataRequestProto },
            { no: 3, name: "update_user_data", kind: "message", oneof: "request", T: () => UpdateUserDataRequestProto }
        ]);
    }
    create(value?: PartialMessage<UserApiRequestProto>): UserApiRequestProto {
        const message = { encodedUserAuth: "", request: { oneofKind: undefined } };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<UserApiRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: UserApiRequestProto): UserApiRequestProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string encoded_user_auth */ 1:
                    message.encodedUserAuth = reader.string();
                    break;
                case /* GetUserDataRequestProto get_user_data */ 2:
                    message.request = {
                        oneofKind: "getUserData",
                        getUserData: GetUserDataRequestProto.internalBinaryRead(reader, reader.uint32(), options, (message.request as any).getUserData)
                    };
                    break;
                case /* UpdateUserDataRequestProto update_user_data */ 3:
                    message.request = {
                        oneofKind: "updateUserData",
                        updateUserData: UpdateUserDataRequestProto.internalBinaryRead(reader, reader.uint32(), options, (message.request as any).updateUserData)
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
    internalBinaryWrite(message: UserApiRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string encoded_user_auth = 1; */
        if (message.encodedUserAuth !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.encodedUserAuth);
        /* GetUserDataRequestProto get_user_data = 2; */
        if (message.request.oneofKind === "getUserData")
            GetUserDataRequestProto.internalBinaryWrite(message.request.getUserData, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* UpdateUserDataRequestProto update_user_data = 3; */
        if (message.request.oneofKind === "updateUserData")
            UpdateUserDataRequestProto.internalBinaryWrite(message.request.updateUserData, writer.tag(3, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message UserApiRequestProto
 */
export const UserApiRequestProto = new UserApiRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class UserApiResponseProto$Type extends MessageType<UserApiResponseProto> {
    constructor() {
        super("UserApiResponseProto", [
            { no: 1, name: "refreshed_encoded_user_auth", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "get_user_data", kind: "message", oneof: "response", T: () => GetUserDataResponseProto },
            { no: 3, name: "update_user_data", kind: "message", oneof: "response", T: () => UpdateUserDataResponseProto },
            { no: 100, name: "latencies", kind: "map", K: 9 /*ScalarType.STRING*/, V: { kind: "message", T: () => Duration } }
        ]);
    }
    create(value?: PartialMessage<UserApiResponseProto>): UserApiResponseProto {
        const message = { refreshedEncodedUserAuth: "", response: { oneofKind: undefined }, latencies: {} };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<UserApiResponseProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: UserApiResponseProto): UserApiResponseProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string refreshed_encoded_user_auth */ 1:
                    message.refreshedEncodedUserAuth = reader.string();
                    break;
                case /* GetUserDataResponseProto get_user_data */ 2:
                    message.response = {
                        oneofKind: "getUserData",
                        getUserData: GetUserDataResponseProto.internalBinaryRead(reader, reader.uint32(), options, (message.response as any).getUserData)
                    };
                    break;
                case /* UpdateUserDataResponseProto update_user_data */ 3:
                    message.response = {
                        oneofKind: "updateUserData",
                        updateUserData: UpdateUserDataResponseProto.internalBinaryRead(reader, reader.uint32(), options, (message.response as any).updateUserData)
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
    private binaryReadMap100(map: UserApiResponseProto["latencies"], reader: IBinaryReader, options: BinaryReadOptions): void {
        let len = reader.uint32(), end = reader.pos + len, key: keyof UserApiResponseProto["latencies"] | undefined, val: UserApiResponseProto["latencies"][any] | undefined;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case 1:
                    key = reader.string();
                    break;
                case 2:
                    val = Duration.internalBinaryRead(reader, reader.uint32(), options);
                    break;
                default: throw new globalThis.Error("unknown map entry field for field UserApiResponseProto.latencies");
            }
        }
        map[key ?? ""] = val ?? Duration.create();
    }
    internalBinaryWrite(message: UserApiResponseProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string refreshed_encoded_user_auth = 1; */
        if (message.refreshedEncodedUserAuth !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.refreshedEncodedUserAuth);
        /* GetUserDataResponseProto get_user_data = 2; */
        if (message.response.oneofKind === "getUserData")
            GetUserDataResponseProto.internalBinaryWrite(message.response.getUserData, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* UpdateUserDataResponseProto update_user_data = 3; */
        if (message.response.oneofKind === "updateUserData")
            UpdateUserDataResponseProto.internalBinaryWrite(message.response.updateUserData, writer.tag(3, WireType.LengthDelimited).fork(), options).join();
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
 * @generated MessageType for protobuf message UserApiResponseProto
 */
export const UserApiResponseProto = new UserApiResponseProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class CardUserDataProto$Type extends MessageType<CardUserDataProto> {
    constructor() {
        super("CardUserDataProto", [
            { no: 1, name: "card_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "prompt_response", kind: "scalar", opt: true, T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<CardUserDataProto>): CardUserDataProto {
        const message = { cardId: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<CardUserDataProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: CardUserDataProto): CardUserDataProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string card_id */ 1:
                    message.cardId = reader.string();
                    break;
                case /* optional string prompt_response */ 3:
                    message.promptResponse = reader.string();
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
    internalBinaryWrite(message: CardUserDataProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string card_id = 1; */
        if (message.cardId !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.cardId);
        /* optional string prompt_response = 3; */
        if (message.promptResponse !== undefined)
            writer.tag(3, WireType.LengthDelimited).string(message.promptResponse);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message CardUserDataProto
 */
export const CardUserDataProto = new CardUserDataProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class StoryUserDataProto$Type extends MessageType<StoryUserDataProto> {
    constructor() {
        super("StoryUserDataProto", [
            { no: 1, name: "story_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "last_modified_at", kind: "message", T: () => Timestamp },
            { no: 3, name: "liked", kind: "scalar", T: 8 /*ScalarType.BOOL*/ }
        ]);
    }
    create(value?: PartialMessage<StoryUserDataProto>): StoryUserDataProto {
        const message = { storyId: "", liked: false };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<StoryUserDataProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: StoryUserDataProto): StoryUserDataProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string story_id */ 1:
                    message.storyId = reader.string();
                    break;
                case /* google.protobuf.Timestamp last_modified_at */ 2:
                    message.lastModifiedAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.lastModifiedAt);
                    break;
                case /* bool liked */ 3:
                    message.liked = reader.bool();
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
    internalBinaryWrite(message: StoryUserDataProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string story_id = 1; */
        if (message.storyId !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.storyId);
        /* google.protobuf.Timestamp last_modified_at = 2; */
        if (message.lastModifiedAt)
            Timestamp.internalBinaryWrite(message.lastModifiedAt, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* bool liked = 3; */
        if (message.liked !== false)
            writer.tag(3, WireType.Varint).bool(message.liked);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message StoryUserDataProto
 */
export const StoryUserDataProto = new StoryUserDataProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class UserDataProto$Type extends MessageType<UserDataProto> {
    constructor() {
        super("UserDataProto", [
            { no: 3, name: "user_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 4, name: "created_at", kind: "message", T: () => Timestamp },
            { no: 2, name: "last_modified_at", kind: "message", T: () => Timestamp },
            { no: 1, name: "stories_data", kind: "message", repeat: 1 /*RepeatType.PACKED*/, T: () => StoryUserDataProto }
        ]);
    }
    create(value?: PartialMessage<UserDataProto>): UserDataProto {
        const message = { userId: "", storiesData: [] };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<UserDataProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: UserDataProto): UserDataProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string user_id */ 3:
                    message.userId = reader.string();
                    break;
                case /* google.protobuf.Timestamp created_at */ 4:
                    message.createdAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.createdAt);
                    break;
                case /* google.protobuf.Timestamp last_modified_at */ 2:
                    message.lastModifiedAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.lastModifiedAt);
                    break;
                case /* repeated StoryUserDataProto stories_data */ 1:
                    message.storiesData.push(StoryUserDataProto.internalBinaryRead(reader, reader.uint32(), options));
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
    internalBinaryWrite(message: UserDataProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string user_id = 3; */
        if (message.userId !== "")
            writer.tag(3, WireType.LengthDelimited).string(message.userId);
        /* google.protobuf.Timestamp created_at = 4; */
        if (message.createdAt)
            Timestamp.internalBinaryWrite(message.createdAt, writer.tag(4, WireType.LengthDelimited).fork(), options).join();
        /* google.protobuf.Timestamp last_modified_at = 2; */
        if (message.lastModifiedAt)
            Timestamp.internalBinaryWrite(message.lastModifiedAt, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* repeated StoryUserDataProto stories_data = 1; */
        for (let i = 0; i < message.storiesData.length; i++)
            StoryUserDataProto.internalBinaryWrite(message.storiesData[i], writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message UserDataProto
 */
export const UserDataProto = new UserDataProto$Type();
