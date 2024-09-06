// DO NOT EDIT.
// swift-format-ignore-file
// swiftlint:disable all
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: CommonProto.proto
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

struct UserAgentProto: @unchecked Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var userAgent: String {
    get {return _storage._userAgent}
    set {_uniqueStorage()._userAgent = newValue}
  }

  var device: DeviceProto {
    get {return _storage._device ?? DeviceProto()}
    set {_uniqueStorage()._device = newValue}
  }
  /// Returns true if `device` has been explicitly set.
  var hasDevice: Bool {return _storage._device != nil}
  /// Clears the value of `device`. Subsequent reads from it will return its default value.
  mutating func clearDevice() {_uniqueStorage()._device = nil}

  var locale: LocaleProto {
    get {return _storage._locale ?? LocaleProto()}
    set {_uniqueStorage()._locale = newValue}
  }
  /// Returns true if `locale` has been explicitly set.
  var hasLocale: Bool {return _storage._locale != nil}
  /// Clears the value of `locale`. Subsequent reads from it will return its default value.
  mutating func clearLocale() {_uniqueStorage()._locale = nil}

  var location: LocationProto {
    get {return _storage._location ?? LocationProto()}
    set {_uniqueStorage()._location = newValue}
  }
  /// Returns true if `location` has been explicitly set.
  var hasLocation: Bool {return _storage._location != nil}
  /// Clears the value of `location`. Subsequent reads from it will return its default value.
  mutating func clearLocation() {_uniqueStorage()._location = nil}

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _storage = _StorageClass.defaultInstance
}

struct LocaleProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var language: String = String()

  var country: String = String()

  var timeZone: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct LocationProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var regionCode: String = String()

  var country: String = String()

  var city: String = String()

  var timeZone: String = String()

  var latitude: Double = 0

  var longitude: Double = 0

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct DeviceProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var type: DeviceProto.OneOf_Type? = nil

  var ios: IOSDeviceProto {
    get {
      if case .ios(let v)? = type {return v}
      return IOSDeviceProto()
    }
    set {type = .ios(newValue)}
  }

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum OneOf_Type: Equatable, Sendable {
    case ios(IOSDeviceProto)

  }

  init() {}
}

