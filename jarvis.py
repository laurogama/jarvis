import speech_recognition
import pyttsx

DRIVER_NAME = 'espeak'  # sapi5 for windows, nsss for MacOSX and espeak for other platforms

speech_engine = pyttsx.init(DRIVER_NAME)  # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)


def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()


recognizer = speech_recognition.Recognizer()


def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_sphinx(audio)
    # or: return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""


speak("Say something!")
speak("I heard you say " + listen())
