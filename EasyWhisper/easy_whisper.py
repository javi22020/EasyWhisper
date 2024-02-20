import whisper as wh
import os
import sys
from typing import Literal
class EasyWhisper:
    def __init__(self, model_name: Literal['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large'], download_root="models"):
        self.model_name = model_name
        try:
            from torch import cuda
            self.device = "cuda" if cuda.is_available() else "cpu"
            print(f"Torch installed, using {self.device.upper()} for inference.")
        except ImportError:
            self.device = "cpu"
            print("Torch not installed, using CPU for inference.")
        self.download_root = download_root
        if not os.path.exists(self.download_root):
            os.mkdir(self.download_root)
        if not os.path.exists(os.path.join(sys.path[0], self.download_root, self.model_name) + ".pt"):
            print(f"Downloading {self.model_name} model...")
        self.model = wh.load_model(self.model_name, device=self.device, download_root=self.download_root)
    def file_to_text(self, audio_path: str, verbose: bool = True):
        """
        Transcribes an spoken audio file to text.\n
        Inputs:
            - audio_path (str): Path to the file to transcribe.
            - verbose (bool): Whether to display more information during inference or not.\n
        Outputs:
            - str containing the complete text
        """
        return self.model.transcribe(audio_path, verbose=verbose)["text"]
    def file_to_timestamps(self, audio_path: str, verbose: bool = True):
        """
        Transcribes an spoken audio file to its timestamps.\n
        Inputs:
            - audio_path (str): Path to the file to transcribe.
            - verbose (bool): Whether to display more information during inference or not.\n
        Outputs:
            - list containing the timestamps
        """
        return self.model.transcribe(audio_path, verbose=verbose)["segments"]
    def file_to_dict(self, audio_path: str, verbose: bool = True):
        """
        Transcribes an spoken audio file to its complete dictionary.\n
        Inputs:
            - audio_path (str): Path to the file to transcribe.
            - verbose (bool): Whether to display more information during inference or not.\n
        Outputs:
            - dict containing the complete transcription, with the following keys:
                - 'text': Contains the complete text.
                - 'segments': Contains short phrases with its respective timestamps.
                - 'language': Contains the detected language.
        """
        return self.model.transcribe(audio_path)