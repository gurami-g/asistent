import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

en = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

ru = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"

Listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 120)

voices = engine.getProperty('voices')
engine.setProperty('voice',en )
engine.setProperty('voice',ru)
def talk(text):
    engine.say(text)
    engine.runAndWait()
#
def take_commamd():
    try:
        with sr.Microphone() as source:
            print('listening... ')
            voice = Listener.listen(source)
            command = Listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:   
                command = command.replace('alexa', '')     
                
    except:
        pass
    return command

def run_alexa():
    command = take_commamd()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)

    elif 'who is' in command:
        person = command.replace('who is', '0')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I habe an headache')

    elif 'are you single' in command:
        talk('I am in relationship with wifi')
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'hay' or 'Привет' in command:
        talk('hay' or 'Привет')
    
    

    else:
        talk('please say the command again.')



while True:
    run_alexa()
