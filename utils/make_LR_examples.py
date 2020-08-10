import cv2
import os
from utils.imresize import imresize

base_dir = '/media/george/storge/USRNet'
hr_dir = os.path.join(base_dir,'DIV2K_HR_ds2')
# lr_dir = os.path.join(base_dir,'DIV2K_HR_ds2')
lr_dir = os.path.join(base_dir,'DIV2K_LR')
hr_list = os.listdir(hr_dir)

for ind,im in enumerate(hr_list):
    hr_img = cv2.imread(os.path.join(hr_dir, im))
    # hr_img = hr_img[:8*(hr_img.shape[0]//8),:8*(hr_img.shape[1]//8),:]
    lr_img = imresize(hr_img, scale_factor=0.25, kernel="cubic")
    cv2.imwrite(os.path.join(lr_dir, f'{im}'), lr_img)
