#!/bin/bash

mkdir -p /var/lib/iot-open/edge/apps
mkdir -p /var/lib/iot-open/edge/configs
mkdir -p /run/mosquitto/
chown mosquitto:mosquitto /run/mosquitto

if [ -e /etc/iot-open/iotopen.json ]; then
  iotopen-verify
fi

if [ "${INSECURE}" == "true" ]; then
  echo "INSECURE=true" >/opt/www/config.sh
else
  echo "INSECURE=false" >/opt/www/config.sh
  echo "BASE=${BASE}" >>/opt/www/config.sh
fi
if [ "${HEADLESS}" == "true" ]; then
  rm /etc/supervisor/conf.d/mini_httpd.conf
fi

exec /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
