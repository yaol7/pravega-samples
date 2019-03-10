# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import SimpleGrpcServer_pb2 as SimpleGrpcServer__pb2


class SimpleGrpcServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateScope = channel.unary_unary(
        '/pravega_simple_grpc_server.SimpleGrpcServer/CreateScope',
        request_serializer=SimpleGrpcServer__pb2.CreateScopeRequest.SerializeToString,
        response_deserializer=SimpleGrpcServer__pb2.CreateScopeResponse.FromString,
        )
    self.CreateStream = channel.unary_unary(
        '/pravega_simple_grpc_server.SimpleGrpcServer/CreateStream',
        request_serializer=SimpleGrpcServer__pb2.CreateStreamRequest.SerializeToString,
        response_deserializer=SimpleGrpcServer__pb2.CreateStreamResponse.FromString,
        )
    self.ReadEvents = channel.unary_stream(
        '/pravega_simple_grpc_server.SimpleGrpcServer/ReadEvents',
        request_serializer=SimpleGrpcServer__pb2.ReadEventsRequest.SerializeToString,
        response_deserializer=SimpleGrpcServer__pb2.ReadEventsResponse.FromString,
        )
    self.WriteEvents = channel.stream_unary(
        '/pravega_simple_grpc_server.SimpleGrpcServer/WriteEvents',
        request_serializer=SimpleGrpcServer__pb2.WriteEventsRequest.SerializeToString,
        response_deserializer=SimpleGrpcServer__pb2.WriteEventsResponse.FromString,
        )


class SimpleGrpcServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateScope(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateStream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadEvents(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteEvents(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SimpleGrpcServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateScope': grpc.unary_unary_rpc_method_handler(
          servicer.CreateScope,
          request_deserializer=SimpleGrpcServer__pb2.CreateScopeRequest.FromString,
          response_serializer=SimpleGrpcServer__pb2.CreateScopeResponse.SerializeToString,
      ),
      'CreateStream': grpc.unary_unary_rpc_method_handler(
          servicer.CreateStream,
          request_deserializer=SimpleGrpcServer__pb2.CreateStreamRequest.FromString,
          response_serializer=SimpleGrpcServer__pb2.CreateStreamResponse.SerializeToString,
      ),
      'ReadEvents': grpc.unary_stream_rpc_method_handler(
          servicer.ReadEvents,
          request_deserializer=SimpleGrpcServer__pb2.ReadEventsRequest.FromString,
          response_serializer=SimpleGrpcServer__pb2.ReadEventsResponse.SerializeToString,
      ),
      'WriteEvents': grpc.stream_unary_rpc_method_handler(
          servicer.WriteEvents,
          request_deserializer=SimpleGrpcServer__pb2.WriteEventsRequest.FromString,
          response_serializer=SimpleGrpcServer__pb2.WriteEventsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pravega_simple_grpc_server.SimpleGrpcServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
