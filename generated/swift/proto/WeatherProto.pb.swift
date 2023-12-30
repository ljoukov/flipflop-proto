// DO NOT EDIT.
// swift-format-ignore-file
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: WeatherProto.proto
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

enum WeatherConditionProto: SwiftProtobuf.Enum {
  typealias RawValue = Int
  case weatherConditionUnknown // = 0
  case weatherConditionThunderstorm // = 1
  case weatherConditionDrizzle // = 2
  case weatherConditionRain // = 3
  case weatherConditionSnow // = 4
  case weatherConditionMist // = 5
  case weatherConditionSmoke // = 6
  case weatherConditionHaze // = 7
  case weatherConditionDust // = 8
  case weatherConditionFog // = 9
  case weatherConditionSand // = 10
  case weatherConditionAsh // = 11
  case weatherConditionSquall // = 12
  case weatherConditionTornado // = 13
  case weatherConditionClear // = 14
  case weatherConditionClouds // = 15
  case UNRECOGNIZED(Int)

  init() {
    self = .weatherConditionUnknown
  }

  init?(rawValue: Int) {
    switch rawValue {
    case 0: self = .weatherConditionUnknown
    case 1: self = .weatherConditionThunderstorm
    case 2: self = .weatherConditionDrizzle
    case 3: self = .weatherConditionRain
    case 4: self = .weatherConditionSnow
    case 5: self = .weatherConditionMist
    case 6: self = .weatherConditionSmoke
    case 7: self = .weatherConditionHaze
    case 8: self = .weatherConditionDust
    case 9: self = .weatherConditionFog
    case 10: self = .weatherConditionSand
    case 11: self = .weatherConditionAsh
    case 12: self = .weatherConditionSquall
    case 13: self = .weatherConditionTornado
    case 14: self = .weatherConditionClear
    case 15: self = .weatherConditionClouds
    default: self = .UNRECOGNIZED(rawValue)
    }
  }

  var rawValue: Int {
    switch self {
    case .weatherConditionUnknown: return 0
    case .weatherConditionThunderstorm: return 1
    case .weatherConditionDrizzle: return 2
    case .weatherConditionRain: return 3
    case .weatherConditionSnow: return 4
    case .weatherConditionMist: return 5
    case .weatherConditionSmoke: return 6
    case .weatherConditionHaze: return 7
    case .weatherConditionDust: return 8
    case .weatherConditionFog: return 9
    case .weatherConditionSand: return 10
    case .weatherConditionAsh: return 11
    case .weatherConditionSquall: return 12
    case .weatherConditionTornado: return 13
    case .weatherConditionClear: return 14
    case .weatherConditionClouds: return 15
    case .UNRECOGNIZED(let i): return i
    }
  }

}

#if swift(>=4.2)

extension WeatherConditionProto: CaseIterable {
  // The compiler won't synthesize support with the UNRECOGNIZED case.
  static var allCases: [WeatherConditionProto] = [
    .weatherConditionUnknown,
    .weatherConditionThunderstorm,
    .weatherConditionDrizzle,
    .weatherConditionRain,
    .weatherConditionSnow,
    .weatherConditionMist,
    .weatherConditionSmoke,
    .weatherConditionHaze,
    .weatherConditionDust,
    .weatherConditionFog,
    .weatherConditionSand,
    .weatherConditionAsh,
    .weatherConditionSquall,
    .weatherConditionTornado,
    .weatherConditionClear,
    .weatherConditionClouds,
  ]
}

#endif  // swift(>=4.2)

struct WeatherProto {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var createdAt: SwiftProtobuf.Google_Protobuf_Timestamp {
    get {return _storage._createdAt ?? SwiftProtobuf.Google_Protobuf_Timestamp()}
    set {_uniqueStorage()._createdAt = newValue}
  }
  /// Returns true if `createdAt` has been explicitly set.
  var hasCreatedAt: Bool {return _storage._createdAt != nil}
  /// Clears the value of `createdAt`. Subsequent reads from it will return its default value.
  mutating func clearCreatedAt() {_uniqueStorage()._createdAt = nil}

  var regionCode: String {
    get {return _storage._regionCode}
    set {_uniqueStorage()._regionCode = newValue}
  }

  var country: String {
    get {return _storage._country}
    set {_uniqueStorage()._country = newValue}
  }

