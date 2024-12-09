import socket
import cv2
import numpy as np

# Function to overlay graphics on the video
def overlay_graphics_on_video(video_path, graphic_data):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('/output/drone_video_with_graphics.avi', fourcc, 20.0, (640, 480))  # Save in /app directory inside container
    out = cv2.VideoWriter('/app/drone_video_with_graphics.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Overlay the graphics (e.g., add text to the video frame)
        cv2.putText(frame, graphic_data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Write the frame to the output video
        out.write(frame)

    cap.release()
    out.release()

# Main function to handle socket communication
def main():
    server_address = ('0.0.0.0', 12346)  # Listening on all IP addresses, port 12345
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)
    sock.listen(1)

    print("Streamer is waiting for connection...")
    connection, client_address = sock.accept()
    print(f"Connection established with {client_address}")

    video_path = '/app/drone_video.mov'  # Video inside /app directory inside the container
    while True:
        #graphic_data = connection.recv(1024).decode()  # Receive graphic data from Unity
        graphic_data = 'EISAI MALAKIA'
	if not graphic_data:
            break
        print(f"Received graphic data: {graphic_data}")
        overlay_graphics_on_video(video_path, graphic_data)

    connection.close()

if __name__ == '__main__':
    main()
    while True:
        pass # Keep the script running

