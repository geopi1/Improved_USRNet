import matplotlib.pyplot as plt
import os
import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim
from USRNet.utils import utils_image as util


SMALL_SIZE = 24
MEDIUM_SIZE = 24
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

res_dir = '/home/george/PycharmProjects/Statistical_im_proc/KernelGAN/results'
gt_dir = '/media/george/storge/USRNet/DIV2K_HR_ds2'
result_list = sorted(os.listdir(res_dir))

psnr_list = list()
ssim_list = list()

for ind,folder in enumerate(result_list):
    zssr_im = util.imread_uint(os.path.join(res_dir,folder, f'ZSSR_{folder}.png'))
    gt_im = util.imread_uint(os.path.join(gt_dir,f'{folder}.png'))
    if gt_im is None or zssr_im is None:
        continue

    psnr_list.append(cv2.PSNR(gt_im,zssr_im))
    ssim_list.append(ssim(gt_im,zssr_im, data_range=gt_im.max()-gt_im.min(), multichannel=True))

print(f'ZSSR PSNR: {np.mean(psnr_list):.2f}')
print(f'ZSSR SSIM: {np.mean(ssim_list):.3f}')

