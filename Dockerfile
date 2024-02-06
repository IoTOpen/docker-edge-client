FROM debian:bookworm

ADD opt /opt
ADD https://pkg.iotopen.se/conf/iotopen.gpg.key /root/iotopen.gpg.key

RUN apt-get update && apt-get install -y gnupg ca-certificates && \
	cat /root/iotopen.gpg.key | gpg --dearmor -o /etc/apt/keyrings/iotopen-apt-keyring.gpg && \
	rm /root/iotopen.gpg.key
ADD etc /etc
RUN apt-get update && \
	apt-get install -y iotopen-verify mosquitto mini-httpd procps curl jq \
	iputils-ping iotopen-edge supervisor mosquitto-clients

CMD ["/opt/iotopen/edge/start.sh"]
