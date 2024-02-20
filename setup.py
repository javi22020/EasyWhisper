from setuptools import setup, find_packages

setup(
    name='easy-whisper',
    version='1.0',
    packages=find_packages(),
    requires=open('requirements.txt').readlines(),
)
