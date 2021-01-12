import datetime
import subprocess
import pyjokes
import pyttsx3
# import pywhatkit
import speech_recognition as sr
import wikipedia
import os
import requests
from bs4 import BeautifulSoup
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey' in command:
                command = command.replace('hey', '')
                print(command)
    except:
        pass
    return command


def play_audio(song_name):
    song_name = song_name.replace(' ', '%20')
    url = 'https://gaana.com/search/{}'.format(song_name)
    source_code = requests.get(url)
    plain_text = source_code.content
    soup = BeautifulSoup(plain_text, "html.parser")
    links = soup.findAll('a', {'class': 'rt_arw'})
    webbrowser.open(links[0]['href'])


def run_alexa():
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    # elif 'play' in command:
    #     song = command.replace('play', '')
    #     talk('playing ' + song)
    #     pywhatkit.playonyt(song)
    elif 'tell about' in command:
        person = command.replace('tell about', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%B %d, %Y')
        print('Today is: ' + date)
        talk('Today is: ' + date)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open notepad' in command:
        print('Opening notepad...')
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
    elif 'open firefox' in command:
        print('Opening firefox...')
        subprocess.Popen('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    elif 'audio' in command:
        song = command.replace('audio', '')
        play_audio(song)
    elif 'exit' in command:
        quit(-1)
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
