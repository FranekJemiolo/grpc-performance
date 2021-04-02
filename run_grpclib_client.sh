docker run -it --rm --network host --entrypoint "data_streamer_grpclib_client" grpc_performance:1.0.0 "${@:1}"