  var city: String {
    get {return _storage._city}
    set {_uniqueStorage()._city = newValue}
  }

  var timeZone: String {
    get {return _storage._timeZone}
    set {_uniqueStorage()._timeZone = newValue}
  }

  var latitude: Double {
    get {return _storage._latitude}
    set {_uniqueStorage()._latitude = newValue}
  }

  var longitude: Double {
    get {return _storage._longitude}
    set {_uniqueStorage()._longitude = newValue}
  }

  var condition: WeatherConditionProto {
    get {return _storage._condition}
    set {_uniqueStorage()._condition = newValue}
  }

  var openWeatherConditionID: Int32 {
    get {return _storage._openWeatherConditionID}
    set {_uniqueStorage()._openWeatherConditionID = newValue}
  }

  /// Celcius
  var temperature: Float {
    get {return _storage._temperature}
    set {_uniqueStorage()._temperature = newValue}
  }

  /// Celcius
  var temperatureFeelsLike: Float {
    get {return _storage._temperatureFeelsLike}
    set {_uniqueStorage()._temperatureFeelsLike = newValue}
  }

  /// Celcius
  var temperatureMin: Float {
    get {return _storage._temperatureMin}
    set {_uniqueStorage()._temperatureMin = newValue}
  }

  /// Celcius
  var temperatureMax: Float {
    get {return _storage._temperatureMax}
    set {_uniqueStorage()._temperatureMax = newValue}
  }

  /// Atmospheric pressure on the sea level, hPa
  var pressure: Int32 {
    get {return _storage._pressure}
    set {_uniqueStorage()._pressure = newValue}
  }

  /// Humidity, %
  var humidity: Int32 {
    get {return _storage._humidity}
    set {_uniqueStorage()._humidity = newValue}
  }

  /// Visibility, meter.
  var visibility: Int32 {
    get {return _storage._visibility}
    set {_uniqueStorage()._visibility = newValue}
  }

  /// Wind speed, meter/sec.
  var windSpeed: Float {
    get {return _storage._windSpeed}
    set {_uniqueStorage()._windSpeed = newValue}
  }

  /// Wind direction, degrees (meteorological)
  var windDegrees: Int32 {
    get {return _storage._windDegrees}
    set {_uniqueStorage()._windDegrees = newValue}
  }

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _storage = _StorageClass.defaultInstance
}

struct WeatherCacheProto {
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

  var weather: [WeatherProto] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _createdAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
}

#if swift(>=5.5) && canImport(_Concurrency)
extension WeatherConditionProto: @unchecked Sendable {}
extension WeatherProto: @unchecked Sendable {}
extension WeatherCacheProto: @unchecked Sendable {}
#endif  // swift(>=5.5) && canImport(_Concurrency)

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension WeatherConditionProto: SwiftProtobuf._ProtoNameProviding {
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    0: .same(proto: "WEATHER_CONDITION_UNKNOWN"),
    1: .same(proto: "WEATHER_CONDITION_THUNDERSTORM"),
    2: .same(proto: "WEATHER_CONDITION_DRIZZLE"),
    3: .same(proto: "WEATHER_CONDITION_RAIN"),
    4: .same(proto: "WEATHER_CONDITION_SNOW"),
    5: .same(proto: "WEATHER_CONDITION_MIST"),
    6: .same(proto: "WEATHER_CONDITION_SMOKE"),
    7: .same(proto: "WEATHER_CONDITION_HAZE"),
    8: .same(proto: "WEATHER_CONDITION_DUST"),
    9: .same(proto: "WEATHER_CONDITION_FOG"),
    10: .same(proto: "WEATHER_CONDITION_SAND"),
    11: .same(proto: "WEATHER_CONDITION_ASH"),
    12: .same(proto: "WEATHER_CONDITION_SQUALL"),
    13: .same(proto: "WEATHER_CONDITION_TORNADO"),
    14: .same(proto: "WEATHER_CONDITION_CLEAR"),
    15: .same(proto: "WEATHER_CONDITION_CLOUDS"),
  ]
}

