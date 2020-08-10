import os

import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm

base_dir = '/media/george/storge/USRNet/results'

dir_list = sorted(os.listdir(base_dir))
# filenames = ['00000.png', '00001.png', '00002.png', '00003.png', '00004.png', '00005.png', '00006.png', '00007.png']
filenames = sorted([f for f in os.listdir(os.path.join(base_dir,dir_list[0])) if f.startswith('0')])

for ind, folder in tqdm(enumerate(dir_list)):
    psnr_list = []
    gt_im = cv2.imread(os.path.join(base_dir, folder, 'GT.png'))
    with open(os.path.join(base_dir, folder, 'psnr.txt'), 'w') as f:
        for im_ind, img_name in enumerate(filenames):
            cur_im = cv2.imread(os.path.join(base_dir, folder, img_name))
            psnr = cv2.PSNR(cur_im, gt_im)
            psnr_list.append(psnr)
            f.write(f'{img_name }\t {psnr}\n')
    plt.clf()
    plt.plot(psnr_list)
    plt.xlabel('img')
    plt.ylabel('psnr')
    plt.title('PSNR per iteration')
    plt.savefig(os.path.join(base_dir, folder, 'psnr_fig.png'))
