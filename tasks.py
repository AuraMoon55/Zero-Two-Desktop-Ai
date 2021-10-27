import configparser

import random

import smtplib

import sys

import pyautogui

import psutil

import pyjokes

import requests, json

import os


import wikipedia


from work import open_url, search

speak

config = configparser.ConfigParser()  # if exists loads library.
config.read('config.ini')




def command_wikipedia(debug, query):

    speak("Searching wikipedia....")

    query = query.replace("wikipedia", "")

    results = wikipedia.summary(query, sentences=2)

    if debug == "True":

        print("wikipedia says" +  results)

    else:

        pass

    speak("wikipedia says" +  results)





def command_whatsup():

    st_msgs = [

        "Just doing my thing!",

        "I am fine!",

        "Nice!",

        "I am nice and full of energy",

    ]

    speak(random.choice(st_msgs))




def command_open(query, popular_websites, debug, search_engine, take_command):

    website = query.replace("open", "").strip().lower()

    try:

        open_url(popular_websites[website])

    except KeyError:
  # If the website is unknown

        if debug == "True":

            print(f"Unknown website: {website}")

        else:

            pass

        speak(f"Sorry, i don't know the website {website}")

        speak(f"¿Do you want me to search {website} in the web?")

        if take_command() == "yes":

            search(website, search_engine)

        else:

            pass


def open_nhen():

   try:

       nhcode = ("183270" "172228" "190509" "180663" "203497" "237556" "117327" "147676" "166412" "173911" "218917" "195287" "316277" "306950" "323026" "297346" "276023" "304002" "319893" "316198" "322874" "316242" "318326" "306672" "310481" "314259" "312354" "300508" "288873" "189632" "289276" "178283" "256038" "185333" "191532" "186151" "240912" "239436" "193941" "319115" "306954" "283001" "310502" "321881" "303578" "276478" "267858" "270370" "278513" "270251" "267979" "265175" "215660" "260606" "308637" "254496" "193876" "193984" "76119" "192874" "107180" "110900" "135193" "161488" "65433" "182327" "78651" "190230" "191880" "180600" "105465" "173023" "191049" "191851" "167112" "177754" "187016" "165961" "165962" "97879" "74500" "133435" "152075" "174888" "93354" "74076" "122948" "104346" "91773" "78226" "76482" "68508" "61224" "60473" "58469" "56295" "53905" "42383" "187611" "19084" "158050" "83269" "146042" "178941" "100401" "181556" "152456" "167936" "139048" "185592" "191427" "175015" "142825" "182290" "192845" "192849" "183099" "192143" "142825" "153856" "158404" "136026" "188918" "193876" "193984" "76119" "192874" "107180" "110900" "135193")

       nhencode = random.choice(nhcode)

       nurl = f"https://nhentai.to/g/{nhencode}"
 
       print("Opening a random nhentai code")
 
       open_url(nurl)




def command_search(query, search_engine):

    search_query = query.split("for")[-1]

    search(search_query, search_engine)





def command_mail(take_command):

    speak("Who is the recipient? ")

    recipient = take_command()


    try:

        speak("What should I say? ")

        content = take_command()


        email = config['EMAIL']

        server = smtplib.SMTP(email['server'], email['port'])

        server.ehlo()

        server.starttls()

        server.login(email['username'], email['password'])

        server.sendmail(email['username'], recipient, content)

        server.close()

        speak("Email sent!")

    except
 Exception:

        speak("Sorry Sir!")

        speak("I am unable to send your message at this moment!")




def command_nothing():

    speak("okay")

    speak("Bye Sir, have a good day.")

    sys.exit()




def command_hello():

    speak("Hello Sir")




def command_bye():

    speak("Bye Sir, have a good day.")

    sys.exit()



def command_henhaven():

    open_url(hentaihaven)



def command_play_music():

    try:

        music_folder = config['DEFAULT']['musicPath']

        music_ext = ["mp3", "wav", "ogg"]

            playables = [songs for songs in os.listdir(music_folder)
 if songs.split(".")[-1] in music_ext]

            os.startfile(os.path.join(music_folder, random.choice(playables)))


    except Exception as e:

        speak(e)



    
def command_ncode():

    try:

        code = ("183270" "172228" "190509" "180663" "203497" "237556" "117327" "147676" "166412" "173911" "218917" "195287" "316277" "306950" "323026" "297346" "276023" "304002" "319893" "316198" "322874" "316242" "318326" "306672" "310481" "314259" "312354" "300508" "288873" "189632" "289276" "178283" "256038" "185333" "191532" "186151" "240912" "239436" "193941" "319115" "306954" "283001" "310502" "321881" "303578" "276478" "267858" "270370" "278513" "270251" "267979" "265175" "215660" "260606" "308637" "254496" "193876" "193984" "76119" "192874" "107180" "110900" "135193" "161488" "65433" "182327" "78651" "190230" "191880" "180600" "105465" "173023" "191049" "191851" "167112" "177754" "187016" "165961" "165962" "97879" "74500" "133435" "152075" "174888" "93354" "74076" "122948" "104346" "91773" "78226" "76482" "68508" "61224" "60473" "58469" "56295" "53905" "42383" "187611" "19084" "158050" "83269" "146042" "178941" "100401" "181556" "152456" "167936" "139048" "185592" "191427" "175015" "142825" "182290" "192845" "192849" "183099" "192143" "142825" "153856" "158404" "136026" "188918" "193876" "193984" "76119" "192874" "107180" "110900" "135193")

        hencode = random.choice(code)

        speak("giving you a random sauce")

        print(hencode)

     except
 Exception as e:

        speak(e)

        


def screenshot():

    img = pyautogui.screenshot()

    img.save(

        "C:\\Users\\abc\\screenshots\\ss.png"

    )

 except
 Exception as e:

    speak(e)

    


def cpu():

    usage = str(psutil.cpu_percent())

    speak('CPU usage is at ' + usage)

    print('CPU usage is at ' + usage)

    battery = psutil.sensors_battery()

    speak("Battery is at")

    speak(battery.percent)

    print("battery is at:" + str(battery.percent))

except
 Exceptiom as e:

    speak(e)

    
 

def jokes():

    j = pyjokes.get_joke()

    print(j)

    speak(j)

  


def cmd_weather():

    api_key = config['DEFAULT']['WEATAPI']

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    speak("tell me which city")

    city_name = takeCommand()

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidiy = y["humidity"]

        z = x["weather"]
        weather_description = z[0]["description"]

        r = ("in " + city_name + " Temperature is " +

             str(int(current_temperature - 273.15)) + " degree celsius " +

             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +

             ", humidity is " + str(current_humidiy) + " percent"

             " and " + str(weather_description))

        print(r)

        speak(r)

    else:

        speak(" City Not Found ")


 
def cmd_logout():

    os.system("shutdown -1")

    
def cmd_restart():

    os.system("shutdown /r /t 1")

   


def cmd_remind():

     speak("What is the reminder?")

     data = takeCommand()

     speak("You said to remember that" + data)

     reminder_file = open("data.txt", 'a')

     reminder_file.write('\n')

     reminder_file.write(data)

     reminder_file.close()

           

 
def cmd_re_remind():

     reminder_file = open("data.txt", 'r')

     speak("You said me to remember that: " + reminder_file.read())
    


def cmd_vlc():

    speak("opening V L C media player")

    path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" #Enter the correct Path according to your system

    os.startfile(path)
