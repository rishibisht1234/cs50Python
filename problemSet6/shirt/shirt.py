import sys
from PIL import Image,ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

source = sys.argv[1]
dest = sys.argv[2]

if not (source.lower().endswith(('.jpg','.jpeg','.png')) and dest.lower().endswith(('.jpg','.jpeg','.png'))):
    sys.exit('Invalid input')

source_ext=source.split('.')[1]
des_ext=dest.split('.')[1]
if source_ext != des_ext:
    sys.exit('Input and output have different extensions')

try:
    image = Image.open(source)
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")

image = ImageOps.fit(image, shirt.size)
image.paste(shirt, shirt)

image.save(dest)


