import time
import speech_recognition as sr
from queue import Queue
from threading import Thread
from New_Voice import get_audio, listen_for_keyword
from Voice_Recognition import start_listening

currentlyListening = False

class ListenerWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.keyword = "Zendaya"

    def run(self):
        global currentlyListening
        while True:
            # Get work from queue and expand tupple
            r, audio = self.queue.get()
            try:
                keywordFound = listen_for_keyword(r, audio, self.keyword)
            finally:
                self.queue.task_done()
                if keywordFound and not currentlyListening:
                    currentlyListening = True
                    start_listening()
                    currentlyListening = False

class RecorderWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        global currentlyListening
        while True:
            r, listenerQ = self.queue.get()
            try:
                audio = get_audio(r)
                listenerQ.put((r, audio))
            finally:
                self.queue.task_done()
        listenerQ.join()
            
def main():
    r = sr.Recognizer()                    
    
    # Create a queue to communicate with worker threads
    ListenerQueue = Queue()
    RecorderQueue = Queue()

    # Create 8 ListenerWorker threads
    for x in range(4):
        worker = ListenerWorker(ListenerQueue)
        worker.daemon = True
        worker.start()
    
    # Create 4 RecorderWorker threads
    for y in range(4):
        worker = RecorderWorker(RecorderQueue)
        worker.daemon = True
        worker.start()

    # Continuously record voice clips and puts them into queue
    while True:
        RecorderQueue.put((r, ListenerQueue))
        time.sleep(1.5)
    RecorderQueue.join()

if __name__ == '__main__':
    main()