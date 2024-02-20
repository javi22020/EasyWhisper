from setuptools import setup, find_packages

setup(
    name='easy-whisper-local',
    version='1.0.3',
    packages=find_packages(),
    install_requires=[
        'openai-whisper'
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
