import pyttsx3

engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty("voices")
print(voices)
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 200)
rate = engine.getProperty("rate")
print(rate)
text = "WHAAT A WONDERFUL EXAMPLE"
print(text)
engine.say(text)
engine.runAndWait()
