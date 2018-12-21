import os, time, subprocess
import getpass as gp
from threading import Lock
lock=Lock()
username=gp.getuser()
class Clean:
    def __init__(self, days=60):
        self.days=days
        self.start=time.time()

    def current(self, p):
        print("In path: "+p)
        for i in os.listdir(p):
            if not os.path.isdir(i):
                print(i)
                d=(self.start-os.stat(p).st_atime)/(3600*24)
                e=(self.start-os.stat(p).st_mtime)/(3600*24)
                if int(d)>self.days or int(e)>self.days:
                    a=input("Delete "+i+"? Yes or No: ")
                    type(a)
                    if a=="Yes":
                        os.system("mv -f " +p+"/"+i+" /home/"+username+"/.local/share/Trash/files/")
                        
    def all(self, p):
        j=subprocess.check_output(["find", p, "-type", "d", "-print"])
        j=j.decode("utf-8")
        line=j.split("\n")
        for k in line:
            with lock:
                try:
                    self.current(k)
                except KeyboardInterrupt:
                    inp=input("\nPress C to Continue to next directory or B to Break the loop: ")
                    type(inp)
                    if inp == "C":
                        continue
                    elif inp == "B":
                        break  
