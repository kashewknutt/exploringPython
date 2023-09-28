from tts import *
import datetime
def note():
    date = datetime.datetime.now()
    file_name = str(date) + ".txt"
    text = []
    speak("Start Entering---")
    while True:
        temp = input(":-")
        if temp in ['exit','close','done','finish']:
            break
        else:
            text.append(temp)
    with open(file_name, "w") as f:
        f.writelines(text)
