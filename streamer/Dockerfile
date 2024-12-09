# Use Python 3.10 slim image as base
FROM python:3.10-slim

# Install OpenCV (for video processing)
RUN pip install opencv-python-headless

# Set the working directory
WORKDIR /app

# Copy the Streamer script into the container
COPY streamer.py /app

# Expose port for the socket (optional, for debugging)
EXPOSE 12346

# Run the Streamer script
CMD ["python", "streamer.py"]
