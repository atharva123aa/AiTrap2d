from textual.app import App as app
import sys
import asyncio
import time as t
from textual.widgets import Static, Input, RichLog
from textual.containers import Horizontal as h


    #will try this thing 1st time sorry for error if present
route =None
a=input("enter the code you got in part 1").strip().upper()
p=a.split("-")

if len(p) !=3:
    print("INVALID and please play part 1 of game so you get it")
    sys.exit()
else:
    prefix=p[0].upper()#useless but don want to do this again
    number=p[1]
    ending=p[2].upper()
    if prefix in ["DEV","ROOT" ,"AIRL","CORE", "SYS"] and number.isdigit() and ending=="P2":
        print("Verified as a vetran of part 1")
        route=prefix
    else:
        print("either verify code or just complete part 1 bruh\n Airl is waitin for you\n") #pls play part 1 to get better knowledge dont just get code froom here:<
        sys.exit()

        #main cooking stuff
class Aitrap2d(app):
    CSS_PATH ="style.css"
    ENABLE_COMMAND_PALETTE= False
    DEFAULT_CSS=""
    BINDINGS=[("ctrl+c","quit","Quit")]
    def compose(self):
       yield RichLog(id="history", markup=False)
       with h():
           yield Static(">")
           yield Input(placeholder= "ENTER CMD..", id="cmd")
    def action_quit(self):
        self.exit()
    
    async def on_mount(self):
        
        terminal=self.query_one("#history",RichLog)
        self.query_one("#cmd",Input).focus()
       
        if route =="DEV":
            terminal.write("\nDev route....loadin'..g")
            terminal.write("[[CODE ACCEPTED ]]")
            terminal.write("dev profile found")
            terminal.write("loading debug memory")
            terminal.write("maybe some log survived\n")
            terminal.write("developer mode!!")
        elif route=="ROOT":
            terminal.write("\nRoot route...rootin'..")
            terminal.write("[[CODE ACCEPTED ]]")
            terminal.write("auth detected of root")
            terminal.write("maybe access restored")
            terminal.write("disabled the security layers\n")
            terminal.write("root completed")
        elif route=="AIRL":
            terminal.write("\nsomeone remember you bro..")
            terminal.write("[[CODE ACCEPTED ]]")
            terminal.write("airl recognise this sign.")
            terminal.write("welcome")
            terminal.write("memory sync,in'\n")
            terminal.write("i think someone wants to join you back")
        elif route=="CORE":
            terminal.write("\ncore access getting...oh!.")
            terminal.write("[[CODE ACCEPTED ]]")
            terminal.write("verified fragment")
            terminal.write("critical.. case")
            terminal.write("maybe connection restored.\n")
            terminal.write("core breach started!")
        elif route=="SYS":
            terminal.write("\nsys. route systeming")
            terminal.write("[[CODE ACCEPTED ]]")
            terminal.write("maybe found sys archs")
            terminal.write("recover..y..")
            terminal.write("bootin'completed\n")
            terminal.write("system open")
        
        for i in range(4,0,-1):
            terminal.write(f"continuing. in {i}....")
            await asyncio.sleep(1)
        terminal.write("\ntype help to cont. and didn't you know that sus guy")
    
    def on_input_submitted(self,event):
        terminal=self.query_one("#history",RichLog)
        cmd=event.value.strip().lower()
        terminal.write(f"> {cmd}  ")
        if cmd=="help":
            terminal.write("CMDS: help,creepy ,leave")
        elif cmd=="creepy":
            if self.has_class("-theme-dark"):
                self.remove_class("-theme-dark")
                terminal.write("Theme restored sucess.")
            else:
                self.add_class("-theme-dark")
                terminal.write("DARK MODE ENABLED")
        elif cmd=="leave":
            self.exit()
        else:
            terminal.write("type help ")# was trying to scare user by changing theme ehehe but i did not do that
        self.query_one("#cmd",Input ).value =""
        self.query_one("#cmd",Input).focus()

        
if __name__=="__main__":
    Aitrap2d().run()


