docker run -it --rm --network host --entrypoint "data_streamer_grpclib_server" grpc_performance:1.0.0 "${@:1}"
