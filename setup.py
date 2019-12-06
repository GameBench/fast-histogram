import os
import io
import sys

from setuptools import setup
from setuptools.extension import Extension
from setuptools.command.build_ext import build_ext


class build_ext_with_numpy(build_ext):
    def run(self):
        import numpy
        self.include_dirs.append(numpy.get_include())
        build_ext.run(self)


extensions = [Extension("gb_fast_histogram._histogram_core",
                        [os.path.join('gb_fast_histogram', '_histogram_core.c')])]

with io.open('README.rst', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

try:
    import numpy
except ImportError:
    # We include an upper limit to the version because setup_requires is
    # honored by easy_install not pip, and the former doesn't ignore pre-
    # releases. It's not an issue if the package is built against 1.15 and
    # then 1.16 gets installed after, but it still makes sense to update the
    # upper limit whenever a new version of Numpy is released.
    setup_requires = ['numpy<1.16']
else:
    setup_requires = []

setup(name='gb-fast-histogram',
      version='0.1gb0',
      description='Fast simple 1D and 2D histograms',
      long_description=LONG_DESCRIPTION,
      setup_requires=setup_requires ,
      install_requires=['numpy'],
      author='Thomas Robitaille',
      author_email='thomas.robitaille@gmail.com',
      license='BSD',
      url='https://github.com/GameBench/gb-fast-histogram',
      packages=['gb_fast_histogram', 'gb_fast_histogram.tests'],
      ext_modules=extensions,
      cmdclass={'build_ext': build_ext_with_numpy})
