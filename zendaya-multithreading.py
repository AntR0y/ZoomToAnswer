import logging
import os
from queue import Queue
from threading import Thread

import speech_recognition as sr
from time import time
from Voice_Recognition import start_listening
from New_Voice import get_audio, listen_for_keyword

#logging.basicConfig(levl=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#
# logger = logging.getLogger(__name__)

class ListenerWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.keyword = "excuse me Zendaya"

    def run(self):
        while True:
            # Get work from queue and expand tupple
            r, audio = self.queue.get()
            try:
                listen_for_keyword(r, audio, self.keyword)
            finally:
                self.queue.task_done()

def main():
    r = sr.Recognizer()                    
    
    # Create a queue to communicate with worker threads
    queue = Queue()

    # Create 8 worker threads
    for x in range(8):
        worker = ListenerWorker(queue)
        worker.daemon = True
        worker.start()

    # Continuously record voice clips and puts them into queue
    while True:
        audio = get_audio(r)
        queue.put((r, audio))
    queue.join()

if __name__ == '__main__':
    main()