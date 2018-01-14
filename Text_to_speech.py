import pyttsx3
engine = pyttsx3.init()
def give_reply(reply):
    rate = engine.getProperty('rate')
    print(rate)
    engine.setProperty('rate',110)
    engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    voices = engine.getProperty('voices')
    if len(voices)>=1:
        engine.setProperty('voice', voices[1])
    else:
        engine.setProperty('voice', voices[1])    
    engine.say(reply)
    engine.runAndWait()
reply = input()
give_reply(reply)
