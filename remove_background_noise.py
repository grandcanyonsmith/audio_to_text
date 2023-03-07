import requests
import io
import pathlib
import base64
from pydub import AudioSegment

API_URL = "https://api-inference.huggingface.co/models/JorisCos/ConvTasNet_Libri2Mix_sepclean_16k"
HEADERS = {"Authorization": "Bearer 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"}
OUTPUT_DIR = "files/audio/cleaned_audio/"

def query(filename: str) -> dict:
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=HEADERS, data=data)
    return response.json()

def remove_background_noise_in_audio(audio_file_path: str) -> None:
    output = query(audio_file_path)

    # extract the label, content-type, and blob for each item in output
    items = [(item['label'], item['content-type'], item['blob']) for item in output]
    
    # decode the base64 encoded content and create an audio segment from a file-like object
    audio_segments = [AudioSegment.from_file(io.BytesIO(base64.b64decode(content))) for _, _, content in items]
    
    # save the audio segments as MP3 files with the corresponding labels as filenames
    output_file_paths = [pathlib.Path(OUTPUT_DIR) / f"{label}.mp3" for label, _, _ in items]
    for output_file_path, audio_segment in zip(output_file_paths, audio_segments):
        with open(output_file_path, "wb") as f:
            audio_segment.export(f, format="mp3")

if __name__ == "__main__":
    audio_file_path = "test.mp3"
    remove_background_noise_in_audio(audio_file_path)
