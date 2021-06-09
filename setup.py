import sys
from setuptools import setup, find_packages

sys.path[0:0] = ['Clip-Gan']
#from version import __version__

setup(
  name = 'Clip-Gan-pytorch',
  packages = find_packages(),
  #version = __version__,
  license='MIT',
  description = 'input for CLIP is the output of some kind of GAN',
  author = 'Shauray Singh',
  author_email = 'shauray9@gmail.com',
  url = 'https://github.com/shauray8/clip-gan',
  keywords = ['generative adversarial networks', 'machine learning',"openai"],
  install_requires=[
      'numpy',
      'tqdm',
      'torch',
      'torchvision',
      'pillow',
  ],
)
