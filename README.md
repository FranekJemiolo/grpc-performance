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
| Gzip | 100 | - |
| Deflate | 100 | - |
| NoCompression | 100 | - |
| Gzip | 1 | - |
| Deflate | 1 | - |
| NoCompression | 1 | - |

