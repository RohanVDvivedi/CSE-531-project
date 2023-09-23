# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import branch_pb2 as branch__pb2


class BranchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Query = channel.unary_unary(
                '/Branch/Query',
                request_serializer=branch__pb2.Request.SerializeToString,
                response_deserializer=branch__pb2.Response.FromString,
                )
        self.Withdraw = channel.unary_unary(
                '/Branch/Withdraw',
                request_serializer=branch__pb2.Request.SerializeToString,
                response_deserializer=branch__pb2.Response.FromString,
                )
        self.Deposit = channel.unary_unary(
                '/Branch/Deposit',
                request_serializer=branch__pb2.Request.SerializeToString,
                response_deserializer=branch__pb2.Response.FromString,
                )
        self.Propogate_Withdraw = channel.unary_unary(
                '/Branch/Propogate_Withdraw',
                request_serializer=branch__pb2.Request.SerializeToString,
                response_deserializer=branch__pb2.Response.FromString,
                )
        self.Propogate_Deposit = channel.unary_unary(
                '/Branch/Propogate_Deposit',
                request_serializer=branch__pb2.Request.SerializeToString,
                response_deserializer=branch__pb2.Response.FromString,
                )


class BranchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Propogate_Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Propogate_Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BranchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=branch__pb2.Request.FromString,
                    response_serializer=branch__pb2.Response.SerializeToString,
            ),
            'Withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.Withdraw,
                    request_deserializer=branch__pb2.Request.FromString,
                    response_serializer=branch__pb2.Response.SerializeToString,
            ),
            'Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Deposit,
                    request_deserializer=branch__pb2.Request.FromString,
                    response_serializer=branch__pb2.Response.SerializeToString,
            ),
            'Propogate_Withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.Propogate_Withdraw,
                    request_deserializer=branch__pb2.Request.FromString,
                    response_serializer=branch__pb2.Response.SerializeToString,
            ),
            'Propogate_Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Propogate_Deposit,
                    request_deserializer=branch__pb2.Request.FromString,
                    response_serializer=branch__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Branch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Branch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Branch/Query',
            branch__pb2.Request.SerializeToString,
            branch__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Branch/Withdraw',
            branch__pb2.Request.SerializeToString,
            branch__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Branch/Deposit',
            branch__pb2.Request.SerializeToString,
            branch__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Propogate_Withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Branch/Propogate_Withdraw',
            branch__pb2.Request.SerializeToString,
            branch__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Propogate_Deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Branch/Propogate_Deposit',
            branch__pb2.Request.SerializeToString,
            branch__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
