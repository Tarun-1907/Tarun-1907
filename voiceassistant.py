import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

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
            
def text(x):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty("rate",119)
    engine.say(x)
    engine.runAndWait()

if __name__=="__main__":
  data1=speech().lower()
  if "name" in data1:
      name="my name is assist-bhai."
      text(name)
  elif "old" in data1:
      age="I am a new born baby."
      text(age)
  elif "time" in data1:
      time=datetime.datetime.now().strftime("%I%M%p")
      text(time)
  elif 'youtube' in data1:
      webbrowser.open('https://www.youtube.com/')
  elif 'profile' in data1:
      webbrowser.open('https://github.com/Tarun-1907')
  elif "joke" in data1:
      joke_1=pyjokes.get_joke(language="en",category="neutral")
      text(joke_1)
      speech(joke_1)
  elif "instagram" in data1:
      webbrowser.open("https://www.instagram.com/")
  elif "linkedin" in data1:
      webbrowser.open("https://in.linkedin.com/?original_referer=https%3A%2F%2Fwww.google.com%2F")
  elif "twitter" in data1:
      webbrowser.open("https://twitter.com/i/flow/login?redirect_after_login=%2Flogin%3Flang%3Den")
  elif "snapchat" in data1:
      webbrowser.open("https://www.snapchat.com/")
  elif "whatsapp" in data1:
      webbrowser.open("https://www.whatsapp.com/")
  elif "swiggy" in data1:
      webbrowser.open("https://www.swiggy.com/")
  elif "zomato" in data1:
      webbrowser.open("https://www.zomato.com/")
  elif "github" in data1:
      webbrowser.open("https://www.github.com/")
  elif "facebook" in data1:
      webbrowser.open("https://www.facebook.com/")
  elif "canva" in data1:
      webbrowser.open("https://www.canva.com/")
  elif "discord" in data1:
      webbrowser.open("https://www.discord.com/")
  elif "brave" in data1:
      webbrowser.open("https://www.brave.com/")
  elif "flipkart" in data1:
      webbrowser.open("https://www.flipkart.com/")
  elif "amazon" in data1:
      webbrowser.open("https://www.amazon.com/")
  elif "spotify" in data1:
      webbrowser.open("https://www.spotify.com/")
  elif "sap" in data1:
      webbrowser.open("https://www.sapportal.com/")
  elif "jupyter notebook" in data1:
      webbrowser.open("https://jupyter.org/")
  elif "google colab" in data1:
      webbrowser.open("https://www.googlecolaboratory.com/")
  elif "google" in data1:
      webbrowser.open("https://www.google.com/")
  elif "microsoft edge" in data1:
      webbrowser.open("https://www.microsoftedge.com/")