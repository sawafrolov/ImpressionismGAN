import torch.nn as nn
from pytorch_lightning import LightningModule
from app.gan.utils import make_conv_layer, make_deconv_layer


RESIDUAL_BLOCKS_NUM = 8


class ResidualBlock(LightningModule):

    def __init__(self, channels):
        super().__init__()
        self.layer_1 = nn.Sequential(
            nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(channels),
            nn.ReLU()
        )
        self.layer_2 = nn.Sequential(
            nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(channels)
        )

    def forward(self, x):
        x1 = self.layer_1(x)
        result = x + self.layer_2(x1)
        return result


class Generator(LightningModule):

    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            make_conv_layer(3, 64),
            make_conv_layer(64, 128),
            make_conv_layer(128, 256)
        )
        layers = [ResidualBlock(256)] * RESIDUAL_BLOCKS_NUM
        self.bottleneck = nn.Sequential(*layers)
        self.decoder = nn.Sequential(
            make_deconv_layer(256, 128),
            make_deconv_layer(128, 64),
            nn.ConvTranspose2d(64, 3, kernel_size=4, stride=2, padding=1, bias=False),
            nn.Tanh()
        )

    def forward(self, x):
        e = self.encoder(x)
        b = self.bottleneck(e)
        result = self.decoder(b)
        return result
