import torch
from diffusers import StableDiffusionInpaintPipeline
from diffusers.utils import PIL_INTERPOLATION
from PIL import Image, ImageOps
import requests
from io import BytesIO

# Load the Stable Diffusion Inpaint pipeline
pipeline = StableDiffusionInpaintPipeline.from_pretrained("runwayml/stable-diffusion-inpainting", torch_dtype=torch.float16)
pipeline = pipeline.to("cuda")

# Download the image
image_url = 'https://drive.google.com/uc?export=download&id=17FCAXI5mS2Iof9NWQAmg68H2rGK0xTIc'
response = requests.get(image_url)
image = Image.open(BytesIO(response.content)).convert("RGB")

# Resize image to 1024x1024 if not already
image = image.resize((1024, 1024), PIL_INTERPOLATION["bicubic"])

# Add 128 pixels on each side
new_width, new_height = 1024 + 2 * 128, 1024 + 2 * 128
outpainted_image = Image.new('RGB', (new_width, new_height), (255, 255, 255))
outpainted_image.paste(image, (128, 128))

# Prepare the mask and prompt
mask = Image.new("L", (new_width, new_height), 0)
mask.paste(Image.new("L", (1024, 1024), 255), (128, 128))
prompt = "A natural extension of the given image"

# Ensure image and mask are in the correct format
outpainted_image = ImageOps.exif_transpose(outpainted_image)
mask = ImageOps.exif_transpose(mask)

# Generate the outpainted image
with torch.no_grad():
    outpainted_image = pipeline(prompt=prompt, image=outpainted_image, mask_image=mask).images[0]

# Display the result
outpainted_image.show()

# Save the outpainted image
outpainted_image.save("outpainted_image.png")
