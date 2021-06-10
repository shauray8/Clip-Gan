import datetime
import numpy as np
import os
import argparse

import torch
import torch.nn as nn
import torchvision 
import torch.optim as optim
import torch.nn.parallel
from torch.utils.data import DataLoader, Dataset
from torch.utils.tensorboard import SummaryWriter
import torchvision.transforms as transforms

from model import *
from utils import *


## ----------------- checking callable functions from model.py ----------------- ##

def callable():
    kwargs = sorted(name for name in model.__dict__
        if name.islower() and not name.startswith("__")
        and callable(model.__dict__[name]))
    return kwargs

## ----------------- Argument Parser just for simpilicity ----------------- ##



if __name__ == "__main__":
    print("training loop goes here ")
