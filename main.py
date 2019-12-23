import speech_recognition as sr
from time import ctime
import webbrowser
import time

r = sr.Recognizer()

def record_audio(ask = False):

    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            #print(voice_data)
        except sr.UnknownValueError:
            print("Sorry, I don't understand what you said.")

        except sr.RequestError:
            print("Sorry, my speech service is down.")

        return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is text to speech interpreter')

    if 'what is the time' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what if found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location of  ' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
print("How can I help you?")
while 1:
    voice_data = record_audio()
    #print(voice_data)
    respond(voice_data)
