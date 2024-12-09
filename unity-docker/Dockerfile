# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Set the environment variable to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive
ENV XDG_RUNTIME_DIR=/tmp/xdg
ENV DISPLAY=:99

# Install necessary dependencies for running Unity applications
RUN apt-get update && apt-get install -y \
    libstdc++6 \
    libgcc1 \
    libx11-6 \
    libxcb1 \
    libxau6 \
    libxdmcp6 \
    libxext6 \
    libgl1 \
    libglib2.0-0 \
    libnss3 \
    libasound2 \
    libpulse0 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*
# Copy your Unity build into the container
COPY UnityProjectBuild_Data/ /unity_project/UnityProjectBuild_Data/
COPY UnityProjectBuild.x86_64 /unity_project/UnityProjectBuild.x86_64
COPY UnityPlayer.so /unity_project/UnityPlayer.so

# Set executable permissions on the Unity executable
RUN chmod +x /unity_project/UnityProjectBuild.x86_64

# Set the working directory
WORKDIR /unity_project

# Run the Unity application in headless mode
CMD ["sh", "-c", "./UnityProjectBuild.x86_64 -batchmode -nographics -logFile /unity_project/unity_log.txt"]

