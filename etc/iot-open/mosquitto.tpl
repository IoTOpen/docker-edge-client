user mosquitto
persistence true
persistence_location /var/lib/mosquitto/
persistence_file mosquitto.db
autosave_interval 3600
autosave_on_changes false

connection lynx-${client_id}
bridge_capath /etc/ssl/certs/
username ${mqtt_username}
password ${mqtt_password}
address ${mqtt_broker}
clientid edge-${client_id}
notification_topic ${client_id}/box/event/status

topic set/# both 1 "" ${client_id}/
topic obj/# both 1 "" ${client_id}/
topic cmd/# both 1 "" ${client_id}/
topic evt/# both 1 "" ${client_id}/
