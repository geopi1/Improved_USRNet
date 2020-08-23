import cv2
import os
from utils.imresize import imresize
import matplotlib.pyplot as plt
from USRNet.utils import utils_deblur
from tqdm import tqdm

base_dir = '/media/george/storge/USRNet'
# hr_dir = os.path.join(base_dir,'DIV2K_HR')
hr_dir = os.path.join(base_dir,'DIV2K_HR_ds2')
lr_dir = os.path.join(base_dir,'DIV2K_LR_custom_kernel')
hr_list = os.listdir(hr_dir)


kernel = utils_deblur.blurkernel_synthesis(h=25)
plt.imsave(os.path.join(lr_dir, 'blur_kernel.png'), cv2.resize(kernel/(kernel.max()-kernel.min()),(150,150), interpolation=cv2.INTER_CUBIC), cmap='gray')

for ind,im in tqdm(enumerate(hr_list)):
    hr_img = cv2.imread(os.path.join(hr_dir, im))
    # hr_img = hr_img[:8*(hr_img.shape[0]//8),:8*(hr_img.shape[1]//8),:]
    lr_img = imresize(hr_img, scale_factor=0.25, kernel=kernel)
    cv2.imwrite(os.path.join(lr_dir, f'{im}'), lr_img)
