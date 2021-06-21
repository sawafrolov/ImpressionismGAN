import torch
from pytorch_lightning import LightningModule
from app.gan.components import Discriminator, Generator


class CycleGAN(LightningModule):

    def __init__(self):
        super().__init__()
        self.photo_discriminator = Discriminator()
        self.impressionism_discriminator = Discriminator()
        self.photo_generator = Generator()
        self.impressionism_generator = Generator()

    def forward(self, x):
        return x

    @torch.no_grad()
    def generate_impressionism(self, photo):
        return self.impressionism_generator(photo)

    @torch.no_grad()
    def generate_photo(self, impressionism):
        return self.photo_generator(impressionism)
