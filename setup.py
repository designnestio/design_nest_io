from setuptools import setup
from design_nest import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='design_nest',
      version=__version__,
      description='Python library which allows to read, modify, create and run EnergyPlus files and simulations.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/designnestio/design_nest_io',
      download_url=f'{__version__}',
      author='https://designnest.io',
      author_email='designnestio@gmail.com',
      license='Apache License 2.0',
      classifiers=(
            'Development Status :: 3 - Alpha',
            "Operating System :: OS Independent",
      ),
      packages=['design_nest'],
      keywords=['EnergyPlus', 'epJSON'])