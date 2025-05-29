import speech_recognition as sr
import webbrowser
import pyttsx3
import appsandmusic
import pywhatkit
import wolframalpha
from dotenv import load_dotenv
import os

#initializing text to speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[117].id)

#setting wolfram for question and answers
load_dotenv()
app_id = os.getenv("WOLFRAM_APP_ID")
client = wolframalpha.Client(app_id)


def ask_wolfram(query):
    res = client.query(query)
    return next(res.results).text


#recognize your voice through speech recognition
def speechrecognizer():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    word = recognizer.recognize_google(audio)
    return word


#enables to speak out the text
def speak(text):
    engine.say(text)
    engine.runAndWait()


def processcommand(c):
    print(c)

    if c.lower() == "menu":
        print("Open Applications or Web browser: Say open and name of website or application")
        print("To play music: Say play and music name")
        print("To search anything: Say Search and whatever you want to search")
        print("Ask any Question by starting with question word ")
        print("Say Exit to exit")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")
        song.remove(song[0])  # remove the word 'play'
        full_length_song = " ".join(song)
        if full_length_song in appsandmusic.music:
            link = appsandmusic.music[full_length_song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        elif c.lower().startswith("play"):
            song = c.lower().replace("play", "").strip()
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)
        else:
            speak("Sorry, I couldn't find the song.")

    elif c.lower().startswith("open"):
        appsandmusic.application(c.lower())

    elif c.lower().startswith("search "):
        search_list = c.lower().split(" ")
        search_list.remove(search_list[0])
        search = " ".join(search_list)
        webbrowser.open("https://www.google.com/search?q=" + search.replace(" ", "+"))

    elif c.lower().startswith(("who", "what", "when", "where", "how")):
        answer = ask_wolfram(c)
        speak(answer)
    elif c.lower().startswith("exit"):
        exit()
    else:
        speak("Sorry, I couldn't get a good response.")


if __name__ == '__main__':
    while True:
        try:
            # recognize speech
            print("SAY TIKU TO ACTIVATE")
            if speechrecognizer().lower() == "tiku":
                speak("Yes")
                print("Listening...")
                #recognize speech
                command = speechrecognizer()
                processcommand(command)
            elif speechrecognizer().lower() == "exit" or speechrecognizer().lower() == "stop":
                exit()
        except sr.UnknownValueError:
            print("Sorry, could not understand audio")
        except Exception as e:
            print("Error ", e)
        except KeyboardInterrupt:
            exit()
