# Statistical Image Processing

A project in Statistical Image Processing.
Extension of [Deep unfolding network for image super-resolution](https://arxiv.org/pdf/2003.10428.pdf) 
for Blind Super Resolution via [Kernel Estimation](https://arxiv.org/abs/1909.06581) 


## Getting Started

Clone the Repo:  
```bash
git clone https://github.com/geopi1/Improved_USRNet.git
```

### Datasets
Download the Datasets (a bicubically downscaled version of DIV2K):

[link to mridata](https://drive.google.com/drive/folders/1wITaNr7KNg_keUnK4myKjUoKA4HGeONA?usp=sharing)

### Prerequisites
Tested and run on UBUNTU 18.04
1. Setup conda 
    ```bash
    conda env create -f env.yml
    ```
    This will create a working environment named Blind_USRNet
2. Setup can also be performed with pip (virtual env) via the requirements.txt file 
    ```bash
    python3 -m venv Blind_USRNet
    pip install -r requirements.txt
    ```
3. put images in right place

## Running Tests
### Code
HOW TO RUN

### Logs
RESULTS 

## Results
![Default](./results/0002_x4_usrnetdefaultdefault_noise_LE.png)

![Ours](./results/0002_x4_usrnetKernelGANdefault_noise_LE.png)

![Default](./results/0008_x4_usrnetdefaultdefault_noise_LE.png)

![Ours](./results/0008_x4_usrnetKernelGANdefault_noise_LE.png)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
[1] Zhang, Kai, Luc Van Gool, and Radu Timofte. "Deep unfolding network for image super-resolution." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.

[2] Bell-Kligler, Sefi, Assaf Shocher, and Michal Irani. "Blind super-resolution kernel estimation using an internal-gan." Advances in Neural Information Processing Systems. 2019.
