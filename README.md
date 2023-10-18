# Sorting Algorithm Visualizer

This is a Python program that visualizes three different sorting algorithms: Bubble Sort, Insertion Sort, and Selection Sort. It uses the Matplotlib library to create visual representations of the sorting process.

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3.x
- Matplotlib

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you've placed the code.

3. Run the program by executing the following command:

   ```bash
   python main.py
   ```

## How It Works

- The program generates a random array of numbers between 1 and 100 and uses randomization to shuffle the order.

- It then visualizes the sorting process for three different sorting algorithms:

 - Bubble Sort: This algorithm repeatedly compares adjacent elements and swaps them if they are in the wrong order. The visualization shows how the largest unsorted element "bubbles" to the end of the array in each pass.

 - Insertion Sort: Insertion sort builds a sorted array one element at a time. It iterates through each element and inserts it into its correct position within the already sorted section of the array.

 - Selection Sort: Selection sort divides the array into a sorted and an unsorted section. It repeatedly finds the minimum element in the unsorted section and moves it to the beginning of the sorted section.

- The visualization shows the progress of the sorting algorithm frame by frame until the array is completely sorted.

