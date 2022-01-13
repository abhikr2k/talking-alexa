import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

import PyPDF2

listener = sr.Recognizer()
engine = pyttsx3.init()

engine.say('hi how can i help you abhishek ')


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
            if 'tom' in command:
                command = command.replace('tom', '')
                print(command)
    except:
        pass
    return command


def run_tom():
    command = take_command()

    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry,I only go with my jaan')
    elif 'are you single' in command:
        talk('I am in a relationship with abhishek')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'marry' in command:
        talk('i am married to my god abhishek who made me')
    elif 'send' in command:
        message = command.replace('send', '')
        talk('sending ' + message)
        pywhatkit.sendwhatmsg("+918130948158", message, 16, 10  )
    elif 'read' in command:
        book = open('data.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages

        speaker = pyttsx3.init()
        for num in range(7, pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()

    elif 'shutdown' in command:

        talk('closing the system')
        pywhatkit.shutdown(time=100)
    elif 'cancel' in command:
        talk('ok not closing the system abhishek baby')
        pywhatkit.cancelShutdown()


    else:
        talk('sorry did not understand please repeat it')


while True:
    run_tom()
