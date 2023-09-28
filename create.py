from tts import *

def addif():
    while True:
        tayp = input("Do you want it to be if, else or elif?")
        if tayp == "if":
            shart = input("Whats the condition sir?")
            code = ["if "+shart+":\n"]
            speak("Start the body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addifnest()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            return code
        elif tayp == "else":
            shart = input("Whats the condition sir?")
            code = ["if "+shart+":\n"]
            speak("Start the if body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addifnest()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            code.append("else:\n")
            speak("Start the else body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addifnest()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            return code
        elif tayp == "elif":
            shart = input("Whats the condition sir?")
            code = ["if "+shart+":\n"]
            speak("Start the if body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addifnest()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            body = []
            shart = input("What's the elif condition?")
            code.append("elif "+shart+":\n")
            speak("Start the elif body sir..")
            loop = True
            while loop == True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    loop = False
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addifnest()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
                code.extend(body)
                ch = input("One more sir?[yes/no]")
                if ch in ["no","nahi","n"]:
                    break
            code.append("else:\n")
            speak("Start the else body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addifnest()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            return code
        else:
            speak("I don't understand sir pls try again...")

def addifnest():
    while True:
        tayp = input("Do you want it to be if, else or elif?")
        if tayp == "if":
            shart = input("Whats the condition sir?")
            code = ["if "+shart+":\n"]
            speak("Start the body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addif()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            return code
        elif tayp == "else":
            shart = input("Whats the condition sir?")
            code = ["if "+shart+":\n"]
            speak("Start the if body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addif()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            code.append("else:\n")
            speak("Start the else body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addif()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            return code
        elif tayp == "elif":
            shart = input("Whats the condition sir?")
            code = ["if "+shart+":\n"]
            speak("Start the if body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addif()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            while True:
                body = []
                shart = input("What's the elif condition?")
                code.append("elif "+shart+":\n")
                speak("Start the elif body sir..")
                loop = True
                while loop == True:
                    temp = input("-->")
                    if temp in ['exit','close','done','finish']:
                        loop = False
                    elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                        templist = addif()
                        for lines in templist:
                            body.append("   "+lines)
                    elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                        templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                    else:
                        body.append("   "+temp+"\n")
                code.extend(body)
                ch = input("One more sir?[yes/no]")
                if ch in ["no","nahi","n"]:
                    break
                code.append("else:\n")
            speak("Start the else body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addif()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            return code
        else:
            speak("I don't understand this sir please try again...")

def addloop():
    while True:
        tayp = input("Do you want it to be a for or while?")
        if tayp in ["f","for"]:
            forvar = input("The variable sir:")
            limit = input("Range:")
            code = ["for "+forvar+" in "+limit+":\n"]
            speak("The body sir...")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addif()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloopnest()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            return code
        elif tayp in ["w","while"]:
            shart = input("The condition sir...")
            code = ["while "+shart+":\n"]
            speak("The body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addif()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloopnest()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            return code
        else:
            speak("Technical error sir please try again..")

def addloopnest():
    while True:
        tayp = input("Do you want it to be a for or while?")
        if tayp in ["f","for"]:
            forvar = input("The variable sir:")
            limit = input("Range:")
            code = ["for "+forvar+" in "+limit+":\n"]
            speak("The body sir...")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addif()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            return code
        elif tayp in ["w","while"]:
            shart = input("The condition sir...")
            code = ["while "+shart+":\n"]
            speak("The body sir..")
            body = []
            while True:
                temp = input("-->")
                if temp in ['exit','close','done','finish']:
                    break
                elif temp in ["add another if","add another elif","add another else","if","elif","else"]:
                    templist = addif()
                    for lines in templist:
                        body.append("   "+lines)
                elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
                    templine = addloop()
                    for lines in templine:
                        body.append("   "+lines)
                else:
                    body.append("   "+temp+"\n")
            code.extend(body)
            return code
        else:
            speak("Technical error sir please try again..")
        
speak("what should be the name sir?")
name = input(":->")
code = []
finalcode = []
while True:
    speak("Start coding..")
    temp = input("-->")
    if temp in ["add another if","add another elif","add another else","if","elif","else","add if","add elif","add else"]:
        templist = addif()
        finalcode.extend(templist)
    elif temp in ["add another loop","add another for","add another while","for","while","add while","add for"]:
        templine = addloop()
        finalcode.extend(templine)
    elif temp in ['exit','close','done','finish']:
        break
    else:
        finalcode.append(temp)
with open(name+".py","a+") as file:
    file.writelines(finalcode)
