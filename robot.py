import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from playsound import playsound
import sys

listner = sr.Recognizer()
# listner.dynamic_energy_threshold = False
engine = pyttsx3.init()
voices =  engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# global command

def talk(text):
    engine.say(text)
    engine.runAndWait()

def exit():
    sys.exit()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listner.listen(source , phrase_time_limit=3)
            command = listner.recognize_google(voice)

            command = command.lower()

            if 'rosa' in command:

                command = command.replace('rosa','')

                print(command)

    except Exception as e:
        print(e)
    return(command)

def laugh():
    playsound('C:\python\opencv\hahaha.mp3')

def run_ai():
    command = take_command()
    print(command)
    if 'play' in command:

        song = command.replace('play','')

        talk("playing " + song)     
        # print(song)     
        pywhatkit.playonyt(song)

    elif 'search' in command:
        result = command.replace('search','')
        talk('searching ' + result)    
        pywhatkit.search(result)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I :%M %p')
        print(time)
        talk("Time is " + time)

    elif 'tell me about' in command:
        person = command.replace('tell me about','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif 'who made you' in command:
        talk('Mr Mohamed Alalamey')    
        print('Mr Mohamed Alalamey')    

    elif 'boyfriend' in command:
        print('Yes i have')
        talk('Yes i have')
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        # print(laugh())
        laugh()

    elif 'thanks' in command:
        talk('You are welcomed')    
        print('You are welcomed')   


    elif 'bye' in command:
        talk('Bye')    
        exit() 

    else:
        talk('Please say the command again.')
        
# that mean reboot will run every time 
while True: 
    run_ai()