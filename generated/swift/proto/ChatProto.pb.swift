// DO NOT EDIT.
// swift-format-ignore-file
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: ChatProto.proto
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

struct ChatActivityProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  /// Machine identifier, LLM-readable, e.g. "compare-and-contrast", "writing-challenge"
  var name: String = String()

  /// How it should be diplayed to the user
  var displayName: String = String()

  var descriptionPrompt: String = String()

  var actionPrompt: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct ChatSystemMessageProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var text: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct ChatAssistantMessageProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var text: String = String()

  var activityName: [String] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct ChatUserMessageProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  /// Explicitly entered by the user
  var text: String = String()

  /// User selected one of the activities
  var actionName: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct ChatMessageProto {
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

  var type: ChatMessageProto.OneOf_Type? = nil

  var system: ChatSystemMessageProto {
    get {
      if case .system(let v)? = type {return v}
      return ChatSystemMessageProto()
    }
    set {type = .system(newValue)}
  }

  var assistant: ChatAssistantMessageProto {
    get {
      if case .assistant(let v)? = type {return v}
      return ChatAssistantMessageProto()
    }
    set {type = .assistant(newValue)}
  }

  var user: ChatUserMessageProto {
    get {
      if case .user(let v)? = type {return v}
      return ChatUserMessageProto()
    }
    set {type = .user(newValue)}
  }

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum OneOf_Type: Equatable {
    case system(ChatSystemMessageProto)
    case assistant(ChatAssistantMessageProto)
    case user(ChatUserMessageProto)

  #if !swift(>=4.1)
    static func ==(lhs: ChatMessageProto.OneOf_Type, rhs: ChatMessageProto.OneOf_Type) -> Bool {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch (lhs, rhs) {
      case (.system, .system): return {
        guard case .system(let l) = lhs, case .system(let r) = rhs else { preconditionFailure() }
        return l == r
      }()
      case (.assistant, .assistant): return {
        guard case .assistant(let l) = lhs, case .assistant(let r) = rhs else { preconditionFailure() }
        return l == r
      }()
      case (.user, .user): return {
        guard case .user(let l) = lhs, case .user(let r) = rhs else { preconditionFailure() }
        return l == r
      }()
      default: return false
      }
    }
  #endif
  }

  init() {}

  fileprivate var _createdAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
}

#if swift(>=5.5) && canImport(_Concurrency)
extension ChatActivityProto: @unchecked Sendable {}
extension ChatSystemMessageProto: @unchecked Sendable {}
extension ChatAssistantMessageProto: @unchecked Sendable {}
extension ChatUserMessageProto: @unchecked Sendable {}
extension ChatMessageProto: @unchecked Sendable {}
extension ChatMessageProto.OneOf_Type: @unchecked Sendable {}
#endif  // swift(>=5.5) && canImport(_Concurrency)

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension ChatActivityProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ChatActivityProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "name"),
    2: .standard(proto: "display_name"),
    3: .standard(proto: "description_prompt"),
    4: .standard(proto: "action_prompt"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.name) }()
      case 2: try { try decoder.decodeSingularStringField(value: &self.displayName) }()
      case 3: try { try decoder.decodeSingularStringField(value: &self.descriptionPrompt) }()
      case 4: try { try decoder.decodeSingularStringField(value: &self.actionPrompt) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.name.isEmpty {
      try visitor.visitSingularStringField(value: self.name, fieldNumber: 1)
    }
    if !self.displayName.isEmpty {
      try visitor.visitSingularStringField(value: self.displayName, fieldNumber: 2)
    }
    if !self.descriptionPrompt.isEmpty {
      try visitor.visitSingularStringField(value: self.descriptionPrompt, fieldNumber: 3)
    }
    if !self.actionPrompt.isEmpty {
      try visitor.visitSingularStringField(value: self.actionPrompt, fieldNumber: 4)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ChatActivityProto, rhs: ChatActivityProto) -> Bool {
    if lhs.name != rhs.name {return false}
    if lhs.displayName != rhs.displayName {return false}
    if lhs.descriptionPrompt != rhs.descriptionPrompt {return false}
    if lhs.actionPrompt != rhs.actionPrompt {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ChatSystemMessageProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ChatSystemMessageProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "text"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.text) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.text.isEmpty {
      try visitor.visitSingularStringField(value: self.text, fieldNumber: 1)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ChatSystemMessageProto, rhs: ChatSystemMessageProto) -> Bool {
    if lhs.text != rhs.text {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ChatAssistantMessageProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ChatAssistantMessageProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "text"),
    2: .standard(proto: "activity_name"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.text) }()
      case 2: try { try decoder.decodeRepeatedStringField(value: &self.activityName) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.text.isEmpty {
      try visitor.visitSingularStringField(value: self.text, fieldNumber: 1)
    }
    if !self.activityName.isEmpty {
      try visitor.visitRepeatedStringField(value: self.activityName, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ChatAssistantMessageProto, rhs: ChatAssistantMessageProto) -> Bool {
    if lhs.text != rhs.text {return false}
    if lhs.activityName != rhs.activityName {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ChatUserMessageProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ChatUserMessageProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "text"),
    2: .standard(proto: "action_name"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.text) }()
      case 2: try { try decoder.decodeSingularStringField(value: &self.actionName) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.text.isEmpty {
      try visitor.visitSingularStringField(value: self.text, fieldNumber: 1)
    }
    if !self.actionName.isEmpty {
      try visitor.visitSingularStringField(value: self.actionName, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ChatUserMessageProto, rhs: ChatUserMessageProto) -> Bool {
    if lhs.text != rhs.text {return false}
    if lhs.actionName != rhs.actionName {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ChatMessageProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ChatMessageProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "created_at"),
    2: .same(proto: "system"),
    3: .same(proto: "assistant"),
    4: .same(proto: "user"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularMessageField(value: &self._createdAt) }()
      case 2: try {
        var v: ChatSystemMessageProto?
        var hadOneofValue = false
        if let current = self.type {
          hadOneofValue = true
          if case .system(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.type = .system(v)
        }
      }()
      case 3: try {
        var v: ChatAssistantMessageProto?
        var hadOneofValue = false
        if let current = self.type {
          hadOneofValue = true
          if case .assistant(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.type = .assistant(v)
        }
      }()
      case 4: try {
        var v: ChatUserMessageProto?
        var hadOneofValue = false
        if let current = self.type {
          hadOneofValue = true
          if case .user(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.type = .user(v)
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
    try { if let v = self._createdAt {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 1)
    } }()
    switch self.type {
    case .system?: try {
      guard case .system(let v)? = self.type else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    }()
    case .assistant?: try {
      guard case .assistant(let v)? = self.type else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 3)
    }()
    case .user?: try {
      guard case .user(let v)? = self.type else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 4)
    }()
    case nil: break
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ChatMessageProto, rhs: ChatMessageProto) -> Bool {
    if lhs._createdAt != rhs._createdAt {return false}
    if lhs.type != rhs.type {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}