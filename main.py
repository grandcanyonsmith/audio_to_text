from transcribe_audio import extract_text_from_audio_file
from remove_background_noise import remove_background_noise_in_audio

# CONSTANTS
AUDIO_FILE_PATH = 'files/audio/Instructions.mp3'
WHISPER_MODEL_NAME = "tiny"

def main(audio_file_path: str, whisper_model_name: str) -> str:
    # clean data
    audio_with_background_noise_removed = remove_background_noise_in_audio(audio_file_path)

    # transcribe
    extracted_text = extract_text_from_audio_file(audio_with_background_noise_removed, whisper_model_name)
    return extracted_text

if __name__ == "__main__":
    print(main(AUDIO_FILE_PATH, WHISPER_MODEL_NAME))
