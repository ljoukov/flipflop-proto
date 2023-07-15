/* eslint-disable */
// @generated by protobuf-ts 2.8.1 with parameter eslint_disable,long_type_string,ts_nocheck
// @generated from protobuf file "AuthProto.proto" (syntax proto3)
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
import { Duration } from "./google/protobuf/duration";
import { Timestamp } from "./google/protobuf/timestamp";
/**
 * @generated from protobuf message UserAuthProto
 */
export interface UserAuthProto {
    /**
     * @generated from protobuf field: string user_id = 1;
     */
    userId: string;
    /**
     * @generated from protobuf field: string access_token = 2;
     */
    accessToken: string;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp expires_at = 3;
     */
    expiresAt?: Timestamp;
    /**
     * @generated from protobuf field: string refresh_token = 4;
     */
    refreshToken: string;
}
/**
 * @generated from protobuf message AuthApiRequestProto
 */
export interface AuthApiRequestProto {
    /**
     * @generated from protobuf oneof: request
     */
    request: {
        oneofKind: "signInWithIdp";
        /**
         * @generated from protobuf field: SignInWithIdpRequestProto sign_in_with_idp = 1;
         */
        signInWithIdp: SignInWithIdpRequestProto;
    } | {
        oneofKind: "signInWithPassword";
        /**
         * @generated from protobuf field: SignInWithPasswordRequestProto sign_in_with_password = 2;
         */
        signInWithPassword: SignInWithPasswordRequestProto;
    } | {
        oneofKind: undefined;
    };
}
/**
 * @generated from protobuf message AuthApiResponseProto
 */
export interface AuthApiResponseProto {
    /**
     * @generated from protobuf oneof: response
     */
    response: {
        oneofKind: "signInWithIdp";
        /**
         * @generated from protobuf field: SignInWithIdpResponseProto sign_in_with_idp = 1;
         */
        signInWithIdp: SignInWithIdpResponseProto;
    } | {
        oneofKind: "signInWithPassword";
        /**
         * @generated from protobuf field: SignInWithPasswordResponseProto sign_in_with_password = 2;
         */
        signInWithPassword: SignInWithPasswordResponseProto;
    } | {
        oneofKind: undefined;
    };
    /**
     * @generated from protobuf field: map<string, google.protobuf.Duration> latencies = 5;
     */
    latencies: {
        [key: string]: Duration;
    };
}
/**
 * @generated from protobuf message SignInWithIdpRequestProto
 */
export interface SignInWithIdpRequestProto {
    /**
     * @generated from protobuf field: string id_token = 1;
     */
    idToken: string;
    /**
     * @generated from protobuf field: string provider_id = 2;
     */
    providerId: string;
    /**
     * @generated from protobuf field: string raw_nonce = 3;
     */
    rawNonce: string;
}
/**
 * @generated from protobuf message SignInWithIdpResponseProto
 */
export interface SignInWithIdpResponseProto {
    /**
     * @generated from protobuf field: string encoded_user_auth = 1;
     */
    encodedUserAuth: string;
}
/**
 * @generated from protobuf message SignInWithPasswordRequestProto
 */
export interface SignInWithPasswordRequestProto {
    /**
     * @generated from protobuf field: string email = 1;
     */
    email: string;
    /**
     * @generated from protobuf field: string password = 2;
     */
    password: string;
}
/**
 * @generated from protobuf message SignInWithPasswordResponseProto
 */
export interface SignInWithPasswordResponseProto {
    /**
     * @generated from protobuf field: string encoded_user_auth = 1;
     */
    encodedUserAuth: string;
    /**
     * @generated from protobuf field: SignInWithPasswordResponseProto.Error error = 2;
     */
    error: SignInWithPasswordResponseProto_Error;
}
/**
 * @generated from protobuf enum SignInWithPasswordResponseProto.Error
 */
