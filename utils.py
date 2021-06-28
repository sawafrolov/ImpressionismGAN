from os import listdir
import numpy as np
import torch
from matplotlib.image import imsave
from skimage.io import imread
from skimage.transform import resize


def load_images():
    images = []
    for filename in listdir("source"):
        if filename.endswith("jpg"):
            img = imread("source/" + filename)
            image = resize(img, (64, 64))
            images.append(image)
    result = np.array(images, np.float32)
    return torch.from_numpy(result)


def save_images(images):
    i = 1
    for image in images:
        image = np.abs(image)
        path = "restyled/" + str(i) + ".jpg"
        imsave(path, image)
        i += 1
    return
