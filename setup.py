import sys
from distutils.core import setup

try:
    import watchdog
except:
    breaker = '#' * 80
    print breaker
    print 'This package required the python "watchdog" module'
    print breaker
    sys.exit(1)

setup(name='watchcompiler',
      version='0.1',
      description='Watch a directory and trigger compilation of new kernels',
      author='Robert McGibbon',
      author_email='rmcgibbo@gmail.com',
      license='GPLv3+',
      scripts=['watchcompiler'],
  )
