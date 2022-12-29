"""
The code below works with two threads: the main thread and one started with the threading.
"""


import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format_str = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    # x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # If the line below is commented out, the program will not wait for thread_function to complete
    # and continue its execution, but the function will be executed. If the thread is created with daemon=true
    # then the line below is required otherwise the program will not wait for the thread_function to execute,
    # and the function will not be executed.
    x.join()
    logging.info("Main    : all done")
