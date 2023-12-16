// DO NOT EDIT.
// swift-format-ignore-file
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: RecsProto.proto
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

enum EmbedTypeProto: SwiftProtobuf.Enum {
  typealias RawValue = Int
  case embedTypeUnknown // = 0
  case embedTypeAda002 // = 1
  case UNRECOGNIZED(Int)

  init() {
    self = .embedTypeUnknown
  }

  init?(rawValue: Int) {
    switch rawValue {
    case 0: self = .embedTypeUnknown
    case 1: self = .embedTypeAda002
    default: self = .UNRECOGNIZED(rawValue)
    }
  }

  var rawValue: Int {
    switch self {
    case .embedTypeUnknown: return 0
    case .embedTypeAda002: return 1
    case .UNRECOGNIZED(let i): return i
    }
  }

}

#if swift(>=4.2)

extension EmbedTypeProto: CaseIterable {
  // The compiler won't synthesize support with the UNRECOGNIZED case.
  static var allCases: [EmbedTypeProto] = [
    .embedTypeUnknown,
    .embedTypeAda002,
  ]
}

#endif  // swift(>=4.2)

enum RecsTopicProto: SwiftProtobuf.Enum {
  typealias RawValue = Int
  case recsTopicUndefined // = 0
  case recsTopicArts // = 1
  case recsTopicBusiness // = 2
  case recsTopicCulture // = 3
  case recsTopicEducation // = 4
  case recsTopicHealth // = 5
  case recsTopicHistory // = 6
  case recsTopicHobbies // = 7
  case recsTopicHumanities // = 8
  case recsTopicMathematics // = 9
  case recsTopicLanguage // = 10
  case recsTopicPsychology // = 11
  case recsTopicRecreation // = 12
  case recsTopicScience // = 13
  case recsTopicSocialStudies // = 14
  case recsTopicTechnology // = 15
  case recsTopicGeography // = 16
  case recsTopicPhysics // = 17
  case recsTopicLiterature // = 18
  case recsTopicPhilosophy // = 19
  case UNRECOGNIZED(Int)

  init() {
    self = .recsTopicUndefined
  }

  init?(rawValue: Int) {
    switch rawValue {
    case 0: self = .recsTopicUndefined
    case 1: self = .recsTopicArts
    case 2: self = .recsTopicBusiness
    case 3: self = .recsTopicCulture
    case 4: self = .recsTopicEducation
    case 5: self = .recsTopicHealth
    case 6: self = .recsTopicHistory
    case 7: self = .recsTopicHobbies
    case 8: self = .recsTopicHumanities
    case 9: self = .recsTopicMathematics
    case 10: self = .recsTopicLanguage
    case 11: self = .recsTopicPsychology
    case 12: self = .recsTopicRecreation
    case 13: self = .recsTopicScience
    case 14: self = .recsTopicSocialStudies
    case 15: self = .recsTopicTechnology
    case 16: self = .recsTopicGeography
    case 17: self = .recsTopicPhysics
    case 18: self = .recsTopicLiterature
    case 19: self = .recsTopicPhilosophy
    default: self = .UNRECOGNIZED(rawValue)
    }
  }

  var rawValue: Int {
    switch self {
    case .recsTopicUndefined: return 0
    case .recsTopicArts: return 1
    case .recsTopicBusiness: return 2
    case .recsTopicCulture: return 3
    case .recsTopicEducation: return 4
    case .recsTopicHealth: return 5
    case .recsTopicHistory: return 6
    case .recsTopicHobbies: return 7
    case .recsTopicHumanities: return 8
    case .recsTopicMathematics: return 9
    case .recsTopicLanguage: return 10
    case .recsTopicPsychology: return 11
    case .recsTopicRecreation: return 12
    case .recsTopicScience: return 13
    case .recsTopicSocialStudies: return 14
    case .recsTopicTechnology: return 15
    case .recsTopicGeography: return 16
    case .recsTopicPhysics: return 17
    case .recsTopicLiterature: return 18
    case .recsTopicPhilosophy: return 19
    case .UNRECOGNIZED(let i): return i
    }
  }

}

#if swift(>=4.2)

