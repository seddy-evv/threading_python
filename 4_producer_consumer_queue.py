"""
Solve the Producer-Consumer problem using a Queue.
"""


import concurrent.futures
import logging
import queue
import random
import threading
import time


def producer(queue_atr, event_atr):
    """Pretend we're getting a number from the network."""
    while not event_atr.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        queue_atr.put(message)

    logging.info("Producer received event. Exiting")


def consumer(queue_atr, event_atr):
    """Pretend we're saving a number in the database."""
    while not event_atr.is_set() or not queue_atr.empty():
        message = queue_atr.get()
        logging.info(
            "Consumer storing message: %s (size=%d)", message, queue_atr.qsize()
        )

    logging.info("Consumer received event. Exiting")


if __name__ == "__main__":
    format_str = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO,
                        datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
