import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pywhatkit
import pyautogui
import webbrowser
import wikipedia

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 = pt-br / 1 = en-us
engine.setProperty('rate',250)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if 3 <= hour < 12:
        talk('Good morning boss! How can I help you today?')
    elif 12 <= hour < 18:
        talk('Good afternoon boss! How can I help you today?')
    else:
        talk('Good evening boss! How can I help you today?')


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            print(command)
            return(command)
    except:
        return ""

def run_lumina():
    command = take_command()
    if 'hello' in command or 'hey' in command or 'hi' in command:
        talk('Hey boss, how are you?')
    
    elif 'stop' in command or 'finish' in command:
        talk('Ok boss, ending our section')
        exit()
    
    elif 'joke' in command:
        talk('Ok boss, here is a joke for you')
        talk(pyjokes.get_joke())
    
    elif 'play' in command:
        song = command.replace('play', "")
        talk('Ok boss, playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'pause' in command or 'start' in command:
        pyautogui.press('k')

    elif 'full screen' in command:
        pyautogui.press('f')

    elif 'subtitle' in command:
        pyautogui.press('c')

    elif 'theater' in command:
        pyautogui.press('t')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('its' + time)
    
    elif 'open' in command:
        command = command.replace('open', "").strip()
        talk('opening ' + command)
        webbrowser.open_new("https://www." + command + ".com")

    elif 'search' in command:
        usercm = command.replace('search', "").strip()
        usercm = usercm.lower()
        webbrowser.open(usercm)
        talk('Here is what I found')

    elif 'close' in command:
        talk('Ok boss, closing')
        pyautogui.hotkey('alt', 'f4')

    elif 'who is' in command:
        person = command.replace('who is', "")
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'remember that' in command:
        rememberMessage = command.replace('remember that', "")
        talk('You told me to remember that' + rememberMessage)
        remember = open('remember.txt', 'a')
        remember.write(rememberMessage)
        remember.close

    elif 'what do you remember' in command:
        remember = open('remember.txt', 'r')
        talk('You told me to remember that' + remember.read())

    elif 'clear remember file' in command:
        file = open('remember.txt', 'w')
        file.write(f"")
        talk('Finished boss, everithing I remember has been deleted!')

    else:
        talk('Sorry, I didnt understand ')

greeting()

while True:
    run_lumina()
