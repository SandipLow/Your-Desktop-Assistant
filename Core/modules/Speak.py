import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def speak(voice, audio):
    print(audio)

    if voice == '2':
        engine.setProperty('voice', voices[0].id)

    elif voice == '1':
        engine.setProperty('voice', voices[1].id)

    engine.say(audio)
    engine.runAndWait()

