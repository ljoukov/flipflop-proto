// DO NOT EDIT.
// swift-format-ignore-file
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: BookProto.proto
//
// For information on using the generated types, please see the documentation:
//   https://github.com/apple/swift-protobuf/

import Foundation
import SwiftProtobuf

// If the compiler emits an error on this type, it is because this file
// was generated by a version of the `protoc` Swift plug-in that is
// incompatible with the version of SwiftProtobuf to which you are linking.
// Please ensure that you are building against the same version of the API
// that was used to generate this file.
fileprivate struct _GeneratedWithProtocGenSwiftVersion: SwiftProtobuf.ProtobufAPIVersionCheck {
  struct _2: SwiftProtobuf.ProtobufAPIVersion_2 {}
  typealias Version = _2
}

enum BookCategoryProto: SwiftProtobuf.Enum {
  typealias RawValue = Int
  case bookCategoryUnknown // = 0
  case bookCategoryEntrepreneurship // = 1
  case bookCategoryPolitics // = 2
  case bookCategoryMarketingAndSales // = 3
  case bookCategoryScience // = 4
  case bookCategoryHealthNutrition // = 5
  case bookCategoryPersonalDevelopment // = 6
  case bookCategoryEconomics // = 7
  case bookCategoryHistory // = 8
  case bookCategoryCommunicationSkills // = 9
  case bookCategoryCorporateCulture // = 10
  case bookCategoryManagementLeadership // = 11
  case bookCategoryMotivationInspiration // = 12
  case bookCategoryMoneyInvestments // = 13
  case bookCategoryPsychology // = 14
  case bookCategoryProductivity // = 15
  case bookCategorySexRelationships // = 16
  case bookCategoryTechnologyTheFuture // = 17
  case bookCategoryMindfulnessHappiness // = 18
  case bookCategoryParenting // = 19
  case bookCategorySocietyCulture // = 20
  case bookCategoryNatureTheEnvironment // = 21
  case bookCategoryBiographyMemoir // = 22
  case bookCategoryCareerSuccess // = 23
  case bookCategoryEducation // = 24
  case bookCategoryReligionSpirituality // = 25
  case bookCategoryCreativity // = 26
  case bookCategoryPhilosophy // = 27
  case UNRECOGNIZED(Int)

  init() {
    self = .bookCategoryUnknown
  }

  init?(rawValue: Int) {
    switch rawValue {
    case 0: self = .bookCategoryUnknown
    case 1: self = .bookCategoryEntrepreneurship
    case 2: self = .bookCategoryPolitics
    case 3: self = .bookCategoryMarketingAndSales
    case 4: self = .bookCategoryScience
    case 5: self = .bookCategoryHealthNutrition
    case 6: self = .bookCategoryPersonalDevelopment
    case 7: self = .bookCategoryEconomics
    case 8: self = .bookCategoryHistory
    case 9: self = .bookCategoryCommunicationSkills
    case 10: self = .bookCategoryCorporateCulture
    case 11: self = .bookCategoryManagementLeadership
    case 12: self = .bookCategoryMotivationInspiration
    case 13: self = .bookCategoryMoneyInvestments
    case 14: self = .bookCategoryPsychology
    case 15: self = .bookCategoryProductivity
    case 16: self = .bookCategorySexRelationships
    case 17: self = .bookCategoryTechnologyTheFuture
    case 18: self = .bookCategoryMindfulnessHappiness
    case 19: self = .bookCategoryParenting
    case 20: self = .bookCategorySocietyCulture
    case 21: self = .bookCategoryNatureTheEnvironment
    case 22: self = .bookCategoryBiographyMemoir
    case 23: self = .bookCategoryCareerSuccess
    case 24: self = .bookCategoryEducation
    case 25: self = .bookCategoryReligionSpirituality
    case 26: self = .bookCategoryCreativity
    case 27: self = .bookCategoryPhilosophy
    default: self = .UNRECOGNIZED(rawValue)
    }
  }

