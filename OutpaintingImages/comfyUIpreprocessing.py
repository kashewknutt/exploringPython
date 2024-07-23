from PIL import Image


# Load the original image
image_path = r"OutpaintingImages\assignment.jpg"
image = Image.open(image_path).convert("RGB")

# Resize image to 1024x1024 if not already
image = image.resize((1024, 1024), Image.BICUBIC)

# Add 128 pixels on each side
new_width, new_height = 1024 + 2 * 128, 1024 + 2 * 128
outpainted_image = Image.new('RGB', (new_width, new_height), (255, 255, 255))
outpainted_image.paste(image, (128, 128))

# Prepare the mask
mask = Image.new("L", (new_width, new_height), 0)
mask.paste(Image.new("L", (1024, 1024), 255), (128, 128))

# Save the prepared images
outpainted_image.save("OutpaintingImages\outpainted_image_prepared.png")
mask.save("OutpaintingImages\mask.png")
