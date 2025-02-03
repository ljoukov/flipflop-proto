// DO NOT EDIT.
// swift-format-ignore-file
// swiftlint:disable all
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: ServerProto.proto
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

enum ServerTTSVoiceProto: SwiftProtobuf.Enum, Swift.CaseIterable {
  typealias RawValue = Int
  case undefined // = 0
  case alloy // = 1
  case echo // = 2
  case fable // = 3
  case onyx // = 4
  case nova // = 5
  case shimmer // = 6
  case meditation // = 7
  case journeyDMale // = 8
  case journeyFFemale // = 9
  case journeyOFemale // = 10
  case UNRECOGNIZED(Int)

  init() {
    self = .undefined
  }

  init?(rawValue: Int) {
    switch rawValue {
    case 0: self = .undefined
    case 1: self = .alloy
    case 2: self = .echo
    case 3: self = .fable
    case 4: self = .onyx
    case 5: self = .nova
    case 6: self = .shimmer
    case 7: self = .meditation
    case 8: self = .journeyDMale
    case 9: self = .journeyFFemale
    case 10: self = .journeyOFemale
    default: self = .UNRECOGNIZED(rawValue)
    }
  }

  var rawValue: Int {
    switch self {
    case .undefined: return 0
    case .alloy: return 1
    case .echo: return 2
    case .fable: return 3
    case .onyx: return 4
    case .nova: return 5
    case .shimmer: return 6
    case .meditation: return 7
    case .journeyDMale: return 8
    case .journeyFFemale: return 9
    case .journeyOFemale: return 10
    case .UNRECOGNIZED(let i): return i
    }
  }

  // The compiler won't synthesize support with the UNRECOGNIZED case.
  static let allCases: [ServerTTSVoiceProto] = [
    .undefined,
    .alloy,
    .echo,
    .fable,
    .onyx,
    .nova,
    .shimmer,
    .meditation,
    .journeyDMale,
    .journeyFFemale,
    .journeyOFemale,
  ]

}

struct ServerApiRequestProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var request: ServerApiRequestProto.OneOf_Request? = nil

  var tts: ServerTTSRequestProto {
    get {
      if case .tts(let v)? = request {return v}
      return ServerTTSRequestProto()
    }
    set {request = .tts(newValue)}
  }

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum OneOf_Request: Equatable, Sendable {
    case tts(ServerTTSRequestProto)

  }

  init() {}
}

struct ServerApiResponseProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var response: ServerApiResponseProto.OneOf_Response? = nil

  var tts: ServerTTSResponseProto {
    get {
      if case .tts(let v)? = response {return v}
      return ServerTTSResponseProto()
    }
    set {response = .tts(newValue)}
  }

  var latencies: Dictionary<String,SwiftProtobuf.Google_Protobuf_Duration> = [:]

  var unknownFields = SwiftProtobuf.UnknownStorage()

  enum OneOf_Response: Equatable, Sendable {
    case tts(ServerTTSResponseProto)

  }

  init() {}
}

struct ServerTTSRequestProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var segments: [ServerTTSSegmentProto] = []

  var silenceSec: Float = 0

  var options: ServerTTSOptionsProto {
    get {return _options ?? ServerTTSOptionsProto()}
    set {_options = newValue}
  }
  /// Returns true if `options` has been explicitly set.
  var hasOptions: Bool {return self._options != nil}
  /// Clears the value of `options`. Subsequent reads from it will return its default value.
  mutating func clearOptions() {self._options = nil}

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _options: ServerTTSOptionsProto? = nil
}

struct ServerTTSOptionsProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var disableTranscription: Bool = false

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct ServerTTSSegmentProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var leadingSilenceSec: Float = 0

  var minDurationSec: Float = 0

  var text: String = String()

  var voice: ServerTTSVoiceProto = .undefined

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct ServerTTSResponseProto: @unchecked Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var audio: Data = Data()

  var audioMetadata: ServerAudioMetadataProto {
    get {return _audioMetadata ?? ServerAudioMetadataProto()}
    set {_audioMetadata = newValue}
  }
  /// Returns true if `audioMetadata` has been explicitly set.
  var hasAudioMetadata: Bool {return self._audioMetadata != nil}
  /// Clears the value of `audioMetadata`. Subsequent reads from it will return its default value.
  mutating func clearAudioMetadata() {self._audioMetadata = nil}

  var segmentTranscripts: [ServerTTSSegmentTranscriptProto] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _audioMetadata: ServerAudioMetadataProto? = nil
}

