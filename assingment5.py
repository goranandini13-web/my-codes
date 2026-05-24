#question1----
import requests
city =input("enyer city name:")
api_key="e1ebcab7b2e5ee3940a1f8ca6ea69b76"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e1ebcab7b2e5ee3940a1f8ca6ea69b76&units=metric"
response=requests.get(url)
data=response.json()

print("city:",data["name"])
print("temperature:",data["main"]["temp"],"celceis")
print("humidity:",data["main"]["humidity"],"%")
print("pressure:",data["main"]["pressure"],"hpa")
print("weather:",data["weather"][0]["description"])
print("wind speed:",data["wind"]["speed"],"m/s")


#question2---
import random
choices =["rock","paper","scissor"]
user=input("enter rock,paper or scissor:").lower()
computer = random.choice(choices)
print("computer chose:",computer)
if user==computer:
    print("its a tie!")

elif((user=="rock"and computer=="scissor")or
     (user=="paper"and computer=="rock")or
     (user=="scissor"and computer=="paper")
):
 print("you win")
elif user in choices:
   print("computer wins!")
else :
   print("invalid choice")


   #question3----
   #random joke api---
   import requests
   url="https://official-joke-api.appspot.com/random_joke"

   response=requests.get(url)
   data=response.json()
   print("setup:",data["setup"])
   print("punchline:",data["punchline"])