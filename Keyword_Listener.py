import speech_recognition as sr

def get_audio(recognizer):
    # get audio from the microphone                                                                                          
    with sr.Microphone() as source:                                                                                                                                                         
        audio = recognizer.record(source, duration=3)
    return audio

def listen_for_keyword(recognizer, aud, key):
    # See if audio contains keyword
    try:
        if  recognizer.recognize_google(aud).find(key) != -1: # Keyword is found
            return True

    # Catches potential errors that might come up while audio is recognized
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))