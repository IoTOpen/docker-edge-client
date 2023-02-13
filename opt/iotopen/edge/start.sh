#!/bin/bash

mkdir -p /var/lib/iot-open/edge/apps
mkdir -p /var/lib/iot-open/edge/configs
mkdir -p /run/mosquitto/

if [ -e /etc/iot-open/iotopen.json ]; then
  iotopen-verify
  cp /etc/iot-open/mosquitto.conf /etc/mosquitto/
  /etc/init.d/mosquitto restart
  edged &
fi

if [ "${INSECURE}" == "true" ]; then
  echo "INSECURE=true" >/opt/www/config.sh
else
  echo "INSECURE=false" >/opt/www/config.sh
  echo "BASE=${BASE}" >>/opt/www/config.sh
fi

if [ "${HEADLESS}" == "true" ]; then
  while true; do sleep 60; done
else
  /usr/sbin/mini_httpd -d /opt/www -c "*.cgi" -u root -D 2>/dev/null
fi
