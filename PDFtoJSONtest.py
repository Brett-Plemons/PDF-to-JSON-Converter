from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

# Initializes OCR tools and Languages
tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()
lang = lang[1]

# Assigns placeholders for input and output
x = 'TestSpec.pdf'
req_image = []
final_text = []

# Converts .pdf to .jpg to use OCR on (Most OCR tools cannot scan .pdf)
image_pdf = Image(filename = x, resolution = 300)
image_jpg = image_pdf.convert('jpeg')

# When converting .pdf to .jpg the file contains a separate image for each page, this creates 1 image using wand
for img in image_jpg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))

# This uses pillow to convert the image to a string using OCR tools
for img in req_image:
    txt = tool.image_to_string(
        PI.open(io.BytesIO(img)),
        lang = lang,
        builder = pyocr.builders.TextBuilder()
    )
    final_text.append(txt)
    return final_text

# this is a test line to check that the code is outputting something
print(final_text)
