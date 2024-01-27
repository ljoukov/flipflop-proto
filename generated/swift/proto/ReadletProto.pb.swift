// DO NOT EDIT.
// swift-format-ignore-file
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: ReadletProto.proto
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

enum ReadletChapterType: SwiftProtobuf.Enum {
  typealias RawValue = Int
  case undefined // = 0
  case introduction // = 1
  case regular // = 2
  case conclusion // = 3
  case UNRECOGNIZED(Int)

  init() {
    self = .undefined
  }

  init?(rawValue: Int) {
    switch rawValue {
    case 0: self = .undefined
    case 1: self = .introduction
    case 2: self = .regular
    case 3: self = .conclusion
    default: self = .UNRECOGNIZED(rawValue)
    }
  }

  var rawValue: Int {
    switch self {
    case .undefined: return 0
    case .introduction: return 1
    case .regular: return 2
    case .conclusion: return 3
    case .UNRECOGNIZED(let i): return i
    }
  }

}

#if swift(>=4.2)

extension ReadletChapterType: CaseIterable {
  // The compiler won't synthesize support with the UNRECOGNIZED case.
  static var allCases: [ReadletChapterType] = [
    .undefined,
    .introduction,
    .regular,
    .conclusion,
  ]
}

#endif  // swift(>=4.2)

struct ReadletApiRequestProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var encodedUserAuth: String = String()

  var request: ReadletApiRequestProto.OneOf_Request? = nil

  var getReadlets: GetReadletsRequestProto {
    get {
      if case .getReadlets(let v)? = request {return v}
      return GetReadletsRequestProto()
    }
    set {request = .getReadlets(newValue)}
  }

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum OneOf_Request: Equatable {
    case getReadlets(GetReadletsRequestProto)

  #if !swift(>=4.1)
    static func ==(lhs: ReadletApiRequestProto.OneOf_Request, rhs: ReadletApiRequestProto.OneOf_Request) -> Bool {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch (lhs, rhs) {
      case (.getReadlets, .getReadlets): return {
        guard case .getReadlets(let l) = lhs, case .getReadlets(let r) = rhs else { preconditionFailure() }
        return l == r
      }()
      }
    }
  #endif
  }

  init() {}
}

struct ReadletApiResponseProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  /// If present the token was refreshed and the client should use this new one from now onwards.
  var refreshedEncodedUserAuth: String = String()

  var response: ReadletApiResponseProto.OneOf_Response? = nil

  var getReadlets: GetReadletsResponseProto {
    get {
      if case .getReadlets(let v)? = response {return v}
      return GetReadletsResponseProto()
    }
    set {response = .getReadlets(newValue)}
  }

  var latencies: Dictionary<String,SwiftProtobuf.Google_Protobuf_Duration> = [:]

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum OneOf_Response: Equatable {
    case getReadlets(GetReadletsResponseProto)

  #if !swift(>=4.1)
    static func ==(lhs: ReadletApiResponseProto.OneOf_Response, rhs: ReadletApiResponseProto.OneOf_Response) -> Bool {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch (lhs, rhs) {
      case (.getReadlets, .getReadlets): return {
        guard case .getReadlets(let l) = lhs, case .getReadlets(let r) = rhs else { preconditionFailure() }
        return l == r
      }()
      }
    }
  #endif
  }

  init() {}
}

struct GetReadletsRequestProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var categoryFilter: [String] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct GetReadletsResponseProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var readlets: [ReadletProto] = []

  var availableCategories: [ReadletCategoryProto] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct ReadletsCacheProto {
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

  var readlets: [ReadletProto] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _createdAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
}

struct ReadletCategoryProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var id: String = String()

  var displayName: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct ReadletChapterProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var type: ReadletChapterType = .undefined

  var title: String = String()

  var subtitle: String = String()

  var text: String = String()

  var audioPath: String = String()

  var audioDuration: SwiftProtobuf.Google_Protobuf_Duration {
    get {return _audioDuration ?? SwiftProtobuf.Google_Protobuf_Duration()}
    set {_audioDuration = newValue}
  }
  /// Returns true if `audioDuration` has been explicitly set.
  var hasAudioDuration: Bool {return self._audioDuration != nil}
  /// Clears the value of `audioDuration`. Subsequent reads from it will return its default value.
  mutating func clearAudioDuration() {self._audioDuration = nil}

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _audioDuration: SwiftProtobuf.Google_Protobuf_Duration? = nil
}

struct ReadletProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var id: String = String()

  var createdAt: SwiftProtobuf.Google_Protobuf_Timestamp {
    get {return _createdAt ?? SwiftProtobuf.Google_Protobuf_Timestamp()}
    set {_createdAt = newValue}
  }
  /// Returns true if `createdAt` has been explicitly set.
  var hasCreatedAt: Bool {return self._createdAt != nil}
  /// Clears the value of `createdAt`. Subsequent reads from it will return its default value.
  mutating func clearCreatedAt() {self._createdAt = nil}

  var title: String = String()

  var titleEmoji: String = String()

  var color: ColorTypeProto = .undefined

  var blurb: String = String()

  var categoryIds: [String] = []

  var chapters: [ReadletChapterProto] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _createdAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
}

