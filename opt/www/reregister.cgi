#!/bin/bash
cat header.inc

if [ ! -e /etc/iot-open/iotopen.json ]; then
  echo "<h2>No config.</h2>"
  echo 'Please <a href="setup.sh">configure</a> this Gateway.'
  cat footer.inc
  exit
fi

echo "<pre>"

echo "<b>Re-registering</b>"
iotopen-verify
cp /etc/iot-open/mosquitto.conf /etc/mosquitto/
/etc/init.d/mosquitto restart

# TODO: Edged restart

echo "</pre>"
cat footer.inc
