import cv2
import numpy as np

# Load the image
image = cv2.imread("istockphoto-97929744-612x612.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and improve circle detection
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Use HoughCircles to detect circles in the image
circles = cv2.HoughCircles(
		blurred,
		cv2.HOUGH_GRADIENT,
		dp=1,
		minDist=250,
		param1=50,
		param2=30,
		minRadius=250,
		maxRadius=300
)

if circles is not None:
		# Convert the coordinates and radius to integers
		circles = np.round(circles[0, :]).astype("int")

		# Draw the circle on the original image
		for (x, y, r) in circles:
				cv2.circle(image, (x, y), r, (0, 255, 0), 4)  # Green circle

				# Draw a line representing the circumference
				cv2.line(image, (x, y), (x + r, y), (0, 255, 0), 2)  # Green line

				# Find the center point of the circle
				center = (x, y)
				cv2.circle(image, center, 5, (255, 0, 0), -1)  # Blue center point

		# Display the result
		cv2.namedWindow("Detected Circle", cv2.WINDOW_NORMAL)
		cv2.imshow("Detected Circle", image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
else:
		print("No circle detected.")
