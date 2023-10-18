import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

def generate_random_array():
    """
    Funcion generated array from 1-100 and uses random library to randomise the order.
    
    RETURNS:
        random array
    """
    initial_array = list(range(1, 101))
    
    random.shuffle(initial_array)
    return initial_array

def is_sorted(arr):
    """
    Function checks if a array is orderd in ascending order with time complexity of O(n) since it only has to check everything ones.
    Instead of the standard 'sorted()' function in python that has a time complexity of O(n*log(n)).

    PARAMETERS:
        array (intergers)
    RETURNS:
        boolean
    """
    return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))

def bubble_sort_and_update(frame):
    """
    Bubble sort algorithm sorts a array with average and worst case time complexity of O(n^2),
    it does this by checking if the next element is bigger and if so, swapping until there are no more swaps.

    PARAMETERS:
        frame (integer): indicating the current frame or step in the visualization.
    RETURNS:
        N/A
    """
    plt.cla()
    for i in range(len(data) - frame - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
    plt.bar(range(len(data)), data, color='skyblue')
    plt.title("Bubble Sort Visualizer (Frame {})".format(frame))
    
    
    if is_sorted(data):
        animation.event_source.stop()
        plt.bar(range(len(data)), data, color='green')
        plt.title("Bubble Sort Complete")



def insertion_sort_and_update(frame):
    """
    Insertion sort algorithm sorts an array with average and worst case time complexity of O(n^2).
    it works by building a sorted array by inserting elements from the unsorted section into their 
    correct positions one at a time. The 'frame' parameter in the visualization function tracks each step.
    
    PARAMETERS:
        frame (integer): An integer indicating the current frame or step in the visualization.
    RETURNS:
        N/A
    """
    plt.cla()
    if frame < len(data):
        key = data[frame]
        j = frame - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    
    plt.bar(range(len(data)), data, color='skyblue')
    plt.title("Insertion Sort Visualizer (Frame {})".format(frame))
    
    if is_sorted(data):
        animation.event_source.stop()
        plt.bar(range(len(data)), data, color='green')
        plt.title("Insertion Sort Complete")



def selection_sort_and_update(frame):
    """
    Selection Sort is a basic sorting technique that divides the array into a sorted and an unsorted section.
    It repeatedly finds the minimum element in the unsorted section and swaps it with the first element of the unsorted section.

    PARAMETERS:
        frame (integer): An integer indicating the current frame or step in the visualization.
    RETURNS:
        N/A
    """

    plt.cla()

    if frame == 0:
        i = 0
        j = i + 1

    if i < len(data) - 1:
        min_index = i

        while j < len(data):
            if data[j] < data[min_index]:
                min_index = j
            j += 1

        data[i], data[min_index] = data[min_index], data[i]
        i += 1
        j = i + 1
    else:
        plt.bar(range(len(data)), data, color='green')
        plt.title("Selection Sort Complete")

    plt.bar(range(len(data)), data, color='skyblue')
    plt.title("Selection Sort Visualizer (Frame {})".format(frame))


    if is_sorted(data):
        animation.event_source.stop()
        plt.bar(range(len(data)), data, color='green')
        plt.title("Insertion Sort Complete")



def run_animation(data, sorting_type):
    """
    runs the FuncAnimation function to start the animation,

    PARAMETERS:
        data (array): An integer array in random order.
        sorting_type (string): string with name of sorting algorithm.
    RETURNS:
        N/A
    """
    global animation
    fig, ax = plt.subplots()
    data = data
    animation = FuncAnimation(fig, sorting_type, frames=range(500), repeat=False)
    plt.show()

data = generate_random_array()
run_animation(data, selection_sort_and_update)

data = generate_random_array()
run_animation(data, bubble_sort_and_update)

data = generate_random_array()
run_animation(data, insertion_sort_and_update)


