# Python Course - Summer 2022
# Homework 4
# Alex Avery

# Assignment instructions:
    # For this homework you will be required to implement two di erent sorting algorithms. 
    # You can choose from the ones we covered in class (not random sort) or use your own (there are lots if you spend some time searching online).
    # The only constraint on the two that you pick is that they must be in di erent complexity classes. 
        # Most likely you will need to find something that is O(n2) and O(nlogn) but feel free to find something exotic or make up your own. 
        # You must implement the sorting algorithms yourself.
    # Once you have verified that your sorts are working properly (using tests), you will need to run a simulation and graph the results. 
    # Specifically, produce a graph with the following characteristics:
        # The vertical axis is some measure of time
        # The horizontal axis is N (size of set to sort)
        # You have one line for each sort algorithm, showing how time goes up with N
        # Everything is labeled appropriately
    # Try to pick an N such that the eff ect is visually noticeable. It should not take a very large increase to make this possible.

# import necessary modules
import matplotlib.pyplot as plt
import random
import time 

# -----------------------------------------------------------------------------

# SORTING ALGORITHM 1: BUBBLE SORT
# complexity O(n2)

# code comes from Python Course 2022 Day 8 Lecture
def bubble_sort(numbers):
    answer = numbers.copy()
    # We go through the list as many times as there are elements
    for i in range(len(answer)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(answer) - 1):
            if answer[j] > answer[j+1]:
                # Swap
                answer[j], answer[j+1] = answer[j+1], answer[j]
        print(answer)
    return answer

#test bubble sort
my_list = random.sample(range(-100, 100), 20)
bubble_sort(my_list)

# -----------------------------------------------------------------------------

# SORTING ALGORITHM 2: QUICK SORT
# complexity O(nlogn)


# Quick sort picks an element as a pivot and partitions the given array around the picked pivot. 
# There are many different options for picking a pivot. 
# But for this particular quick sort we will always choose the last element as our pivot.
# Quick sort also utilizes a pointer to keep track of elements smaller than the pivot.
# The key process in quickSort is a partition(). 
# The target of partitions is, given a list of numbers and an element x of a list as the pivot, 
# put x at its correct position in a sorted list and put all smaller elements (smaller than x) before x, 
# and put all greater elements (greater than x) after x. 
# Source: https://www.geeksforgeeks.org/quick-sort/ 

# first we set up our partition function
def partition(numbers, start, end):
    # choose our pivot (the last element)
    pivot = numbers[end]
    # assign our pointer 
    pointer = start
    for i in range(start, end):
        if numbers[i] <= pivot:
            # we move values smaller than the pivot to the front
            numbers[i], numbers[pointer] = numbers[pointer], numbers[i]
            # we increase our pointer with each swap
            pointer += 1
    # we swap the last element with the pointer
    numbers[pointer], numbers[end] = numbers[end], numbers[pointer]
    # return the pointer value 
    return pointer

# next we can create our quicksort function
# our start value will be the first index (should always be 0)
# our end value will be the last index (should be length of our list minus 1)
def quick_sort(numbers, start, end):
    if len(str(numbers)) == 1:
        return numbers
    if start < end:
        # first call partition function
        part = partition(numbers, start, end)
        # recursively sorting the left values
        quick_sort(numbers, start, part - 1)
        # recursively sorting the right values
        quick_sort(numbers, part + 1, end)
    return numbers
    
#test quick sort
my_list = random.sample(range(-100, 100), 20)
quick_sort(my_list, 0, 19)

# -----------------------------------------------------------------------------

# AVERAGE RUN TIMES

#create empty list to record bubble sort times
bubble_time = []

# getting the run times for sample sizes up to 500
for i in range(1, 500):
    random_sample = random.sample(range(-500, 500), i)
    start_time = time.time()
    bubble_sort(random_sample)
    bubble_time.append(time.time() - start_time)

# create emptty list to record quick sort times
quick_time = []
  
# getting the run times for sample sizes up to 500
for i in range(1, 500):
    random_sample = random.sample(range(-500, 500), i)
    start_time = time.time()
    quick_sort(random_sample, 0, i-1)
    quick_time.append(time.time() - start_time)  
    
# -----------------------------------------------------------------------------

# PLOTTING

# x-axis: sample size
n = range(1, 500)
# plot bubble time
plt.plot(n, bubble_time, 'r-', label = 'bubble sort time')
# plot quick time
plt.plot(n, quick_time, 'b-', label = 'quick sort time')
# implement legend if needed
plt.legend()
# add x axis label
plt.xlabel('sample size')
# add y axis label
plt.ylabel('time (seconds)')
# add plot title
plt.title("Average time of Bubble and Quick Sorting Algorithms")
# save plot 
plt.savefig('/Users/alexcisco/Library/Mobile Documents/com~apple~CloudDocs/Documents/WUSTL/Courses/Python Course/python_summer2022/HW/hw4')

  
    
    
