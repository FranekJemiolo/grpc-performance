FROM python:3.8.6-slim-buster

WORKDIR /app
ADD . ./

RUN pip install -e .

ENTRYPOINT ["/bin/bash"]
