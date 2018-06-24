from setuptools import setup
from design_nest import __version__

setup(name='designNest',
      version=__version__,
      description='Python library which allows to read, modify, create and run EnergyPlus files and simulations.',
      url='',
      download_url=f'{__version__}',
      author='https://designnest.io',
      author_email='designnestio@gmail.com',
      license='Apache License 2.0',
      classifiers=['Development Status :: 3 - Alpha'],
      packages=['design_nest'],
      keywords=['EnergyPlus', 'epJSON'])