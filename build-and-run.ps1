docker build -t smck83/geoip-cache .
# docker run -it -p 8000:8000 -v ${PWD}/data1/:/opt/geoip-cache/data/ smck83/geoip-cache
docker run -it -p 8000:8000 smck83/geoip-cache
