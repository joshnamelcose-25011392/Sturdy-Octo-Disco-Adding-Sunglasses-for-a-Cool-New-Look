import cv2

# Load the passport photo
img = cv2.imread("images/passport.jpg")

if img is None:
    print("Error: passport.jpg not found!")
    exit()

# Get coordinates when you click the image
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"X = {x}, Y = {y}")

# Create window
cv2.namedWindow("Passport Photo")

# Connect mouse callback
cv2.setMouseCallback("Passport Photo", mouse_event)

# Show image
cv2.imshow("Passport Photo", img)

print("Click on the image to get coordinates.")
print("Press ESC to close.")

while True:
    key = cv2.waitKey(1)

    if key == 27:  # ESC
        break

cv2.destroyAllWindows()