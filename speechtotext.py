import pyttsx3 
import speech_recognition as sr


def speech():
    recognit=sr.Recognizer()   
    with sr.Microphone() as source:
        print("Say something !")
        recognit.adjust_for_ambient_noise(source)
        audio=recognit.listen(source)
        try:
            print("Listening....")
            data=recognit.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understood")
            
speech()