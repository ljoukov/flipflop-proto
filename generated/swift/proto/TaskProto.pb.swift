// DO NOT EDIT.
// swift-format-ignore-file
// swiftlint:disable all
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: TaskProto.proto
//
// For information on using the generated types, please see the documentation:
//   https://github.com/apple/swift-protobuf/

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

struct TaskProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var taskID: String = String()

  var createdAt: SwiftProtobuf.Google_Protobuf_Timestamp {
    get {return _createdAt ?? SwiftProtobuf.Google_Protobuf_Timestamp()}
    set {_createdAt = newValue}
  }
  /// Returns true if `createdAt` has been explicitly set.
  var hasCreatedAt: Bool {return self._createdAt != nil}
  /// Clears the value of `createdAt`. Subsequent reads from it will return its default value.
  mutating func clearCreatedAt() {self._createdAt = nil}

  /// IDs start at 10
  var type: TaskProto.OneOf_Type? = nil

  var generatePodcast: GeneratePodcastTaskProto {
    get {
      if case .generatePodcast(let v)? = type {return v}
      return GeneratePodcastTaskProto()
    }
    set {type = .generatePodcast(newValue)}
  }

  var generateStory: GeneratePodcastStoryTaskProto {
    get {
      if case .generateStory(let v)? = type {return v}
      return GeneratePodcastStoryTaskProto()
    }
    set {type = .generateStory(newValue)}
  }

  var createSuggestions: CreatePodcastSuggestionsTaskProto {
    get {
      if case .createSuggestions(let v)? = type {return v}
      return CreatePodcastSuggestionsTaskProto()
    }
    set {type = .createSuggestions(newValue)}
  }

  var generateSuggestions: GeneratePodcastSuggestionsTaskProto {
    get {
      if case .generateSuggestions(let v)? = type {return v}
      return GeneratePodcastSuggestionsTaskProto()
    }
    set {type = .generateSuggestions(newValue)}
  }

  var publishSuggestions: PublishPodcastSuggestionsTaskProto {
    get {
      if case .publishSuggestions(let v)? = type {return v}
      return PublishPodcastSuggestionsTaskProto()
    }
    set {type = .publishSuggestions(newValue)}
  }

  var unknownFields = SwiftProtobuf.UnknownStorage()

  /// IDs start at 10
  enum OneOf_Type: Equatable, Sendable {
    case generatePodcast(GeneratePodcastTaskProto)
    case generateStory(GeneratePodcastStoryTaskProto)
    case createSuggestions(CreatePodcastSuggestionsTaskProto)
    case generateSuggestions(GeneratePodcastSuggestionsTaskProto)
    case publishSuggestions(PublishPodcastSuggestionsTaskProto)

  }

  init() {}

  fileprivate var _createdAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
}