export enum SignInWithPasswordResponseProto_Error {
    /**
     * @generated from protobuf enum value: NO_ERROR = 0;
     */
    NO_ERROR = 0,
    /**
     * @generated from protobuf enum value: INVALID_PASSWORD = 1;
     */
    INVALID_PASSWORD = 1
}
// @generated message type with reflection information, may provide speed optimized methods
class UserAuthProto$Type extends MessageType<UserAuthProto> {
    constructor() {
        super("UserAuthProto", [
            { no: 1, name: "user_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "access_token", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "expires_at", kind: "message", T: () => Timestamp },
            { no: 4, name: "refresh_token", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<UserAuthProto>): UserAuthProto {
        const message = { userId: "", accessToken: "", refreshToken: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<UserAuthProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: UserAuthProto): UserAuthProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string user_id */ 1:
                    message.userId = reader.string();
                    break;
                case /* string access_token */ 2:
                    message.accessToken = reader.string();
                    break;
                case /* google.protobuf.Timestamp expires_at */ 3:
                    message.expiresAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.expiresAt);
                    break;
                case /* string refresh_token */ 4:
                    message.refreshToken = reader.string();
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
    internalBinaryWrite(message: UserAuthProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string user_id = 1; */
        if (message.userId !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.userId);
        /* string access_token = 2; */
        if (message.accessToken !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.accessToken);
        /* google.protobuf.Timestamp expires_at = 3; */
        if (message.expiresAt)
            Timestamp.internalBinaryWrite(message.expiresAt, writer.tag(3, WireType.LengthDelimited).fork(), options).join();
        /* string refresh_token = 4; */
        if (message.refreshToken !== "")
            writer.tag(4, WireType.LengthDelimited).string(message.refreshToken);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message UserAuthProto
 */
export const UserAuthProto = new UserAuthProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class AuthApiRequestProto$Type extends MessageType<AuthApiRequestProto> {
    constructor() {
        super("AuthApiRequestProto", [
            { no: 1, name: "sign_in_with_idp", kind: "message", oneof: "request", T: () => SignInWithIdpRequestProto },
            { no: 2, name: "sign_in_with_password", kind: "message", oneof: "request", T: () => SignInWithPasswordRequestProto }
        ]);
    }
    create(value?: PartialMessage<AuthApiRequestProto>): AuthApiRequestProto {
        const message = { request: { oneofKind: undefined } };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<AuthApiRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: AuthApiRequestProto): AuthApiRequestProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* SignInWithIdpRequestProto sign_in_with_idp */ 1:
                    message.request = {
                        oneofKind: "signInWithIdp",
                        signInWithIdp: SignInWithIdpRequestProto.internalBinaryRead(reader, reader.uint32(), options, (message.request as any).signInWithIdp)
                    };
                    break;
                case /* SignInWithPasswordRequestProto sign_in_with_password */ 2:
                    message.request = {
                        oneofKind: "signInWithPassword",
                        signInWithPassword: SignInWithPasswordRequestProto.internalBinaryRead(reader, reader.uint32(), options, (message.request as any).signInWithPassword)
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
    internalBinaryWrite(message: AuthApiRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* SignInWithIdpRequestProto sign_in_with_idp = 1; */
        if (message.request.oneofKind === "signInWithIdp")
            SignInWithIdpRequestProto.internalBinaryWrite(message.request.signInWithIdp, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        /* SignInWithPasswordRequestProto sign_in_with_password = 2; */
        if (message.request.oneofKind === "signInWithPassword")
            SignInWithPasswordRequestProto.internalBinaryWrite(message.request.signInWithPassword, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message AuthApiRequestProto
 */
export const AuthApiRequestProto = new AuthApiRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class AuthApiResponseProto$Type extends MessageType<AuthApiResponseProto> {
    constructor() {
        super("AuthApiResponseProto", [
            { no: 1, name: "sign_in_with_idp", kind: "message", oneof: "response", T: () => SignInWithIdpResponseProto },
            { no: 2, name: "sign_in_with_password", kind: "message", oneof: "response", T: () => SignInWithPasswordResponseProto },
            { no: 5, name: "latencies", kind: "map", K: 9 /*ScalarType.STRING*/, V: { kind: "message", T: () => Duration } }
        ]);
    }
    create(value?: PartialMessage<AuthApiResponseProto>): AuthApiResponseProto {
        const message = { response: { oneofKind: undefined }, latencies: {} };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<AuthApiResponseProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: AuthApiResponseProto): AuthApiResponseProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* SignInWithIdpResponseProto sign_in_with_idp */ 1:
                    message.response = {
                        oneofKind: "signInWithIdp",
                        signInWithIdp: SignInWithIdpResponseProto.internalBinaryRead(reader, reader.uint32(), options, (message.response as any).signInWithIdp)
                    };
                    break;
                case /* SignInWithPasswordResponseProto sign_in_with_password */ 2:
                    message.response = {
                        oneofKind: "signInWithPassword",
                        signInWithPassword: SignInWithPasswordResponseProto.internalBinaryRead(reader, reader.uint32(), options, (message.response as any).signInWithPassword)
                    };
                    break;
                case /* map<string, google.protobuf.Duration> latencies */ 5:
                    this.binaryReadMap5(message.latencies, reader, options);
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
    private binaryReadMap5(map: AuthApiResponseProto["latencies"], reader: IBinaryReader, options: BinaryReadOptions): void {
        let len = reader.uint32(), end = reader.pos + len, key: keyof AuthApiResponseProto["latencies"] | undefined, val: AuthApiResponseProto["latencies"][any] | undefined;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case 1:
                    key = reader.string();
                    break;
                case 2:
                    val = Duration.internalBinaryRead(reader, reader.uint32(), options);
                    break;
                default: throw new globalThis.Error("unknown map entry field for field AuthApiResponseProto.latencies");
            }
        }
        map[key ?? ""] = val ?? Duration.create();
    }
    internalBinaryWrite(message: AuthApiResponseProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* SignInWithIdpResponseProto sign_in_with_idp = 1; */
        if (message.response.oneofKind === "signInWithIdp")
            SignInWithIdpResponseProto.internalBinaryWrite(message.response.signInWithIdp, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        /* SignInWithPasswordResponseProto sign_in_with_password = 2; */
        if (message.response.oneofKind === "signInWithPassword")
            SignInWithPasswordResponseProto.internalBinaryWrite(message.response.signInWithPassword, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* map<string, google.protobuf.Duration> latencies = 5; */
        for (let k of Object.keys(message.latencies)) {
            writer.tag(5, WireType.LengthDelimited).fork().tag(1, WireType.LengthDelimited).string(k);
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
 * @generated MessageType for protobuf message AuthApiResponseProto
 */
export const AuthApiResponseProto = new AuthApiResponseProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class SignInWithIdpRequestProto$Type extends MessageType<SignInWithIdpRequestProto> {
    constructor() {
        super("SignInWithIdpRequestProto", [
            { no: 1, name: "id_token", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "provider_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "raw_nonce", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<SignInWithIdpRequestProto>): SignInWithIdpRequestProto {
        const message = { idToken: "", providerId: "", rawNonce: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<SignInWithIdpRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: SignInWithIdpRequestProto): SignInWithIdpRequestProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string id_token */ 1:
                    message.idToken = reader.string();
                    break;
                case /* string provider_id */ 2:
                    message.providerId = reader.string();
                    break;
                case /* string raw_nonce */ 3:
                    message.rawNonce = reader.string();
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
    internalBinaryWrite(message: SignInWithIdpRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string id_token = 1; */
        if (message.idToken !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.idToken);
        /* string provider_id = 2; */
        if (message.providerId !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.providerId);
        /* string raw_nonce = 3; */
        if (message.rawNonce !== "")
            writer.tag(3, WireType.LengthDelimited).string(message.rawNonce);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message SignInWithIdpRequestProto
 */
export const SignInWithIdpRequestProto = new SignInWithIdpRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class SignInWithIdpResponseProto$Type extends MessageType<SignInWithIdpResponseProto> {
    constructor() {
        super("SignInWithIdpResponseProto", [
            { no: 1, name: "encoded_user_auth", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<SignInWithIdpResponseProto>): SignInWithIdpResponseProto {
        const message = { encodedUserAuth: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<SignInWithIdpResponseProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: SignInWithIdpResponseProto): SignInWithIdpResponseProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string encoded_user_auth */ 1:
                    message.encodedUserAuth = reader.string();
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
    internalBinaryWrite(message: SignInWithIdpResponseProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string encoded_user_auth = 1; */
        if (message.encodedUserAuth !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.encodedUserAuth);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message SignInWithIdpResponseProto
 */
export const SignInWithIdpResponseProto = new SignInWithIdpResponseProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class SignInWithPasswordRequestProto$Type extends MessageType<SignInWithPasswordRequestProto> {
    constructor() {
        super("SignInWithPasswordRequestProto", [
            { no: 1, name: "email", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "password", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<SignInWithPasswordRequestProto>): SignInWithPasswordRequestProto {
        const message = { email: "", password: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<SignInWithPasswordRequestProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: SignInWithPasswordRequestProto): SignInWithPasswordRequestProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string email */ 1:
                    message.email = reader.string();
                    break;
                case /* string password */ 2:
                    message.password = reader.string();
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
    internalBinaryWrite(message: SignInWithPasswordRequestProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string email = 1; */
        if (message.email !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.email);
        /* string password = 2; */
        if (message.password !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.password);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message SignInWithPasswordRequestProto
 */
export const SignInWithPasswordRequestProto = new SignInWithPasswordRequestProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class SignInWithPasswordResponseProto$Type extends MessageType<SignInWithPasswordResponseProto> {
    constructor() {
        super("SignInWithPasswordResponseProto", [
            { no: 1, name: "encoded_user_auth", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "error", kind: "enum", T: () => ["SignInWithPasswordResponseProto.Error", SignInWithPasswordResponseProto_Error] }
        ]);
    }
    create(value?: PartialMessage<SignInWithPasswordResponseProto>): SignInWithPasswordResponseProto {
        const message = { encodedUserAuth: "", error: 0 };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<SignInWithPasswordResponseProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: SignInWithPasswordResponseProto): SignInWithPasswordResponseProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string encoded_user_auth */ 1:
                    message.encodedUserAuth = reader.string();
                    break;
                case /* SignInWithPasswordResponseProto.Error error */ 2:
                    message.error = reader.int32();
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
    internalBinaryWrite(message: SignInWithPasswordResponseProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string encoded_user_auth = 1; */
        if (message.encodedUserAuth !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.encodedUserAuth);
        /* SignInWithPasswordResponseProto.Error error = 2; */
        if (message.error !== 0)
            writer.tag(2, WireType.Varint).int32(message.error);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message SignInWithPasswordResponseProto
 */
export const SignInWithPasswordResponseProto = new SignInWithPasswordResponseProto$Type();
