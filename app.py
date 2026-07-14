from textual.app import App as app
import time as t
from textual.widgets import Static, Input, RichLog
from textual.containers import Horizontal as h


    #will try this thing 1st time sorry for error if present
route =None
a=input("enter the code you got in part 1").strip().lower()
p=a.split("-")

if len(p) !=3:
    print("INVALID")
    exit()
else:
    prefix=p[0].upper()
    number=p[1]
    ending=p[2].upper()
    if prefix in ["DEV","ROOT" ,"AIRL","CORE", "SYS"] and number.isdigit() and ending=="P2":
        print("Verified as a vetran of part 1")
        route=prefix
    else:
        print("either verify code or just complete part 1 bruh\n Airl is waitin for you\n") #pls play part 1 to get better knowledge dont just get code froom here:<
        exit()

        #main cooking stuff
class Aitrap2d(app):
    CSS_PATH ="style.css"
    ENABLE_COMMAND_PALETTE= False
    DEFAULT_CSS=""
    def compose(self):
       yield RichLog(id="history",markup="False")
       with h():
           yield Static(">")
           yield Input(placeholder= "ENTER CMD..", id="cmd")
    
    def on_mount(self):
        terminal=self.query_one("#history",RichLog)
        self.query_one("#cmd",Input).focus()
       
        if route =="DEV":
            terminal.write("\nDev route....loadin'..g")
            terminal.write("[[CODE ACCEPTED ]]")
            terminal.write("dev profile found")
            terminal.write("loading debug memory")
            terminal.write("maybe some log survived\n")
        elif route=="ROOT":
            terminal.write("\nRoot route...rootin'..")
            terminal.write("[[CODE ACCEPTED ]]")
            terminal.write("auth detected of root")
            terminal.write("maybe access restored")
            terminal.write("disabled the security layers\n")
        elif route=="AIRL":
            terminal.write("\nsomeone remember you bro..")
            terminal.write("[[CODE ACCEPTED ]]")
            terminal.write("airl recognise this sign.")
            terminal.write("welcome")
            terminal.write("memory sync,in'\n")
        elif route=="CORE":
            terminal.write("\ncore access getting...oh!.")
            terminal.write("[[CODE ACCEPTED ]]")
            terminal.write("verified fragment")
            terminal.write("critical.. case")
            terminal.write("maybe connection restored.\n")
        elif route=="SYS":
            terminal.write("\nsys. route systeming")
            terminal.write("[[CODE ACCEPTED ]]")
            terminal.write("maybe found sys archs")
            terminal.write("recover..y..")
            terminal.write("bootin'completed\n")
        for i in range(4,0,-1):
            terminal.write(f"cont. in {i}....")
            t.sleep(1) 
        terminal.write("\ntype help to cont. and didn't you know that sus guy")
    

        
if __name__=="__main__":
    Aitrap2d().run()


