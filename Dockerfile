FROM python:3.8.13-slim

ENV PIP_NO_CACHE_DIR=1
WORKDIR /notify-server/
COPY / /notify-server
RUN pip install .
CMD notify-server 0.0.0.0:20109 -p