struct ServerAudioMetadataProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var durationSec: Float = 0

  var sampleRate: Int32 = 0

  var numChannels: Int32 = 0

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct ServerTTSSegmentTranscriptProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var offsetSec: Float = 0

  var durationSec: Float = 0

  var transcript: ServerTranscriptProto {
    get {return _transcript ?? ServerTranscriptProto()}
    set {_transcript = newValue}
  }
  /// Returns true if `transcript` has been explicitly set.
  var hasTranscript: Bool {return self._transcript != nil}
  /// Clears the value of `transcript`. Subsequent reads from it will return its default value.
  mutating func clearTranscript() {self._transcript = nil}

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _transcript: ServerTranscriptProto? = nil
}

struct ServerTranscriptProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var text: String = String()

  var words: [ServerTranscriptWordProto] = []

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

struct ServerTranscriptWordProto: Sendable {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var word: String = String()

  var startSec: Float = 0

  var endSec: Float = 0

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}
}

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension ServerTTSVoiceProto: SwiftProtobuf._ProtoNameProviding {
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    0: .same(proto: "SERVER_TTS_VOICE_PROTO_UNDEFINED"),
    1: .same(proto: "SERVER_TTS_VOICE_PROTO_ALLOY"),
    2: .same(proto: "SERVER_TTS_VOICE_PROTO_ECHO"),
    3: .same(proto: "SERVER_TTS_VOICE_PROTO_FABLE"),
    4: .same(proto: "SERVER_TTS_VOICE_PROTO_ONYX"),
    5: .same(proto: "SERVER_TTS_VOICE_PROTO_NOVA"),
    6: .same(proto: "SERVER_TTS_VOICE_PROTO_SHIMMER"),
    7: .same(proto: "SERVER_TTS_VOICE_PROTO_MEDITATION"),
    8: .same(proto: "SERVER_TTS_VOICE_PROTO_JOURNEY_D_MALE"),
    9: .same(proto: "SERVER_TTS_VOICE_PROTO_JOURNEY_F_FEMALE"),
    10: .same(proto: "SERVER_TTS_VOICE_PROTO_JOURNEY_O_FEMALE"),
  ]
}

