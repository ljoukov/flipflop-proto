// DO NOT EDIT.
// swift-format-ignore-file
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: UserDataProto.proto
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

struct StoryUserDataProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var storyID: String = String()

  var lastModifiedAt: SwiftProtobuf.Google_Protobuf_Timestamp {
    get {return _lastModifiedAt ?? SwiftProtobuf.Google_Protobuf_Timestamp()}
    set {_lastModifiedAt = newValue}
  }
  /// Returns true if `lastModifiedAt` has been explicitly set.
  var hasLastModifiedAt: Bool {return self._lastModifiedAt != nil}
  /// Clears the value of `lastModifiedAt`. Subsequent reads from it will return its default value.
  mutating func clearLastModifiedAt() {self._lastModifiedAt = nil}

  var liked: Bool = false

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _lastModifiedAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
}

struct UserDataProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var storiesData: [StoryUserDataProto] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct GetUserDataRequestProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct GetUserDataResponseProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var userData: UserDataProto {
    get {return _userData ?? UserDataProto()}
    set {_userData = newValue}
  }
  /// Returns true if `userData` has been explicitly set.
  var hasUserData: Bool {return self._userData != nil}
  /// Clears the value of `userData`. Subsequent reads from it will return its default value.
  mutating func clearUserData() {self._userData = nil}

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _userData: UserDataProto? = nil
}

struct UserApiRequestProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var request: UserApiRequestProto.OneOf_Request? = nil

  var getUserData: GetUserDataRequestProto {
    get {
      if case .getUserData(let v)? = request {return v}
      return GetUserDataRequestProto()
    }
    set {request = .getUserData(newValue)}
  }

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum OneOf_Request: Equatable {
    case getUserData(GetUserDataRequestProto)

  #if !swift(>=4.1)
    static func ==(lhs: UserApiRequestProto.OneOf_Request, rhs: UserApiRequestProto.OneOf_Request) -> Bool {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch (lhs, rhs) {
      case (.getUserData, .getUserData): return {
        guard case .getUserData(let l) = lhs, case .getUserData(let r) = rhs else { preconditionFailure() }
        return l == r
      }()
      }
    }
  #endif
  }

  init() {}
}

struct UserApiResponseProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var response: UserApiResponseProto.OneOf_Response? = nil

  var getUserData: GetUserDataResponseProto {
    get {
      if case .getUserData(let v)? = response {return v}
      return GetUserDataResponseProto()
    }
    set {response = .getUserData(newValue)}
  }

  var latencies: Dictionary<String,SwiftProtobuf.Google_Protobuf_Duration> = [:]

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum OneOf_Response: Equatable {
    case getUserData(GetUserDataResponseProto)

  #if !swift(>=4.1)
    static func ==(lhs: UserApiResponseProto.OneOf_Response, rhs: UserApiResponseProto.OneOf_Response) -> Bool {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch (lhs, rhs) {
      case (.getUserData, .getUserData): return {
        guard case .getUserData(let l) = lhs, case .getUserData(let r) = rhs else { preconditionFailure() }
        return l == r
      }()
      }
    }
  #endif
  }

  init() {}
}

#if swift(>=5.5) && canImport(_Concurrency)
extension StoryUserDataProto: @unchecked Sendable {}
extension UserDataProto: @unchecked Sendable {}
extension GetUserDataRequestProto: @unchecked Sendable {}
extension GetUserDataResponseProto: @unchecked Sendable {}
extension UserApiRequestProto: @unchecked Sendable {}
extension UserApiRequestProto.OneOf_Request: @unchecked Sendable {}
extension UserApiResponseProto: @unchecked Sendable {}
extension UserApiResponseProto.OneOf_Response: @unchecked Sendable {}
#endif  // swift(>=5.5) && canImport(_Concurrency)

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension StoryUserDataProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "StoryUserDataProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "story_id"),
    2: .standard(proto: "last_modified_at"),
    3: .same(proto: "liked"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.storyID) }()
      case 2: try { try decoder.decodeSingularMessageField(value: &self._lastModifiedAt) }()
      case 3: try { try decoder.decodeSingularBoolField(value: &self.liked) }()
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
    try { if let v = self._lastModifiedAt {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    } }()
    if self.liked != false {
      try visitor.visitSingularBoolField(value: self.liked, fieldNumber: 3)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: StoryUserDataProto, rhs: StoryUserDataProto) -> Bool {
    if lhs.storyID != rhs.storyID {return false}
    if lhs._lastModifiedAt != rhs._lastModifiedAt {return false}
    if lhs.liked != rhs.liked {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension UserDataProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "UserDataProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "stories_data"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeRepeatedMessageField(value: &self.storiesData) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.storiesData.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.storiesData, fieldNumber: 1)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: UserDataProto, rhs: UserDataProto) -> Bool {
    if lhs.storiesData != rhs.storiesData {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension GetUserDataRequestProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "GetUserDataRequestProto"
  static let _protobuf_nameMap = SwiftProtobuf._NameMap()

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let _ = try decoder.nextFieldNumber() {
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: GetUserDataRequestProto, rhs: GetUserDataRequestProto) -> Bool {
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension GetUserDataResponseProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "GetUserDataResponseProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "user_data"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularMessageField(value: &self._userData) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    try { if let v = self._userData {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 1)
    } }()
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: GetUserDataResponseProto, rhs: GetUserDataResponseProto) -> Bool {
    if lhs._userData != rhs._userData {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension UserApiRequestProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "UserApiRequestProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "get_user_data"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try {
        var v: GetUserDataRequestProto?
        var hadOneofValue = false
        if let current = self.request {
          hadOneofValue = true
          if case .getUserData(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.request = .getUserData(v)
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
    try { if case .getUserData(let v)? = self.request {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 1)
    } }()
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: UserApiRequestProto, rhs: UserApiRequestProto) -> Bool {
    if lhs.request != rhs.request {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension UserApiResponseProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "UserApiResponseProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "get_user_data"),
    5: .same(proto: "latencies"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try {
        var v: GetUserDataResponseProto?
        var hadOneofValue = false
        if let current = self.response {
          hadOneofValue = true
          if case .getUserData(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.response = .getUserData(v)
        }
      }()
      case 5: try { try decoder.decodeMapField(fieldType: SwiftProtobuf._ProtobufMessageMap<SwiftProtobuf.ProtobufString,SwiftProtobuf.Google_Protobuf_Duration>.self, value: &self.latencies) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    try { if case .getUserData(let v)? = self.response {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 1)
    } }()
    if !self.latencies.isEmpty {
      try visitor.visitMapField(fieldType: SwiftProtobuf._ProtobufMessageMap<SwiftProtobuf.ProtobufString,SwiftProtobuf.Google_Protobuf_Duration>.self, value: self.latencies, fieldNumber: 5)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: UserApiResponseProto, rhs: UserApiResponseProto) -> Bool {
    if lhs.response != rhs.response {return false}
    if lhs.latencies != rhs.latencies {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}
