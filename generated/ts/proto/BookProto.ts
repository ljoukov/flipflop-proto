/* eslint-disable */
// @generated by protobuf-ts 2.9.1 with parameter eslint_disable,long_type_string,ts_nocheck
// @generated from protobuf file "BookProto.proto" (syntax proto3)
// tslint:disable
// @ts-nocheck
import type { BinaryWriteOptions } from "@protobuf-ts/runtime";
import type { IBinaryWriter } from "@protobuf-ts/runtime";
import type { BinaryReadOptions } from "@protobuf-ts/runtime";
import type { IBinaryReader } from "@protobuf-ts/runtime";
import { UnknownFieldHandler } from "@protobuf-ts/runtime";
import { WireType } from "@protobuf-ts/runtime";
import type { PartialMessage } from "@protobuf-ts/runtime";
import { reflectionMergePartial } from "@protobuf-ts/runtime";
import { MESSAGE_TYPE } from "@protobuf-ts/runtime";
import { MessageType } from "@protobuf-ts/runtime";
import { Duration } from "./google/protobuf/duration";
import { Timestamp } from "./google/protobuf/timestamp";
/**
 * @generated from protobuf message BookProto
 */
export interface BookProto {
    /**
     * @generated from protobuf field: string id = 1;
     */
    id: string;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp published_at = 2;
     */
    publishedAt?: Timestamp;
    /**
     * @generated from protobuf field: string title = 3;
     */
    title: string;
    /**
     * @generated from protobuf field: string subtitle = 4;
     */
    subtitle: string;
    /**
     * @generated from protobuf field: string about_book = 5;
     */
    aboutBook: string;
    /**
     * @generated from protobuf field: string author = 6;
     */
    author: string;
    /**
     * @generated from protobuf field: string about_author = 7;
     */
    aboutAuthor: string;
    /**
     * @generated from protobuf field: int32 num_chapters = 8;
     */
    numChapters: number;
    /**
     * @generated from protobuf field: int32 reading_minutes = 9;
     */
    readingMinutes: number;
    /**
     * @generated from protobuf field: float rating = 10;
     */
    rating: number;
    /**
     * @generated from protobuf field: int32 num_ratings = 11;
     */
    numRatings: number;
    /**
     * @generated from protobuf field: string quote = 12;
     */
    quote: string;
    /**
     * @generated from protobuf field: string language = 13;
     */
    language: string;
    /**
     * @generated from protobuf field: repeated BookCategoryProto categories = 14;
     */
    categories: BookCategoryProto[];
    /**
     * @generated from protobuf field: string target_audience = 15;
     */
    targetAudience: string;
}
/**
 * @generated from protobuf message BookAudioPart
 */
export interface BookAudioPart {
    /**
     * @generated from protobuf field: string text = 1;
     */
    text: string;
    /**
     * @generated from protobuf field: string audio_key = 2;
     */
    audioKey: string;
    /**
     * @generated from protobuf field: google.protobuf.Duration duration = 3;
     */
    duration?: Duration;
}
/**
 * @generated from protobuf message BookAudioChapter
 */
export interface BookAudioChapter {
    /**
     * @generated from protobuf field: google.protobuf.Timestamp created_at = 1;
     */
    createdAt?: Timestamp;
    /**
     * @generated from protobuf field: repeated BookAudioPart parts = 2;
     */
    parts: BookAudioPart[];
}
/**
 * @generated from protobuf message BookAudio
 */
export interface BookAudio {
    /**
     * @generated from protobuf field: string book_id = 1;
     */
    bookId: string;
    /**
     * @generated from protobuf field: google.protobuf.Timestamp updated_at = 2;
     */
    updatedAt?: Timestamp;
    /**
     * @generated from protobuf field: BookAudioChapter introduction = 3;
     */
    introduction?: BookAudioChapter;
    /**
     * @generated from protobuf field: BookAudioChapter conclusion = 4;
     */
    conclusion?: BookAudioChapter;
    /**
     * @generated from protobuf field: map<int32, BookAudioChapter> chapters = 5;
     */
    chapters: {
        [key: number]: BookAudioChapter;
    };
}
/**
 * @generated from protobuf enum BookCategoryProto
 */