  var rawValue: Int {
    switch self {
    case .bookCategoryUnknown: return 0
    case .bookCategoryEntrepreneurship: return 1
    case .bookCategoryPolitics: return 2
    case .bookCategoryMarketingAndSales: return 3
    case .bookCategoryScience: return 4
    case .bookCategoryHealthNutrition: return 5
    case .bookCategoryPersonalDevelopment: return 6
    case .bookCategoryEconomics: return 7
    case .bookCategoryHistory: return 8
    case .bookCategoryCommunicationSkills: return 9
    case .bookCategoryCorporateCulture: return 10
    case .bookCategoryManagementLeadership: return 11
    case .bookCategoryMotivationInspiration: return 12
    case .bookCategoryMoneyInvestments: return 13
    case .bookCategoryPsychology: return 14
    case .bookCategoryProductivity: return 15
    case .bookCategorySexRelationships: return 16
    case .bookCategoryTechnologyTheFuture: return 17
    case .bookCategoryMindfulnessHappiness: return 18
    case .bookCategoryParenting: return 19
    case .bookCategorySocietyCulture: return 20
    case .bookCategoryNatureTheEnvironment: return 21
    case .bookCategoryBiographyMemoir: return 22
    case .bookCategoryCareerSuccess: return 23
    case .bookCategoryEducation: return 24
    case .bookCategoryReligionSpirituality: return 25
    case .bookCategoryCreativity: return 26
    case .bookCategoryPhilosophy: return 27
    case .UNRECOGNIZED(let i): return i
    }
  }

}

#if swift(>=4.2)

extension BookCategoryProto: CaseIterable {
  // The compiler won't synthesize support with the UNRECOGNIZED case.
  static var allCases: [BookCategoryProto] = [
    .bookCategoryUnknown,
    .bookCategoryEntrepreneurship,
    .bookCategoryPolitics,
    .bookCategoryMarketingAndSales,
    .bookCategoryScience,
    .bookCategoryHealthNutrition,
    .bookCategoryPersonalDevelopment,
    .bookCategoryEconomics,
    .bookCategoryHistory,
    .bookCategoryCommunicationSkills,
    .bookCategoryCorporateCulture,
    .bookCategoryManagementLeadership,
    .bookCategoryMotivationInspiration,
    .bookCategoryMoneyInvestments,
    .bookCategoryPsychology,
    .bookCategoryProductivity,
    .bookCategorySexRelationships,
    .bookCategoryTechnologyTheFuture,
    .bookCategoryMindfulnessHappiness,
    .bookCategoryParenting,
    .bookCategorySocietyCulture,
    .bookCategoryNatureTheEnvironment,
    .bookCategoryBiographyMemoir,
    .bookCategoryCareerSuccess,
    .bookCategoryEducation,
    .bookCategoryReligionSpirituality,
    .bookCategoryCreativity,
    .bookCategoryPhilosophy,
  ]
}

#endif  // swift(>=4.2)

struct BookProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var id: String = String()

  var publishedAt: SwiftProtobuf.Google_Protobuf_Timestamp {
    get {return _publishedAt ?? SwiftProtobuf.Google_Protobuf_Timestamp()}
    set {_publishedAt = newValue}
  }
  /// Returns true if `publishedAt` has been explicitly set.
  var hasPublishedAt: Bool {return self._publishedAt != nil}
  /// Clears the value of `publishedAt`. Subsequent reads from it will return its default value.
  mutating func clearPublishedAt() {self._publishedAt = nil}

  var title: String = String()

  var subtitle: String = String()

  var aboutBook: String = String()

  var author: String = String()

  var aboutAuthor: String = String()

  var numChapters: Int32 = 0

  var readingMinutes: Int32 = 0

  var rating: Float = 0

  var numRatings: Int32 = 0

  var quote: String = String()

  var language: String = String()

  var categories: [BookCategoryProto] = []

  var targetAudience: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _publishedAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
}

struct BookAudioChapter {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var createdAt: SwiftProtobuf.Google_Protobuf_Timestamp {
    get {return _createdAt ?? SwiftProtobuf.Google_Protobuf_Timestamp()}
    set {_createdAt = newValue}
  }
  /// Returns true if `createdAt` has been explicitly set.
  var hasCreatedAt: Bool {return self._createdAt != nil}
  /// Clears the value of `createdAt`. Subsequent reads from it will return its default value.
  mutating func clearCreatedAt() {self._createdAt = nil}

