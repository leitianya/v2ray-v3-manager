# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/app/log/command/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/app/log/command/config.proto',
  package='v2ray.core.app.log.command',
  syntax='proto3',
  serialized_options=_b('\n\036com.v2ray.core.app.log.commandP\001Z\007command\252\002\032V2Ray.Core.App.Log.Command'),
  serialized_pb=_b('\n+v2ray.com/core/app/log/command/config.proto\x12\x1av2ray.core.app.log.command\"\x08\n\x06\x43onfig\"\x16\n\x14RestartLoggerRequest\"\x17\n\x15RestartLoggerResponse2\x87\x01\n\rLoggerService\x12v\n\rRestartLogger\x12\x30.v2ray.core.app.log.command.RestartLoggerRequest\x1a\x31.v2ray.core.app.log.command.RestartLoggerResponse\"\x00\x42H\n\x1e\x63om.v2ray.core.app.log.commandP\x01Z\x07\x63ommand\xaa\x02\x1aV2Ray.Core.App.Log.Commandb\x06proto3')
)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.app.log.command.Config',
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
  serialized_start=75,
  serialized_end=83,
)


_RESTARTLOGGERREQUEST = _descriptor.Descriptor(
  name='RestartLoggerRequest',
  full_name='v2ray.core.app.log.command.RestartLoggerRequest',
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
  serialized_start=85,
  serialized_end=107,
)


_RESTARTLOGGERRESPONSE = _descriptor.Descriptor(
  name='RestartLoggerResponse',
  full_name='v2ray.core.app.log.command.RestartLoggerResponse',
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
  serialized_start=109,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['RestartLoggerRequest'] = _RESTARTLOGGERREQUEST
DESCRIPTOR.message_types_by_name['RestartLoggerResponse'] = _RESTARTLOGGERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'v2ray.com.core.app.log.command.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.log.command.Config)
  ))
_sym_db.RegisterMessage(Config)

RestartLoggerRequest = _reflection.GeneratedProtocolMessageType('RestartLoggerRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESTARTLOGGERREQUEST,
  __module__ = 'v2ray.com.core.app.log.command.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.log.command.RestartLoggerRequest)
  ))
_sym_db.RegisterMessage(RestartLoggerRequest)

RestartLoggerResponse = _reflection.GeneratedProtocolMessageType('RestartLoggerResponse', (_message.Message,), dict(
  DESCRIPTOR = _RESTARTLOGGERRESPONSE,
  __module__ = 'v2ray.com.core.app.log.command.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.log.command.RestartLoggerResponse)
  ))
_sym_db.RegisterMessage(RestartLoggerResponse)


DESCRIPTOR._options = None

_LOGGERSERVICE = _descriptor.ServiceDescriptor(
  name='LoggerService',
  full_name='v2ray.core.app.log.command.LoggerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=135,
  serialized_end=270,
  methods=[
  _descriptor.MethodDescriptor(
    name='RestartLogger',
    full_name='v2ray.core.app.log.command.LoggerService.RestartLogger',
    index=0,
    containing_service=None,
    input_type=_RESTARTLOGGERREQUEST,
    output_type=_RESTARTLOGGERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGGERSERVICE)

DESCRIPTOR.services_by_name['LoggerService'] = _LOGGERSERVICE

# @@protoc_insertion_point(module_scope)