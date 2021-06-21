import torch
import torch.nn as nn


def real_mse_loss(D_out):
    return torch.mean((D_out - 1) ** 2)


def fake_mse_loss(D_out):
    return torch.mean(D_out ** 2)


cycle_loss = nn.MSELoss()
