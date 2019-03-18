from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()
lang = lang[1]

x = 'TestSpec.pdf'
req_image = []
final_text = []

image_pdf = Image(filename = x, resolution = 300)
image_jpg = image_pdf.convert('jpeg')

for img in image_jpg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))

for img in req_image:
    txt = tool.image_to_string(
        PI.open(io.BytesIO(img)),
        lang = lang,
        builder = pyocr.builders.TextBuilder()
    )
    final_text.append(txt)
    return final_text

print(final_text)