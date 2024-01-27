// DO NOT EDIT.
// swift-format-ignore-file
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: ColorProto.proto
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

enum ColorTypeProto: SwiftProtobuf.Enum {
  typealias RawValue = Int
  case undefined // = 0
  case blue // = 1
  case indigo // = 2
  case green // = 3
  case UNRECOGNIZED(Int)

  init() {
    self = .undefined
  }

  init?(rawValue: Int) {
    switch rawValue {
    case 0: self = .undefined
    case 1: self = .blue
    case 2: self = .indigo
    case 3: self = .green
    default: self = .UNRECOGNIZED(rawValue)
    }
  }

  var rawValue: Int {
    switch self {
    case .undefined: return 0
    case .blue: return 1
    case .indigo: return 2
    case .green: return 3
    case .UNRECOGNIZED(let i): return i
    }
  }

}

#if swift(>=4.2)

extension ColorTypeProto: CaseIterable {
  // The compiler won't synthesize support with the UNRECOGNIZED case.
  static var allCases: [ColorTypeProto] = [
    .undefined,
    .blue,
    .indigo,
    .green,
  ]
}

#endif  // swift(>=4.2)

#if swift(>=5.5) && canImport(_Concurrency)
extension ColorTypeProto: @unchecked Sendable {}
#endif  // swift(>=5.5) && canImport(_Concurrency)

// MARK: - Code below here is support for the SwiftProtobuf runtime.

extension ColorTypeProto: SwiftProtobuf._ProtoNameProviding {
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    0: .same(proto: "COLOR_TYPE_PROTO_UNDEFINED"),
    1: .same(proto: "COLOR_TYPE_PROTO_BLUE"),
    2: .same(proto: "COLOR_TYPE_PROTO_INDIGO"),
    3: .same(proto: "COLOR_TYPE_PROTO_GREEN"),
  ]
}
