from setuptools import setup, find_packages

setup(
    name='easy-whisper-local',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'openai-whisper'
    ]
)
