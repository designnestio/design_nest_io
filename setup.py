from setuptools import setup
from design_nest import __version__

setup(name='designnest',
      version=__version__,
      description='Python library to generate building analysis models.',
      url='',
      download_url='{}'.format(__version__),
      author='https://designnest.io',
      author_email='designnestio@gmail.com',
      license='Apache License 2.0',
      classifiers=['Development Status :: 3 - Alpha'],
      packages=['design_nest'],
      keywords=['EnergyPlus', 'epJSON', 'Load Calculation'])