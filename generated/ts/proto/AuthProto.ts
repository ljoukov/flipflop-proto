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
