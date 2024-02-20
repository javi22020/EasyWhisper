from setuptools import setup, find_packages

setup(
    name='easy-whisper-local',
    version='1.2.0',
    packages=find_packages(),
    install_requires=[
        'openai-whisper',
        'numpy'
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
