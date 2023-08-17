import cv2

# Open the video file
cap = cv2.VideoCapture(r"C:\Users\aksha\Downloads\testvideo.mp4")

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    
    # If the frame was not read successfully, break the loop
    if not ret:
        break
    
    # Display the frame in a window named "Video"
    cv2.imshow("Original Video", frame)
    
    # Wait for a key press and break the loop if the 'q' key is pressed
    if cv2.waitKey(12) & 0xFF == ord("q"):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()

# Open the input video file
cap = cv2.VideoCapture(r"C:\Users\aksha\Downloads\testvideo.mp4")

# Get video properties
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)


# Create an output video writer
output_path = "SlowedReversedVideo.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(output_path, fourcc, int(fps/3), (width, height))  # Slowed down by half

# Read frames and write to output video
frame_list = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_list.append(frame)
    output.write(frame)
    cv2.imshow("Slowed Video", frame)
    if cv2.waitKey(24) == ord("q"):
        break

# Release input and output video resources
cap.release()
cv2.destroyAllWindows()

# Create a new output video writer for the reversed video
reversed_output_path = "SlowedReversedVideo_Reversed.mp4"
reversed_output = cv2.VideoWriter(reversed_output_path, fourcc, int(fps / 3), (width, height))

# Write frames in reverse order to the reversed output video
for frame in reversed(frame_list):
    reversed_output.write(frame)
    cv2.imshow("Reversed Video", frame)
    if cv2.waitKey(24) == ord("q"):
        break

# Release the reversed output video resource
reversed_output.release()
cv2.destroyAllWindows()
