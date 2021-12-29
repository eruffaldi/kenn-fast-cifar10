
# setup.py
from setuptools import setup,find_packages

setup(
    name='kenn-fast',
      version='1.0.0',
      description='KENN fast CIFAR10',
      author='Emanuele Ruffaldi',
      author_email='emanuele.ruffaldi@gmail.com',
      url='',
      package_dir = {'': 'src'},
      packages=['ekennfast'],
     # package_data={'mmi_buildmaker': ['templates/*']},
    scripts=[
    ],
    entry_points = {
        #'console_scripts': ['mmi_build_auto=mmi_buildmaker.autoupdate:main'],
    }
)