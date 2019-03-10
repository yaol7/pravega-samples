# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SimpleGrpcServer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SimpleGrpcServer.proto',
  package='pravega_simple_grpc_server',
  syntax='proto3',
  serialized_options=_b('\n%io.pravega.example.simple_grpc_serverB\025SimpleGrpcServerProtoP\001\242\002\004PSGS'),
  serialized_pb=_b('\n\x16SimpleGrpcServer.proto\x12\x1apravega_simple_grpc_server\"#\n\x12\x43reateScopeRequest\x12\r\n\x05scope\x18\x01 \x01(\t\"&\n\x13\x43reateScopeResponse\x12\x0f\n\x07\x63reated\x18\x01 \x01(\x08\"4\n\x13\x43reateStreamRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\x0e\n\x06stream\x18\x02 \x01(\t\"\'\n\x14\x43reateStreamResponse\x12\x0f\n\x07\x63reated\x18\x01 \x01(\x08\"F\n\x11ReadEventsRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\x0e\n\x06stream\x18\x02 \x01(\t\x12\x12\n\ntimeout_ms\x18\x03 \x01(\x03\"e\n\x12ReadEventsResponse\x12\r\n\x05\x65vent\x18\x01 \x01(\x0c\x12\x10\n\x08position\x18\x02 \x01(\t\x12\x15\n\revent_pointer\x18\x03 \x01(\t\x12\x17\n\x0f\x63heckpoint_name\x18\x04 \x01(\t\"W\n\x12WriteEventsRequest\x12\r\n\x05\x65vent\x18\x01 \x01(\x0c\x12\r\n\x05scope\x18\x02 \x01(\t\x12\x0e\n\x06stream\x18\x03 \x01(\t\x12\x13\n\x0brouting_key\x18\x04 \x01(\t\"\x15\n\x13WriteEventsResponse2\xde\x03\n\x10SimpleGrpcServer\x12p\n\x0b\x43reateScope\x12..pravega_simple_grpc_server.CreateScopeRequest\x1a/.pravega_simple_grpc_server.CreateScopeResponse\"\x00\x12s\n\x0c\x43reateStream\x12/.pravega_simple_grpc_server.CreateStreamRequest\x1a\x30.pravega_simple_grpc_server.CreateStreamResponse\"\x00\x12o\n\nReadEvents\x12-.pravega_simple_grpc_server.ReadEventsRequest\x1a..pravega_simple_grpc_server.ReadEventsResponse\"\x00\x30\x01\x12r\n\x0bWriteEvents\x12..pravega_simple_grpc_server.WriteEventsRequest\x1a/.pravega_simple_grpc_server.WriteEventsResponse\"\x00(\x01\x42G\n%io.pravega.example.simple_grpc_serverB\x15SimpleGrpcServerProtoP\x01\xa2\x02\x04PSGSb\x06proto3')
)




_CREATESCOPEREQUEST = _descriptor.Descriptor(
  name='CreateScopeRequest',
  full_name='pravega_simple_grpc_server.CreateScopeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scope', full_name='pravega_simple_grpc_server.CreateScopeRequest.scope', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=89,
)


_CREATESCOPERESPONSE = _descriptor.Descriptor(
  name='CreateScopeResponse',
  full_name='pravega_simple_grpc_server.CreateScopeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='pravega_simple_grpc_server.CreateScopeResponse.created', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=129,
)


_CREATESTREAMREQUEST = _descriptor.Descriptor(
  name='CreateStreamRequest',
  full_name='pravega_simple_grpc_server.CreateStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scope', full_name='pravega_simple_grpc_server.CreateStreamRequest.scope', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream', full_name='pravega_simple_grpc_server.CreateStreamRequest.stream', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=183,
)


_CREATESTREAMRESPONSE = _descriptor.Descriptor(
  name='CreateStreamResponse',
  full_name='pravega_simple_grpc_server.CreateStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='pravega_simple_grpc_server.CreateStreamResponse.created', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=224,
)


_READEVENTSREQUEST = _descriptor.Descriptor(
  name='ReadEventsRequest',
  full_name='pravega_simple_grpc_server.ReadEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scope', full_name='pravega_simple_grpc_server.ReadEventsRequest.scope', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream', full_name='pravega_simple_grpc_server.ReadEventsRequest.stream', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout_ms', full_name='pravega_simple_grpc_server.ReadEventsRequest.timeout_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=296,
)


_READEVENTSRESPONSE = _descriptor.Descriptor(
  name='ReadEventsResponse',
  full_name='pravega_simple_grpc_server.ReadEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='pravega_simple_grpc_server.ReadEventsResponse.event', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='pravega_simple_grpc_server.ReadEventsResponse.position', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_pointer', full_name='pravega_simple_grpc_server.ReadEventsResponse.event_pointer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_name', full_name='pravega_simple_grpc_server.ReadEventsResponse.checkpoint_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=399,
)


_WRITEEVENTSREQUEST = _descriptor.Descriptor(
  name='WriteEventsRequest',
  full_name='pravega_simple_grpc_server.WriteEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='pravega_simple_grpc_server.WriteEventsRequest.event', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='pravega_simple_grpc_server.WriteEventsRequest.scope', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream', full_name='pravega_simple_grpc_server.WriteEventsRequest.stream', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='routing_key', full_name='pravega_simple_grpc_server.WriteEventsRequest.routing_key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=401,
  serialized_end=488,
)


