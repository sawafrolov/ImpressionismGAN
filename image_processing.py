import numpy as np
import torch
from matplotlib.image import imsave
from skimage.io import imread
from skimage.transform import resize
from gan import CycleGAN


SOURCE_PATH = "app/static/source.png"
RESTYLED_PATH = "app/static/restyled.png"

model = CycleGAN.load_from_checkpoint("resources/model.ckpt")
model.eval()


def write_source(image):
    image.save(SOURCE_PATH)


def write_image(image: np.array, path: str):
    imsave(path, image)


def restyle_image(image):
    write_source(image)
    img = imread(SOURCE_PATH)
    source = resize(img, (64, 64))
    write_image(source, SOURCE_PATH)
    photo = torch.from_numpy(np.array([source], np.float32))
    restyled = model.generate_impressionism(photo.permute(0, 3, 2, 1))
    restyled = restyled.permute(0, 3, 2, 1).numpy()[0]
    write_image(restyled, RESTYLED_PATH)
