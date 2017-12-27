from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules = cythonize(Extension(
  "convu",                                # the extension name
  sources=["convu.pyx", "convutils.cpp"], # the Cython source and
  # additional C++ source files
  language="c++",                        # generate and compile C++ code
  extra_compile_args=['-std=c++11', '-O3'],
)))