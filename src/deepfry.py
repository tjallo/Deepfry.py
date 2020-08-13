import os, sys
from PIL import Image, ImageEnhance, ImageOps

def deepfry(imagePath, outputFolder):
    filename, fileExt = os.path.splitext(imagePath)
    filename = filename.split('/')[-1]
    with Image.open(imagePath) as im:
        width, height = im.width, im.height
        im = im.resize((int(width ** 0.8969), int((height ** 0.8969))), Image.BILINEAR)
        im = im.resize((int(width ** 0.89420), int((height ** 0.89420))), Image.BILINEAR)
        im = im.resize((width, height), Image.BILINEAR)
        im.save(f'{outputFolder}/{filename}.png')
    return f'{filename}.png'