#if swift(>=5.5) && canImport(_Concurrency)
extension ReadletChapterType: @unchecked Sendable {}
extension ReadletApiRequestProto: @unchecked Sendable {}
extension ReadletApiRequestProto.OneOf_Request: @unchecked Sendable {}
extension ReadletApiResponseProto: @unchecked Sendable {}
extension ReadletApiResponseProto.OneOf_Response: @unchecked Sendable {}
extension GetReadletsRequestProto: @unchecked Sendable {}
extension GetReadletsResponseProto: @unchecked Sendable {}
extension ReadletsCacheProto: @unchecked Sendable {}
extension ReadletCategoryProto: @unchecked Sendable {}
extension ReadletChapterProto: @unchecked Sendable {}
extension ReadletProto: @unchecked Sendable {}
#endif  // swift(>=5.5) && canImport(_Concurrency)

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension ReadletChapterType: SwiftProtobuf._ProtoNameProviding {
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    0: .same(proto: "READLET_CHAPTER_TYPE_UNDEFINED"),
    1: .same(proto: "READLET_CHAPTER_TYPE_INTRODUCTION"),
    2: .same(proto: "READLET_CHAPTER_TYPE_REGULAR"),
    3: .same(proto: "READLET_CHAPTER_TYPE_CONCLUSION"),
  ]
}