export enum BookCategoryProto {
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_UNKNOWN = 0;
     */
    BOOK_CATEGORY_UNKNOWN = 0,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_ENTREPRENEURSHIP = 1;
     */
    BOOK_CATEGORY_ENTREPRENEURSHIP = 1,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_POLITICS = 2;
     */
    BOOK_CATEGORY_POLITICS = 2,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_MARKETING_AND_SALES = 3;
     */
    BOOK_CATEGORY_MARKETING_AND_SALES = 3,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_SCIENCE = 4;
     */
    BOOK_CATEGORY_SCIENCE = 4,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_HEALTH_NUTRITION = 5;
     */
    BOOK_CATEGORY_HEALTH_NUTRITION = 5,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_PERSONAL_DEVELOPMENT = 6;
     */
    BOOK_CATEGORY_PERSONAL_DEVELOPMENT = 6,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_ECONOMICS = 7;
     */
    BOOK_CATEGORY_ECONOMICS = 7,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_HISTORY = 8;
     */
    BOOK_CATEGORY_HISTORY = 8,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_COMMUNICATION_SKILLS = 9;
     */
    BOOK_CATEGORY_COMMUNICATION_SKILLS = 9,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_CORPORATE_CULTURE = 10;
     */
    BOOK_CATEGORY_CORPORATE_CULTURE = 10,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_MANAGEMENT_LEADERSHIP = 11;
     */
    BOOK_CATEGORY_MANAGEMENT_LEADERSHIP = 11,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_MOTIVATION_INSPIRATION = 12;
     */
    BOOK_CATEGORY_MOTIVATION_INSPIRATION = 12,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_MONEY_INVESTMENTS = 13;
     */
    BOOK_CATEGORY_MONEY_INVESTMENTS = 13,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_PSYCHOLOGY = 14;
     */
    BOOK_CATEGORY_PSYCHOLOGY = 14,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_PRODUCTIVITY = 15;
     */
    BOOK_CATEGORY_PRODUCTIVITY = 15,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_SEX_RELATIONSHIPS = 16;
     */
    BOOK_CATEGORY_SEX_RELATIONSHIPS = 16,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_TECHNOLOGY_THE_FUTURE = 17;
     */
    BOOK_CATEGORY_TECHNOLOGY_THE_FUTURE = 17,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_MINDFULNESS_HAPPINESS = 18;
     */
    BOOK_CATEGORY_MINDFULNESS_HAPPINESS = 18,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_PARENTING = 19;
     */
    BOOK_CATEGORY_PARENTING = 19,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_SOCIETY_CULTURE = 20;
     */
    BOOK_CATEGORY_SOCIETY_CULTURE = 20,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_NATURE_THE_ENVIRONMENT = 21;
     */
    BOOK_CATEGORY_NATURE_THE_ENVIRONMENT = 21,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_BIOGRAPHY_MEMOIR = 22;
     */
    BOOK_CATEGORY_BIOGRAPHY_MEMOIR = 22,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_CAREER_SUCCESS = 23;
     */
    BOOK_CATEGORY_CAREER_SUCCESS = 23,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_EDUCATION = 24;
     */
    BOOK_CATEGORY_EDUCATION = 24,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_RELIGION_SPIRITUALITY = 25;
     */
    BOOK_CATEGORY_RELIGION_SPIRITUALITY = 25,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_CREATIVITY = 26;
     */
    BOOK_CATEGORY_CREATIVITY = 26,
    /**
     * @generated from protobuf enum value: BOOK_CATEGORY_PHILOSOPHY = 27;
     */
    BOOK_CATEGORY_PHILOSOPHY = 27
}
// @generated message type with reflection information, may provide speed optimized methods
class BookProto$Type extends MessageType<BookProto> {
    constructor() {
        super("BookProto", [
            { no: 1, name: "id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "published_at", kind: "message", T: () => Timestamp },
            { no: 3, name: "title", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 4, name: "subtitle", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 5, name: "about_book", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 6, name: "author", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 7, name: "about_author", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 8, name: "num_chapters", kind: "scalar", T: 5 /*ScalarType.INT32*/ },
            { no: 9, name: "reading_minutes", kind: "scalar", T: 5 /*ScalarType.INT32*/ },
            { no: 10, name: "rating", kind: "scalar", T: 2 /*ScalarType.FLOAT*/ },
            { no: 11, name: "num_ratings", kind: "scalar", T: 5 /*ScalarType.INT32*/ },
            { no: 12, name: "quote", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 13, name: "language", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 14, name: "categories", kind: "enum", repeat: 1 /*RepeatType.PACKED*/, T: () => ["BookCategoryProto", BookCategoryProto] },
            { no: 15, name: "target_audience", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<BookProto>): BookProto {
        const message = { id: "", title: "", subtitle: "", aboutBook: "", author: "", aboutAuthor: "", numChapters: 0, readingMinutes: 0, rating: 0, numRatings: 0, quote: "", language: "", categories: [], targetAudience: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<BookProto>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: BookProto): BookProto {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string id */ 1:
                    message.id = reader.string();
                    break;
                case /* google.protobuf.Timestamp published_at */ 2:
                    message.publishedAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.publishedAt);
                    break;
                case /* string title */ 3:
                    message.title = reader.string();
                    break;
                case /* string subtitle */ 4:
                    message.subtitle = reader.string();
                    break;
                case /* string about_book */ 5:
                    message.aboutBook = reader.string();
                    break;
                case /* string author */ 6:
                    message.author = reader.string();
                    break;
                case /* string about_author */ 7:
                    message.aboutAuthor = reader.string();
                    break;
                case /* int32 num_chapters */ 8:
                    message.numChapters = reader.int32();
                    break;
                case /* int32 reading_minutes */ 9:
                    message.readingMinutes = reader.int32();
                    break;
                case /* float rating */ 10:
                    message.rating = reader.float();
                    break;
                case /* int32 num_ratings */ 11:
                    message.numRatings = reader.int32();
                    break;
                case /* string quote */ 12:
                    message.quote = reader.string();
                    break;
                case /* string language */ 13:
                    message.language = reader.string();
                    break;
                case /* repeated BookCategoryProto categories */ 14:
                    if (wireType === WireType.LengthDelimited)
                        for (let e = reader.int32() + reader.pos; reader.pos < e;)
                            message.categories.push(reader.int32());
                    else
                        message.categories.push(reader.int32());
                    break;
                case /* string target_audience */ 15:
                    message.targetAudience = reader.string();
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
    internalBinaryWrite(message: BookProto, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string id = 1; */
        if (message.id !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.id);
        /* google.protobuf.Timestamp published_at = 2; */
        if (message.publishedAt)
            Timestamp.internalBinaryWrite(message.publishedAt, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* string title = 3; */
        if (message.title !== "")
            writer.tag(3, WireType.LengthDelimited).string(message.title);
        /* string subtitle = 4; */
        if (message.subtitle !== "")
            writer.tag(4, WireType.LengthDelimited).string(message.subtitle);
        /* string about_book = 5; */
        if (message.aboutBook !== "")
            writer.tag(5, WireType.LengthDelimited).string(message.aboutBook);
        /* string author = 6; */
        if (message.author !== "")
            writer.tag(6, WireType.LengthDelimited).string(message.author);
        /* string about_author = 7; */
        if (message.aboutAuthor !== "")
            writer.tag(7, WireType.LengthDelimited).string(message.aboutAuthor);
        /* int32 num_chapters = 8; */
        if (message.numChapters !== 0)
            writer.tag(8, WireType.Varint).int32(message.numChapters);
        /* int32 reading_minutes = 9; */
        if (message.readingMinutes !== 0)
            writer.tag(9, WireType.Varint).int32(message.readingMinutes);
        /* float rating = 10; */
        if (message.rating !== 0)
            writer.tag(10, WireType.Bit32).float(message.rating);
        /* int32 num_ratings = 11; */
        if (message.numRatings !== 0)
            writer.tag(11, WireType.Varint).int32(message.numRatings);
        /* string quote = 12; */
        if (message.quote !== "")
            writer.tag(12, WireType.LengthDelimited).string(message.quote);
        /* string language = 13; */
        if (message.language !== "")
            writer.tag(13, WireType.LengthDelimited).string(message.language);
        /* repeated BookCategoryProto categories = 14; */
        if (message.categories.length) {
            writer.tag(14, WireType.LengthDelimited).fork();
            for (let i = 0; i < message.categories.length; i++)
                writer.int32(message.categories[i]);
            writer.join();
        }
        /* string target_audience = 15; */
        if (message.targetAudience !== "")
            writer.tag(15, WireType.LengthDelimited).string(message.targetAudience);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message BookProto
 */
export const BookProto = new BookProto$Type();
// @generated message type with reflection information, may provide speed optimized methods
class BookAudioPart$Type extends MessageType<BookAudioPart> {
    constructor() {
        super("BookAudioPart", [
            { no: 1, name: "text", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "audio_key", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "duration", kind: "message", T: () => Duration }
        ]);
    }
    create(value?: PartialMessage<BookAudioPart>): BookAudioPart {
        const message = { text: "", audioKey: "" };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<BookAudioPart>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: BookAudioPart): BookAudioPart {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string text */ 1:
                    message.text = reader.string();
                    break;
                case /* string audio_key */ 2:
                    message.audioKey = reader.string();
                    break;
                case /* google.protobuf.Duration duration */ 3:
                    message.duration = Duration.internalBinaryRead(reader, reader.uint32(), options, message.duration);
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
    internalBinaryWrite(message: BookAudioPart, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string text = 1; */
        if (message.text !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.text);
        /* string audio_key = 2; */
        if (message.audioKey !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.audioKey);
        /* google.protobuf.Duration duration = 3; */
        if (message.duration)
            Duration.internalBinaryWrite(message.duration, writer.tag(3, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message BookAudioPart
 */
export const BookAudioPart = new BookAudioPart$Type();
// @generated message type with reflection information, may provide speed optimized methods
class BookAudioChapter$Type extends MessageType<BookAudioChapter> {
    constructor() {
        super("BookAudioChapter", [
            { no: 1, name: "created_at", kind: "message", T: () => Timestamp },
            { no: 2, name: "parts", kind: "message", repeat: 1 /*RepeatType.PACKED*/, T: () => BookAudioPart }
        ]);
    }
    create(value?: PartialMessage<BookAudioChapter>): BookAudioChapter {
        const message = { parts: [] };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<BookAudioChapter>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: BookAudioChapter): BookAudioChapter {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* google.protobuf.Timestamp created_at */ 1:
                    message.createdAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.createdAt);
                    break;
                case /* repeated BookAudioPart parts */ 2:
                    message.parts.push(BookAudioPart.internalBinaryRead(reader, reader.uint32(), options));
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
    internalBinaryWrite(message: BookAudioChapter, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* google.protobuf.Timestamp created_at = 1; */
        if (message.createdAt)
            Timestamp.internalBinaryWrite(message.createdAt, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        /* repeated BookAudioPart parts = 2; */
        for (let i = 0; i < message.parts.length; i++)
            BookAudioPart.internalBinaryWrite(message.parts[i], writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message BookAudioChapter
 */
export const BookAudioChapter = new BookAudioChapter$Type();
// @generated message type with reflection information, may provide speed optimized methods
class BookAudio$Type extends MessageType<BookAudio> {
    constructor() {
        super("BookAudio", [
            { no: 1, name: "book_id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "updated_at", kind: "message", T: () => Timestamp },
            { no: 3, name: "introduction", kind: "message", T: () => BookAudioChapter },
            { no: 4, name: "conclusion", kind: "message", T: () => BookAudioChapter },
            { no: 5, name: "chapters", kind: "map", K: 5 /*ScalarType.INT32*/, V: { kind: "message", T: () => BookAudioChapter } }
        ]);
    }
    create(value?: PartialMessage<BookAudio>): BookAudio {
        const message = { bookId: "", chapters: {} };
        globalThis.Object.defineProperty(message, MESSAGE_TYPE, { enumerable: false, value: this });
        if (value !== undefined)
            reflectionMergePartial<BookAudio>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: BookAudio): BookAudio {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string book_id */ 1:
                    message.bookId = reader.string();
                    break;
                case /* google.protobuf.Timestamp updated_at */ 2:
                    message.updatedAt = Timestamp.internalBinaryRead(reader, reader.uint32(), options, message.updatedAt);
                    break;
                case /* BookAudioChapter introduction */ 3:
                    message.introduction = BookAudioChapter.internalBinaryRead(reader, reader.uint32(), options, message.introduction);
                    break;
                case /* BookAudioChapter conclusion */ 4:
                    message.conclusion = BookAudioChapter.internalBinaryRead(reader, reader.uint32(), options, message.conclusion);
                    break;
                case /* map<int32, BookAudioChapter> chapters */ 5:
                    this.binaryReadMap5(message.chapters, reader, options);
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
    private binaryReadMap5(map: BookAudio["chapters"], reader: IBinaryReader, options: BinaryReadOptions): void {
        let len = reader.uint32(), end = reader.pos + len, key: keyof BookAudio["chapters"] | undefined, val: BookAudio["chapters"][any] | undefined;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case 1:
                    key = reader.int32();
                    break;
                case 2:
                    val = BookAudioChapter.internalBinaryRead(reader, reader.uint32(), options);
                    break;
                default: throw new globalThis.Error("unknown map entry field for field BookAudio.chapters");
            }
        }
        map[key ?? 0] = val ?? BookAudioChapter.create();
    }
    internalBinaryWrite(message: BookAudio, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string book_id = 1; */
        if (message.bookId !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.bookId);
        /* google.protobuf.Timestamp updated_at = 2; */
        if (message.updatedAt)
            Timestamp.internalBinaryWrite(message.updatedAt, writer.tag(2, WireType.LengthDelimited).fork(), options).join();
        /* BookAudioChapter introduction = 3; */
        if (message.introduction)
            BookAudioChapter.internalBinaryWrite(message.introduction, writer.tag(3, WireType.LengthDelimited).fork(), options).join();
        /* BookAudioChapter conclusion = 4; */
        if (message.conclusion)
            BookAudioChapter.internalBinaryWrite(message.conclusion, writer.tag(4, WireType.LengthDelimited).fork(), options).join();
        /* map<int32, BookAudioChapter> chapters = 5; */
        for (let k of Object.keys(message.chapters)) {
            writer.tag(5, WireType.LengthDelimited).fork().tag(1, WireType.Varint).int32(parseInt(k));
            writer.tag(2, WireType.LengthDelimited).fork();
            BookAudioChapter.internalBinaryWrite(message.chapters[k as any], writer, options);
            writer.join().join();
        }
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
/**
 * @generated MessageType for protobuf message BookAudio
 */
export const BookAudio = new BookAudio$Type();
