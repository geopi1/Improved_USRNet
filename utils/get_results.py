import matplotlib.pyplot as plt
import os
import numpy as np

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

base_dir = './results_usrnet_8iter'
result_list = sorted(os.listdir(base_dir))

default_psnr = list()
default_ssim = list()
k_gan_psnr = list()
k_gan_ssim = list()
noise_est_psnr = list()
noise_est_ssim = list()
noise_kernel_psnr = list()
noise_kernel_ssim = list()

for ind,folder in enumerate(result_list):
    if not os.path.exists(os.path.join(base_dir,folder,'psnr_log.txt')):
        continue
    with open(os.path.join(base_dir,folder,'psnr_log.txt'), 'r') as f:
        data = f.readlines()


    default_psnr.append(float(data[0].split()[4]))
    default_ssim.append(float(data[0].split()[-1]))
    k_gan_psnr.append(float(data[1].split()[4]))
    k_gan_ssim.append(float(data[1].split()[-1]))
    noise_est_psnr.append(float(data[2].split()[4]))
    noise_est_ssim.append(float(data[2].split()[-1]))
    noise_kernel_psnr.append(float(data[3].split()[4]))
    noise_kernel_ssim.append(float(data[3].split()[-1]))

print(f'Default PSNR: {np.mean(default_psnr):.3f}, STD: {np.std(default_psnr):.3f}')
print(f'Default SSIM: {np.mean(default_ssim):.3f}, STD: {np.std(default_ssim):.3f}')
print(f'noise PSNR: {np.mean(noise_est_psnr):.3f}, STD: {np.std(noise_est_psnr):.3f}')
print(f'noise SSIM: {np.mean(noise_est_ssim):.3f}, STD: {np.std(noise_est_ssim):.3f}')
print(f'Kernel PSNR: {np.mean(k_gan_psnr):.3f}, STD: {np.std(k_gan_psnr):.3f}')
print(f'Kernel SSIM: {np.mean(k_gan_ssim):.3f}, STD: {np.std(k_gan_ssim):.3f}')
print(f'noise+Kernel PSNR: {np.mean(noise_kernel_psnr):.3f}, STD: {np.std(noise_kernel_psnr):.3f}')
print(f'noise+kernel SSIM: {np.mean(noise_kernel_ssim):.3f}, STD: {np.std(noise_kernel_ssim):.3f}')

plt.figure()
plt.title('Method Comparison')
plt.xlabel('image')
plt.ylabel('PSNR [dB]')
plt.plot(default_psnr,'--o')
plt.plot(k_gan_psnr,'--o')
# plt.plot(noise_est_psnr)
# plt.plot(noise_kernel_psnr)
plt.legend([f'default mean={np.mean(default_psnr):.2f}', f'kernel est mean={np.mean(k_gan_psnr):.2f}', 'noise est', 'kernel+noise'])

plt.figure()
plt.title('Method Comparison')
plt.xlabel('image')
plt.ylabel('SSIM')
plt.plot(default_ssim,'--o')
plt.plot(k_gan_ssim,'--o')
# plt.plot(noise_est_ssim)
# plt.plot(noise_kernel_ssim)
plt.legend([f'default mean={np.mean(default_ssim):.3f}',f'kernel est mean={np.mean(k_gan_ssim):.3f}', 'noise est', 'kernel+noise'])
plt.show()