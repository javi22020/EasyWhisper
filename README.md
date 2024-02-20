# EasyWhisper

EasyWhisper is a simple Python package that allows you to convert speech to text using OpenAI's model Whisper locally.  
It is a wrapper around the openai-whisper package.  

## Installation
Use 
```bash
pip install easy-whisper-local
```
This is enough to install the package and its dependencies.  
Besides, you can also install torch with CUDA support to speed up the process using your GPU.  
The model will be downloaded automatically when you run the package for the first time, and it will be saved in the subdirectory `models/`.
## Usage
```python
ew = EasyWhisper()
text = ew.file_to_text('audio.mp3')
times = ew.file_to_timestamps('audio.mp3')
dictionary = ew.file_to_dictionary('audio.mp3')
print(text)
```
