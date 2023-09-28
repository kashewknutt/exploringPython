import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    print(text)
    engine.say(text)
    engine.runAndWait()
