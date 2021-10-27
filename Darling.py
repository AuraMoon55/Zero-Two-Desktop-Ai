import configparser  

import os 


import gui 

import SpeechRecognition as sr  

from work import (
 
 change_rate,

  change_voice,

  change_volume,

  search_engine_selector,

  set_gui_speak,

  speak,

  wish_me
)

from tasks import(
 
 command_bye,

  command_hello,

  command_mail,

  command_nothing,

  command_open,

  command_play_music,

  command_search,

  command_whatsup,

  command_wikipedia,

  command_ncode,

  command_henhaven,

  cpu,

  screenshot,

  cmd_weather,

  cmd_remind,

  cmd_re_remind,

  jokes,
  cmd_logout,
  cmd_restart,
  cmd_vlc,
  open_nhen
)

from Arq.modules import(
   ly_find,
   py_inf,
   torr_find,
   wp,
   yt_vid,
   song_dl
)


useful_web = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
    "github": "https://www.github.com",
}

hentaihaven = {"https://www.hentaihaven.xxx"}

def main(search_engine, take_command, debug):
    def execute_the_command_said_by_user():
        query = take_command()

       
        phrases = {
            "what's up": command_whatsup,
            "nothing": command_nothing,
            "abort": command_nothing,
            "stop": command_nothing,
            "hello": command_hello,
            "bye": command_bye,
            "play music": command_play_music,
        }
        for phrase, command in phrases.items():
            if phrase in query:
                command()

        # logic for executing commands with arguments
        if "wikipedia" in query:
            command_wikipedia(speak, debug, query)

        elif "open" in query:
            command_open(
                query,
                Useful_web,
                debug,
                search_engine,
                take_command
            )

        elif "search" in query:
            command_search(query, search_engine)

        elif "mail" in query:
            command_mail(take_command)
            
        elif "nhentai code" in query:
            command_ncode()  
            
        elif "hentai" in query:
            command_henhaven(take_command)    

        elif "change rate" in query:
            change_rate(query, take_command)

        elif "change voice" in query.lower():
            change_voice(query, take_command)

        elif "change volume" in query.lower():
            change_volume(query, take_command)
        
        elif "logout" in query:
          cmd_logout()
        
        elif "restart" in query:
          cmd_restart()
        
        elif "joke" in query:
          jokes()
          
        elif "cpu" in query:
          cpu()
          
        elif "usage" in query:
          cpu()
          
        elif "battery" in query:
          cpu()
          
        elif "weather" in query:
          cmd_weather(query, take_command)
          
        elif "screenshot" in query:
          screenshot()
          
        elif "v l c" in query:
          cmd_vlc()
          
        elif "go to nhentai" in query:
         open_nhen()

        elif "torrent" in query:
          torr_find(query)
          
        elif "yt" in query:
          yt_vid(query)
          
        elif "wallpaper" in query:
         wp(query)

        elif "song" in query:
          song_dl(query)

        elif "python" in query:
         py_inf(query)

        elif "lyrics" in query:
         ly_find(query)


        speak("Next Command! Sir!")
    gui.set_speak_command(execute_the_command_said_by_user)
    set_gui_speak(gui.speak)
    gui.mainloop()


def run():
    master = config['DEFAULT']['master']

    search_engine = search_engine_selector(config)

    debug = config['DEFAULT']['debug']

    if debug == "True":
        def take_command():
            return input("Command |--> ")
    else:
        def take_command():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold = 0.5
                audio = r.listen(source)

            query = " "
            try:
                print("Recognizing....")
                query = r.recognize_google(audio, language="en-in")
                print("user said: " + query)

            except sr.UnknownValueError:
                if debug == "True":
                    print("Sorry Could You please try again")
                else:
                    pass
                speak("Sorry Could You please try again")

            except Exception as e:
                if debug == "True":
                    print(e)
                    print("Say That Again Please")
                else:
                    pass

            return query

    speak(text="Initializing Zero Two....")
    wish_me(master)
    main(search_engine, take_command, debug)


if os.path.isfile('./config.ini'): 
    config = configparser.ConfigParser()  
    config.read('config.ini')  # and also the file.
    run()  # Then it launches the main program
else:
    print('You need a config.ini file')
