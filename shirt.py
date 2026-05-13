import sys
from PIL import Image, ImageOps

if len (sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

valid_ext = [".jpg", ".jpeg", ".png"]

def get_ext (filename):
    return filename.lower().rsplit(".", 1) [-1]
if "." not in input_file or "." not in output_file:
    sys.exit("Invalid input")
input_ext = "." + get_ext(input_file)
output_ext = "." + get_ext(output_file)

if input_ext not in valid_ext:
    sys.exit("Invalid input")

if output_ext not in valid_ext:
    sys.exit("Invalid output")

if input_ext != output_ext:
    sys.exit("Input and output have diffrent extensions")

try:
    with Image.open(input_file) as img:
        shirt = Image.open("shirt.png")

        img = ImageOps.fit(img, shirt.size)
        img.paste(shirt, shirt)
        img.save(output_file)
except FileNotFoundError:
    sys.exit("Input does not exist")
