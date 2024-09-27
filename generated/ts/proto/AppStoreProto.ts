/* eslint-disable */
// @generated by protobuf-ts 2.9.4 with parameter eslint_disable,long_type_string,ts_nocheck
// @generated from protobuf file "AppStoreProto.proto" (syntax proto3)
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
import { Timestamp } from "./google/protobuf/timestamp";
/**
 * Docs:
 * https://developer.apple.com/documentation/appstoreserverapi/jwstransactiondecodedpayload
 *
 * @generated from protobuf message AppStoreTransactionProto
 */
export interface AppStoreTransactionProto {
    /**
     * @generated from protobuf field: string original_transaction_id = 1;
     */
    originalTransactionId: string;
    /**
     * @generated from protobuf field: string transaction_id = 2;
     */
    transactionId: string;
    /**
     * @generated from protobuf field: string web_order_line_item_id = 3;
     */
    webOrderLineItemId: string;
    /**
     * @generated from protobuf field: string bundle_id = 4;
     */
    bundleId: string;
    /**
     * @generated from protobuf field: string product_id = 5;
     */
    productId: string;
    /**
     * @generated from protobuf field: string subscription_group_identifier = 6;
     */
    subscriptionGroupIdentifier: string;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp purchase_date = 7;
     */
    purchaseDate?: Timestamp;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp original_purchase_date = 8;
     */
    originalPurchaseDate?: Timestamp;
    /**
     * an auto-renewable subscription expires or renews.
     *
     * @generated from protobuf field: google.protobuf.Timestamp expires_date = 9;
     */
    expiresDate?: Timestamp;
    /**
     * The number of consumable products purchased.
     *
     * @generated from protobuf field: int32 quantity = 10;
     */
    quantity: number;
    /**
     * @generated from protobuf field: AppStorePurchaseTypeProto type = 11;
     */
    type: AppStorePurchaseTypeProto;
    /**
     * The UUID that an app optionally generates to map a customer’s in-app
     * purchase with its resulting App Store transaction.
     *
     * @generated from protobuf field: string app_account_token = 12;
     */
    appAccountToken: string;
    /**
     * A string that describes whether the transaction was purchased by the user,
     * or is available to them through Family Sharing.
     *
     * @generated from protobuf field: AppStoreInAppOwnershipTypeProto in_app_ownership_type = 13;
     */
    inAppOwnershipType: AppStoreInAppOwnershipTypeProto;
    /**
     * The time when the App Store signed the JSON Web Signature data.
     *
     * @generated from protobuf field: google.protobuf.Timestamp signed_date = 14;
     */
    signedDate?: Timestamp;
    /**
     * The reason that the App Store refunded the transaction or revoked it from
     * family sharing.
     *
     * @generated from protobuf field: AppStoreRevocationReasonProto revocation_reason = 15;
     */
    revocationReason: AppStoreRevocationReasonProto;
    /**
     * The time when Apple Support refunded a transaction.
     *
     * @generated from protobuf field: google.protobuf.Timestamp revocation_date = 16;
     */
    revocationDate?: Timestamp;
    /**
     * The Boolean value that indicates whether the user upgraded to another
     * subscription.
     *
     * @generated from protobuf field: bool is_upgraded = 17;
     */
    isUpgraded: boolean;
    /**
     * A value that represents the promotional offer type.
     *
     * @generated from protobuf field: AppStoreOfferTypeProto offer_type = 18;
     */
    offerType: AppStoreOfferTypeProto;
    /**
     * The identifier that contains the promo code or the promotional offer
     * identifier.
     *
     * @generated from protobuf field: string offer_identifier = 19;
     */
    offerIdentifier: string;
    /**
     * The server environment, either sandbox or production.
     *
     * @generated from protobuf field: AppStoreEnvironmentProto environment = 20;
     */
    environment: AppStoreEnvironmentProto;
    /**
     * The three-letter code that represents the country or region associated with
     * the App Store storefront for the purchase.
     *
     * @generated from protobuf field: string storefront = 21;
     */
    storefront: string;
    /**
     * An Apple-defined value that uniquely identifies the App Store storefront
     * associated with the purchase.
     *
     * @generated from protobuf field: string storefront_id = 22;
     */
    storefrontId: string;
    /**
     * The reason for the purchase transaction, which indicates whether it’s a
     * customer’s purchase or a renewal for an auto-renewable subscription that
     * the system initiates.
     *
     * @generated from protobuf field: AppStoreTransactionReasonProto transaction_reason = 23;
     */
    transactionReason: AppStoreTransactionReasonProto;
    /**
     * The three-letter ISO 4217 currency code for the price of the product.
     *
     * @generated from protobuf field: string currency = 24;
     */
    currency: string;
    /**
     * The price, in milliunits, of the in-app purchase or subscription offer that
     * you configured in App Store Connect.
     *
     * @generated from protobuf field: int64 price = 25;
     */
    price: string;
    /**
     * The payment mode you configure for an introductory offer, promotional
     * offer, or offer code on an auto-renewable subscription.
     *
     * @generated from protobuf field: AppStoreOfferDiscountTypeProto offer_discount_type = 26;
     */
    offerDiscountType: AppStoreOfferDiscountTypeProto;
}
/**
 * @generated from protobuf enum AppStorePurchaseTypeProto
 */
