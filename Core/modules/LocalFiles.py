import os
import webbrowser


music_dir = 'C:\\Users\\ASUS\\Music'

songs = os.listdir(music_dir)

def PlayMusic(query) :

    i = 0

    if 'play mon bebagi' in query:
        os.startfile(os.path.join(music_dir, 'Ley-Chakka-Kunal-Ganjawala_Prasenjit-Mukherjee.mp3'))

    elif 'play char chakka' in query or 'play four six' in query:
        os.startfile(os.path.join(music_dir, 'Char Chokka Hoi Hoi (ICC WT20 Cricket Theme Song).mp3'))

    elif 'play i am a rider' in query or 'play i\'m a rider' in query:
        os.startfile(os.path.join(music_dir, 'I Am a Rider_192(PaglaSongs).mp3'))

    elif 'play kuch to bata zindagi' in query or 'play life tell something' in query:
        os.startfile(os.path.join(music_dir, 'Zindagi Kuch Toh Bata.mp3'))

    elif 'play zindagi ek safar' in query or 'play life is a journey' in query:
        os.startfile(os.path.join(music_dir, 'Zindagi Ek Safar Hai Suhana - Kishore Kumar (DJJOhAL.Com).mp3'))

    elif 'play cat vibing' in query:
        webbrowser.open("https://www.youtube.com/watch?v=NUYvbT6vTPs")

    elif 'play g t a' in query : 
        os.startfile(os.path.join(music_dir, 'Grand-Theft-Auto-San-Andreas-Theme-Song.mp3'))

    elif 'play music' in query:
        os.startfile(os.path.join(music_dir, songs[i]))

    elif 'play next music' in query : 
        os.startfile(os.path.join(dir, os.listdir(dir)[i+1]))
        i+=1


def openProgram(query) :

    if 'open google drive' in query:
        dir = "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Brave Apps"
        os.startfile(os.path.join(dir, os.listdir(dir)[0]))

    elif 'open powerpoint' in query:
        dir = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office'
        os.startfile(os.path.join(dir, os.listdir(dir)[6]))

    elif 'open paint' in query :
        dir = 'C:\\Windows\\system32\\mspaint.exe'
        os.startfile(os.path.join(dir))

i = 1
print("\n")
for x in songs:
    print(i, ":", x, "\n")
    i = i + 1

