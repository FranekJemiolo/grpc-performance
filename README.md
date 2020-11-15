# grpc-performance
Simple grpc performance tool in Python

## Building
```bash
./build.sh
```

## Running
First start up the server
```bash
./run_server.sh
```
then a corresponding client
```bash
./run_client.sh
```

## Example results
Tested on i5-8250U CPU (4 cores, 1.60GHZ) with 1000000 messages.

| Compression | Batch size | Result |
| --- | --- | --- |
| Gzip | 100 | 75,000 msg/s |
| Deflate | 100 | 78,000 msg/s |
| NoCompression | 100 | 90,000 msg/s |
| Gzip | 1 | 5,100 msg/s |
| Deflate | 1 | 4,900 msg/s |
| NoCompression | 1 | 4,600 msg/s |

Batching and no compression offers the best throughput when testing locally.
This is similar to the results achieved in [https://github.com/FranekJemiolo/websockets-performance#example-results](https://github.com/FranekJemiolo/websockets-performance#example-results).
Conclusions are similar, when network connection becomes an issue I would suspect compression would lead to better results.

What is interesting is that out of the box websockets offers almost 3x better performance than gRPC in certain situations.