  var audioKey: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _createdAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
}

struct BookAudio {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var bookID: String = String()

  var updatedAt: SwiftProtobuf.Google_Protobuf_Timestamp {
    get {return _updatedAt ?? SwiftProtobuf.Google_Protobuf_Timestamp()}
    set {_updatedAt = newValue}
  }
  /// Returns true if `updatedAt` has been explicitly set.
  var hasUpdatedAt: Bool {return self._updatedAt != nil}
  /// Clears the value of `updatedAt`. Subsequent reads from it will return its default value.
  mutating func clearUpdatedAt() {self._updatedAt = nil}

  var introduction: BookAudioChapter {
    get {return _introduction ?? BookAudioChapter()}
    set {_introduction = newValue}
  }
  /// Returns true if `introduction` has been explicitly set.
  var hasIntroduction: Bool {return self._introduction != nil}
  /// Clears the value of `introduction`. Subsequent reads from it will return its default value.
  mutating func clearIntroduction() {self._introduction = nil}

  var conclusion: BookAudioChapter {
    get {return _conclusion ?? BookAudioChapter()}
    set {_conclusion = newValue}
  }
  /// Returns true if `conclusion` has been explicitly set.
  var hasConclusion: Bool {return self._conclusion != nil}
  /// Clears the value of `conclusion`. Subsequent reads from it will return its default value.
  mutating func clearConclusion() {self._conclusion = nil}

  var numChapters: Int32 = 0

  var chapters: Dictionary<Int32,BookAudioChapter> = [:]

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _updatedAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
  fileprivate var _introduction: BookAudioChapter? = nil
  fileprivate var _conclusion: BookAudioChapter? = nil
}

#if swift(>=5.5) && canImport(_Concurrency)
extension BookCategoryProto: @unchecked Sendable {}
extension BookProto: @unchecked Sendable {}
extension BookAudioChapter: @unchecked Sendable {}
extension BookAudio: @unchecked Sendable {}
#endif  // swift(>=5.5) && canImport(_Concurrency)

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension BookCategoryProto: SwiftProtobuf._ProtoNameProviding {
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    0: .same(proto: "BOOK_CATEGORY_UNKNOWN"),
    1: .same(proto: "BOOK_CATEGORY_ENTREPRENEURSHIP"),
    2: .same(proto: "BOOK_CATEGORY_POLITICS"),
    3: .same(proto: "BOOK_CATEGORY_MARKETING_AND_SALES"),
    4: .same(proto: "BOOK_CATEGORY_SCIENCE"),
    5: .same(proto: "BOOK_CATEGORY_HEALTH_NUTRITION"),
    6: .same(proto: "BOOK_CATEGORY_PERSONAL_DEVELOPMENT"),
    7: .same(proto: "BOOK_CATEGORY_ECONOMICS"),
    8: .same(proto: "BOOK_CATEGORY_HISTORY"),
    9: .same(proto: "BOOK_CATEGORY_COMMUNICATION_SKILLS"),
    10: .same(proto: "BOOK_CATEGORY_CORPORATE_CULTURE"),
    11: .same(proto: "BOOK_CATEGORY_MANAGEMENT_LEADERSHIP"),
    12: .same(proto: "BOOK_CATEGORY_MOTIVATION_INSPIRATION"),
    13: .same(proto: "BOOK_CATEGORY_MONEY_INVESTMENTS"),
    14: .same(proto: "BOOK_CATEGORY_PSYCHOLOGY"),
    15: .same(proto: "BOOK_CATEGORY_PRODUCTIVITY"),
    16: .same(proto: "BOOK_CATEGORY_SEX_RELATIONSHIPS"),
    17: .same(proto: "BOOK_CATEGORY_TECHNOLOGY_THE_FUTURE"),
    18: .same(proto: "BOOK_CATEGORY_MINDFULNESS_HAPPINESS"),
    19: .same(proto: "BOOK_CATEGORY_PARENTING"),
    20: .same(proto: "BOOK_CATEGORY_SOCIETY_CULTURE"),
    21: .same(proto: "BOOK_CATEGORY_NATURE_THE_ENVIRONMENT"),
    22: .same(proto: "BOOK_CATEGORY_BIOGRAPHY_MEMOIR"),
    23: .same(proto: "BOOK_CATEGORY_CAREER_SUCCESS"),
    24: .same(proto: "BOOK_CATEGORY_EDUCATION"),
    25: .same(proto: "BOOK_CATEGORY_RELIGION_SPIRITUALITY"),
    26: .same(proto: "BOOK_CATEGORY_CREATIVITY"),
    27: .same(proto: "BOOK_CATEGORY_PHILOSOPHY"),
  ]
}

