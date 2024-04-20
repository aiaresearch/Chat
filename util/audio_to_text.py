import whisper

model = whisper.load_model("base")

def audio_to_text(audio_file):
    result = model.transcribe(audio_file)
    print(result)