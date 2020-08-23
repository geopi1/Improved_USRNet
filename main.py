import os
import matplotlib.pyplot as plt
from KernelGAN.est_kernel import estimate_kernel
from NoiseEstimator.noise_estimation import noise_estimate
from USRNet.main_test_realapplication import run_USRnet
import cv2
import numpy as np
from USRNet.utils import utils_sisr as sr
from USRNet.utils import utils_deblur


# 'usrgan' | 'usrnet' | 'usrgan_tiny' | 'usrnet_tiny'
config = {'net': 'usrnet'}
# list all images
ext = ['.png', '.jpg', 'jpeg']

img_list = sorted([f for f in os.listdir('input_images') if f.endswith(tuple(ext))])
# img_list = sorted([f for f in os.listdir(os.path.join('/media/george/storge', 'USRNet', 'DIV2K_LR')) if f.endswith(tuple(ext))])


for f in img_list:
    noise_est = noise_estimate(plt.imread(os.path.join(r'./input_images', f)), 4)
    kernel = estimate_kernel(f, 'input_images', 'results', noise_est*255)

    # plt.imsave(fr'./results/{f.split(".png")[0]}/kernel.png', cv2.resize(kernel, (170, 170), interpolation=cv2.INTER_CUBIC), cmap='gray')
    #
    # k = utils_deblur.fspecial('gaussian', 25, 2.0)
    # k /= np.sum(k)
    # plt.imsave(fr'./results/{f.split(".png")[0]}/default_kernel.png', cv2.resize(k, (170, 170), interpolation=cv2.INTER_CUBIC), cmap='gray')


    # SR with default kernel
    run_USRnet(config, f)

    # SR with estimated kernel
    run_USRnet(config, f, kernel)

    # SR with estimated kernel
    run_USRnet(config, f, k=None, noise_level_img=noise_est)

    # SR with estimated kernel
    run_USRnet(config, f, kernel, noise_est)
