FROM debian:bookworm

ADD opt /opt
ADD https://pkg.iotopen.se/conf/iotopen.gpg.key /root/iotopen.gpg.key

RUN apt-get update && apt-get install -y gnupg ca-certificates && \
	apt-key add /root/iotopen.gpg.key && \
	rm /root/iotopen.gpg.key
ADD etc /etc
RUN apt-get update && \
	apt-get install -y iotopen-verify mosquitto mini-httpd procps curl jq \
	iputils-ping iotopen-edge

CMD ["/opt/iotopen/edge/start.sh"]