extension RecsTopicProto: CaseIterable {
  // The compiler won't synthesize support with the UNRECOGNIZED case.
  static var allCases: [RecsTopicProto] = [
    .recsTopicUndefined,
    .recsTopicArts,
    .recsTopicBusiness,
    .recsTopicCulture,
    .recsTopicEducation,
    .recsTopicHealth,
    .recsTopicHistory,
    .recsTopicHobbies,
    .recsTopicHumanities,
    .recsTopicMathematics,
    .recsTopicLanguage,
    .recsTopicPsychology,
    .recsTopicRecreation,
    .recsTopicScience,
    .recsTopicSocialStudies,
    .recsTopicTechnology,
    .recsTopicGeography,
    .recsTopicPhysics,
    .recsTopicLiterature,
    .recsTopicPhilosophy,
  ]
}

#endif  // swift(>=4.2)

/// Emotional impact on the user.
enum RecsImpactProto: SwiftProtobuf.Enum {
  typealias RawValue = Int
  case recsImpactUnknown // = 0
  case recsImpactLow // = 1
  case recsImpactMed // = 2
  case recsImpactHigh // = 3
  case UNRECOGNIZED(Int)

  init() {
    self = .recsImpactUnknown
  }

  init?(rawValue: Int) {
    switch rawValue {
    case 0: self = .recsImpactUnknown
    case 1: self = .recsImpactLow
    case 2: self = .recsImpactMed
    case 3: self = .recsImpactHigh
    default: self = .UNRECOGNIZED(rawValue)
    }
  }

  var rawValue: Int {
    switch self {
    case .recsImpactUnknown: return 0
    case .recsImpactLow: return 1
    case .recsImpactMed: return 2
    case .recsImpactHigh: return 3
    case .UNRECOGNIZED(let i): return i
    }
  }

}

#if swift(>=4.2)

extension RecsImpactProto: CaseIterable {
  // The compiler won't synthesize support with the UNRECOGNIZED case.
  static var allCases: [RecsImpactProto] = [
    .recsImpactUnknown,
    .recsImpactLow,
    .recsImpactMed,
    .recsImpactHigh,
  ]
}

#endif  // swift(>=4.2)

enum RecsContentTypeProto: SwiftProtobuf.Enum {
  typealias RawValue = Int
  case recsContentTypeUnknown // = 0
  case recsContentTypeInfo // = 1
  case recsContentTypeAbc // = 2
  case recsContentTypeTrueFalse // = 3
  case recsContentTypeVoting // = 4
  case recsContentTypeChallenge // = 5
  case UNRECOGNIZED(Int)

  init() {
    self = .recsContentTypeUnknown
  }

  init?(rawValue: Int) {
    switch rawValue {
    case 0: self = .recsContentTypeUnknown
    case 1: self = .recsContentTypeInfo
    case 2: self = .recsContentTypeAbc
    case 3: self = .recsContentTypeTrueFalse
    case 4: self = .recsContentTypeVoting
    case 5: self = .recsContentTypeChallenge
    default: self = .UNRECOGNIZED(rawValue)
    }
  }

  var rawValue: Int {
    switch self {
    case .recsContentTypeUnknown: return 0
    case .recsContentTypeInfo: return 1
    case .recsContentTypeAbc: return 2
    case .recsContentTypeTrueFalse: return 3
    case .recsContentTypeVoting: return 4
    case .recsContentTypeChallenge: return 5
    case .UNRECOGNIZED(let i): return i
    }
  }

}

#if swift(>=4.2)

extension RecsContentTypeProto: CaseIterable {
  // The compiler won't synthesize support with the UNRECOGNIZED case.
  static var allCases: [RecsContentTypeProto] = [
    .recsContentTypeUnknown,
    .recsContentTypeInfo,
    .recsContentTypeAbc,
    .recsContentTypeTrueFalse,
    .recsContentTypeVoting,
    .recsContentTypeChallenge,
  ]
}

#endif  // swift(>=4.2)

struct EmbedProto {
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

  var embedType: EmbedTypeProto = .embedTypeUnknown

  var inputHash: Data = Data()

  var embedding: [Float] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _createdAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
}

struct RecsScoredTopic {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var topic: RecsTopicProto = .recsTopicUndefined

