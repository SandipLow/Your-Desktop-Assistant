This is a python project that is able to Listen, Speak and do actions on the basis of your command

First install the dependencies by using executing the command in Terminal by using : 

    pip install Requirement.txt

Then you have to install vosk api from here --> https://alphacephei.com/vosk/models/vosk-model-en-in-0.4.zip.
Then extrct it in this directory.


For working offline :
    Uses vosk api. A bit unaccurate.

1. open the Terminal in this directory and execute the commands : 
        
        cd .\Core
        python index.py

2. Enter your name : ___
3. Enter 1 or 2 as per voice preference
4. Now it is ready to use....

For working online :
    Uses Speech_recognizer module. More accurate.

1. Start offline mode first.
2. Then say the command "start online mode"



Use the following commands for test :

    'what is the time now' --- know the time
    'what is the day/date today' --- know the day/date of that day
    'search ___ from google/wikipedia/youtube' -- search some thing from as you wish
    'tell me about ___' -- listen about something from wikipedia.
    'open youtube' -- open YT for you
    'play music' -- play 1st song in dir 'C:\Users\<USERPROFILE>/Music'
