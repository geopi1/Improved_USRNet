# BLIND USRNET

A project in Statistical Image Processing.
Extension of [Deep unfolding network for image super-resolution](https://arxiv.org/pdf/2003.10428.pdf) 
for Blind Super Resolution via [Kernel Estimation](https://arxiv.org/abs/1909.06581) 

In this project we aim to extend USRNet [1] for Blind Super Resolution. We
added a step of blind kernel estimation [2] and noise STD estimation [3] algorithm. These additions show SOTA performance in Blind-SR

Written with Eyal Naor - https://github.com/eyalnaor

![Default](./results/0002_x4_usrnetdefaultdefault_noise_LE.png)
## Getting Started

Clone the Repo:  
```bash
git clone https://github.com/geopi1/Improved_USRNet.git
```

### Datasets
Download the Datasets (a bicubically downscaled version of DIV2K):

The following links will download the data folders:
* [DIV2K_HR_ds2](https://technionmail-my.sharepoint.com/:f:/g/personal/pisha_campus_technion_ac_il/EvDI2KscamdIthHRiThIGkIBlDVlADiD6C89g4w0Yr6qbQ?e=Y7MBql) - Ground truth high resolution images
* [DIV2K_LR](https://technionmail-my.sharepoint.com/:f:/g/personal/pisha_campus_technion_ac_il/EpBY9tozdZhNiM7m1M4yQtsB-GGHnDKHQK_KidTVYpCwVQ?e=u4hhZ1) - the low resolution input

To reproduce the results place the DIV2K_LR images in ./input_images
### Prerequisites
Tested and ran on:  
 * UBUNTU 18.04  
 * RTX 2080  
 * Nvidia driver 440.95.10  
 * cuda 10.1.243  
 * cudnn 7.6.5  
 * pytorch 1.5  
 * TF 1.14  
for additional package information please refer to requirements.txt or env.yml 
 
 
1. Setup conda 
    ```bash
    conda env create -f env.yml
    ```
    This will create a working environment named Blind_USRNet
2. Setup can also be performed with pip (virtual env) via the requirements.txt file 
    ```bash
    python -m venv Blind_USRNet
    pip install -r requirements.txt
    ```
3. There are several examples provided with the code in ./input_images
4. All other images to be tested should be placed in ./input_images

## Running the Code
### Code
```bash
python main.py 
```
This will output 4 types of images to ./results: 
* Default USRNet settings
* Default USRNet settings + estimated Noise STD 
* Kernel estimated USRNet
* Kernel estimated USRNet + estimated Noise STD

Additionally, for each estimated image a side-by-side image with the LR version is saved with the degredation kernel (default or estimated)  

### Numerical Evaluation
To calculate the numerical results on the whole dataset run:
```bash
python utils/get_results.py
```
This will calculate the mean PSNR and SSIM on the SR<->HR on all the results

## Numerical Results
| Metric        | Default        | Default + Noise Est. | Kernel Est.          | Kernel Est. + Noise Est. |
| ------------- | -------------- | -------------------- | -------------------- | ------------------------ |
| PSNR          | 22.35 dB       | 22.30 (-0.05) dB     | **26.31 (+3.96) dB** | 26.29 (+3.94) dB         |
| SSIM          | 0.756          | 0.755 (-0.001)       | **0.797 (+0.041)**   | 0.797 (+0.041)           |

To download the results use the following links:

* [USRGAN_results](https://technionmail-my.sharepoint.com/:f:/g/personal/pisha_campus_technion_ac_il/Evr8_LPl4YREoNp8Lvy4TVcBoXoqrxCB32dQDgDeFz0MQw?e=omnuhY) - USRGAN Results
* [USRNet_results](https://technionmail-my.sharepoint.com/:f:/g/personal/pisha_campus_technion_ac_il/Ej-ltn6AfO1PlaV1qdXKODABkEGoPZPSnJdQvDB_2OjrWg?e=mSAbKx) - USRNet Results  

Each will download 800 folders where each folder has the following files:
1. <im_number>_kernel_x2.mat - the estimated kernel
2. <im_number>\_x4\_<net_type>\_defaultdefualt_noise.png - HR reconstruction with default kernel and default noise levels
3. <im_number>\_x4\_<net_type>\_defaultdefualt_noise_LE.png - side-by-side of (2) and NN interpolation LR image 
4. <im_number>\_x4\_<net_type>\_defaultest_noise.png - HR reconstruction with default kernel and estimated noise levels 
5. <im_number>\_x4\_<net_type>\_defaultdest_noise_LE.png - side-by-side of (4) and NN interpolation LR image 
6. <im_number>\_x4\_<net_type>\_KernelGANdefault_noise.png - HR reconstruction with estimated kernel and default noise levels 
7. <im_number>\_x4\_<net_type>\_KernelGANdefault_noise_LE.png - side-by-side of (6) and NN interpolation LR image 
8. <im_number>\_x4\_<net_type>\_KernelGANest_noise.png - HR reconstruction with estimated kernel and estimated noise levels 
9. <im_number>\_x4\_<net_type>\_KernelGANest_noise_LE.png - side-by-side of (8) and NN interpolation LR image 
 
5. psnr_log.txt - psnr & SSIM calculation for each image 

## Visual Results
On each image we see (top) the default USRNet estimation with the default kernel, (middle) Blind-USRNet with the estimated kernel and (bottom) Ground Truth.  
The blur kernel of the LR image is at the top left corner.  
Example 1:   
![Default](./results/Picture1.png)  
Example 2:  
![Ours](./results/Picture2.png)  
Example 3:  
![Default](./results/Picture3.png)  

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
[1] Zhang, Kai, Luc Van Gool, and Radu Timofte. "Deep unfolding network for image super-resolution." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.

[2] Bell-Kligler, Sefi, Assaf Shocher, and Michal Irani. "Blind super-resolution kernel estimation using an internal-gan." Advances in Neural Information Processing Systems. 2019.

[3] Chen G , Zhu F , Heng P A . "An Efficient Statistical Method for Image Noise Level Estimation" 2015 IEEE International Conference on Computer Vision (ICCV). IEEE Computer Society, 2015.