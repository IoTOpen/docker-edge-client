#!/bin/bash
. header.sh

if [ ! -e /etc/iot-open/iotopen.json ]; then
  echo "<h2>No config.</h2>"
  echo 'Please <a href="setup.sh">configure</a> this Gateway.'
  cat footer.inc
  exit
fi

echo "<pre>"

echo "<b>Testing Mosqutitto</b>"
if /etc/init.d/mosquitto status >/dev/null; then
  echo "Mosquitto is running<br>"
else
  iotopen-verify

  cp /etc/iot-open/mosquitto.conf /etc/mosquitto/

  /etc/init.d/mosquitto restart
fi

echo "<b>Testing Edged</b>"
if pgrep edged >/dev/null; then
  echo "Edged running <br>"
else
  edged &
fi

echo "</pre>"
cat footer.inc
