# # Unity Docker Renderer - Real-Time Graphics Overlay


## Description
This project implements a **headless Unity rendering system** running inside a Docker container. The Unity-generated graphics are overlaid on a video stream in real-time, enabling efficient and automated rendering workflows.

## Commands to run

In order to build and run all the container, run the following commands:

To build and run all containers, execute the following commands:

```bash
# Inspect or create the network
docker network inspect my_network || docker network create my_network

# Start the web server container
cd web_server
docker build -t web_server .
docker run -d --name web_server --network my_network -p 5000:5000 web_server

# Start the streamer container
cd ../streamer
docker build -t streamer_container .
docker run --rm -d --name streamer_container --network my_network streamer_container
docker cp drone_video.mov streamer_container:/app/

# Start the Unity engine container
cd ../unity-docker
docker build -t unity_engine .
docker run -d --name unity_engine --network my_network unity_engine

# Execute commands inside the streamer container
docker exec -it streamer_container bash
docker cp streamer_container:/app/drone_video_with_graphics.avi ~/Desktop
