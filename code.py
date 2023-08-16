import cv2

#get image from path
image_path = r"C:\Users\aksha\Downloads\thug duck.jpeg"
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)  # Adjust the threshold values as needed

# Display the original image and edge-detected image
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
