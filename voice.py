from logging import FATAL
import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
from gtts import gTTS

machine = pyttsx3.init()
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[1].id)

def speak(text):
    # tts= gTTS(text=text, lang='en')
    # file =person+'.mp3'
    # tts.save(file)
    machine.say(text)
    machine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('Speak Now')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            said = ''
            said = r.recognize_google(audio)
            said = said.lower()
            # print(said)
    except:
        pass
    return said

# def get_typing():
#     try:
#         typeIn = input('Type here: ')
#         typeIn = typeIn.replace('Type here: ')
#     except:
#         pass
#     return typeIn

def run_voice():
    voice = get_audio()
    print (voice)
    if "hello" in voice:
        speak("Hi, How are you?")
    elif "time" in voice:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak ('Time is '+ time)
    elif "date" in voice:
        date = datetime.datetime.now().strftime('%A %d %B %Y')
        speak ('Today '+ date)
    elif "about" in voice:
        try:
            person = voice.replace('about', '')
            info = wikipedia.summary(person, 1)
            speak(info)
            print(info)
        except Exception as e:
            print(e)
    elif "stop" in voice:
        exit(0)
        
    else:
        speak('Please ask me any question.')

while True:
    run_voice()