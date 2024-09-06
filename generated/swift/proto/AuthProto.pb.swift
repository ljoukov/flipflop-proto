// DO NOT EDIT.
// swift-format-ignore-file
// swiftlint:disable all
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: AuthProto.proto
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

struct UserAuthProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var userID: String = String()

  var accessToken: String = String()

  var expiresAt: SwiftProtobuf.Google_Protobuf_Timestamp {
    get {return _expiresAt ?? SwiftProtobuf.Google_Protobuf_Timestamp()}
    set {_expiresAt = newValue}
  }
  /// Returns true if `expiresAt` has been explicitly set.
  var hasExpiresAt: Bool {return self._expiresAt != nil}
  /// Clears the value of `expiresAt`. Subsequent reads from it will return its default value.
  mutating func clearExpiresAt() {self._expiresAt = nil}

  var refreshToken: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _expiresAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
}

struct AuthApiRequestProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var request: AuthApiRequestProto.OneOf_Request? = nil

  var signInWithIdp: SignInWithIdpRequestProto {
    get {
      if case .signInWithIdp(let v)? = request {return v}
      return SignInWithIdpRequestProto()
    }
    set {request = .signInWithIdp(newValue)}
  }

  var signInWithPassword: SignInWithPasswordRequestProto {
    get {
      if case .signInWithPassword(let v)? = request {return v}
      return SignInWithPasswordRequestProto()
    }
    set {request = .signInWithPassword(newValue)}
  }

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum OneOf_Request: Equatable, Sendable {
    case signInWithIdp(SignInWithIdpRequestProto)
    case signInWithPassword(SignInWithPasswordRequestProto)

  }

  init() {}
}

struct AuthApiResponseProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var response: AuthApiResponseProto.OneOf_Response? = nil

  var signInWithIdp: SignInWithIdpResponseProto {
    get {
      if case .signInWithIdp(let v)? = response {return v}
      return SignInWithIdpResponseProto()
    }
    set {response = .signInWithIdp(newValue)}
  }

  var signInWithPassword: SignInWithPasswordResponseProto {
    get {
      if case .signInWithPassword(let v)? = response {return v}
      return SignInWithPasswordResponseProto()
    }
    set {response = .signInWithPassword(newValue)}
  }

  var latencies: Dictionary<String,SwiftProtobuf.Google_Protobuf_Duration> = [:]

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum OneOf_Response: Equatable, Sendable {
    case signInWithIdp(SignInWithIdpResponseProto)
    case signInWithPassword(SignInWithPasswordResponseProto)

  }

  init() {}
}

