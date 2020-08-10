import os
from KernelGAN.train import estimate_kernel
from USRNet.main_test_realapplication import run_USRnet
import numpy as np


# 'usrgan' | 'usrnet' | 'usrgan_tiny' | 'usrnet_tiny'
config = {'net': 'usrnet'}
# list all images
ext = ['.png', '.jpg', 'jpeg']

# img_list = sorted([f for f in os.listdir('input_images') if f.endswith(tuple(ext))])
img_list = sorted([f for f in os.listdir(os.path.join('/media/george/storge', 'USRNet', 'DIV2K_LR')) if f.endswith(tuple(ext))])

# TODO: add noise estimation
noise = 1

for f in img_list:
    # kernel = estimate_kernel(f, 'input_images', 'results', noise)

    # SR with default kernel
    run_USRnet(config, f)
    # SR with estimated kernel
    # run_USRnet(config, f, kernel)
    # comapre and print/save results

