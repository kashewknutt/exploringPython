#Importing class required
import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import datetime
import audiotest

#Defining variables....	
goodBye = ["Catch you later sir...", "Good bye sir...", "Till next time sir...:)", "Exiting.............", "Bye sir."]
r = sr.Recognizer()
m = sr.Microphone()
with m as source: r.adjust_for_ambient_noise(source)

############Defining functions
#Defining voice acceptor
def getAudio():
	print("Say")
	with m as source:
		audio = r.listen(source)
		print("caught")
		said = ""
		try: #inspired from techwithtim.net
			print("Wait")
			said = r.recognize_google(audio)
			print("{}".format(said))
		except sr.UnknownValueError:
			print("LOG Errorororo:::   Unknown Value")
		except sr.RequestError as e:
			print("Exception: " + str(e))
	return "{}".format(said).lower()

def getAudio4verify():
	print("Say")
	with m as source:
		audio = r.listen2callword(source)
		print("caught")
		said = ""
		try: #inspired from techwithtim.net
			print("Wait")
			said = r.recognize_google(audio)
			print("{}".format(said))
		except sr.WaitTimeoutError:
			print("Timeout going again")
		except sr.UnknownValueError:
			print("LOG Errorororo:::   Unknown Value")
		except sr.RequestError as e:
			print("Exception: " + str(e))
	return "{}".format(said).lower()

#Defining Talk Function
def speak(statement):
	pathway = pyttsx3.init()
	pathway.say(statement)
	print(statement)
	pathway.runAndWait()

#Define Noting down
def note(text):
	date = datetime.datetime.now()
	file_name = str(date).replace(":", "-") + "-note.txt"
	with open(file_name, "w") as f:
		f.write(text)
	textEditor  = "Documents/Apps/sublime_text_3/sublime_text"
	subprocess.Popen([textEditor, file_name])

#Defining called functions
def quotient(num1,num2):
	speak("Their complete division is", num1 / num2)
	speak("But, their quotient is ", num1 // num2, " while their remainder is ", num1 % num2)
def wlcm():
	speak("Hello Sir...")
	speak("How are you?")
	verify = getAudio4verify()
	if verify == "just like you":
		speak("Why thank you sir.\nNice to know that.")
		speak("Shall we begin?")
		loop = True
		while loop == True:
			command = getAudio()
			bitOrder = command.split(" and ")
			for co in range(0,len(bitOrder)):
				temporary = bitOrder[co]
				order = temporary.split(" ")
				if "note" in order or "Note" in order:
					speak("What do you want me to note down sir?")
					toBeNoted = getAudio()
					note(toBeNoted)	
				elif "thnx" in order or "thanks" in order or "thank" in order:
					speak("Why thanks sir.....?")
				elif "search" in order:
					if "Search" in order:
						order.remove("Search")
						search_term = " ".join(order)
					if "search" in order:
						order.remove("search")
						search_term = " ".join(order)
					url = "https://www.google.com.tr/search?q={}".format(search_term)
					webbrowser.open(url)
				elif "sum" in order or "add" in order:
					total = 0
					if len(order) == 1:
						speak("There aren't any numbers to add....\nAre you toying with me sir?")
					elif len(order) == 2:
						speak("Isn't the sum of a single number the number itself?")
					elif len(order) >= 3:
						for added in range(0,len(order)):
							currentNO = order[added]
							if currentNO.isdigit() == True:
								total += int(currentNO)
							else:
								continue
						temp = "There sum is"+str(total)
						speak(temp)
				elif "product" in order or "multiply" in order:
					total = 1 
					if len(order) == 1:
						speak("There aren't any numbers to multiply....Are you toying with me sir?")
					elif len(order) == 2:
						speak("Isn't the product of a single number the number itself?")
					elif len(order) >= 3:
						for multiplied in range(0,len(order)):
							currentNO = order[multiplied]
							if currentNO.isdigit() == True:
								total *= int(currentNO)
							else:
								continue
						temp = "Their product is "+str(total)
						speak(temp)
				elif "subtract" in order or "minus" in order:
					total = 0
					if len(order) == 1:
						speak("There aren't any numbers to sutract....Are you toying with me sir?")
					elif len(order) == 2:
						speak("Isn't the difference of a single number the number itself?")
					elif len(order) >= 3:
						for minused in range(0,len(order)):
							currentNO = order[minused]
							if currentNO.isdigit() == True:
								total -= int(currentNO)
							else:
								continue
						temp = "There difference is "+str(total)
						speak(temp)
				elif "divide" in order:
					if len(order) <= 2:
						speak("Numbers are not enough...Are you toying with me sir?")
					elif len(order) == 3:
						if order[0].isdigit() == True:
							ek = int(order[0])
						if order[1].isdigit() == True and order[0].isdigit == True:
							be = int(order[1])
						if order[0].isdigit == True and order[1].isdigit == False:
							be = int(order[2])
						if order[1].isdigit == True and order[0].isdigit == False and order[2].isdigit == True:
							ek = int(order[1])
							be = int(order[2])
						quotient(ek,be)
					else:
						speak("Confusing usage of quotient.....")

				elif "bye" in order or "exit" in order:
					speak(goodBye)
					loop = False
				else:
					speak("I do not understand sir please try again")
					speak("Do you want me search it?(yes or no):")
					query = getAudio()
					if query in ["yes", "yaa", "yeah"]:
						search_term = " ".join(order)
						url = "https://www.google.com.tr/search?q={}".format(search_term)
						webbrowser.open(url)
					elif query in ["no", "naa", "nah"]:
						speak("Alright sir...")
					else:
						speak("Not understandable....")
	else:
		speak("Just as I thought.....")
wakeUp = "shivraj"
print("Start")
while True:
        text = getAudio4verify()
	#text = audiotest.talk()
        if text.count(wakeUp) > 0:
                wlcm()
