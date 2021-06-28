from utils import load_images, save_images
from gan import CycleGAN

model = CycleGAN.load_from_checkpoint("model.ckpt")
images = load_images().permute(0, 3, 2, 1)
restyled = model.generate_impressionism(images)
restyled = restyled.permute(0, 3, 2, 1).numpy()
save_images(restyled)
