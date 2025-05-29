import os
import webbrowser
import openai
league = ["open league of legends","open league","open lol","open league of legend"]
def application(word):
    if word.lower() in league:
        os.system('open "/Applications/League of Legends.app"')
    elif word.lower() == "open safari":
        os.system("open -a Safari")
    elif word.lower() == "open discord":
        os.system("open -a Discord")
    elif word.lower() == "open google":
        webbrowser.open("https://google.com")
    elif word.lower() == "open youtube":
        webbrowser.open("https://youtube.com")
    elif word.lower() == "open facebook":
        webbrowser.open("https://facebook.com")
    elif word.lower() == "open spotify":
        os.system("open -a Spotify")
    elif word.lower() == "open chatgpt" or word.lower() == "open chat gpt":
        os.system("open -a ChatGpt")

music={
    "balen": "https://www.youtube.com/watch?v=Ir-SAvHLt1E&list=RDIr-SAvHLt1E&start_radio=1",
    "wishlist": "https://www.youtube.com/watch?v=hFGG7T3Mq3w&list=RDIr-SAvHLt1E&index=3",
    "gulabi":"https://www.youtube.com/watch?v=QFoPEP-V764&list=RDIr-SAvHLt1E&index=14",
    "dhairya":"https://www.youtube.com/watch?v=6FEsFvZ-hqY&list=RDIr-SAvHLt1E&index=15",
    "paisa":"https://www.youtube.com/watch?v=Tb3x5I0ulCg&list=RDIr-SAvHLt1E&index=18",
    "maya":"https://www.youtube.com/watch?v=kEbcHhNsRoU&list=RDIr-SAvHLt1E&index=24",
    "kasari bhanu":   "https://www.youtube.com/watch?v=7SaM24Cjzj0",
    "ma timro":"https://www.youtube.com/watch?v=WLyeVC6tU6s",
    "je chau timi":"https://www.youtube.com/watch?v=_Tk9_kPpO1U",
    "batash":"https://www.youtube.com/watch?v=AtoZw7o2kRo"
}