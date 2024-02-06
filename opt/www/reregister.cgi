#!/bin/bash
cat header.inc

if [ ! -e /etc/iot-open/iotopen.json ]; then
  echo "<h2>No config.</h2>"
  echo 'Please <a href="setup.cgi">configure</a> this Gateway.'
  cat footer.inc
  exit
fi

echo "<pre>"

echo "<b>Re-registering</b>"
iotopen-verify
supervisorctl restart mosquitto
supervisorctl restart edged

echo "</pre>"
cat footer.inc
