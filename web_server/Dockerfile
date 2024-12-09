# Use Python 3.10-slim image as a base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the Web Server script into the container
COPY web_server.py /app

# Install Flask
RUN pip install flask

# Expose the necessary port
EXPOSE 5000

# Run the Web Server script
CMD ["python", "web_server.py"]
