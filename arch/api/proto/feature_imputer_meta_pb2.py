# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature-imputer-meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feature-imputer-meta.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x66\x65\x61ture-imputer-meta.proto\"J\n\x0bImputerMeta\x12\x12\n\nis_imputer\x18\x01 \x01(\x08\x12\x10\n\x08strategy\x18\x02 \x01(\t\x12\x15\n\rmissing_value\x18\x03 \x03(\tb\x06proto3')
)




_IMPUTERMETA = _descriptor.Descriptor(
  name='ImputerMeta',
  full_name='ImputerMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_imputer', full_name='ImputerMeta.is_imputer', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='ImputerMeta.strategy', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missing_value', full_name='ImputerMeta.missing_value', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=30,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['ImputerMeta'] = _IMPUTERMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImputerMeta = _reflection.GeneratedProtocolMessageType('ImputerMeta', (_message.Message,), dict(
  DESCRIPTOR = _IMPUTERMETA,
  __module__ = 'feature_imputer_meta_pb2'
  # @@protoc_insertion_point(class_scope:ImputerMeta)
  ))
_sym_db.RegisterMessage(ImputerMeta)


# @@protoc_insertion_point(module_scope)