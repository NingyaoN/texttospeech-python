import speech_recognition as sr
from time import ctime
import webbrowser
import time
from playsound import playsound
import os
import random
from gtts import gTTS
import subprocess

r = sr.Recognizer()

def record_audio(ask = False):

    with sr.Microphone() as source:
        if ask:
            texttospeech_speak(ask)
            #print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            #print(voice_data)
        except sr.UnknownValueError:
            #print("Sorry, I don't understand what you said.")
            texttospeech_speak("Sorry, I don't understand what you said.")
        except sr.RequestError:
            #print("Sorry, my speech service is down.")
            texttospeech_speak("Sorry, my speech service is down.")
        return voice_data

def texttospeech_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    #print(audio_string)
    os.remove(audio_file)
def open_folder():
    webbrowser.open("//home/ningshen//workspace")

def respond(voice_data):
    if 'what is your name' in voice_data:
        #print('My name is text to speech interpreter')
        texttospeech_speak('My name is text to speech interpreter')
    if 'what is the time' in voice_data:
        #print(ctime())
        texttospeech_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        #print('Here is what if found for ' + search)
        texttospeech_speak('Here is what i have found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        #print('Here is the location of  ' + location)
        texttospeech_speak('Here is the location that you ask for.')
    if 'open  workspace one' in voice_data:
        texttospeech_speak('opening workspace one')
        open_folder();
    if 'open current project' in voice_data:
        subprocess.call(["./test.sh"])
        texttospeech_speak("Directory changed, Opening project")
        
    if 'exit' in voice_data:
        texttospeech_speak('Stopping application')
        exit()

time.sleep(1)
texttospeech_speak("How can I help you?")
while 1:
    voice_data = record_audio()
    #print(voice_data)
    respond(voice_data)
