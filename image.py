from PIL import Image
from PIL import ImageFilter

with Image.open(r"C:\Users\Mr Prince\Downloads\great-wave-off-kanagawa.jpg") as img:
    img=img.rotate(180)
    img=img.filter(ImageFilter.FIND_EDGES)
    img.save("output.jpeg")