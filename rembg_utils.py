from rembg import remove
from PIL import Image

def fix_image(upload):
    image = Image.open(upload)
    fixed = remove(image)
    return fixed
