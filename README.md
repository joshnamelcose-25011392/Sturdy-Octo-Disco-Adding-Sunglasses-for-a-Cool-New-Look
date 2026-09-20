# Sturdy-Octo-Disco-Adding-Sunglasses-for-a-Cool-New-Look

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
