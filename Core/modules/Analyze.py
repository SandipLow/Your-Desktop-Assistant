from modules import LocalFiles, Search, WebShortcuts
import datetime

def greet(state, say):
    hour = int(datetime.datetime.now().hour)
    if 4 <= hour < 12:
        say("Good morning " + state.name)

    elif 12 <= hour < 16:
        say("Good noon " + state.name)

    elif 16 <= hour < 18:
        say("Good afternoon " + state.name)

    elif 18 <= hour < 20:
        say("Good evening " + state.name)

    elif 20 <= hour < 24:
        say("I'm not disturbed " + state.name)

    say("I'm your Desktop assistant...")
    say("How may I help you...?")


def main(state, say, listen):
    greet(state, say)

    active = True
    while active:
        query = listen()
        print(query)
        if 'what' in query and 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strTime}")

        elif 'search' in query:
            query = query.replace("search", "")

            # Google Search
            if 'google' in query:
                say("Okay... Searching on google...")
                Search.GoogleSearch(query)

            # wikipedia search
            elif "wikipedia" in query:
                say("Searching wikipedia...")
                say("According to wikipedia" + Search.WikiSearch(query))

            # YouTube Search
            elif "youtube" in query:
                Search.YouTubeSearch(query)
                say("Okay... Searching on youtube...")

            else:
                print("unrecognised search engine")
                say("unrecognised search engine")

        elif 'tell me about' in query:
            query = query.replace("tell me about", "")

            if "wikipedia" in query:
                query = query.replace("wikipedia", "")

            say("Searching wikipedia...")
            say("According to wikipedia" + Search.WikiSearch(query))

        elif 'open' in query:
            WebShortcuts.Browse(query)

        elif 'play' in query:
            LocalFiles.PlayMusic(query)
            
        # F.A.Qs
        elif 'what' in query and 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strTime}")

        elif 'what' in query and 'day today' in query:
            d = datetime.datetime.today().weekday()
            day = "none"
            if d == 0:
                day = "monday"
            elif d == 1:
                day = "tuesday"
            elif d == 2:
                day = "wednesday"
            elif d == 3:
                day = "thursday"
            elif d == 4:
                day = "friday"
            elif d == 5:
                day = "saturday"
            elif d == 6:
                day = "sunday"
            say(f"today is {day}")

        elif 'date' in query and 'today' in query:
            current_time = datetime.datetime.now()
            say(f"Today date is {current_time.day} of Month {current_time.month} year {current_time.year}")

        elif 'introduce yourself' in query:
            say("I'm Iron assistant Made by Sandip Low.")
            say("How may I help you?")

        elif 'change' in query and 'voice' in query:
            voice = state.changeVoice(voice)
            say("Thanks for chosing my voice...")

        elif 'hear me' in query or "listen me" in query or 'you listening' in query:
            say("I am Listening whatever you say.")

        elif 'iron' and 'great' in query:
            say("I really flattered")

        elif 'thanks' in query or 'thank you' in query:
            say("It is my pleasure")

        elif 'who are you' in query:
            say("I am Iron. Your Iron Assistant. Made by Sandip Low")

        elif 'exit' in query:
            say("Okay... take care of yourself..")
            active = False

        elif 'start online mode' in query:
            say("Turning on Online mode. Make sure you are online")
            state.changeMode()