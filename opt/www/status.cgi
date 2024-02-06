#!/bin/bash
. header.sh

if [ ! -e /etc/iot-open/iotopen.json ]; then
  echo "<h2>No config.</h2>"
  echo 'Please <a href="setup.cgi">configure</a> this Gateway.'
  cat footer.inc
  exit
fi

echo "<pre>"

echo "<b>Testing Mosqutitto</b>"
if pgrep mosquitto >/dev/null; then
  echo "Mosquitto is running<br>"
fi

echo "<b>Testing Edged</b>"
if pgrep edged >/dev/null; then
  echo "Edged running <br>"
fi

echo "</pre>"
cat footer.inc
