"""CSC148 Lab 4: Abstract Data Types

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module runs timing experiments to determine how the time taken
to enqueue or dequeue grows as the queue size grows.
"""
from timeit import timeit
from typing import List, Tuple
# ====================== (Question 2, Task 4, Lab 4) ==========================
import matplotlib.pyplot as plt
#==============================================================================

from myqueue import Queue


###############################################################################
# Task 3: Running timing experiments
###############################################################################
# TODO: implement this function
def _setup_queues(qsize: int, n: int) -> List[Queue]:
    """Return a list of <n> queues, each of the given size."""
    # Experiment preparation: make a list containing <n> queues,
    # each of size <qsize>.
    # You can "cheat" here and set your queue's _items attribute directly
    # to a list of the appropriate size by writing something like
    #
    #     queue._items = list(range(qsize))
    #
    # to save a bit of time in setting up the experiment.

    queue_list = []

    i = 0
    while i < n:
        queue = Queue()
        queue._items = list(range(qsize))

        queue_list.append(queue)
        i += 1

    return queue_list


def time_queue() -> None:
    """Run timing experiments for Queue.enqueue and Queue.dequeue."""
    # The queue sizes to try.
    # You can change these values if you'd like.
    queue_sizes = [10000, 20000, 40000, 80000, 160000]

    # The number of times to call a single enqueue or dequeue operation.
    trials = 200

    # This loop runs the timing experiment. It has three main steps:
    for queue_size in queue_sizes:
        #   1. Initialize the sample queues.
        queues = _setup_queues(queue_size, trials)

        #   2. For each one, calling the function "timeit", takes three
        #      arguments:
        #        - a *string* representation of a piece of code to run
        #        - the number of times to run it (just 1 for us)
        #        - globals is a technical argument that you DON'T need to
        #          care about
        time = 0
        for queue in queues:
            time += timeit('queue.enqueue(1)', number=1, globals=locals())

        #   3. Report the total time taken to do an enqueue on each queue.
        print(f'enqueue: Queue size {queue_size:>7}, time {time}')

    # TODO: using the above loop as an analogy, write a second timing
    # experiment here that runs dequeue on the given queues, and reports the
    # time taken. Note that you can reuse most of the same code.
    for queue_size in queue_sizes:
        queues = _setup_queues(queue_size, trials)

        time = 0
        for queue in queues:
            time += timeit('queue.dequeue()', number=1, globals=locals())

        #   3. Report the total time taken to do an enqueue on each queue.
        print(f'dequeue: Queue size {queue_size:>7}, time {time}')

# TODO: implement this function
def time_queue_lists() -> Tuple[List[int], List[float], List[float]]:
    """Run timing experiments for Queue.enqueue and Queue.dequeue.

    Return lists storing the results of the experiments.  See the lab
    handout for further details.
    """
    queue_sizes = [10000, 20000, 40000, 80000, 160000]
    enqueue_time_list = []
    dequeue_time_list = []

    trials = 200

    for queue_size in queue_sizes:
        queues = _setup_queues(queue_size, trials)

        time = 0
        for queue in queues:
            time += timeit('queue.enqueue(1)', number=1, globals=locals())

        print(f'enqueue: Queue size {queue_size:>7}, time {time}')
        enqueue_time_list.append(time)

    for queue_size in queue_sizes:
        queues = _setup_queues(queue_size, trials)

        time = 0
        for queue in queues:
            time += timeit('queue.dequeue()', number=1, globals=locals())

        print(f'dequeue: Queue size {queue_size:>7}, time {time}')
        dequeue_time_list.append(time)

    return (queue_sizes, enqueue_time_list, dequeue_time_list)

if __name__ == '__main__':
    print(time_queue_lists())
