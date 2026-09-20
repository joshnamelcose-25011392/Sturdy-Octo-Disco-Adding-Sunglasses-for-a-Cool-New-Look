import cv2
import numpy as np

# ---------------------------------------------------------
# STEP 1: Load the original passport-size image
# ---------------------------------------------------------
img = cv2.imread("images/passport.jpg")

if img is None:
    print("Error: passport.jpg could not be loaded.")
    exit()

# ---------------------------------------------------------
# STEP 2: Load the converted sunglasses image
# IMREAD_UNCHANGED preserves the alpha/transparency channel
# ---------------------------------------------------------
sunglasses = cv2.imread(
    "images/sunglasses_real.png",
    cv2.IMREAD_UNCHANGED
)

if sunglasses is None:
    print("Error: sunglasses image could not be loaded.")
    exit()

# ---------------------------------------------------------
# STEP 3: Define the eye region
# Coordinates were obtained using coordinate_finder.py
# ---------------------------------------------------------
x1 = 140
y1 = 70
x2 = 225
y2 = 110

# Calculate width and height of the eye region
width = x2 - x1
height = y2 - y1

# ---------------------------------------------------------
# STEP 4: Resize sunglasses to fit the eye region
# ---------------------------------------------------------
sunglasses = cv2.resize(
    sunglasses,
    (width, height),
    interpolation=cv2.INTER_AREA
)

# ---------------------------------------------------------
# STEP 5: Extract the sunglasses and alpha mask
# ---------------------------------------------------------
if sunglasses.shape[2] == 4:

    # First 3 channels contain the BGR image
    overlay = sunglasses[:, :, :3]

    # Fourth channel contains transparency information
    alpha = sunglasses[:, :, 3]

else:

    # Fallback if the image has no alpha channel
    overlay = sunglasses

    gray = cv2.cvtColor(overlay, cv2.COLOR_BGR2GRAY)

    _, alpha = cv2.threshold(
        gray,
        240,
        255,
        cv2.THRESH_BINARY_INV
    )

# ---------------------------------------------------------
# STEP 6: Normalize alpha mask
# Convert 0-255 values to 0-1
# ---------------------------------------------------------
alpha = alpha.astype(np.float32) / 255.0

# Make the mask 3-channel for color blending
alpha = cv2.merge([alpha, alpha, alpha])

# ---------------------------------------------------------
# STEP 7: Extract the eye region from the original image
# ---------------------------------------------------------
roi = img[y1:y2, x1:x2].astype(np.float32)

# Convert sunglasses to float for arithmetic operations
overlay = overlay.astype(np.float32)

# ---------------------------------------------------------
# STEP 8: Blend the sunglasses with the original image
#
# Formula:
# Result = Overlay × Alpha + Original × (1 - Alpha)
# ---------------------------------------------------------
blended = (
    overlay * alpha
    + roi * (1 - alpha)
)

# Convert back to 8-bit image
blended = blended.astype(np.uint8)

# ---------------------------------------------------------
# STEP 9: Replace the original eye region
# with the blended region
# ---------------------------------------------------------
img[y1:y2, x1:x2] = blended

# ---------------------------------------------------------
# STEP 10: Save the final output
# ---------------------------------------------------------
cv2.imwrite("images/output.jpg", img)

print("Sunglasses applied successfully!")
print("Final image saved as output.jpg")

# ---------------------------------------------------------
# STEP 11: Display the final result
# ---------------------------------------------------------
cv2.imshow("Sunglasses Overlay - Final Output", img)

print("Press any key to close the image.")
cv2.waitKey(0)
cv2.destroyAllWindows()