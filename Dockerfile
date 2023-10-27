FROM debian:11
LABEL maintainer="s@mck.la"
ARG MY_APP_PATH=/opt/geoip-cache

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ntp python3 pip \
    && mkdir -p ${MY_APP_PATH}/data

ADD main.py kv.py requirements.txt run.py ${MY_APP_PATH}
#COPY data ${MY_APP_PATH}/data
RUN pip install -r ${MY_APP_PATH}/requirements.txt
#RUN pip3 install fastapi uvicorn[standard] qrcode[pil] requests
WORKDIR ${MY_APP_PATH}


VOLUME [${MY_APP_PATH}]

ENTRYPOINT /usr/bin/python3 -u run.py
#ENTRYPOINT pypy3 -u run.py

EXPOSE 8000/tcp
