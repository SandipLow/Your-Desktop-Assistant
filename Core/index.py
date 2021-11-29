from modules import Analyze, Speak, Hear


class State:

    def __init__(self, mode):
        self.name = self.setName()
        self.mode = mode
        self.voice = self.setVoice()

    def changeMode(self):
        if self.mode == "offline":
            self.mode = "online"
        else:
            self.mode = "online"

    def setVoice(self):
        print(" MS Zira [1] \n MS David [2]")
        voice = input("Enter the voice number : ")
        return voice

    def changeVoice(voice):
        if voice == '2':
            voice = '1'
        elif voice == '1':
            voice = '2'
        return voice

    def setName(self):
        return input("Enter your name : ")


state = State("offline")
        

def say(audio):
    Speak.speak(state.voice, audio)


def listen():
    query = ""

    if state.mode == "offline":
        query = Hear.offline()
    else:
        query = Hear.online()

    return query

Analyze.main(state, say, listen)