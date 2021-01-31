import random, os, requests, sys
from datetime import datetime
try:
    import uservars
except ImportError:
    if not os.path.exists("uservars.py"):
        uservarFile = open("uservars.py", "a")
        uservarFile.writelines([
            'groupCode = ""\n',
            'memberId = ""\n',
            'pin = ""\n'
        ])
    sys.exit("uservars file has been generated, please fill in the relevant details in the file")

def getDate():
    return datetime.now().strftime("%d/%m/%Y")

def getMeridies():
    if int(datetime.now().strftime("%H")) < 12:
        return "AM"
    else:
        return "PM"

def generateTemp():
    if getMeridies() == "AM":
        temperature = random.uniform(35.4, 36.7)
    if getMeridies() == "PM":
        temperature = random.uniform(35.9, 36.9)

    return round(temperature,1)

def sendReq():
    temperature = generateTemp()
    date = getDate()
    meridies =  getMeridies()

    data = {
        "groupCode":uservars.groupCode,
        "date": date,
        "meridies": meridies,
        "memberId": uservars.memberId,
        "temperature": temperature,
        "pin": uservars.pin
    }
    try:
        result = requests.post("https://temptaking.ado.sg/group/MemberSubmitTemperature", data = data)
        file = open("tempLog.txt", "a")
        file.write(datetime.now().strftime("%d%m%y-%H%M") + "|" + str(temperature) + "|" + meridies + "\n")
        if result.text == "OK":
            print("Success! Temperature recorded as: {}°C at {}, {} time".format(temperature, date, meridies) )
            
    except Exception as a:
        file.write(datetime.now().strftime("%d%m%y-%H%M") + "|" + str(a) + "\n")
        
    file.close()

def checkVariables():
    if uservars.groupCode == "" or uservars.memberId == "" or uservars.pin == "":
        print("Please fill in all the fields in uservars.py before continuing")
        return False

    return True
    
if checkVariables():
    sendReq()