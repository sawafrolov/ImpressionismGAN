import torch.nn as nn
from pytorch_lightning import LightningModule
from app.gan.utils import make_conv_layer


class Discriminator(LightningModule):

    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=4, stride=2, padding=1, bias=False),
            nn.ReLU(),
            make_conv_layer(64, 128),
            make_conv_layer(128, 256),
            make_conv_layer(256, 512),
            nn.Conv2d(512, 1, kernel_size=4, stride=1, padding=0, bias=False),
            nn.Flatten(),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)
