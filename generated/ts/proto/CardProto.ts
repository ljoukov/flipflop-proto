/* eslint-disable */
// @generated by protobuf-ts 2.9.1 with parameter eslint_disable,long_type_string,ts_nocheck
// @generated from protobuf file "CardProto.proto" (package "card", syntax proto3)
// tslint:disable
// @ts-nocheck
import type { BinaryWriteOptions } from "@protobuf-ts/runtime";
import type { IBinaryWriter } from "@protobuf-ts/runtime";
import { UnknownFieldHandler } from "@protobuf-ts/runtime";
import type { BinaryReadOptions } from "@protobuf-ts/runtime";
import type { IBinaryReader } from "@protobuf-ts/runtime";
import type { PartialMessage } from "@protobuf-ts/runtime";
import { reflectionMergePartial } from "@protobuf-ts/runtime";
import { MESSAGE_TYPE } from "@protobuf-ts/runtime";
import { MessageType } from "@protobuf-ts/runtime";
/**
 * @generated from protobuf message card.CardProto
 */
export interface CardProto {
}
// @generated message type with reflection information, may provide speed optimized methods
class CardProto$Type extends MessageType<CardProto> {
    constructor() {
        super("card.CardProto", []);
    }
    create(value?: PartialMessage<CardProto>): CardProto {
        const message = {};
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<CardProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: CardProto): CardProto {
        return target ?? this.create();
    }
    internalBinaryWrite(message: CardProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message card.CardProto
 */
export const CardProto = new CardProto$Type();