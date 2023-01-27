import speech_recognition as speechRecognition
import pyttsx3




recognition = speechRecognition.Recognizer()

#converting text to speech

def TexttoSpeak(command):
    assistant = pyttsx3.init()
    assistant.say(command)
    assistant.runAndWait()



#Using the microphone as input source for audio

with speechRecognition.Microphone() as source2:
    recognition.adjust_for_ambient_noise(source2, duration=0.2)
    print("Please say something")
    
    audio2 = recognition.listen(source2)
    
    text = recognition.recognize_google(audio2, language="en-US",show_all=True)

    
    print(text['alternative'])
    TexttoSpeak(text)