# Phase 2

## Description
bla bla bla

## Commands to run

In order to build and run all the container, run the following commands:

```bash
docker network inspect my_network
cd web_server
docker build -t web_server .
docker run -d --name web_server --network my_network -p 5000:5000 web_server
cd ../streamer
docker build -t streamer_container .
docker run --rm -d --name streamer_container --network my_network streamer_container
docker cp drone_video.mov streamer_container:/app/
cd ../unity-docker
docker build -t unity_engine .
docker run -d --name unity_engine --network my_network unity_engine
docker exec -it streamer_container bash
docker cp streamer_container:/app/drone_video_with_graphics.avi ~/Desktop
```
