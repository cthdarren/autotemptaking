import random
import requests
from datetime import datetime

groupCode = ""
memberId = ""
pin = ""
date = datetime.now().strftime("%d/%m/%Y")
if int(datetime.now().strftime("%H")) < 12:
    meridies = "AM"
else:
    meridies = "PM"

if meridies == "AM":
    temperature = random.uniform(35.4, 36.7)
if meridies == "PM":
    temperature = random.uniform(35.9, 36.9)

temperature = round(temperature,1)

data = {
    "groupCode":groupCode,
    "date": date,
    "meridies": meridies,
    "memberId": memberId,
    "temperature": temperature,
    "pin": pin
}

try:
    result = requests.post("https://temptaking.ado.sg/group/MemberSubmitTemperature", data = data)
    file = open("tempLog.txt", "a")
    file.write(datetime.now().strftime("%d%m%y-%H%M") + "|" + str(temperature) + "|" + meridies + "\n")
except Exception as a:
    file.write(datetime.now().strftime("%d%m%y-%H%M") + "|" + str(a))

file.close()

if result.text == "OK":
    print("Success! Temperature recorded as: {}°C at {}, {} time".format(temperature, date, meridies) )