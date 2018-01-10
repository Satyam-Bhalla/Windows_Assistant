import urllib.request
import urllib.parse
import re
import webbrowser
def playing_songs_and_videos():
    inp = input("Enter your query\n")
    query_string = urllib.parse.urlencode({"search_query" : inp})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    print("Processing your query")
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
playing_songs_and_videos()
