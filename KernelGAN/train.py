import os
import tqdm

from KernelGAN.configs import Config
from KernelGAN.data import DataGenerator
from KernelGAN.kernelGAN import KernelGAN
from KernelGAN.learner import Learner


def estimate_kernel(filename, input_dir, output_dir, noise_scale=1):
    """The main function - performs kernel estimation (+ ZSSR) for all images in the 'test_images' folder"""
    # Run the KernelGAN sequentially on all images in the input directory
    conf = Config().parse(create_params(filename, input_dir, output_dir, noise_scale))
    gan = KernelGAN(conf)
    learner = Learner()
    data = DataGenerator(conf, gan)
    for iteration in tqdm.tqdm(range(conf.max_iters), ncols=60):
        [g_in, d_in] = data.__getitem__(iteration)
        gan.train(g_in, d_in)
        learner.update(iteration, gan)
    return gan.finish()


def create_params(filename, input_dir, output_dir, noise_scale):
    params = ['--input_image_path', os.path.join(input_dir, filename),
              '--output_dir_path', os.path.abspath(output_dir),
              '--noise_scale', str(noise_scale)]

    return params