struct IOSDeviceProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var deviceModel: String = String()

  var deviceIdentifier: String = String()

  var isSimulator: Bool = false

  var osName: String = String()

  var osVersion: String = String()

  var appBundleName: String = String()

  var appBundleVersion: String = String()

  var appBuildNumber: String = String()

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension UserAgentProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "UserAgentProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "user_agent"),
    2: .same(proto: "device"),
    3: .same(proto: "locale"),
    4: .same(proto: "location"),
  ]

  fileprivate class _StorageClass {
    var _userAgent: String = String()
    var _device: DeviceProto? = nil
    var _locale: LocaleProto? = nil
    var _location: LocationProto? = nil

    #if swift(>=5.10)
      // This property is used as the initial default value for new instances of the type.
      // The type itself is protecting the reference to its storage via CoW semantics.
      // This will force a copy to be made of this reference when the first mutation occurs;
      // hence, it is safe to mark this as `nonisolated(unsafe)`.
      static nonisolated(unsafe) let defaultInstance = _StorageClass()
    #else
      static let defaultInstance = _StorageClass()
    #endif

    private init() {}

    init(copying source: _StorageClass) {
      _userAgent = source._userAgent
      _device = source._device
      _locale = source._locale
      _location = source._location
    }
  }

  fileprivate mutating func _uniqueStorage() -> _StorageClass {
    if !isKnownUniquelyReferenced(&_storage) {
      _storage = _StorageClass(copying: _storage)
    }
    return _storage
  }

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    _ = _uniqueStorage()
    try withExtendedLifetime(_storage) { (_storage: _StorageClass) in
      while let fieldNumber = try decoder.nextFieldNumber() {
        // The use of inline closures is to circumvent an issue where the compiler
        // allocates stack space for every case branch when no optimizations are
        // enabled. https://github.com/apple/swift-protobuf/issues/1034
        switch fieldNumber {
        case 1: try { try decoder.decodeSingularStringField(value: &_storage._userAgent) }()
        case 2: try { try decoder.decodeSingularMessageField(value: &_storage._device) }()
        case 3: try { try decoder.decodeSingularMessageField(value: &_storage._locale) }()
        case 4: try { try decoder.decodeSingularMessageField(value: &_storage._location) }()
        default: break
        }
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    try withExtendedLifetime(_storage) { (_storage: _StorageClass) in
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every if/case branch local when no optimizations
      // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
      // https://github.com/apple/swift-protobuf/issues/1182
      if !_storage._userAgent.isEmpty {
        try visitor.visitSingularStringField(value: _storage._userAgent, fieldNumber: 1)
      }
      try { if let v = _storage._device {
        try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
      } }()
      try { if let v = _storage._locale {
        try visitor.visitSingularMessageField(value: v, fieldNumber: 3)
      } }()
      try { if let v = _storage._location {
        try visitor.visitSingularMessageField(value: v, fieldNumber: 4)
      } }()
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: UserAgentProto, rhs: UserAgentProto) -> Bool {
    if lhs._storage !== rhs._storage {
      let storagesAreEqual: Bool = withExtendedLifetime((lhs._storage, rhs._storage)) { (_args: (_StorageClass, _StorageClass)) in
        let _storage = _args.0
        let rhs_storage = _args.1
        if _storage._userAgent != rhs_storage._userAgent {return false}
        if _storage._device != rhs_storage._device {return false}
        if _storage._locale != rhs_storage._locale {return false}
        if _storage._location != rhs_storage._location {return false}
        return true
      }
      if !storagesAreEqual {return false}
    }
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension LocaleProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "LocaleProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "language"),
    2: .same(proto: "country"),
    3: .standard(proto: "time_zone"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.language) }()
      case 2: try { try decoder.decodeSingularStringField(value: &self.country) }()
      case 3: try { try decoder.decodeSingularStringField(value: &self.timeZone) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.language.isEmpty {
      try visitor.visitSingularStringField(value: self.language, fieldNumber: 1)
    }
    if !self.country.isEmpty {
      try visitor.visitSingularStringField(value: self.country, fieldNumber: 2)
    }
    if !self.timeZone.isEmpty {
      try visitor.visitSingularStringField(value: self.timeZone, fieldNumber: 3)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: LocaleProto, rhs: LocaleProto) -> Bool {
    if lhs.language != rhs.language {return false}
    if lhs.country != rhs.country {return false}
    if lhs.timeZone != rhs.timeZone {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension LocationProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "LocationProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "region_code"),
    2: .same(proto: "country"),
    3: .same(proto: "city"),
    4: .standard(proto: "time_zone"),
    5: .same(proto: "latitude"),
    6: .same(proto: "longitude"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.regionCode) }()
      case 2: try { try decoder.decodeSingularStringField(value: &self.country) }()
      case 3: try { try decoder.decodeSingularStringField(value: &self.city) }()
      case 4: try { try decoder.decodeSingularStringField(value: &self.timeZone) }()
      case 5: try { try decoder.decodeSingularDoubleField(value: &self.latitude) }()
      case 6: try { try decoder.decodeSingularDoubleField(value: &self.longitude) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.regionCode.isEmpty {
      try visitor.visitSingularStringField(value: self.regionCode, fieldNumber: 1)
    }
    if !self.country.isEmpty {
      try visitor.visitSingularStringField(value: self.country, fieldNumber: 2)
    }
    if !self.city.isEmpty {
      try visitor.visitSingularStringField(value: self.city, fieldNumber: 3)
    }
    if !self.timeZone.isEmpty {
      try visitor.visitSingularStringField(value: self.timeZone, fieldNumber: 4)
    }
    if self.latitude.bitPattern != 0 {
      try visitor.visitSingularDoubleField(value: self.latitude, fieldNumber: 5)
    }
    if self.longitude.bitPattern != 0 {
      try visitor.visitSingularDoubleField(value: self.longitude, fieldNumber: 6)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: LocationProto, rhs: LocationProto) -> Bool {
    if lhs.regionCode != rhs.regionCode {return false}
    if lhs.country != rhs.country {return false}
    if lhs.city != rhs.city {return false}
    if lhs.timeZone != rhs.timeZone {return false}
    if lhs.latitude != rhs.latitude {return false}
    if lhs.longitude != rhs.longitude {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension DeviceProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "DeviceProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "ios"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try {
        var v: IOSDeviceProto?
        var hadOneofValue = false
        if let current = self.type {
          hadOneofValue = true
          if case .ios(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.type = .ios(v)
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
    try { if case .ios(let v)? = self.type {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 1)
    } }()
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: DeviceProto, rhs: DeviceProto) -> Bool {
    if lhs.type != rhs.type {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension IOSDeviceProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "IOSDeviceProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "device_model"),
    2: .standard(proto: "device_identifier"),
    3: .standard(proto: "is_simulator"),
    4: .standard(proto: "os_name"),
    5: .standard(proto: "os_version"),
    6: .standard(proto: "app_bundle_name"),
    7: .standard(proto: "app_bundle_version"),
    8: .standard(proto: "app_build_number"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.deviceModel) }()
      case 2: try { try decoder.decodeSingularStringField(value: &self.deviceIdentifier) }()
      case 3: try { try decoder.decodeSingularBoolField(value: &self.isSimulator) }()
      case 4: try { try decoder.decodeSingularStringField(value: &self.osName) }()
      case 5: try { try decoder.decodeSingularStringField(value: &self.osVersion) }()
      case 6: try { try decoder.decodeSingularStringField(value: &self.appBundleName) }()
      case 7: try { try decoder.decodeSingularStringField(value: &self.appBundleVersion) }()
      case 8: try { try decoder.decodeSingularStringField(value: &self.appBuildNumber) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.deviceModel.isEmpty {
      try visitor.visitSingularStringField(value: self.deviceModel, fieldNumber: 1)
    }
    if !self.deviceIdentifier.isEmpty {
      try visitor.visitSingularStringField(value: self.deviceIdentifier, fieldNumber: 2)
    }
    if self.isSimulator != false {
      try visitor.visitSingularBoolField(value: self.isSimulator, fieldNumber: 3)
    }
    if !self.osName.isEmpty {
      try visitor.visitSingularStringField(value: self.osName, fieldNumber: 4)
    }
    if !self.osVersion.isEmpty {
      try visitor.visitSingularStringField(value: self.osVersion, fieldNumber: 5)
    }
    if !self.appBundleName.isEmpty {
      try visitor.visitSingularStringField(value: self.appBundleName, fieldNumber: 6)
    }
    if !self.appBundleVersion.isEmpty {
      try visitor.visitSingularStringField(value: self.appBundleVersion, fieldNumber: 7)
    }
    if !self.appBuildNumber.isEmpty {
      try visitor.visitSingularStringField(value: self.appBuildNumber, fieldNumber: 8)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: IOSDeviceProto, rhs: IOSDeviceProto) -> Bool {
    if lhs.deviceModel != rhs.deviceModel {return false}
    if lhs.deviceIdentifier != rhs.deviceIdentifier {return false}
    if lhs.isSimulator != rhs.isSimulator {return false}
    if lhs.osName != rhs.osName {return false}
    if lhs.osVersion != rhs.osVersion {return false}
    if lhs.appBundleName != rhs.appBundleName {return false}
    if lhs.appBundleVersion != rhs.appBundleVersion {return false}
    if lhs.appBuildNumber != rhs.appBuildNumber {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}
