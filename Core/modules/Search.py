import webbrowser
import wikipedia as wikipedia
from wikipedia.wikipedia import search


# Google Search
def GoogleSearch(query) :
    query = query.replace("google","")

    if 'from' in query:
        query = query.replace("from", "")

    link = "https://www.google.com/search?q=" + query + "&oq=" + query + "&aqs=chrome..69i57.12574j0j1&sourceid=chrome&ie=UTF-8"
    webbrowser.open(link)


# Wikipedia Search
def WikiSearch(query) :
    query = query.replace("wikipedia","")

    if 'from' in query:
        query = query.replace("from", "")

    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    return results


# Youtube Search
def YouTubeSearch(query) :
    query = query.replace("youtube","")
            
    if 'from' in query:
        query = query.replace("from", "")

    link = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(link)