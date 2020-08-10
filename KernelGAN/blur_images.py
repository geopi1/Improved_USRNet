import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter


img = cv.imread('/home/george/PycharmProjects/Statistical_im_proc/KernelGAN/test.jpg')
kernel = np.ones((17,17),np.float32)/289
dst = cv.filter2D(img,-1,kernel)

g_img = gaussian_filter(img, [1,10,0])

cv.imwrite('/home/george/PycharmProjects/Statistical_im_proc/KernelGAN/images/blur.png', dst)
cv.imwrite('/home/george/PycharmProjects/Statistical_im_proc/KernelGAN/images/g_blur.png', g_img)
plt.subplot(131),plt.imshow(img[:,:,::-1]),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(dst[:,:,::-1]),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(g_img[:,:,::-1]),plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.show()