  var score: Float = 0

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct StoryRecsProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var storyID: String = String()

  var embed: EmbedProto {
    get {return _embed ?? EmbedProto()}
    set {_embed = newValue}
  }
  /// Returns true if `embed` has been explicitly set.
  var hasEmbed: Bool {return self._embed != nil}
  /// Clears the value of `embed`. Subsequent reads from it will return its default value.
  mutating func clearEmbed() {self._embed = nil}

  var impact: RecsImpactProto = .recsImpactUnknown

  var topics: [RecsScoredTopic] = []

  var contentType: RecsContentTypeProto = .recsContentTypeUnknown

  /// 0-1
  var quality: Float = 0

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _embed: EmbedProto? = nil
}

struct StoriesRecsCacheProto {
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

  var recs: [StoryRecsProto] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _createdAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
}

#if swift(>=5.5) && canImport(_Concurrency)
extension EmbedTypeProto: @unchecked Sendable {}
extension RecsTopicProto: @unchecked Sendable {}
extension RecsImpactProto: @unchecked Sendable {}
extension RecsContentTypeProto: @unchecked Sendable {}
extension EmbedProto: @unchecked Sendable {}
extension RecsScoredTopic: @unchecked Sendable {}
extension StoryRecsProto: @unchecked Sendable {}
extension StoriesRecsCacheProto: @unchecked Sendable {}
#endif  // swift(>=5.5) && canImport(_Concurrency)

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension EmbedTypeProto: SwiftProtobuf._ProtoNameProviding {
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    0: .same(proto: "EMBED_TYPE_UNKNOWN"),
    1: .same(proto: "EMBED_TYPE_ADA_002"),
  ]
}

extension RecsTopicProto: SwiftProtobuf._ProtoNameProviding {
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    0: .same(proto: "RECS_TOPIC_UNDEFINED"),
    1: .same(proto: "RECS_TOPIC_ARTS"),
    2: .same(proto: "RECS_TOPIC_BUSINESS"),
    3: .same(proto: "RECS_TOPIC_CULTURE"),
    4: .same(proto: "RECS_TOPIC_EDUCATION"),
    5: .same(proto: "RECS_TOPIC_HEALTH"),
    6: .same(proto: "RECS_TOPIC_HISTORY"),
    7: .same(proto: "RECS_TOPIC_HOBBIES"),
    8: .same(proto: "RECS_TOPIC_HUMANITIES"),
    9: .same(proto: "RECS_TOPIC_MATHEMATICS"),
    10: .same(proto: "RECS_TOPIC_LANGUAGE"),
    11: .same(proto: "RECS_TOPIC_PSYCHOLOGY"),
    12: .same(proto: "RECS_TOPIC_RECREATION"),
    13: .same(proto: "RECS_TOPIC_SCIENCE"),
    14: .same(proto: "RECS_TOPIC_SOCIAL_STUDIES"),
    15: .same(proto: "RECS_TOPIC_TECHNOLOGY"),
    16: .same(proto: "RECS_TOPIC_GEOGRAPHY"),
    17: .same(proto: "RECS_TOPIC_PHYSICS"),
    18: .same(proto: "RECS_TOPIC_LITERATURE"),
    19: .same(proto: "RECS_TOPIC_PHILOSOPHY"),
  ]
}

extension RecsImpactProto: SwiftProtobuf._ProtoNameProviding {
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    0: .same(proto: "RECS_IMPACT_UNKNOWN"),
    1: .same(proto: "RECS_IMPACT_LOW"),
    2: .same(proto: "RECS_IMPACT_MED"),
    3: .same(proto: "RECS_IMPACT_HIGH"),
  ]
}

extension RecsContentTypeProto: SwiftProtobuf._ProtoNameProviding {
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    0: .same(proto: "RECS_CONTENT_TYPE_UNKNOWN"),
    1: .same(proto: "RECS_CONTENT_TYPE_INFO"),
    2: .same(proto: "RECS_CONTENT_TYPE_ABC"),
    3: .same(proto: "RECS_CONTENT_TYPE_TRUE_FALSE"),
    4: .same(proto: "RECS_CONTENT_TYPE_VOTING"),
    5: .same(proto: "RECS_CONTENT_TYPE_CHALLENGE"),
  ]
}

