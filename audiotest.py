from vosk import Model, KaldiRecognizer
import pyaudio

model = Model("./Vosk/vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def talk():
    while True:
        data = stream.read(4096)
        if len(data)==0:
            print("LogError Traceback No  mic data input")
            return "MicError"
            break
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            print(f"' {text[14:-3]} '")
            return(f"' {text[14:-3]} '")
            break

