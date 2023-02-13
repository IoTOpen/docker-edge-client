# IoT Open Edge Client

This is a Docker image that functions as a IoT Open Edge client. It was built as a way to play with Edge apps without
Edge hardware. Please do not expect too much.

## Prerequisites

In order for this to work you need an IoT Open Lynx account and an installation connected to you.

## Getting started with the image

### Build the image

```
docker build -t ghcr.io/iotopen/edge-client .
```

### Run the image

Run the image on any unprivileged port (8088 in the example)

```
docker run -d -p 8088:80 ghcr.io/iotopen/edge-client:latest
```

### Authentication to web gui

The authentication are controlled by environment variables. Either there are no authentication at all. That is suitable
on well protected networks or when another authentication is used.

```
INSECURE=true
```

To use authentication specify the BASE uri for the Lynx-platform.

```
BASE=https://lynx.iotopen.se
```

Then authentication is done by supplying a valid API-key from BASE as a GET parameter called `access-token` to `/` or `/index.cgi`.

#### Examples:

```
docker run -d -e INSECURE=true -p 8088:80 ghcr.io/iotopen/edge-client:latest
docker run -d -e BASE=https://lynx.iotopen.se -p 8088:80 ghcr.io/iotopen/edge-client:latest
```

After starting the container, navigate to `http://localhost:8088/index.cgi?access-token=<insert-api-key>`

#### Headless

Add environment variable `HEADLESS=true` to run without the web interface.

### Stop the image

```
docker ps
docker stop <container id>
```

## Create a secret for your edge-client

This is done from the Installation in the Lynx Web interface

* Click on the Settings menu option
* At the very bottom, click "Create credentials for edge client". Please note that there can only be one. It will be
  regenerated on consecutive clicks.
* Save the information you get for later use.
    * URL (Should be the same as the url in your browser)
    * Client ID
    * Password
    * Installation ID

## Configure your image

* Open running [container in your browser](http://localhost:8088)
* Click on [Setup](http://localhost:8088/setup.sh)
* Enter the credentials as above (the server name should be without protocol, e.g. lynx.iotopen.se.
* Click "Submit" and you should see the config created.
* Click on [Re-register](http://localhost:8088/reregister.sh) to re-register the docker-gateway with the new credentials.
* Under [System Status](http://localhost:8088/status.sh) everything should look nice now.

## Where to go from here

When an Edge app is added to the installation it will automatically be fetched to the container and executed. If the
configuration changes it should also be a sync performed. By following the output you can see the messages from the edge
daemon.

## Further tips

You might use some other flags to Docker to make the image data persistent. You also might forward port 1883 from inside
the container to be able to listen and send commands to the container.

Creating the Edge Apps is out of scope for this document.


