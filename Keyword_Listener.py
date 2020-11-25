import speech_recognition as sr
import time
from multiprocessing import Process
from Voice_Recognition import start_listening

class ForeverListener():
    def __init__(self, still_listening=True):
        self.still_listening = still_listening
        #self.p1 = Process(target=self.listen_for_keyword, args=(1,))
        #self.p2 = Process(target=self.listen_for_keyword, args=(2,))
        self.bank = None
        self.foundKeyword = False


        self.count = 0 # To ensure listner does not listen to question twice

    def listen_for_keyword(self):
        # get audio from the microphone                                                                       
        r = sr.Recognizer()                    
        keyword = "Zelda"                                                                
        with sr.Microphone() as source:                                                                       
            print("Speak:")                                                                                   
            audio = r.listen(source)
            print("Done listening") 

        p1 = Process(target=self.is_keyword_in_query, args=(keyword, audio, r))
        p1.start()
        p2 = Process(target=self.listen_during_gap, args=(r,))
        p2.start()
        p1.join()
        p2.join()
        print("DONE")
        if self.foundKeyword:
            print("now ask q")
            start_listening()
        else:
            print("no keyword")
            self.listen_for_keyword()


    def listen_during_gap(self, rec):                 
        # keyword = "Zelda"                                                                
        with sr.Microphone() as source:                                                                       
            print("Speak during gap:")                                                                                   
            audio = rec.record(source, duration=5)
            self.bank = audio
    
    def is_keyword_in_query(self, keyword, aud, rec):
        try:
            if  rec.recognize_google(aud).find(keyword) != -1:
                print("woohoo!")
                self.foundKeyword = True
            elif self.bank != None and rec.recognize_google(self.bank).find(keyword) != -1:
                print("woohoo!")
                self.foundKeyword = True
            else:
                print("aww")
                #print(rec.recognize_google(aud))
                #print(self.bank)
                #self.listen_for_keyword()

        except sr.UnknownValueError:
            print("Could not understand audio")
            #self.listen_for_keyword()
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            #self.listen_for_keyword()

if __name__ == '__main__':
    Zelda = ForeverListener()
    Zelda.listen_for_keyword()


    
#        """
#        try:
#            if  r.recognize_google(audio).find(keyword) != -1:
#                print("woohoo!")
#                start_listening()
#            else:
#                print("aww")
#                print(r.recognize_google(audio))
#                self.listen_for_keyword()#
#
#        except sr.UnknownValueError:
#            print("Could not understand audio")
#            self.listen_for_keyword()
#        except sr.RequestError as e:
#            print("Could not request results; {0}".format(e))
#            self.listen_for_keyword()
#        """

           #p2.join()

    #def listen_1_then_2(self):
        #p1 = Process(target=self.listen_for_keyword, args=(1,))
    #    self.p1.start()
        #p2 = Process(target=self.listen_for_keyword, args=(2,))
    #    time.sleep(5)
    #    self.p2.start()
        #p1.join()
        #p2.join()