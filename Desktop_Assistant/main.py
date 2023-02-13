import speech_recognition as speechRecognition
import pyttsx3
import webbrowser as wb



recognition = speechRecognition.Recognizer()


def openBrowser():
    path = "C:\Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"


    r = speechRecognition.Recognizer()

    with speechRecognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
    
        print("Please say something...")
    
        audio = r.listen(source)
    
        print("processing your request")
    
        try:
            dest = r.recognize_google(audio)
            print("you said ..." + dest)
        
            wb.get(path).open(dest)
        
        except Exception as e:
            print("Error : " + str(e))

    



if __name__ == "__main__":
    openBrowser()


#Using the microphone as input source for audio

""" 


#converting text to speech

def TexttoSpeak(command):
    assistant = pyttsx3.init()
    assistant.say(command)
    assistant.runAndWait()


with speechRecognition.Microphone() as source2:
    recognition.adjust_for_ambient_noise(source2, duration=0.2)
    print("Please say something")
    
    audio2 = recognition.listen(source2)
    
    text = recognition.recognize_google(audio2, language="en-US",show_all=True)

    
    print(text)
    TexttoSpeak(text)
    
"""