struct SignInWithIdpRequestProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var idToken: String = String()

  var providerID: String = String()

  var rawNonce: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct SignInWithIdpResponseProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var encodedUserAuth: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct SignInWithPasswordRequestProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var email: String = String()

  var password: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct SignInWithPasswordResponseProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var encodedUserAuth: String = String()

  var error: SignInWithPasswordResponseProto.Error = .noError

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum Error: SwiftProtobuf.Enum, Swift.CaseIterable {
    typealias RawValue = Int
    case noError // = 0
    case invalidPassword // = 1
    case emailNotFound // = 2
    case UNRECOGNIZED(Int)

    init() {
      self = .noError
    }

    init?(rawValue: Int) {
      switch rawValue {
      case 0: self = .noError
      case 1: self = .invalidPassword
      case 2: self = .emailNotFound
      default: self = .UNRECOGNIZED(rawValue)
      }
    }

    var rawValue: Int {
      switch self {
      case .noError: return 0
      case .invalidPassword: return 1
      case .emailNotFound: return 2
      case .UNRECOGNIZED(let i): return i
      }
    }

    // The compiler won't synthesize support with the UNRECOGNIZED case.
    static let allCases: [SignInWithPasswordResponseProto.Error] = [
      .noError,
      .invalidPassword,
      .emailNotFound,
    ]

  }

  init() {}
}

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension UserAuthProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "UserAuthProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "user_id"),
    2: .standard(proto: "access_token"),
    3: .standard(proto: "expires_at"),
    4: .standard(proto: "refresh_token"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.userID) }()
      case 2: try { try decoder.decodeSingularStringField(value: &self.accessToken) }()
      case 3: try { try decoder.decodeSingularMessageField(value: &self._expiresAt) }()
      case 4: try { try decoder.decodeSingularStringField(value: &self.refreshToken) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    if !self.userID.isEmpty {
      try visitor.visitSingularStringField(value: self.userID, fieldNumber: 1)
    }
    if !self.accessToken.isEmpty {
      try visitor.visitSingularStringField(value: self.accessToken, fieldNumber: 2)
    }
    try { if let v = self._expiresAt {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 3)
    } }()
    if !self.refreshToken.isEmpty {
      try visitor.visitSingularStringField(value: self.refreshToken, fieldNumber: 4)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: UserAuthProto, rhs: UserAuthProto) -> Bool {
    if lhs.userID != rhs.userID {return false}
    if lhs.accessToken != rhs.accessToken {return false}
    if lhs._expiresAt != rhs._expiresAt {return false}
    if lhs.refreshToken != rhs.refreshToken {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension AuthApiRequestProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "AuthApiRequestProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "sign_in_with_idp"),
    2: .standard(proto: "sign_in_with_password"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try {
        var v: SignInWithIdpRequestProto?
        var hadOneofValue = false
        if let current = self.request {
          hadOneofValue = true
          if case .signInWithIdp(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.request = .signInWithIdp(v)
        }
      }()
      case 2: try {
        var v: SignInWithPasswordRequestProto?
        var hadOneofValue = false
        if let current = self.request {
          hadOneofValue = true
          if case .signInWithPassword(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.request = .signInWithPassword(v)
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
    switch self.request {
    case .signInWithIdp?: try {
      guard case .signInWithIdp(let v)? = self.request else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 1)
    }()
    case .signInWithPassword?: try {
      guard case .signInWithPassword(let v)? = self.request else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    }()
    case nil: break
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: AuthApiRequestProto, rhs: AuthApiRequestProto) -> Bool {
    if lhs.request != rhs.request {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension AuthApiResponseProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "AuthApiResponseProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "sign_in_with_idp"),
    2: .standard(proto: "sign_in_with_password"),
    5: .same(proto: "latencies"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try {
        var v: SignInWithIdpResponseProto?
        var hadOneofValue = false
        if let current = self.response {
          hadOneofValue = true
          if case .signInWithIdp(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.response = .signInWithIdp(v)
        }
      }()
      case 2: try {
        var v: SignInWithPasswordResponseProto?
        var hadOneofValue = false
        if let current = self.response {
          hadOneofValue = true
          if case .signInWithPassword(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.response = .signInWithPassword(v)
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
    switch self.response {
    case .signInWithIdp?: try {
      guard case .signInWithIdp(let v)? = self.response else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 1)
    }()
    case .signInWithPassword?: try {
      guard case .signInWithPassword(let v)? = self.response else { preconditionFailure() }
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    }()
    case nil: break
    }
    if !self.latencies.isEmpty {
      try visitor.visitMapField(fieldType: SwiftProtobuf._ProtobufMessageMap<SwiftProtobuf.ProtobufString,SwiftProtobuf.Google_Protobuf_Duration>.self, value: self.latencies, fieldNumber: 5)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: AuthApiResponseProto, rhs: AuthApiResponseProto) -> Bool {
    if lhs.response != rhs.response {return false}
    if lhs.latencies != rhs.latencies {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension SignInWithIdpRequestProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "SignInWithIdpRequestProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "id_token"),
    2: .standard(proto: "provider_id"),
    3: .standard(proto: "raw_nonce"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.idToken) }()
      case 2: try { try decoder.decodeSingularStringField(value: &self.providerID) }()
      case 3: try { try decoder.decodeSingularStringField(value: &self.rawNonce) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.idToken.isEmpty {
      try visitor.visitSingularStringField(value: self.idToken, fieldNumber: 1)
    }
    if !self.providerID.isEmpty {
      try visitor.visitSingularStringField(value: self.providerID, fieldNumber: 2)
    }
    if !self.rawNonce.isEmpty {
      try visitor.visitSingularStringField(value: self.rawNonce, fieldNumber: 3)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: SignInWithIdpRequestProto, rhs: SignInWithIdpRequestProto) -> Bool {
    if lhs.idToken != rhs.idToken {return false}
    if lhs.providerID != rhs.providerID {return false}
    if lhs.rawNonce != rhs.rawNonce {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension SignInWithIdpResponseProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "SignInWithIdpResponseProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "encoded_user_auth"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.encodedUserAuth) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.encodedUserAuth.isEmpty {
      try visitor.visitSingularStringField(value: self.encodedUserAuth, fieldNumber: 1)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: SignInWithIdpResponseProto, rhs: SignInWithIdpResponseProto) -> Bool {
    if lhs.encodedUserAuth != rhs.encodedUserAuth {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension SignInWithPasswordRequestProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "SignInWithPasswordRequestProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "email"),
    2: .same(proto: "password"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.email) }()
      case 2: try { try decoder.decodeSingularStringField(value: &self.password) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.email.isEmpty {
      try visitor.visitSingularStringField(value: self.email, fieldNumber: 1)
    }
    if !self.password.isEmpty {
      try visitor.visitSingularStringField(value: self.password, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: SignInWithPasswordRequestProto, rhs: SignInWithPasswordRequestProto) -> Bool {
    if lhs.email != rhs.email {return false}
    if lhs.password != rhs.password {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension SignInWithPasswordResponseProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "SignInWithPasswordResponseProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "encoded_user_auth"),
    2: .same(proto: "error"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.encodedUserAuth) }()
      case 2: try { try decoder.decodeSingularEnumField(value: &self.error) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.encodedUserAuth.isEmpty {
      try visitor.visitSingularStringField(value: self.encodedUserAuth, fieldNumber: 1)
    }
    if self.error != .noError {
      try visitor.visitSingularEnumField(value: self.error, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: SignInWithPasswordResponseProto, rhs: SignInWithPasswordResponseProto) -> Bool {
    if lhs.encodedUserAuth != rhs.encodedUserAuth {return false}
    if lhs.error != rhs.error {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension SignInWithPasswordResponseProto.Error: SwiftProtobuf._ProtoNameProviding {
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    0: .same(proto: "NO_ERROR"),
    1: .same(proto: "INVALID_PASSWORD"),
    2: .same(proto: "EMAIL_NOT_FOUND"),
  ]
}
