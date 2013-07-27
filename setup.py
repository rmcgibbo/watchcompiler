import sys
from distutils.core import setup

setup(name='watchcompiler',
      version='0.1',
      description='Watch a directory and trigger compilation of new kernels',
      author='Robert McGibbon',
      author_email='rmcgibbo@gmail.com',
      license='GPLv3+',
      scripts=['watchcompiler'],
  )
