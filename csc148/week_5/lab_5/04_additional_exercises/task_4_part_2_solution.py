"""CSC148 Lab 5: Linked Lists

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module runs timing experiments to determine how the time taken
to call `len` on a Python list vs. a LinkedList grows as the list size grows.
"""
from timeit import timeit
from task_4_part_1_solution import LinkedList
import matplotlib.pyplot as plt

NUM_TRIALS = 3000                        # The number of trials to run.
SIZES = [1000, 2000, 4000, 8000, 16000]  # The list sizes to try.

def profile_getitem(list_class: type, size: int) -> float:
    """Return the time taken to call len on a list of the given class and size.

    Precondition: list_class is either list or LinkedList.
    """
    # TODO: Create an instance of list_class containing <size> 0's.
    my_list = LinkedList([0 for x in range(size)])

    # TODO: call timeit appropriately to check the runtime of len on the list.
    # Look at the Lab 4 starter code if you don't remember how to use timeit:
    # https://www.teach.cs.toronto.edu/~csc148h/winter/labs/w4_ADTs/starter-code/timequeue.py

    time = timeit('my_list[-1]', number=1, globals=locals())

    return time

def profile_slice(list_class: type, size: int) -> float:
    """Return the time taken to call len on a list of the given class and size.

    Precondition: list_class is either list or LinkedList.
    """
    # TODO: Create an instance of list_class containing <size> 0's.
    my_list = LinkedList([0 for x in range(size)])
    n = len(my_list)

    # TODO: call timeit appropriately to check the runtime of len on the list.
    # Look at the Lab 4 starter code if you don't remember how to use timeit:
    # https://www.teach.cs.toronto.edu/~csc148h/winter/labs/w4_ADTs/starter-code/timequeue.py

    time = timeit('my_list[n::-1]', number=1, globals=locals())

    return time



if __name__ == '__main__':
    getitem_time_list = []
    slice_time_list = []

    for list_class in [LinkedList]:
        # Try each list size
        print('=========== __getitem__ ==========')
        for s in SIZES:
            time = profile_getitem(list_class, s)
            getitem_time_list.append(time)
            print(f'[{list_class.__name__}] Size {s:>6}: {time}')

        print('=========== slice ==========')

        for s in SIZES:
            time = profile_slice(list_class, s)
            slice_time_list.append(time)
            print(f'[{list_class.__name__}] Size {s:>6}: {time}')

    ax = plt.subplot(1,1,1)

    ax1 = plt.subplot(2, 1, 1)
    plt1, = ax1.plot(SIZES, getitem_time_list, 'ro')
    ax1.legend([plt1],["'__getitem__'"], loc="lower right")
    ax1.set_ylabel ('Time (Seconds)')
    ax1.set_title('Worst-Case Algorithm Run time vs Node Size')

    ax2 = plt.subplot(2, 1, 2)
    plt2, = ax2.plot(SIZES, slice_time_list, 'bo')
    ax2.legend([plt2],["'__getitem__.slice(...)'"], loc="lower right")
    ax2.set_xlabel('Size')
    ax2.set_ylabel('Time (Seconds)')

    plt.show()