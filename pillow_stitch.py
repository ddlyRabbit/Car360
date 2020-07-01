from PIL import Image
import numpy
import json
import os
import glob
import time
import copy

folder = "360photos_comp"
images = glob.glob(folder + "/*.jpg")
images = sorted(images)
image = Image.open(images[0])
width, height = image.size
result_width = 1500 * len(images)
result_height = 1000
result_image = Image.new('RGB',(result_width,result_height))

for i,image_path in enumerate(images):
    image = Image.open(image_path)
    image = image.resize((1500,1000))
    result_image.paste(im=image, box=(i*1500,0))

result_image.save(folder + "/stitched_image.jpg")