# Sturdy-Octo-Disco-Adding-Sunglasses-for-a-Cool-New-Look

Reference Number: 212225230118
Name: Joshna.M

Sturdy Octo Disco is a fun project that adds sunglasses to photos using image processing.

Welcome to Sturdy Octo Disco, a fun and creative computer vision project designed to overlay sunglasses on passport-size photos. This repository demonstrates how image processing techniques can be used to create a playful transformation.

## Features:

- Identifies the eye region using pixel coordinates.
- Places a sunglasses overlay on the selected eye region.
- Works with individual passport-size photos.
- Uses masking and alpha blending for smooth results.
- Can be customized with different sunglasses images.

## Technologies Used:

- Python
- OpenCV for image processing
- NumPy for array manipulations
- Pillow for image format conversion

## Code:

The main program uses OpenCV and NumPy to resize the sunglasses, create an alpha mask, and blend the overlay with the selected eye region.

### Load the Images

```python
import cv2
import numpy as np

img = cv2.imread("images/passport.jpg")

sunglasses = cv2.imread(
    "images/sunglasses_real.png",
    cv2.IMREAD_UNCHANGED
)

Define the Eye Region
x1 = 140
y1 = 70
x2 = 225
y2 = 110

width = x2 - x1
height = y2 - y1

Resize and Create the Alpha Mask

sunglasses = cv2.resize(
    sunglasses,
    (width, height),
    interpolation=cv2.INTER_AREA
)

overlay = sunglasses[:, :, :3]
alpha = sunglasses[:, :, 3]

alpha = alpha.astype(np.float32) / 255.0
alpha = cv2.merge([alpha, alpha, alpha])

Blend the Sunglasses
roi = img[y1:y2, x1:x2].astype(np.float32)
overlay = overlay.astype(np.float32)

blended = (
    overlay * alpha
    + roi * (1 - alpha)
)

blended = blended.astype(np.uint8)

img[y1:y2, x1:x2] = blended

Save the Result
cv2.imwrite("images/output.jpg", img)

## How to Use:

1. Clone this repository.
2. Install the required Python packages.
3. Add your passport-size photo to the `images` folder.
4. Run `coordinate_finder.py` to identify the eye-region coordinates.
5. Update the coordinates in `sunglass_overlay.py`.
6. Run the script to create the sunglasses transformation.

## Applications:

- Learning basic image processing techniques.
- Understanding image masking and alpha blending.
- Practicing computer vision workflows.
- Creating fun image transformations.
