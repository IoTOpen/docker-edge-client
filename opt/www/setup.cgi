#!/bin/bash
. header.sh

function urldecode() {
  sed 's/%3A/:/g' | sed 's/%2F/\//g'
}

function remove_nasty_chars() {
  tr -d -c 'a-zA-Z0-9:_\-+\.@'
}

function remove_nasty_chars_url () {
	tr -d -c '[a-zA-Z0-9:_\-+/\.]'
}

if [ -n "${QUERY_STRING}" ]; then
  SERVER=$(echo "${QUERY_STRING}" | urldecode | sed 's/.*server=\([^&]*\).*/\1/' | remove_nasty_chars_url)
  CID=$(echo "${QUERY_STRING}" | urldecode | sed 's/.*client_id=\([^&]*\).*/\1/' | remove_nasty_chars)
  PASSWORD=$(echo "${QUERY_STRING}" | urldecode | sed 's/.*password=\([^&]*\).*/\1/' | remove_nasty_chars)
  IID=$(echo "${QUERY_STRING}" | urldecode | sed 's/.*installation_id=\([^&]*\).*/\1/' | remove_nasty_chars)
  MQTT_USER=$(echo "${QUERY_STRING}" | urldecode | sed 's/.*mqttuser=\([^&]*\).*/\1/' | remove_nasty_chars)
  MQTT_BROKER=$(echo "${QUERY_STRING}" | urldecode | sed 's/.*broker=\([^&]*\).*/\1/' | remove_nasty_chars)
fi

mkdir -p /etc/iot-open/

if [ -n "${SERVER}" ]; then
  cat >/etc/iot-open/iotopen.json <<__END__
{
	"client_id": ${CID},
	"installation_id": ${IID},
	"aam": "${SERVER}",
	"api": "${SERVER}",
	"broker": "${MQTT_BROKER}",
	"mqtt_username":"${MQTT_USER}",
	"mqtt_password":"${PASSWORD}"
}
__END__

  echo "You probably need to <a href=\"reregister.cgi\">re-register</a> this gateway."
fi

echo '<h2>Current config</h2>'
if [ -e /etc/iot-open/iotopen.json ]; then
  echo '<pre>'
  cat /etc/iot-open/iotopen.json
  echo '</pre>'
else
  echo "No config available"
fi

echo "<h2>Configure</h2>"

cat <<__END__
<form method="GET">
<div class="mb-1 row">
    <label for="client_id" class="col-sm-3 col-form-label">Client ID</label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="client_id" name="client_id">
    </div>
</div>
<div class="mb-1 row">
    <label for="client_id" class="col-sm-3 col-form-label">Installation ID</label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="installation_id" name="installation_id">
    </div>
</div>
<div class="mb-1 row">
    <label for="client_id" class="col-sm-3 col-form-label">API</label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="server" name="server">
    </div>
</div>
<div class="mb-1 row">
    <label for="client_id" class="col-sm-3 col-form-label">MQTT broker</label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="broker" name="broker">
    </div>
</div>
<div class="mb-1 row">
    <label for="client_id" class="col-sm-3 col-form-label">MQTT username</label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="mqttuser" name="mqttuser">
    </div>
</div>
<div class="mb-1 row">
    <label for="client_id" class="col-sm-3 col-form-label">MQTT password</label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="password" name="password">
    </div>
</div>

<input class="btn btn-primary" type="submit" value="Submit">
</form>
__END__

cat footer.inc