export enum AppStorePurchaseTypeProto {
    /**
     * @generated from protobuf enum value: APP_STORE_PURCHASE_TYPE_PROTO_UNSPECIFIED = 0;
     */
    UNSPECIFIED = 0,
    /**
     * @generated from protobuf enum value: APP_STORE_PURCHASE_TYPE_PROTO_AUTO_RENEWABLE_SUBSCRIPTION = 1;
     */
    AUTO_RENEWABLE_SUBSCRIPTION = 1,
    /**
     * @generated from protobuf enum value: APP_STORE_PURCHASE_TYPE_PROTO_NON_CONSUMABLE = 2;
     */
    NON_CONSUMABLE = 2,
    /**
     * @generated from protobuf enum value: APP_STORE_PURCHASE_TYPE_PROTO_CONSUMABLE = 3;
     */
    CONSUMABLE = 3,
    /**
     * @generated from protobuf enum value: APP_STORE_PURCHASE_TYPE_PROTO_NON_RENEWING_SUBSCRIPTION = 4;
     */
    NON_RENEWING_SUBSCRIPTION = 4
}
/**
 * @generated from protobuf enum AppStoreInAppOwnershipTypeProto
 */
export enum AppStoreInAppOwnershipTypeProto {
    /**
     * @generated from protobuf enum value: APP_STORE_IN_APP_OWNERSHIP_TYPE_PROTO_UNSPECIFIED = 0;
     */
    UNSPECIFIED = 0,
    /**
     * @generated from protobuf enum value: APP_STORE_IN_APP_OWNERSHIP_TYPE_PROTO_PURCHASED = 1;
     */
    PURCHASED = 1,
    /**
     * @generated from protobuf enum value: APP_STORE_IN_APP_OWNERSHIP_TYPE_PROTO_FAMILY_SHARED = 2;
     */
    FAMILY_SHARED = 2
}
/**
 * @generated from protobuf enum AppStoreRevocationReasonProto
 */
export enum AppStoreRevocationReasonProto {
    /**
     * @generated from protobuf enum value: APP_STORE_REVOCATION_REASON_PROTO_UNSPECIFIED = 0;
     */
    UNSPECIFIED = 0,
    /**
     * @generated from protobuf enum value: APP_STORE_REVOCATION_REASON_PROTO_REFUNDED_FOR_OTHER_REASON = 1;
     */
    REFUNDED_FOR_OTHER_REASON = 1,
    /**
     * @generated from protobuf enum value: APP_STORE_REVOCATION_REASON_PROTO_REFUNDED_DUE_TO_ISSUE = 2;
     */
    REFUNDED_DUE_TO_ISSUE = 2
}
/**
 * @generated from protobuf enum AppStoreOfferTypeProto
 */
export enum AppStoreOfferTypeProto {
    /**
     * @generated from protobuf enum value: APP_STORE_OFFER_TYPE_PROTO_UNSPECIFIED = 0;
     */
    UNSPECIFIED = 0,
    /**
     * @generated from protobuf enum value: APP_STORE_OFFER_TYPE_PROTO_INTRODUCTORY_OFFER = 1;
     */
    INTRODUCTORY_OFFER = 1,
    /**
     * @generated from protobuf enum value: APP_STORE_OFFER_TYPE_PROTO_PROMOTIONAL_OFFER = 2;
     */
    PROMOTIONAL_OFFER = 2,
    /**
     * @generated from protobuf enum value: APP_STORE_OFFER_TYPE_PROTO_SUBSCRIPTION_OFFER_CODE = 3;
     */
    SUBSCRIPTION_OFFER_CODE = 3,
    /**
     * @generated from protobuf enum value: APP_STORE_OFFER_TYPE_PROTO_WIN_BACK_OFFER = 4;
     */
    WIN_BACK_OFFER = 4
}
/**
 * @generated from protobuf enum AppStoreEnvironmentProto
 */
