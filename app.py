from textual.app import App as app
from textual.widgets import Static,Input
from textual.containers import Horizontal as h
class Aitrap2d(app):
    CSS_PATH ="style.css"
    ENABLE_COMMAND_PALLETE=False
    DEFAULT_CSS=""

    #will try this thing 1st time sorry for error if present
a=input("enter the code you got in part 1").strip().lower()
p=a.split("-")
if  len(p) !=3:
    print("INVALID")
else:
    prefix=p[0]
    number=p[1]
    ending=p[2]
    if prefix in ["DEV","ROOT" ,"AIRL","CORE", "SYS"] and number.isdigit() and ending=="P2":
        print("Verified as a vetran of part 1")
        if prefix=="DEV":
            print("Dev route.")
        elif prefix=="ROOT":
            print("Root route.")
        elif prefix=="AIRL":
            print("someone remember you bro")
        elif prefix=="CORE":
            print("core access got")
        elif prefix=="SYS":
            print("sys. route")
    else:
        print("either verify code or just complete part 1 bruh\n Airl is waitin for you\n") #pls play part 1 to get better knowledge dont just get code froom here:<

        
if __name__=="__main__":
    Aitrap2d().run()


