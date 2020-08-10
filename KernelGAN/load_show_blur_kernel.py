from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np


# kernel = np.zeros((17,17))
# kernel[6:11,6:11] = np.ones((5,5),np.float32)/25
x = loadmat('./results/soldiers_ww2_small/soldiers_ww2_small_kernel_x2.mat')['Kernel']
plt.figure()
# plt.subplot(1,2,1)
# plt.title('original kernel')
# plt.imshow(kernel,'gray')
# plt.subplot(1,2,2)
plt.title('estimated kernel')
plt.imshow(x,'gray')

plt.show()