export enum AppStoreEnvironmentProto {
    /**
     * @generated from protobuf enum value: APP_STORE_ENVIRONMENT_PROTO_UNSPECIFIED = 0;
     */
    UNSPECIFIED = 0,
    /**
     * @generated from protobuf enum value: APP_STORE_ENVIRONMENT_PROTO_SANDBOX = 1;
     */
    SANDBOX = 1,
    /**
     * @generated from protobuf enum value: APP_STORE_ENVIRONMENT_PROTO_PRODUCTION = 2;
     */
    PRODUCTION = 2,
    /**
     * @generated from protobuf enum value: APP_STORE_ENVIRONMENT_PROTO_XCODE = 3;
     */
    XCODE = 3,
    /**
     * @generated from protobuf enum value: APP_STORE_ENVIRONMENT_PROTO_LOCAL_TESTING = 4;
     */
    LOCAL_TESTING = 4
}
/**
 * @generated from protobuf enum AppStoreTransactionReasonProto
 */
export enum AppStoreTransactionReasonProto {
    /**
     * @generated from protobuf enum value: APP_STORE_TRANSACTION_REASON_PROTO_UNSPECIFIED = 0;
     */
    UNSPECIFIED = 0,
    /**
     * @generated from protobuf enum value: APP_STORE_TRANSACTION_REASON_PROTO_PURCHASE = 1;
     */
    PURCHASE = 1,
    /**
     * @generated from protobuf enum value: APP_STORE_TRANSACTION_REASON_PROTO_RENEWAL = 2;
     */
    RENEWAL = 2
}
/**
 * @generated from protobuf enum AppStoreOfferDiscountTypeProto
 */