extension BookProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "BookProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "id"),
    2: .standard(proto: "published_at"),
    3: .same(proto: "title"),
    4: .same(proto: "subtitle"),
    5: .standard(proto: "about_book"),
    6: .same(proto: "author"),
    7: .standard(proto: "about_author"),
    8: .standard(proto: "num_chapters"),
    9: .standard(proto: "reading_minutes"),
    10: .same(proto: "rating"),
    11: .standard(proto: "num_ratings"),
    12: .same(proto: "quote"),
    13: .same(proto: "language"),
    14: .same(proto: "categories"),
    15: .standard(proto: "target_audience"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.id) }()
      case 2: try { try decoder.decodeSingularMessageField(value: &self._publishedAt) }()
      case 3: try { try decoder.decodeSingularStringField(value: &self.title) }()
      case 4: try { try decoder.decodeSingularStringField(value: &self.subtitle) }()
      case 5: try { try decoder.decodeSingularStringField(value: &self.aboutBook) }()
      case 6: try { try decoder.decodeSingularStringField(value: &self.author) }()
      case 7: try { try decoder.decodeSingularStringField(value: &self.aboutAuthor) }()
      case 8: try { try decoder.decodeSingularInt32Field(value: &self.numChapters) }()
      case 9: try { try decoder.decodeSingularInt32Field(value: &self.readingMinutes) }()
      case 10: try { try decoder.decodeSingularFloatField(value: &self.rating) }()
      case 11: try { try decoder.decodeSingularInt32Field(value: &self.numRatings) }()
      case 12: try { try decoder.decodeSingularStringField(value: &self.quote) }()
      case 13: try { try decoder.decodeSingularStringField(value: &self.language) }()
      case 14: try { try decoder.decodeRepeatedEnumField(value: &self.categories) }()
      case 15: try { try decoder.decodeSingularStringField(value: &self.targetAudience) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    if !self.id.isEmpty {
      try visitor.visitSingularStringField(value: self.id, fieldNumber: 1)
    }
    try { if let v = self._publishedAt {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    } }()
    if !self.title.isEmpty {
      try visitor.visitSingularStringField(value: self.title, fieldNumber: 3)
    }
    if !self.subtitle.isEmpty {
      try visitor.visitSingularStringField(value: self.subtitle, fieldNumber: 4)
    }
    if !self.aboutBook.isEmpty {
      try visitor.visitSingularStringField(value: self.aboutBook, fieldNumber: 5)
    }
    if !self.author.isEmpty {
      try visitor.visitSingularStringField(value: self.author, fieldNumber: 6)
    }
    if !self.aboutAuthor.isEmpty {
      try visitor.visitSingularStringField(value: self.aboutAuthor, fieldNumber: 7)
    }
    if self.numChapters != 0 {
      try visitor.visitSingularInt32Field(value: self.numChapters, fieldNumber: 8)
    }
    if self.readingMinutes != 0 {
      try visitor.visitSingularInt32Field(value: self.readingMinutes, fieldNumber: 9)
    }
    if self.rating != 0 {
      try visitor.visitSingularFloatField(value: self.rating, fieldNumber: 10)
    }
    if self.numRatings != 0 {
      try visitor.visitSingularInt32Field(value: self.numRatings, fieldNumber: 11)
    }
    if !self.quote.isEmpty {
      try visitor.visitSingularStringField(value: self.quote, fieldNumber: 12)
    }
    if !self.language.isEmpty {
      try visitor.visitSingularStringField(value: self.language, fieldNumber: 13)
    }
    if !self.categories.isEmpty {
      try visitor.visitPackedEnumField(value: self.categories, fieldNumber: 14)
    }
    if !self.targetAudience.isEmpty {
      try visitor.visitSingularStringField(value: self.targetAudience, fieldNumber: 15)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: BookProto, rhs: BookProto) -> Bool {
    if lhs.id != rhs.id {return false}
    if lhs._publishedAt != rhs._publishedAt {return false}
    if lhs.title != rhs.title {return false}
    if lhs.subtitle != rhs.subtitle {return false}
    if lhs.aboutBook != rhs.aboutBook {return false}
    if lhs.author != rhs.author {return false}
    if lhs.aboutAuthor != rhs.aboutAuthor {return false}
    if lhs.numChapters != rhs.numChapters {return false}
    if lhs.readingMinutes != rhs.readingMinutes {return false}
    if lhs.rating != rhs.rating {return false}
    if lhs.numRatings != rhs.numRatings {return false}
    if lhs.quote != rhs.quote {return false}
    if lhs.language != rhs.language {return false}
    if lhs.categories != rhs.categories {return false}
    if lhs.targetAudience != rhs.targetAudience {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension BookAudioChapter: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "BookAudioChapter"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "created_at"),
    2: .standard(proto: "audio_key"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularMessageField(value: &self._createdAt) }()
      case 2: try { try decoder.decodeSingularStringField(value: &self.audioKey) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    try { if let v = self._createdAt {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 1)
    } }()
    if !self.audioKey.isEmpty {
      try visitor.visitSingularStringField(value: self.audioKey, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: BookAudioChapter, rhs: BookAudioChapter) -> Bool {
    if lhs._createdAt != rhs._createdAt {return false}
    if lhs.audioKey != rhs.audioKey {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension BookAudio: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "BookAudio"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "book_id"),
    2: .standard(proto: "updated_at"),
    3: .same(proto: "introduction"),
    4: .same(proto: "conclusion"),
    5: .standard(proto: "num_chapters"),
    6: .same(proto: "chapters"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.bookID) }()
      case 2: try { try decoder.decodeSingularMessageField(value: &self._updatedAt) }()
      case 3: try { try decoder.decodeSingularMessageField(value: &self._introduction) }()
      case 4: try { try decoder.decodeSingularMessageField(value: &self._conclusion) }()
      case 5: try { try decoder.decodeSingularInt32Field(value: &self.numChapters) }()
      case 6: try { try decoder.decodeMapField(fieldType: SwiftProtobuf._ProtobufMessageMap<SwiftProtobuf.ProtobufInt32,BookAudioChapter>.self, value: &self.chapters) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    if !self.bookID.isEmpty {
      try visitor.visitSingularStringField(value: self.bookID, fieldNumber: 1)
    }
    try { if let v = self._updatedAt {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    } }()
    try { if let v = self._introduction {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 3)
    } }()
    try { if let v = self._conclusion {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 4)
    } }()
    if self.numChapters != 0 {
      try visitor.visitSingularInt32Field(value: self.numChapters, fieldNumber: 5)
    }
    if !self.chapters.isEmpty {
      try visitor.visitMapField(fieldType: SwiftProtobuf._ProtobufMessageMap<SwiftProtobuf.ProtobufInt32,BookAudioChapter>.self, value: self.chapters, fieldNumber: 6)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: BookAudio, rhs: BookAudio) -> Bool {
    if lhs.bookID != rhs.bookID {return false}
    if lhs._updatedAt != rhs._updatedAt {return false}
    if lhs._introduction != rhs._introduction {return false}
    if lhs._conclusion != rhs._conclusion {return false}
    if lhs.numChapters != rhs.numChapters {return false}
    if lhs.chapters != rhs.chapters {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}
