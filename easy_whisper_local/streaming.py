import whisper as wh
import numpy as np
import os
import sys
from typing import Literal, Generator
class EasyWhisperStreaming:
    """
    Still in development, this class will allow you to transcribe audio streams in real time.
    """
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
    def stream_to_text(self, stream: Generator[bytes], verbose: bool = False):
        """
        Pass a stream to the model and get the transcription text.\n
        Inputs:
            - stream: Generator to transcribe from, with its chunks in bytes format.
            - verbose (bool): Whether to display more information during inference or not (default False).
        """
        for chunk in stream:
            yield self.model.transcribe(np.frombuffer(chunk), verbose=verbose)["text"]