_WRITEEVENTSRESPONSE = _descriptor.Descriptor(
  name='WriteEventsResponse',
  full_name='pravega_simple_grpc_server.WriteEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=490,
  serialized_end=511,
)

DESCRIPTOR.message_types_by_name['CreateScopeRequest'] = _CREATESCOPEREQUEST
DESCRIPTOR.message_types_by_name['CreateScopeResponse'] = _CREATESCOPERESPONSE
DESCRIPTOR.message_types_by_name['CreateStreamRequest'] = _CREATESTREAMREQUEST
DESCRIPTOR.message_types_by_name['CreateStreamResponse'] = _CREATESTREAMRESPONSE
DESCRIPTOR.message_types_by_name['ReadEventsRequest'] = _READEVENTSREQUEST
DESCRIPTOR.message_types_by_name['ReadEventsResponse'] = _READEVENTSRESPONSE
DESCRIPTOR.message_types_by_name['WriteEventsRequest'] = _WRITEEVENTSREQUEST
DESCRIPTOR.message_types_by_name['WriteEventsResponse'] = _WRITEEVENTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateScopeRequest = _reflection.GeneratedProtocolMessageType('CreateScopeRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESCOPEREQUEST,
  __module__ = 'SimpleGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:pravega_simple_grpc_server.CreateScopeRequest)
  ))
_sym_db.RegisterMessage(CreateScopeRequest)

CreateScopeResponse = _reflection.GeneratedProtocolMessageType('CreateScopeResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATESCOPERESPONSE,
  __module__ = 'SimpleGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:pravega_simple_grpc_server.CreateScopeResponse)
  ))
_sym_db.RegisterMessage(CreateScopeResponse)

CreateStreamRequest = _reflection.GeneratedProtocolMessageType('CreateStreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESTREAMREQUEST,
  __module__ = 'SimpleGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:pravega_simple_grpc_server.CreateStreamRequest)
  ))
_sym_db.RegisterMessage(CreateStreamRequest)

CreateStreamResponse = _reflection.GeneratedProtocolMessageType('CreateStreamResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATESTREAMRESPONSE,
  __module__ = 'SimpleGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:pravega_simple_grpc_server.CreateStreamResponse)
  ))
_sym_db.RegisterMessage(CreateStreamResponse)

ReadEventsRequest = _reflection.GeneratedProtocolMessageType('ReadEventsRequest', (_message.Message,), dict(
  DESCRIPTOR = _READEVENTSREQUEST,
  __module__ = 'SimpleGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:pravega_simple_grpc_server.ReadEventsRequest)
  ))
_sym_db.RegisterMessage(ReadEventsRequest)

ReadEventsResponse = _reflection.GeneratedProtocolMessageType('ReadEventsResponse', (_message.Message,), dict(
  DESCRIPTOR = _READEVENTSRESPONSE,
  __module__ = 'SimpleGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:pravega_simple_grpc_server.ReadEventsResponse)
  ))
_sym_db.RegisterMessage(ReadEventsResponse)

WriteEventsRequest = _reflection.GeneratedProtocolMessageType('WriteEventsRequest', (_message.Message,), dict(
  DESCRIPTOR = _WRITEEVENTSREQUEST,
  __module__ = 'SimpleGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:pravega_simple_grpc_server.WriteEventsRequest)
  ))
_sym_db.RegisterMessage(WriteEventsRequest)

WriteEventsResponse = _reflection.GeneratedProtocolMessageType('WriteEventsResponse', (_message.Message,), dict(
  DESCRIPTOR = _WRITEEVENTSRESPONSE,
  __module__ = 'SimpleGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:pravega_simple_grpc_server.WriteEventsResponse)
  ))
_sym_db.RegisterMessage(WriteEventsResponse)


DESCRIPTOR._options = None

_SIMPLEGRPCSERVER = _descriptor.ServiceDescriptor(
  name='SimpleGrpcServer',
  full_name='pravega_simple_grpc_server.SimpleGrpcServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=514,
  serialized_end=992,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateScope',
    full_name='pravega_simple_grpc_server.SimpleGrpcServer.CreateScope',
    index=0,
    containing_service=None,
    input_type=_CREATESCOPEREQUEST,
    output_type=_CREATESCOPERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateStream',
    full_name='pravega_simple_grpc_server.SimpleGrpcServer.CreateStream',
    index=1,
    containing_service=None,
    input_type=_CREATESTREAMREQUEST,
    output_type=_CREATESTREAMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReadEvents',
    full_name='pravega_simple_grpc_server.SimpleGrpcServer.ReadEvents',
    index=2,
    containing_service=None,
    input_type=_READEVENTSREQUEST,
    output_type=_READEVENTSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WriteEvents',
    full_name='pravega_simple_grpc_server.SimpleGrpcServer.WriteEvents',
    index=3,
    containing_service=None,
    input_type=_WRITEEVENTSREQUEST,
    output_type=_WRITEEVENTSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMPLEGRPCSERVER)

DESCRIPTOR.services_by_name['SimpleGrpcServer'] = _SIMPLEGRPCSERVER

# @@protoc_insertion_point(module_scope)
