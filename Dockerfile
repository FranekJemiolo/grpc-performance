FROM python:3.8.6-slim-buster

WORKDIR /app
ADD setup.py ./
ADD protos ./protos
ADD grpc_performance ./grpc_performance

RUN pip install -e .

ENTRYPOINT ["/bin/bash"]
