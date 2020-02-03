import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine=pyttsx3.init("sapi5")
voice=engine.getProperty("voices")
engine.setProperty("voice",voice[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    time=int(datetime.datetime.now().hour)
    if time>=0 and time<12 :
        print("Good Morning")
        speak("Good Morning")
        
    elif(time>=12 and time<16):
        print("Good Afternoon")
        speak("Good Afternoon")
       
    else:
        print("Good Evening")
        speak("Good Evening")
        
    print("I am Kunal. How can i help You.")
    speak("I am Kunal How can i help You.")
 
def take_commond():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recogniting...")
        query=r.recognize(audio)
        print(f"you say : {query} \n")
        speak(query)
        return query
    except Exception as e:
        print(e)
        print("Please say again...\n")
        return "None"
if __name__=="__main__":
    wish_me()
    e=True
    while e:
        query=take_commond().lower()
        if "wikipedia" in query:
            speak("Searching in Wikipedia....")
            query=query.replace("wikipedia"," ")
            
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            e=False
        elif "open google" in query:
            webbrowser.open("google.com")
            e=False
        elif "open whataap" in query:
            webbrowser.open("https://web.whatsapp.com/")
            e=False
        elif "play music" in query:
            path1="E:\Videos\\music"
            if os.path.exists(path1)==True:
                songs=os.listdir(path1)
               # print(songs)
                flag=True
                while(flag==True):
                   
                    print("Which music you want to play")
                    speak("Which music you want to play")
                    name=take_commond()
                    print("You say : ",name)
                    for i in songs:
                        if name.lower() in i.lower():
                            print("Injoy music")
                            speak("Injoy music ")
                            speak(i)
                            os.startfile(os.path.join(path1,i))
                            e=False
                            flag=False
                            break
                        elif(name=="close music"):
                            flag=False
                            break
                        

                    if(e==True):        
                        print("Please say again i have not found that music from you music collection :")    
                        speak("please tell me again ")
                     
                            
            else:
                print("Sorry we are unable to find your music folder")
                
        elif "pubg" in query:
            path1="F:\\Program Files\\TxGameAssistant\\AppMarket\\AppMarket"
            if os.path.exists(path1)==True:
                print("Enjoy your pubg Game")
                speak("Enjoy your pubg Game")
                os.startfile(path1)
            else:
                print()
        elif "open photo" in query:
            path1="C:\\Users\\user\\Pictures\\Puja\\IMG-20190209-WA0060.jpg"
            if(os.path.exists(path1)==True):
                os.startfile(path1)
            else:
                print("sorry this pic already deleted")

        
        elif query=="close" or query=="exit":
            e=False
        elif query=="none":
            print("please Again tell me")
            speak("please Again tell me")
        else:
             webbrowser.open(query)
             e=False





