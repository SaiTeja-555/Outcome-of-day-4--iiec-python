import os
import pyttsx3

open_array = ["run","open","launch","start","execute"]
applications = [["notepad","editor","text editor"],["chrome","browser","google chrome"],["wmplayer","media player","windows media player"],
                ["Code","virtual studio code"],["firefox","mozilla","mozilla firefox"],["vlc","vlc player"],["python"],
                ["mspaint","paint","microsoft paint"],["xampp-control","xampp"],["AutodeskDesktopApp"],["maya"],["EXCEL","ms excel","microsoft excel"],
                ["kile"],["OneDrive","one drive"],["VirtualBox","virual box"],
                ["OUTLOOK"],["POWERPNT","ms powerpoint","microsoft powerpoint"],["MSPUB","ms publisher","microsoft publisher"],["SHAREit","share it"],
                ["sublime_text","sublime text editor"],["control","control panel"],
                ["iexplore","internet explorer"],["wordpad"],["Magnify","magnifier"],["osk","on screen keyboard"],["Narrator"],["cmd","command prompt"],
                ["Taskmgr","task manager"],["WinRAR"],["WINWORD","word"],["Zoom"]]


pyttsx3.speak("Welcome, dear user.")
print("Welcome, dear user.")
pyttsx3.speak("I am your assistant")
print("I am your assistant")
while True:
    pyttsx3.speak("Please enter your query")
    query = input("Please enter your query:")
    if "exit" in query:
        pyttsx3.speak("Closing the application.")
        print("Closing the application.")
        pyttsx3.speak("Thank you")
        print("Thank you")
        break
    flag = 0
    if not "dont" in query:
        for open_key in open_array:
            if open_key in query.lower():
                for application_set in applications:
                    for application in application_set: 
                        if application.lower() in query.lower():
                            flag = 1
                            pyttsx3.speak("Opening"+application_set[-1])
                            print("Opening",application_set[-1])
                            os.system(application_set[0])
                            pyttsx3.speak("Closing"+application_set[-1])
                            print("Closing",application_set[-1])
                            
                            break
                    if flag:
                        break
                break
        if not flag:
            print("Sorry...Invalid query")
            pyttsx3.speak("Sorry.Invalid query")
    else:
        print("Mentioned the word \"dont\" in the query")
        pyttsx3.speak("Mentioned the word dont in the query")
        
            
