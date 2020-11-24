import speech_recognition as sr
from Voice_Recognition import start_listening
def listen():
    # get audio from the microphone                                                                       
    r = sr.Recognizer()                    
    keyword = "excuse me Zelda"                                                                
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)   

    try:
        if  r.recognize_google(audio).find(keyword) != -1:
            print("woohoo!")
            start_listening()
        else:
            print("aww")
            print(r.recognize_google(audio))
            listen()
    except sr.UnknownValueError:
        print("Could not understand audio")
        listen()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        listen()

listen()