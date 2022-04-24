from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

sourcefiles = ['JavaToPySo.pyx', 'main.c']

extensions = [Extension("JavaToPySo", sourcefiles, 
  include_dirs=['/data/java/jdk1.8.0_202/include/linux','/data/java/jdk1.8.0_202/include','/data/python/Python-3.7.0/Include','/usr/local/python3/include/python3.7m'],
  library_dirs=['/data/python/Python-3.7.0/Lib'],libraries=['python3.7m'])]

setup(ext_modules=cythonize(extensions, language_level = 3))
