"""
An example of how code works with multiple threads using ThreadPoolExecutor.
"""


import logging
import concurrent.futures
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format_str = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
