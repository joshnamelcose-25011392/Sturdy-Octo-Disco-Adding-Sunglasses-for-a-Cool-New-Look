from PIL import Image
import pillow_avif

# Open the AVIF image
img = Image.open("images/sunglasses.png")

# Convert and save as a real PNG
img.save("images/sunglasses_real.png", "PNG")

print("Conversion successful!")
print("Created: images/sunglasses_real.png")