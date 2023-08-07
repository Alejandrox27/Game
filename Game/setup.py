from setuptools import setup

setup(name = 'Game',version = '1.0.0',packages = ['game'], 
      entry_points = {'console_scripts': ['Game = game.__main__:main']})