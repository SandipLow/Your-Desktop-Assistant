import webbrowser
from modules import LocalFiles


def Browse(query):
    if 'open youtube' in query:
        link = "https://youtube.com"
        webbrowser.open(link)

    elif 'open codewithharry' in query or 'open code with harry' in query:
        link = "https://codewithharry.com"
        webbrowser.open(link)

    elif 'open ration card website portal' in query:
        webbrowser.open("https://food.wb.gov.in/HomePage/Offlineforms.aspx")

    elif 'open unity docs' in query:
        webbrowser.open("file:///E:/Unity/2020.3.9f1/Editor/Data/Documentation/en/ScriptReference/MonoBehaviour"
                        ".OnCollisionEnter.html")

    else:
        LocalFiles.openProgram(query)