extension ReadletApiRequestProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ReadletApiRequestProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "encoded_user_auth"),
    2: .standard(proto: "get_readlets"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.encodedUserAuth) }()
      case 2: try {
        var v: GetReadletsRequestProto?
        var hadOneofValue = false
        if let current = self.request {
          hadOneofValue = true
          if case .getReadlets(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.request = .getReadlets(v)
        }
      }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    if !self.encodedUserAuth.isEmpty {
      try visitor.visitSingularStringField(value: self.encodedUserAuth, fieldNumber: 1)
    }
    try { if case .getReadlets(let v)? = self.request {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    } }()
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ReadletApiRequestProto, rhs: ReadletApiRequestProto) -> Bool {
    if lhs.encodedUserAuth != rhs.encodedUserAuth {return false}
    if lhs.request != rhs.request {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ReadletApiResponseProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ReadletApiResponseProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "refreshed_encoded_user_auth"),
    2: .standard(proto: "get_readlets"),
    100: .same(proto: "latencies"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.refreshedEncodedUserAuth) }()
      case 2: try {
        var v: GetReadletsResponseProto?
        var hadOneofValue = false
        if let current = self.response {
          hadOneofValue = true
          if case .getReadlets(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.response = .getReadlets(v)
        }
      }()
      case 100: try { try decoder.decodeMapField(fieldType: SwiftProtobuf._ProtobufMessageMap<SwiftProtobuf.ProtobufString,SwiftProtobuf.Google_Protobuf_Duration>.self, value: &self.latencies) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    if !self.refreshedEncodedUserAuth.isEmpty {
      try visitor.visitSingularStringField(value: self.refreshedEncodedUserAuth, fieldNumber: 1)
    }
    try { if case .getReadlets(let v)? = self.response {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    } }()
    if !self.latencies.isEmpty {
      try visitor.visitMapField(fieldType: SwiftProtobuf._ProtobufMessageMap<SwiftProtobuf.ProtobufString,SwiftProtobuf.Google_Protobuf_Duration>.self, value: self.latencies, fieldNumber: 100)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ReadletApiResponseProto, rhs: ReadletApiResponseProto) -> Bool {
    if lhs.refreshedEncodedUserAuth != rhs.refreshedEncodedUserAuth {return false}
    if lhs.response != rhs.response {return false}
    if lhs.latencies != rhs.latencies {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension GetReadletsRequestProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "GetReadletsRequestProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "category_filter"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeRepeatedStringField(value: &self.categoryFilter) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.categoryFilter.isEmpty {
      try visitor.visitRepeatedStringField(value: self.categoryFilter, fieldNumber: 1)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: GetReadletsRequestProto, rhs: GetReadletsRequestProto) -> Bool {
    if lhs.categoryFilter != rhs.categoryFilter {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension GetReadletsResponseProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "GetReadletsResponseProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "readlets"),
    2: .standard(proto: "available_categories"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeRepeatedMessageField(value: &self.readlets) }()
      case 2: try { try decoder.decodeRepeatedMessageField(value: &self.availableCategories) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.readlets.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.readlets, fieldNumber: 1)
    }
    if !self.availableCategories.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.availableCategories, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: GetReadletsResponseProto, rhs: GetReadletsResponseProto) -> Bool {
    if lhs.readlets != rhs.readlets {return false}
    if lhs.availableCategories != rhs.availableCategories {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ReadletsCacheProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ReadletsCacheProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "created_at"),
    2: .same(proto: "readlets"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularMessageField(value: &self._createdAt) }()
      case 2: try { try decoder.decodeRepeatedMessageField(value: &self.readlets) }()
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
    if !self.readlets.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.readlets, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ReadletsCacheProto, rhs: ReadletsCacheProto) -> Bool {
    if lhs._createdAt != rhs._createdAt {return false}
    if lhs.readlets != rhs.readlets {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ReadletCategoryProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ReadletCategoryProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "id"),
    2: .standard(proto: "display_name"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.id) }()
      case 2: try { try decoder.decodeSingularStringField(value: &self.displayName) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.id.isEmpty {
      try visitor.visitSingularStringField(value: self.id, fieldNumber: 1)
    }
    if !self.displayName.isEmpty {
      try visitor.visitSingularStringField(value: self.displayName, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ReadletCategoryProto, rhs: ReadletCategoryProto) -> Bool {
    if lhs.id != rhs.id {return false}
    if lhs.displayName != rhs.displayName {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ReadletChapterProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ReadletChapterProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "type"),
    2: .same(proto: "title"),
    3: .same(proto: "subtitle"),
    4: .same(proto: "text"),
    5: .standard(proto: "audio_path"),
    6: .standard(proto: "audio_duration"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularEnumField(value: &self.type) }()
      case 2: try { try decoder.decodeSingularStringField(value: &self.title) }()
      case 3: try { try decoder.decodeSingularStringField(value: &self.subtitle) }()
      case 4: try { try decoder.decodeSingularStringField(value: &self.text) }()
      case 5: try { try decoder.decodeSingularStringField(value: &self.audioPath) }()
      case 6: try { try decoder.decodeSingularMessageField(value: &self._audioDuration) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    if self.type != .undefined {
      try visitor.visitSingularEnumField(value: self.type, fieldNumber: 1)
    }
    if !self.title.isEmpty {
      try visitor.visitSingularStringField(value: self.title, fieldNumber: 2)
    }
    if !self.subtitle.isEmpty {
      try visitor.visitSingularStringField(value: self.subtitle, fieldNumber: 3)
    }
    if !self.text.isEmpty {
      try visitor.visitSingularStringField(value: self.text, fieldNumber: 4)
    }
    if !self.audioPath.isEmpty {
      try visitor.visitSingularStringField(value: self.audioPath, fieldNumber: 5)
    }
    try { if let v = self._audioDuration {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 6)
    } }()
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ReadletChapterProto, rhs: ReadletChapterProto) -> Bool {
    if lhs.type != rhs.type {return false}
    if lhs.title != rhs.title {return false}
    if lhs.subtitle != rhs.subtitle {return false}
    if lhs.text != rhs.text {return false}
    if lhs.audioPath != rhs.audioPath {return false}
    if lhs._audioDuration != rhs._audioDuration {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ReadletProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ReadletProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "id"),
    2: .standard(proto: "created_at"),
    3: .same(proto: "title"),
    4: .standard(proto: "title_emoji"),
    8: .same(proto: "color"),
    5: .same(proto: "blurb"),
    6: .standard(proto: "category_ids"),
    7: .same(proto: "chapters"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.id) }()
      case 2: try { try decoder.decodeSingularMessageField(value: &self._createdAt) }()
      case 3: try { try decoder.decodeSingularStringField(value: &self.title) }()
      case 4: try { try decoder.decodeSingularStringField(value: &self.titleEmoji) }()
      case 5: try { try decoder.decodeSingularStringField(value: &self.blurb) }()
      case 6: try { try decoder.decodeRepeatedStringField(value: &self.categoryIds) }()
      case 7: try { try decoder.decodeRepeatedMessageField(value: &self.chapters) }()
      case 8: try { try decoder.decodeSingularEnumField(value: &self.color) }()
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
    try { if let v = self._createdAt {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    } }()
    if !self.title.isEmpty {
      try visitor.visitSingularStringField(value: self.title, fieldNumber: 3)
    }
    if !self.titleEmoji.isEmpty {
      try visitor.visitSingularStringField(value: self.titleEmoji, fieldNumber: 4)
    }
    if !self.blurb.isEmpty {
      try visitor.visitSingularStringField(value: self.blurb, fieldNumber: 5)
    }
    if !self.categoryIds.isEmpty {
      try visitor.visitRepeatedStringField(value: self.categoryIds, fieldNumber: 6)
    }
    if !self.chapters.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.chapters, fieldNumber: 7)
    }
    if self.color != .undefined {
      try visitor.visitSingularEnumField(value: self.color, fieldNumber: 8)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ReadletProto, rhs: ReadletProto) -> Bool {
    if lhs.id != rhs.id {return false}
    if lhs._createdAt != rhs._createdAt {return false}
    if lhs.title != rhs.title {return false}
    if lhs.titleEmoji != rhs.titleEmoji {return false}
    if lhs.color != rhs.color {return false}
    if lhs.blurb != rhs.blurb {return false}
    if lhs.categoryIds != rhs.categoryIds {return false}
    if lhs.chapters != rhs.chapters {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}