extension WeatherProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "WeatherProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "created_at"),
    2: .standard(proto: "region_code"),
    3: .same(proto: "country"),
    4: .same(proto: "city"),
    5: .standard(proto: "time_zone"),
    6: .same(proto: "latitude"),
    7: .same(proto: "longitude"),
    8: .same(proto: "condition"),
    9: .standard(proto: "open_weather_condition_id"),
    10: .same(proto: "temperature"),
    11: .standard(proto: "temperature_feels_like"),
    12: .standard(proto: "temperature_min"),
    13: .standard(proto: "temperature_max"),
    14: .same(proto: "pressure"),
    15: .same(proto: "humidity"),
    16: .same(proto: "visibility"),
    17: .standard(proto: "wind_speed"),
    18: .standard(proto: "wind_degrees"),
  ]

  fileprivate class _StorageClass {
    var _createdAt: SwiftProtobuf.Google_Protobuf_Timestamp? = nil
    var _regionCode: String = String()
    var _country: String = String()
    var _city: String = String()
    var _timeZone: String = String()
    var _latitude: Double = 0
    var _longitude: Double = 0
    var _condition: WeatherConditionProto = .weatherConditionUnknown
    var _openWeatherConditionID: Int32 = 0
    var _temperature: Float = 0
    var _temperatureFeelsLike: Float = 0
    var _temperatureMin: Float = 0
    var _temperatureMax: Float = 0
    var _pressure: Int32 = 0
    var _humidity: Int32 = 0
    var _visibility: Int32 = 0
    var _windSpeed: Float = 0
    var _windDegrees: Int32 = 0

    static let defaultInstance = _StorageClass()

    private init() {}

    init(copying source: _StorageClass) {
      _createdAt = source._createdAt
      _regionCode = source._regionCode
      _country = source._country
      _city = source._city
      _timeZone = source._timeZone
      _latitude = source._latitude
      _longitude = source._longitude
      _condition = source._condition
      _openWeatherConditionID = source._openWeatherConditionID
      _temperature = source._temperature
      _temperatureFeelsLike = source._temperatureFeelsLike
      _temperatureMin = source._temperatureMin
      _temperatureMax = source._temperatureMax
      _pressure = source._pressure
      _humidity = source._humidity
      _visibility = source._visibility
      _windSpeed = source._windSpeed
      _windDegrees = source._windDegrees
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
        case 1: try { try decoder.decodeSingularMessageField(value: &_storage._createdAt) }()
        case 2: try { try decoder.decodeSingularStringField(value: &_storage._regionCode) }()
        case 3: try { try decoder.decodeSingularStringField(value: &_storage._country) }()
        case 4: try { try decoder.decodeSingularStringField(value: &_storage._city) }()
        case 5: try { try decoder.decodeSingularStringField(value: &_storage._timeZone) }()
        case 6: try { try decoder.decodeSingularDoubleField(value: &_storage._latitude) }()
        case 7: try { try decoder.decodeSingularDoubleField(value: &_storage._longitude) }()
        case 8: try { try decoder.decodeSingularEnumField(value: &_storage._condition) }()
        case 9: try { try decoder.decodeSingularInt32Field(value: &_storage._openWeatherConditionID) }()
        case 10: try { try decoder.decodeSingularFloatField(value: &_storage._temperature) }()
        case 11: try { try decoder.decodeSingularFloatField(value: &_storage._temperatureFeelsLike) }()
        case 12: try { try decoder.decodeSingularFloatField(value: &_storage._temperatureMin) }()
        case 13: try { try decoder.decodeSingularFloatField(value: &_storage._temperatureMax) }()
        case 14: try { try decoder.decodeSingularInt32Field(value: &_storage._pressure) }()
        case 15: try { try decoder.decodeSingularInt32Field(value: &_storage._humidity) }()
        case 16: try { try decoder.decodeSingularInt32Field(value: &_storage._visibility) }()
        case 17: try { try decoder.decodeSingularFloatField(value: &_storage._windSpeed) }()
        case 18: try { try decoder.decodeSingularInt32Field(value: &_storage._windDegrees) }()
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
      try { if let v = _storage._createdAt {
        try visitor.visitSingularMessageField(value: v, fieldNumber: 1)
      } }()
      if !_storage._regionCode.isEmpty {
        try visitor.visitSingularStringField(value: _storage._regionCode, fieldNumber: 2)
      }
      if !_storage._country.isEmpty {
        try visitor.visitSingularStringField(value: _storage._country, fieldNumber: 3)
      }
      if !_storage._city.isEmpty {
        try visitor.visitSingularStringField(value: _storage._city, fieldNumber: 4)
      }
      if !_storage._timeZone.isEmpty {
        try visitor.visitSingularStringField(value: _storage._timeZone, fieldNumber: 5)
      }
      if _storage._latitude != 0 {
        try visitor.visitSingularDoubleField(value: _storage._latitude, fieldNumber: 6)
      }
      if _storage._longitude != 0 {
        try visitor.visitSingularDoubleField(value: _storage._longitude, fieldNumber: 7)
      }
      if _storage._condition != .weatherConditionUnknown {
        try visitor.visitSingularEnumField(value: _storage._condition, fieldNumber: 8)
      }
      if _storage._openWeatherConditionID != 0 {
        try visitor.visitSingularInt32Field(value: _storage._openWeatherConditionID, fieldNumber: 9)
      }
      if _storage._temperature != 0 {
        try visitor.visitSingularFloatField(value: _storage._temperature, fieldNumber: 10)
      }
      if _storage._temperatureFeelsLike != 0 {
        try visitor.visitSingularFloatField(value: _storage._temperatureFeelsLike, fieldNumber: 11)
      }
      if _storage._temperatureMin != 0 {
        try visitor.visitSingularFloatField(value: _storage._temperatureMin, fieldNumber: 12)
      }
      if _storage._temperatureMax != 0 {
        try visitor.visitSingularFloatField(value: _storage._temperatureMax, fieldNumber: 13)
      }
      if _storage._pressure != 0 {
        try visitor.visitSingularInt32Field(value: _storage._pressure, fieldNumber: 14)
      }
      if _storage._humidity != 0 {
        try visitor.visitSingularInt32Field(value: _storage._humidity, fieldNumber: 15)
      }
      if _storage._visibility != 0 {
        try visitor.visitSingularInt32Field(value: _storage._visibility, fieldNumber: 16)
      }
      if _storage._windSpeed != 0 {
        try visitor.visitSingularFloatField(value: _storage._windSpeed, fieldNumber: 17)
      }
      if _storage._windDegrees != 0 {
        try visitor.visitSingularInt32Field(value: _storage._windDegrees, fieldNumber: 18)
      }
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: WeatherProto, rhs: WeatherProto) -> Bool {
    if lhs._storage !== rhs._storage {
      let storagesAreEqual: Bool = withExtendedLifetime((lhs._storage, rhs._storage)) { (_args: (_StorageClass, _StorageClass)) in
        let _storage = _args.0
        let rhs_storage = _args.1
        if _storage._createdAt != rhs_storage._createdAt {return false}
        if _storage._regionCode != rhs_storage._regionCode {return false}
        if _storage._country != rhs_storage._country {return false}
        if _storage._city != rhs_storage._city {return false}
        if _storage._timeZone != rhs_storage._timeZone {return false}
        if _storage._latitude != rhs_storage._latitude {return false}
        if _storage._longitude != rhs_storage._longitude {return false}
        if _storage._condition != rhs_storage._condition {return false}
        if _storage._openWeatherConditionID != rhs_storage._openWeatherConditionID {return false}
        if _storage._temperature != rhs_storage._temperature {return false}
        if _storage._temperatureFeelsLike != rhs_storage._temperatureFeelsLike {return false}
        if _storage._temperatureMin != rhs_storage._temperatureMin {return false}
        if _storage._temperatureMax != rhs_storage._temperatureMax {return false}
        if _storage._pressure != rhs_storage._pressure {return false}
        if _storage._humidity != rhs_storage._humidity {return false}
        if _storage._visibility != rhs_storage._visibility {return false}
        if _storage._windSpeed != rhs_storage._windSpeed {return false}
        if _storage._windDegrees != rhs_storage._windDegrees {return false}
        return true
      }
      if !storagesAreEqual {return false}
    }
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension WeatherCacheProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "WeatherCacheProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "created_at"),
    2: .same(proto: "weather"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularMessageField(value: &self._createdAt) }()
      case 2: try { try decoder.decodeRepeatedMessageField(value: &self.weather) }()
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
    if !self.weather.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.weather, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: WeatherCacheProto, rhs: WeatherCacheProto) -> Bool {
    if lhs._createdAt != rhs._createdAt {return false}
    if lhs.weather != rhs.weather {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}
