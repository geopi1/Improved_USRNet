import os
from KernelGAN.train import estimate_kernel
from USRNet.main_test_realapplication import run_USRnet
import numpy as np


# 'usrgan' | 'usrnet' | 'usrgan_tiny' | 'usrnet_tiny'
config = {'net': 'usrgan'}
# list all images
ext = ['.png', '.jpg', 'jpeg']

img_list = sorted([f for f in os.listdir('input_images') if f.endswith(tuple(ext))])

# TODO: add noise estimation
noise = 1

for f in img_list:
    kernel = estimate_kernel(f, 'input_images', 'results', noise)


    # SR with default kernel
    run_USRnet(config, f)
    # SR with estimated kernel
    run_USRnet(config, f, kernel)
    # comapre and print/save results
