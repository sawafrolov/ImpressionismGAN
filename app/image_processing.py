import numpy as np
import matplotlib.image
from skimage.io import imread
from skimage.transform import resize


SOURCE_PATH = "app/static/source.png"
RESTYLED_PATH = "app/static/restyled.png"


def write_source(image):
    image.save(SOURCE_PATH)


def write_image(image: np.array, path: str):
    matplotlib.image.imsave(path, image)


def restyle_image(image):
    write_source(image)
    source = imread(SOURCE_PATH)
    write_image(source, SOURCE_PATH)
    write_image(source, RESTYLED_PATH)