struct GeneratePodcastTaskProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var podcastID: String = String()

  var generateCards: Bool = false

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct GeneratePodcastStoryTaskProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var storyID: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct CreatePodcastSuggestionsTaskProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var userID: String = String()

  var ignorePartiallyGenerated: Bool = false

  var ignoreRecentlyGenerated: Bool = false

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct GeneratePodcastSuggestionsTaskProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var suggestionsID: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct PublishPodcastSuggestionsTaskProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var suggestionsID: String = String()

  var trigger: PublishPodcastSuggestionsTaskProto.OneOf_Trigger? = nil

  var readySuggestedPodcastID: String {
    get {
      if case .readySuggestedPodcastID(let v)? = trigger {return v}
      return String()
    }
    set {trigger = .readySuggestedPodcastID(newValue)}
  }

  var readySuggestedStoryID: String {
    get {
      if case .readySuggestedStoryID(let v)? = trigger {return v}
      return String()
    }
    set {trigger = .readySuggestedStoryID(newValue)}
  }

  var cleanup: Bool {
    get {
      if case .cleanup(let v)? = trigger {return v}
      return false
    }
    set {trigger = .cleanup(newValue)}
  }

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum OneOf_Trigger: Equatable, Sendable {
    case readySuggestedPodcastID(String)
    case readySuggestedStoryID(String)
    case cleanup(Bool)

  }

  init() {}
}

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension TaskProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "TaskProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "task_id"),
    2: .standard(proto: "created_at"),
    10: .standard(proto: "generate_podcast"),
    11: .standard(proto: "generate_story"),
    12: .standard(proto: "create_suggestions"),
    13: .standard(proto: "generate_suggestions"),
    14: .standard(proto: "publish_suggestions"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.taskID) }()
      case 2: try { try decoder.decodeSingularMessageField(value: &self._createdAt) }()
      case 10: try {
        var v: GeneratePodcastTaskProto?
        var hadOneofValue = false
        if let current = self.type {
          hadOneofValue = true
          if case .generatePodcast(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.type = .generatePodcast(v)
        }
      }()
      case 11: try {
        var v: GeneratePodcastStoryTaskProto?
        var hadOneofValue = false
        if let current = self.type {
          hadOneofValue = true
          if case .generateStory(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.type = .generateStory(v)
        }
      }()
      case 12: try {
        var v: CreatePodcastSuggestionsTaskProto?
        var hadOneofValue = false
        if let current = self.type {
          hadOneofValue = true
          if case .createSuggestions(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.type = .createSuggestions(v)
        }
      }()
      case 13: try {
        var v: GeneratePodcastSuggestionsTaskProto?
        var hadOneofValue = false
        if let current = self.type {
          hadOneofValue = true
          if case .generateSuggestions(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.type = .generateSuggestions(v)
        }
      }()
      case 14: try {
        var v: PublishPodcastSuggestionsTaskProto?
        var hadOneofValue = false
        if let current = self.type {
          hadOneofValue = true
          if case .publishSuggestions(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.type = .publishSuggestions(v)
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
    if !self.taskID.isEmpty {
      try visitor.visitSingularStringField(value: self.taskID, fieldNumber: 1)
    }
    try { if let v = self._createdAt {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    } }()
    switch self.type {
    case .generatePodcast?: try {
      guard case .generatePodcast(let v)? = self.type else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 10)
    }()
    case .generateStory?: try {
      guard case .generateStory(let v)? = self.type else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 11)
    }()
    case .createSuggestions?: try {
      guard case .createSuggestions(let v)? = self.type else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 12)
    }()
    case .generateSuggestions?: try {
      guard case .generateSuggestions(let v)? = self.type else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 13)
    }()
    case .publishSuggestions?: try {
      guard case .publishSuggestions(let v)? = self.type else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 14)
    }()
    case nil: break
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: TaskProto, rhs: TaskProto) -> Bool {
    if lhs.taskID != rhs.taskID {return false}
    if lhs._createdAt != rhs._createdAt {return false}
    if lhs.type != rhs.type {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension GeneratePodcastTaskProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "GeneratePodcastTaskProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "podcast_id"),
    2: .standard(proto: "generate_cards"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.podcastID) }()
      case 2: try { try decoder.decodeSingularBoolField(value: &self.generateCards) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.podcastID.isEmpty {
      try visitor.visitSingularStringField(value: self.podcastID, fieldNumber: 1)
    }
    if self.generateCards != false {
      try visitor.visitSingularBoolField(value: self.generateCards, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: GeneratePodcastTaskProto, rhs: GeneratePodcastTaskProto) -> Bool {
    if lhs.podcastID != rhs.podcastID {return false}
    if lhs.generateCards != rhs.generateCards {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension GeneratePodcastStoryTaskProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "GeneratePodcastStoryTaskProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "story_id"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.storyID) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.storyID.isEmpty {
      try visitor.visitSingularStringField(value: self.storyID, fieldNumber: 1)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: GeneratePodcastStoryTaskProto, rhs: GeneratePodcastStoryTaskProto) -> Bool {
    if lhs.storyID != rhs.storyID {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension CreatePodcastSuggestionsTaskProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "CreatePodcastSuggestionsTaskProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "user_id"),
    2: .standard(proto: "ignore_partially_generated"),
    3: .standard(proto: "ignore_recently_generated"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.userID) }()
      case 2: try { try decoder.decodeSingularBoolField(value: &self.ignorePartiallyGenerated) }()
      case 3: try { try decoder.decodeSingularBoolField(value: &self.ignoreRecentlyGenerated) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.userID.isEmpty {
      try visitor.visitSingularStringField(value: self.userID, fieldNumber: 1)
    }
    if self.ignorePartiallyGenerated != false {
      try visitor.visitSingularBoolField(value: self.ignorePartiallyGenerated, fieldNumber: 2)
    }
    if self.ignoreRecentlyGenerated != false {
      try visitor.visitSingularBoolField(value: self.ignoreRecentlyGenerated, fieldNumber: 3)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: CreatePodcastSuggestionsTaskProto, rhs: CreatePodcastSuggestionsTaskProto) -> Bool {
    if lhs.userID != rhs.userID {return false}
    if lhs.ignorePartiallyGenerated != rhs.ignorePartiallyGenerated {return false}
    if lhs.ignoreRecentlyGenerated != rhs.ignoreRecentlyGenerated {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension GeneratePodcastSuggestionsTaskProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "GeneratePodcastSuggestionsTaskProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "suggestions_id"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.suggestionsID) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.suggestionsID.isEmpty {
      try visitor.visitSingularStringField(value: self.suggestionsID, fieldNumber: 1)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: GeneratePodcastSuggestionsTaskProto, rhs: GeneratePodcastSuggestionsTaskProto) -> Bool {
    if lhs.suggestionsID != rhs.suggestionsID {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension PublishPodcastSuggestionsTaskProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "PublishPodcastSuggestionsTaskProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "suggestions_id"),
    2: .standard(proto: "ready_suggested_podcast_id"),
    3: .standard(proto: "ready_suggested_story_id"),
    4: .same(proto: "cleanup"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.suggestionsID) }()
      case 2: try {
        var v: String?
        try decoder.decodeSingularStringField(value: &v)
        if let v = v {
          if self.trigger != nil {try decoder.handleConflictingOneOf()}
          self.trigger = .readySuggestedPodcastID(v)
        }
      }()
      case 3: try {
        var v: String?
        try decoder.decodeSingularStringField(value: &v)
        if let v = v {
          if self.trigger != nil {try decoder.handleConflictingOneOf()}
          self.trigger = .readySuggestedStoryID(v)
        }
      }()
      case 4: try {
        var v: Bool?
        try decoder.decodeSingularBoolField(value: &v)
        if let v = v {
          if self.trigger != nil {try decoder.handleConflictingOneOf()}
          self.trigger = .cleanup(v)
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
    if !self.suggestionsID.isEmpty {
      try visitor.visitSingularStringField(value: self.suggestionsID, fieldNumber: 1)
    }
    switch self.trigger {
    case .readySuggestedPodcastID?: try {
      guard case .readySuggestedPodcastID(let v)? = self.trigger else { preconditionFailure() }
      try visitor.visitSingularStringField(value: v, fieldNumber: 2)
    }()
    case .readySuggestedStoryID?: try {
      guard case .readySuggestedStoryID(let v)? = self.trigger else { preconditionFailure() }
      try visitor.visitSingularStringField(value: v, fieldNumber: 3)
    }()
    case .cleanup?: try {
      guard case .cleanup(let v)? = self.trigger else { preconditionFailure() }
      try visitor.visitSingularBoolField(value: v, fieldNumber: 4)
    }()
    case nil: break
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: PublishPodcastSuggestionsTaskProto, rhs: PublishPodcastSuggestionsTaskProto) -> Bool {
    if lhs.suggestionsID != rhs.suggestionsID {return false}
    if lhs.trigger != rhs.trigger {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}