export enum AppStoreOfferDiscountTypeProto {
    /**
     * @generated from protobuf enum value: APP_STORE_OFFER_DISCOUNT_TYPE_PROTO_UNSPECIFIED = 0;
     */
    UNSPECIFIED = 0,
    /**
     * @generated from protobuf enum value: APP_STORE_OFFER_DISCOUNT_TYPE_PROTO_FREE_TRIAL = 1;
     */
    FREE_TRIAL = 1,
    /**
     * @generated from protobuf enum value: APP_STORE_OFFER_DISCOUNT_TYPE_PROTO_PAY_AS_YOU_GO = 2;
     */
    PAY_AS_YOU_GO = 2,
    /**
     * @generated from protobuf enum value: APP_STORE_OFFER_DISCOUNT_TYPE_PROTO_PAY_UP_FRONT = 3;
     */
    PAY_UP_FRONT = 3
}
// @generated message type with reflection information, may provide speed optimized methods
class AppStoreTransactionProto$Type extends MessageType<AppStoreTransactionProto> {
    constructor() {
        super("AppStoreTransactionProto", [
            { no: 1, name: "original_transaction_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "transaction_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "web_order_line_item_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 4, name: "bundle_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 5, name: "product_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 6, name: "subscription_group_identifier", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 7, name: "purchase_date", kind: "message", T: () => Timestamp },
            { no: 8, name: "original_purchase_date", kind: "message", T: () => Timestamp },
            { no: 9, name: "expires_date", kind: "message", T: () => Timestamp },
            { no: 10, name: "quantity", kind: "scalar", T: 5 /*ScalarType.INT32*/ },
            { no: 11, name: "type", kind: "enum", T: () => ["AppStorePurchaseTypeProto", AppStorePurchaseTypeProto, "APP_STORE_PURCHASE_TYPE_PROTO_"] },
            { no: 12, name: "app_account_token", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 13, name: "in_app_ownership_type", kind: "enum", T: () => ["AppStoreInAppOwnershipTypeProto", AppStoreInAppOwnershipTypeProto, "APP_STORE_IN_APP_OWNERSHIP_TYPE_PROTO_"] },
            { no: 14, name: "signed_date", kind: "message", T: () => Timestamp },
            { no: 15, name: "revocation_reason", kind: "enum", T: () => ["AppStoreRevocationReasonProto", AppStoreRevocationReasonProto, "APP_STORE_REVOCATION_REASON_PROTO_"] },
            { no: 16, name: "revocation_date", kind: "message", T: () => Timestamp },
            { no: 17, name: "is_upgraded", kind: "scalar", T: 8 /*ScalarType.BOOL*/ },
            { no: 18, name: "offer_type", kind: "enum", T: () => ["AppStoreOfferTypeProto", AppStoreOfferTypeProto, "APP_STORE_OFFER_TYPE_PROTO_"] },
            { no: 19, name: "offer_identifier", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 20, name: "environment", kind: "enum", T: () => ["AppStoreEnvironmentProto", AppStoreEnvironmentProto, "APP_STORE_ENVIRONMENT_PROTO_"] },
            { no: 21, name: "storefront", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 22, name: "storefront_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 23, name: "transaction_reason", kind: "enum", T: () => ["AppStoreTransactionReasonProto", AppStoreTransactionReasonProto, "APP_STORE_TRANSACTION_REASON_PROTO_"] },
            { no: 24, name: "currency", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 25, name: "price", kind: "scalar", T: 3 /*ScalarType.INT64*/ },
            { no: 26, name: "offer_discount_type", kind: "enum", T: () => ["AppStoreOfferDiscountTypeProto", AppStoreOfferDiscountTypeProto, "APP_STORE_OFFER_DISCOUNT_TYPE_PROTO_"] }
        ]);
    }
    create(value?: PartialMessage<AppStoreTransactionProto>): AppStoreTransactionProto {
        const message = globalThis.Object.create((this.messagePrototype!));
        message.originalTransactionId = "";
        message.transactionId = "";
        message.webOrderLineItemId = "";
        message.bundleId = "";
        message.productId = "";
        message.subscriptionGroupIdentifier = "";
        message.quantity = 0;
        message.type = 0;
        message.appAccountToken = "";
        message.inAppOwnershipType = 0;
        message.revocationReason = 0;
        message.isUpgraded = false;
        message.offerType = 0;
        message.offerIdentifier = "";
        message.environment = 0;
        message.storefront = "";
        message.storefrontId = "";
        message.transactionReason = 0;
        message.currency = "";
        message.price = "0";
        message.offerDiscountType = 0;
        if (value !== undefined)
            reflectionMergePartial<AppStoreTransactionProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: AppStoreTransactionProto): AppStoreTransactionProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string original_transaction_id */ 1:
                    message.originalTransactionId = reader.string();
                    break;
                case /* string transaction_id */ 2:
                    message.transactionId = reader.string();
                    break;
                case /* string web_order_line_item_id */ 3:
                    message.webOrderLineItemId = reader.string();
                    break;
                case /* string bundle_id */ 4:
                    message.bundleId = reader.string();
                    break;
                case /* string product_id */ 5:
                    message.productId = reader.string();
                    break;
                case /* string subscription_group_identifier */ 6:
                    message.subscriptionGroupIdentifier = reader.string();
                    break;
                case /* google.protobuf.Timestamp purchase_date */ 7:
                    message.purchaseDate = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.purchaseDate);
                    break;
                case /* google.protobuf.Timestamp original_purchase_date */ 8:
                    message.originalPurchaseDate = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.originalPurchaseDate);
                    break;
                case /* google.protobuf.Timestamp expires_date */ 9:
                    message.expiresDate = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.expiresDate);
                    break;
                case /* int32 quantity */ 10:
                    message.quantity = reader.int32();
                    break;
                case /* AppStorePurchaseTypeProto type */ 11:
                    message.type = reader.int32();
                    break;
                case /* string app_account_token */ 12:
                    message.appAccountToken = reader.string();
                    break;
                case /* AppStoreInAppOwnershipTypeProto in_app_ownership_type */ 13:
                    message.inAppOwnershipType = reader.int32();
                    break;
                case /* google.protobuf.Timestamp signed_date */ 14:
                    message.signedDate = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.signedDate);
                    break;
                case /* AppStoreRevocationReasonProto revocation_reason */ 15:
                    message.revocationReason = reader.int32();
                    break;
                case /* google.protobuf.Timestamp revocation_date */ 16:
                    message.revocationDate = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.revocationDate);
                    break;
                case /* bool is_upgraded */ 17:
                    message.isUpgraded = reader.bool();
                    break;
                case /* AppStoreOfferTypeProto offer_type */ 18:
                    message.offerType = reader.int32();
                    break;
                case /* string offer_identifier */ 19:
                    message.offerIdentifier = reader.string();
                    break;
                case /* AppStoreEnvironmentProto environment */ 20:
                    message.environment = reader.int32();
                    break;
                case /* string storefront */ 21:
                    message.storefront = reader.string();
                    break;
                case /* string storefront_id */ 22:
                    message.storefrontId = reader.string();
                    break;
                case /* AppStoreTransactionReasonProto transaction_reason */ 23:
                    message.transactionReason = reader.int32();
                    break;
                case /* string currency */ 24:
                    message.currency = reader.string();
                    break;
                case /* int64 price */ 25:
                    message.price = reader.int64().toString();
                    break;
                case /* AppStoreOfferDiscountTypeProto offer_discount_type */ 26:
                    message.offerDiscountType = reader.int32();
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
    internalBinaryWrite(message: AppStoreTransactionProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string original_transaction_id = 1; */
        if (message.originalTransactionId !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.originalTransactionId);
        /* string transaction_id = 2; */
        if (message.transactionId !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.transactionId);
        /* string web_order_line_item_id = 3; */
        if (message.webOrderLineItemId !== "")
            writer.tag(3, WireType.LengthDelimited).string(message.webOrderLineItemId);
        /* string bundle_id = 4; */
        if (message.bundleId !== "")
            writer.tag(4, WireType.LengthDelimited).string(message.bundleId);
        /* string product_id = 5; */
        if (message.productId !== "")
            writer.tag(5, WireType.LengthDelimited).string(message.productId);
        /* string subscription_group_identifier = 6; */
        if (message.subscriptionGroupIdentifier !== "")
            writer.tag(6, WireType.LengthDelimited).string(message.subscriptionGroupIdentifier);
        /* google.protobuf.Timestamp purchase_date = 7; */
        if (message.purchaseDate)
            Timestamp.internalBinaryWrite(message.purchaseDate, writer.tag(7, WireType.LengthDelimited).fork(), options).join();
        /* google.protobuf.Timestamp original_purchase_date = 8; */
        if (message.originalPurchaseDate)
            Timestamp.internalBinaryWrite(message.originalPurchaseDate, writer.tag(8, WireType.LengthDelimited).fork(), options).join();
        /* google.protobuf.Timestamp expires_date = 9; */
        if (message.expiresDate)
            Timestamp.internalBinaryWrite(message.expiresDate, writer.tag(9, WireType.LengthDelimited).fork(), options).join();
        /* int32 quantity = 10; */
        if (message.quantity !== 0)
            writer.tag(10, WireType.Varint).int32(message.quantity);
        /* AppStorePurchaseTypeProto type = 11; */
        if (message.type !== 0)
            writer.tag(11, WireType.Varint).int32(message.type);
        /* string app_account_token = 12; */
        if (message.appAccountToken !== "")
            writer.tag(12, WireType.LengthDelimited).string(message.appAccountToken);
        /* AppStoreInAppOwnershipTypeProto in_app_ownership_type = 13; */
        if (message.inAppOwnershipType !== 0)
            writer.tag(13, WireType.Varint).int32(message.inAppOwnershipType);
        /* google.protobuf.Timestamp signed_date = 14; */
        if (message.signedDate)
            Timestamp.internalBinaryWrite(message.signedDate, writer.tag(14, WireType.LengthDelimited).fork(), options).join();
        /* AppStoreRevocationReasonProto revocation_reason = 15; */
        if (message.revocationReason !== 0)
            writer.tag(15, WireType.Varint).int32(message.revocationReason);
        /* google.protobuf.Timestamp revocation_date = 16; */
        if (message.revocationDate)
            Timestamp.internalBinaryWrite(message.revocationDate, writer.tag(16, WireType.LengthDelimited).fork(), options).join();
        /* bool is_upgraded = 17; */
        if (message.isUpgraded !== false)
            writer.tag(17, WireType.Varint).bool(message.isUpgraded);
        /* AppStoreOfferTypeProto offer_type = 18; */
        if (message.offerType !== 0)
            writer.tag(18, WireType.Varint).int32(message.offerType);
        /* string offer_identifier = 19; */
        if (message.offerIdentifier !== "")
            writer.tag(19, WireType.LengthDelimited).string(message.offerIdentifier);
        /* AppStoreEnvironmentProto environment = 20; */
        if (message.environment !== 0)
            writer.tag(20, WireType.Varint).int32(message.environment);
        /* string storefront = 21; */
        if (message.storefront !== "")
            writer.tag(21, WireType.LengthDelimited).string(message.storefront);
        /* string storefront_id = 22; */
        if (message.storefrontId !== "")
            writer.tag(22, WireType.LengthDelimited).string(message.storefrontId);
        /* AppStoreTransactionReasonProto transaction_reason = 23; */
        if (message.transactionReason !== 0)
            writer.tag(23, WireType.Varint).int32(message.transactionReason);
        /* string currency = 24; */
        if (message.currency !== "")
            writer.tag(24, WireType.LengthDelimited).string(message.currency);
        /* int64 price = 25; */
        if (message.price !== "0")
            writer.tag(25, WireType.Varint).int64(message.price);
        /* AppStoreOfferDiscountTypeProto offer_discount_type = 26; */
        if (message.offerDiscountType !== 0)
            writer.tag(26, WireType.Varint).int32(message.offerDiscountType);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message AppStoreTransactionProto
 */
export const AppStoreTransactionProto = new AppStoreTransactionProto$Type();