extension ServerApiRequestProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ServerApiRequestProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    10: .same(proto: "tts"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 10: try {
        var v: ServerTTSRequestProto?
        var hadOneofValue = false
        if let current = self.request {
          hadOneofValue = true
          if case .tts(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.request = .tts(v)
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
    try { if case .tts(let v)? = self.request {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 10)
    } }()
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ServerApiRequestProto, rhs: ServerApiRequestProto) -> Bool {
    if lhs.request != rhs.request {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ServerApiResponseProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ServerApiResponseProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    10: .same(proto: "tts"),
    100: .same(proto: "latencies"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 10: try {
        var v: ServerTTSResponseProto?
        var hadOneofValue = false
        if let current = self.response {
          hadOneofValue = true
          if case .tts(let m) = current {v = m}
        }
        try decoder.decodeSingularMessageField(value: &v)
        if let v = v {
          if hadOneofValue {try decoder.handleConflictingOneOf()}
          self.response = .tts(v)
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
    try { if case .tts(let v)? = self.response {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 10)
    } }()
    if !self.latencies.isEmpty {
      try visitor.visitMapField(fieldType: SwiftProtobuf._ProtobufMessageMap<SwiftProtobuf.ProtobufString,SwiftProtobuf.Google_Protobuf_Duration>.self, value: self.latencies, fieldNumber: 100)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ServerApiResponseProto, rhs: ServerApiResponseProto) -> Bool {
    if lhs.response != rhs.response {return false}
    if lhs.latencies != rhs.latencies {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ServerTTSRequestProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ServerTTSRequestProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "segments"),
    2: .standard(proto: "silence_sec"),
    3: .same(proto: "options"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeRepeatedMessageField(value: &self.segments) }()
      case 2: try { try decoder.decodeSingularFloatField(value: &self.silenceSec) }()
      case 3: try { try decoder.decodeSingularMessageField(value: &self._options) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    if !self.segments.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.segments, fieldNumber: 1)
    }
    if self.silenceSec.bitPattern != 0 {
      try visitor.visitSingularFloatField(value: self.silenceSec, fieldNumber: 2)
    }
    try { if let v = self._options {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 3)
    } }()
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ServerTTSRequestProto, rhs: ServerTTSRequestProto) -> Bool {
    if lhs.segments != rhs.segments {return false}
    if lhs.silenceSec != rhs.silenceSec {return false}
    if lhs._options != rhs._options {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ServerTTSOptionsProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ServerTTSOptionsProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "disable_transcription"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularBoolField(value: &self.disableTranscription) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if self.disableTranscription != false {
      try visitor.visitSingularBoolField(value: self.disableTranscription, fieldNumber: 1)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ServerTTSOptionsProto, rhs: ServerTTSOptionsProto) -> Bool {
    if lhs.disableTranscription != rhs.disableTranscription {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ServerTTSSegmentProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ServerTTSSegmentProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "leading_silence_sec"),
    2: .standard(proto: "min_duration_sec"),
    3: .same(proto: "text"),
    4: .same(proto: "voice"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularFloatField(value: &self.leadingSilenceSec) }()
      case 2: try { try decoder.decodeSingularFloatField(value: &self.minDurationSec) }()
      case 3: try { try decoder.decodeSingularStringField(value: &self.text) }()
      case 4: try { try decoder.decodeSingularEnumField(value: &self.voice) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if self.leadingSilenceSec.bitPattern != 0 {
      try visitor.visitSingularFloatField(value: self.leadingSilenceSec, fieldNumber: 1)
    }
    if self.minDurationSec.bitPattern != 0 {
      try visitor.visitSingularFloatField(value: self.minDurationSec, fieldNumber: 2)
    }
    if !self.text.isEmpty {
      try visitor.visitSingularStringField(value: self.text, fieldNumber: 3)
    }
    if self.voice != .undefined {
      try visitor.visitSingularEnumField(value: self.voice, fieldNumber: 4)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ServerTTSSegmentProto, rhs: ServerTTSSegmentProto) -> Bool {
    if lhs.leadingSilenceSec != rhs.leadingSilenceSec {return false}
    if lhs.minDurationSec != rhs.minDurationSec {return false}
    if lhs.text != rhs.text {return false}
    if lhs.voice != rhs.voice {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ServerTTSResponseProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ServerTTSResponseProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "audio"),
    2: .standard(proto: "audio_metadata"),
    3: .standard(proto: "segment_transcripts"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularBytesField(value: &self.audio) }()
      case 2: try { try decoder.decodeSingularMessageField(value: &self._audioMetadata) }()
      case 3: try { try decoder.decodeRepeatedMessageField(value: &self.segmentTranscripts) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    if !self.audio.isEmpty {
      try visitor.visitSingularBytesField(value: self.audio, fieldNumber: 1)
    }
    try { if let v = self._audioMetadata {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    } }()
    if !self.segmentTranscripts.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.segmentTranscripts, fieldNumber: 3)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ServerTTSResponseProto, rhs: ServerTTSResponseProto) -> Bool {
    if lhs.audio != rhs.audio {return false}
    if lhs._audioMetadata != rhs._audioMetadata {return false}
    if lhs.segmentTranscripts != rhs.segmentTranscripts {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ServerAudioMetadataProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ServerAudioMetadataProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "duration_sec"),
    2: .standard(proto: "sample_rate"),
    3: .standard(proto: "num_channels"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularFloatField(value: &self.durationSec) }()
      case 2: try { try decoder.decodeSingularInt32Field(value: &self.sampleRate) }()
      case 3: try { try decoder.decodeSingularInt32Field(value: &self.numChannels) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if self.durationSec.bitPattern != 0 {
      try visitor.visitSingularFloatField(value: self.durationSec, fieldNumber: 1)
    }
    if self.sampleRate != 0 {
      try visitor.visitSingularInt32Field(value: self.sampleRate, fieldNumber: 2)
    }
    if self.numChannels != 0 {
      try visitor.visitSingularInt32Field(value: self.numChannels, fieldNumber: 3)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ServerAudioMetadataProto, rhs: ServerAudioMetadataProto) -> Bool {
    if lhs.durationSec != rhs.durationSec {return false}
    if lhs.sampleRate != rhs.sampleRate {return false}
    if lhs.numChannels != rhs.numChannels {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ServerTTSSegmentTranscriptProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ServerTTSSegmentTranscriptProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .standard(proto: "offset_sec"),
    2: .standard(proto: "duration_sec"),
    3: .same(proto: "transcript"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularFloatField(value: &self.offsetSec) }()
      case 2: try { try decoder.decodeSingularFloatField(value: &self.durationSec) }()
      case 3: try { try decoder.decodeSingularMessageField(value: &self._transcript) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    // The use of inline closures is to circumvent an issue where the compiler
    // allocates stack space for every if/case branch local when no optimizations
    // are enabled. https://github.com/apple/swift-protobuf/issues/1034 and
    // https://github.com/apple/swift-protobuf/issues/1182
    if self.offsetSec.bitPattern != 0 {
      try visitor.visitSingularFloatField(value: self.offsetSec, fieldNumber: 1)
    }
    if self.durationSec.bitPattern != 0 {
      try visitor.visitSingularFloatField(value: self.durationSec, fieldNumber: 2)
    }
    try { if let v = self._transcript {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 3)
    } }()
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ServerTTSSegmentTranscriptProto, rhs: ServerTTSSegmentTranscriptProto) -> Bool {
    if lhs.offsetSec != rhs.offsetSec {return false}
    if lhs.durationSec != rhs.durationSec {return false}
    if lhs._transcript != rhs._transcript {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ServerTranscriptProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ServerTranscriptProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "text"),
    2: .same(proto: "words"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.text) }()
      case 2: try { try decoder.decodeRepeatedMessageField(value: &self.words) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.text.isEmpty {
      try visitor.visitSingularStringField(value: self.text, fieldNumber: 1)
    }
    if !self.words.isEmpty {
      try visitor.visitRepeatedMessageField(value: self.words, fieldNumber: 2)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ServerTranscriptProto, rhs: ServerTranscriptProto) -> Bool {
    if lhs.text != rhs.text {return false}
    if lhs.words != rhs.words {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}

extension ServerTranscriptWordProto: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = "ServerTranscriptWordProto"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "word"),
    2: .standard(proto: "start_sec"),
    3: .standard(proto: "end_sec"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      // The use of inline closures is to circumvent an issue where the compiler
      // allocates stack space for every case branch when no optimizations are
      // enabled. https://github.com/apple/swift-protobuf/issues/1034
      switch fieldNumber {
      case 1: try { try decoder.decodeSingularStringField(value: &self.word) }()
      case 2: try { try decoder.decodeSingularFloatField(value: &self.startSec) }()
      case 3: try { try decoder.decodeSingularFloatField(value: &self.endSec) }()
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if !self.word.isEmpty {
      try visitor.visitSingularStringField(value: self.word, fieldNumber: 1)
    }
    if self.startSec.bitPattern != 0 {
      try visitor.visitSingularFloatField(value: self.startSec, fieldNumber: 2)
    }
    if self.endSec.bitPattern != 0 {
      try visitor.visitSingularFloatField(value: self.endSec, fieldNumber: 3)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: ServerTranscriptWordProto, rhs: ServerTranscriptWordProto) -> Bool {
    if lhs.word != rhs.word {return false}
    if lhs.startSec != rhs.startSec {return false}
    if lhs.endSec != rhs.endSec {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}
