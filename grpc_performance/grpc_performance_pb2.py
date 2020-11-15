# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_performance.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_performance.proto',
  package='grpc_performance',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16grpc_performance.proto\x12\x10grpc_performance\"$\n\rStreamRequest\x12\x13\n\x0bjsonRequest\x18\x01 \x01(\x0c\" \n\rSingleMessage\x12\x0f\n\x07message\x18\x01 \x01(\x0c\x32\x62\n\x0c\x44\x61taStreamer\x12R\n\nstreamData\x12\x1f.grpc_performance.StreamRequest\x1a\x1f.grpc_performance.SingleMessage\"\x00\x30\x01\x62\x06proto3'
)




_STREAMREQUEST = _descriptor.Descriptor(
  name='StreamRequest',
  full_name='grpc_performance.StreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jsonRequest', full_name='grpc_performance.StreamRequest.jsonRequest', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=44,
  serialized_end=80,
)


_SINGLEMESSAGE = _descriptor.Descriptor(
  name='SingleMessage',
  full_name='grpc_performance.SingleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc_performance.SingleMessage.message', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=82,
  serialized_end=114,
)

DESCRIPTOR.message_types_by_name['StreamRequest'] = _STREAMREQUEST
DESCRIPTOR.message_types_by_name['SingleMessage'] = _SINGLEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamRequest = _reflection.GeneratedProtocolMessageType('StreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMREQUEST,
  '__module__' : 'grpc_performance_pb2'
  # @@protoc_insertion_point(class_scope:grpc_performance.StreamRequest)
  })
_sym_db.RegisterMessage(StreamRequest)

SingleMessage = _reflection.GeneratedProtocolMessageType('SingleMessage', (_message.Message,), {
  'DESCRIPTOR' : _SINGLEMESSAGE,
  '__module__' : 'grpc_performance_pb2'
  # @@protoc_insertion_point(class_scope:grpc_performance.SingleMessage)
  })
_sym_db.RegisterMessage(SingleMessage)



_DATASTREAMER = _descriptor.ServiceDescriptor(
  name='DataStreamer',
  full_name='grpc_performance.DataStreamer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=116,
  serialized_end=214,
  methods=[
  _descriptor.MethodDescriptor(
    name='streamData',
    full_name='grpc_performance.DataStreamer.streamData',
    index=0,
    containing_service=None,
    input_type=_STREAMREQUEST,
    output_type=_SINGLEMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATASTREAMER)

DESCRIPTOR.services_by_name['DataStreamer'] = _DATASTREAMER

# @@protoc_insertion_point(module_scope)