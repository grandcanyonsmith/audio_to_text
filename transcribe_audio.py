import whisper

def extract_text_from_audio_file(audio_file_path, whisper_model_name):
    model = whisper.load_model(whisper_model_name)
    result = model.transcribe(audio_file_path)
    return result["text"]