#!/usr/bin/env python

from setuptools import setup

import pyHannanum

setup(name='Korean-morpheme-analyzer',
      version=pyHannanum.__version__,
      description='Korean morpheme analyzer with hannanum',
      author='Brenden Jeon',
      author_email='chulwook.jeonb@gmail.com',
      url='https://github.com/brenden15/pyHnnnanum',
      packages=['pyHnnnanum'],
      keywords=['Korean', 'morpheme'],
      install_requires=[
          'Cython>=0.18',
          'jnius>=1.1-dev']
)