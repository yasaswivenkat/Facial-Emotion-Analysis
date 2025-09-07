import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import subprocess
import glob

engine=pyttsx3.init()
def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=2
        try:
            audio=r.listen(source)
            query=r.recognize_google(audio,language="en-in")
            print(f"User said:{query}")
            return query.lower()
        except Exception:
            return ""

def find_app_path(app_name):
    try:
        result=subprocess.check_output(f'where {app_name}',shell=True,text=True).strip()
        if result:
            return result.split("\n")[0]
    except subprocess.CalledProcessError:
        pass

    search_paths=["C:/Program Files/","C:/Program Files (x86)/","C:/Users/%USERNAME%/AppData/Local/Programs/"]
    for path in search_paths:
        exe_files=glob.glob(f"{path}**/{app_name}.exe",recursive=True)
        if exe_files:
            return exe_files[0]
    return None

def open_app(app_name):
    app_path=find_app_path(app_name)
    if app_path:
        say(f"Opening {app_name}")
        print(f"Opening {app_name} from {app_path}")

        if any(cmd_app in app_name.lower() for cmd_app in ["cmd","powershell","terminal"]):
            os.system(f'start cmd /k "{app_path}"')
        else:
            os.startfile(app_path)
    else:
        say(f"Trying to open {app_name}")
        os.system(f"start {app_name}")

if __name__ == '__main__':
    print("Pycharm")
    print("Hello, I am Jarvis AI")
    say("Hello, I am Jarvis AI")
    while True:
        text = takeCommand()
        if "close" in text:
            break

        sites={"google": "https://google.com","chatgpt": "https://chat.openai.com","youtube": "https://youtube.com",
            "instagram": "https://instagram.com","whatsapp": "https://web.whatsapp.com"}
        for site in sites:
            if f"open {site}" in text:
                say(f"Opening {site}")
                webbrowser.open(sites[site])
        #It can open Chrome,Excel,Notepad,CMD,Powershell,File explorer,VS code,Pycharm
        if "open" in text:
            words=text.split(" ")
            app_name=" ".join(words[1:])
            open_app(app_name)

        if "open german video" in text:
            germanfile = "C://Users/yasas/OneDrive/Desktop/german.mp4"
            say("Opening German video")
            os.startfile(germanfile)

        if "what's the time" in text:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Time is: {strfTime}")
            say(f'The time is {strfTime}')