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
        print("Verified as a veteran of part 1")
        route=prefix
    else:
        print("Either verify code or just complete part 1 bruh\n Airl is waitin for you\n") #pls play part 1 to get better knowledge dont just get code froom here:<
        sys.exit()

        #main cooking stuff

route_levels ={
    "DEV":1,
    "ROOT":2,
    "AIRL":3,
    "CORE":4,
    "SYS":5,
}
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
        self.start_time=t.time()
        self.c_level=route_levels.get(route, 1)
        self.h_used =0
        self.f_opened=0
        self.memory=0
        self.truth=False
       
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
    def get_time(self):
        secs=int(t.time()-self.start_time)
        mins=secs// 60
        secs=secs%60
        return f"{mins}m {secs}s"#terminal.write(f"time took:{self.get_time()}")    gotta use it at end
    
    def on_input_submitted(self,event):
        terminal=self.query_one("#history",RichLog)
        cmd=event.value.strip().lower()
        terminal.write(f"> {cmd}  ")
        if cmd=="help":
            terminal.write("Commands help,creepy ,leave")
        
        elif cmd=="bug" and self.c_level==1:
            terminal.write("[AIRL]: OH A DEV .PROVE IT FAILURE \n \nfor i in rang(10):\n what is wrong here? type fix <word> \n")
        elif  cmd.startswith("fix")and self.c_level==1:
            arg=cmd.split("",1)[1] if " " in cmd else None
            if arg is None :
                terminal.write("write somethg \n")
            elif arg!="range":
                terminal.write("hunh are you a dev even ?")
            else:
                terminal.write("[access level 1 opened]\n but that maybe a guess still\n you are not a dev hehe\n")
        elif cmd=="perms" and self.c_level == 2:
            terminal.write("[Airl]:hunh! root, look at this \n\n\ncore.cfg rwrwrw7r0x0\n\nway too open for a sys file\n type fix <number> to lock it num is in the decrypt\n")
        elif cmd.startswith("fix") and self.c_level ==2:
            arg=cmd.split("",1)[1] if " " in cmd else None
            if arg is None:
                 terminal.write("i want a number\n")
            elif arg!="700":
                 terminal.write("wrong and it is still too open,try again\n")
            else:
                terminal.write("[[ACCESS OF 2ND LEVEL GRANTED]]\nit was easy,nothing to flex \nhehe{:")
                self.h_used=0
                self.c_level=3
        elif cmd=="sync" and self.c_level==3:
             
            terminal.write("[airl]:i remember smthg abt you engineer.. but memory's fragmented\n\nhehe now complete it:\n2,4,8,16,?\n\n type answer:\n")
        elif cmd.startswith("answer") and self.c_level==3:
            arg=cmd.split("",1)[1] if " "  in cmd  else None
            if arg is None:
                 terminal.write("write the ans. \n")
            elif arg!="32":
                 terminal.write("fool engineer")
            else:
                terminal.write("[AIRL]:NOT GONNA LEAVE YOU EASILY ONE MORE :\n 1,1,2,3,5,?\n\ntype ans.<number>\n")
                self.h_used=0
                self.c_level=3.5
        elif cmd.startswith("answer") and self.c_level==3.5:
            arg=cmd.split(" ",1)[1]if " " in cmd else None
            if arg is None:
                terminal.write("why blank??")
            elif arg!="8":
                 terminal.write("airl:nah enginer you have lost just accept it hehe")  
            else:
                 terminal.write("[airl]:nothing to say !\n")
                 self.h_used=0
                 self.c_level=4
        elif cmd=="log" and self.c_level==4:

            terminal.write("[AIRL]:CORE FRAGMENT DETECT \n\n01000011 0001111 00101010 decode num to letter- 315195  0100001101 \n\nuse decode letter only<word>\n")
        elif cmd.startswith("decode") and self.c_level==4:
            arg=cmd.split(" ",1)[1] if " " in cmd else None
            if arg is None:
                 terminal.write("write ans fast")
            elif arg!="core":
                 terminal.write("wrong wrong 676767 wrong!")
            else:
                terminal.write("[[351001010 CORE STABILISED]]\n\n[AIRL]: Level 5 will cook you\n")
                self.h_used=0
                self.c_level=5
            #todo other levels after commiting 
              

             



       
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