extension EmbedProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "EmbedProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "created_at"),
    2: .standard(proto: "embed_type"),
    3: .standard(proto: "input_hash"),
    4: .same(proto: "embedding"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularMessageField(value: &self._createdAt) }()
      case 2: try { try decoder.decodeSingularEnumField(value: &self.embedType) }()
      case 3: try { try decoder.decodeSingularBytesField(value: &self.inputHash) }()
      case 4: try { try decoder.decodeRepeatedFloatField(value: &self.embedding) }()
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
    if self.embedType != .embedTypeUnknown {
      try visitor.visitSingularEnumField(value: self.embedType, fieldNumber: 2)
    }
    if !self.inputHash.isEmpty {
      try visitor.visitSingularBytesField(value: self.inputHash, fieldNumber: 3)
    }
    if !self.embedding.isEmpty {
      try visitor.visitPackedFloatField(value: self.embedding, fieldNumber: 4)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: EmbedProto, rhs: EmbedProto) -> Bool {
    if lhs._createdAt != rhs._createdAt {return false}
    if lhs.embedType != rhs.embedType {return false}
    if lhs.inputHash != rhs.inputHash {return false}
    if lhs.embedding != rhs.embedding {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension RecsScoredTopic: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "RecsScoredTopic"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "topic"),
    2: .same(proto: "score"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularEnumField(value: &self.topic) }()
      case 2: try { try decoder.decodeSingularFloatField(value: &self.score) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if self.topic != .recsTopicUndefined {
      try visitor.visitSingularEnumField(value: self.topic, fieldNumber: 1)
    }
    if self.score != 0 {
      try visitor.visitSingularFloatField(value: self.score, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: RecsScoredTopic, rhs: RecsScoredTopic) -> Bool {
    if lhs.topic != rhs.topic {return false}
    if lhs.score != rhs.score {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension StoryRecsProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "StoryRecsProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "story_id"),
    2: .same(proto: "embed"),
    3: .same(proto: "impact"),
    4: .same(proto: "topics"),
    5: .standard(proto: "content_type"),
    6: .same(proto: "quality"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.storyID) }()
      case 2: try { try decoder.decodeSingularMessageField(value: &self._embed) }()
      case 3: try { try decoder.decodeSingularEnumField(value: &self.impact) }()
      case 4: try { try decoder.decodeRepeatedMessageField(value: &self.topics) }()
      case 5: try { try decoder.decodeSingularEnumField(value: &self.contentType) }()
      case 6: try { try decoder.decodeSingularFloatField(value: &self.quality) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    if !self.storyID.isEmpty {
      try visitor.visitSingularStringField(value: self.storyID, fieldNumber: 1)
    }
    try { if let v = self._embed {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    } }()
    if self.impact != .recsImpactUnknown {
      try visitor.visitSingularEnumField(value: self.impact, fieldNumber: 3)
    }
    if !self.topics.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.topics, fieldNumber: 4)
    }
    if self.contentType != .recsContentTypeUnknown {
      try visitor.visitSingularEnumField(value: self.contentType, fieldNumber: 5)
    }
    if self.quality != 0 {
      try visitor.visitSingularFloatField(value: self.quality, fieldNumber: 6)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: StoryRecsProto, rhs: StoryRecsProto) -> Bool {
    if lhs.storyID != rhs.storyID {return false}
    if lhs._embed != rhs._embed {return false}
    if lhs.impact != rhs.impact {return false}
    if lhs.topics != rhs.topics {return false}
    if lhs.contentType != rhs.contentType {return false}
    if lhs.quality != rhs.quality {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension StoriesRecsCacheProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "StoriesRecsCacheProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "created_at"),
    2: .same(proto: "recs"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularMessageField(value: &self._createdAt) }()
      case 2: try { try decoder.decodeRepeatedMessageField(value: &self.recs) }()
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
    if !self.recs.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.recs, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: StoriesRecsCacheProto, rhs: StoriesRecsCacheProto) -> Bool {
    if lhs._createdAt != rhs._createdAt {return false}
    if lhs.recs != rhs.recs {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}
