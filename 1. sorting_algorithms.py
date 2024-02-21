import sys, time
from random import randint
# In order to create a functional table, we installed the "tabulate" package from Python Packages.
# !pip install tabulate
from tabulate import tabulate

sys.setrecursionlimit(10 ** 7)


# Class for all the Sorting Algorithms that will be used for this exercise
class Sorting:
    def __init__(self, test_list):
        self.test_list = test_list


    # Swap two values in a list
    def swap(self, list_to_swap, A, B):
        tempo = list_to_swap[A]
        list_to_swap[A] = list_to_swap[B]
        list_to_swap[B] = tempo


    #Selection sort
    def selection_sort(self, list_to_sort=None):
        if list_to_sort is None:
            list_to_sort = [value for value in self.test_list]

        for index in range(len(list_to_sort)):
            min_index = index
            for index_element in range(index + 1, len(list_to_sort)):
                if list_to_sort[index_element] < list_to_sort[min_index]:
                    min_index = index_element
            self.swap(list_to_sort, min_index, index)

        # return list_to_sort


    # Bubble sort
    def bubble_sort(self, list_to_sort=None):
        if list_to_sort is None:
            list_to_sort = [value for value in self.test_list]

        for list_index in range(len(list_to_sort) - 1):
            swapped = False
            for element_index in range(0, len(list_to_sort) - 1):
                if list_to_sort[element_index] > list_to_sort[element_index + 1]:
                    self.swap(list_to_sort, element_index, element_index + 1)
                    swapped = True
            if not swapped:
                break

        # return list_to_sort


    # Insertion sort
    def insertion_sort(self, list_to_sort=None):
        if list_to_sort is None:
            list_to_sort = [value for value in self.test_list]

        for i in range(1, len(list_to_sort)):
            sort_value = list_to_sort[i]
            while list_to_sort[i - 1] > sort_value and i > 0:
                self.swap(list_to_sort, i, i - 1)
                i = i - 1

        # return list_to_sort

    # Merge Sort
    def merge(self, left_list, right_list):
        result = []
        i = j = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                result.append(left_list[i])
                i += 1
            else:
                result.append(right_list[j])
                j += 1
        result.extend(left_list[i:])
        result.extend(right_list[j:])
        return result


    def merge_sort(self, list_to_sort=None):
        if list_to_sort is None:
            list_to_sort = [value for value in self.test_list]

        if len(list_to_sort) == 1:
            return list_to_sort

        middle = len(list_to_sort) // 2
        left = self.merge_sort(list_to_sort[:middle])
        right = self.merge_sort(list_to_sort[middle:])
        return self.merge(left, right)
        # return list_to_sort

    # Quick sort
    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                self.swap(arr, i, j)

        self.swap(arr, i + 1, high)
        return i + 1


    def quick_sort(self, low, high, list_to_sort=None):
        if list_to_sort is None:
            list_to_sort = [value for value in self.test_list]

        if len(list_to_sort) == 1:
            return list_to_sort

        if low < high:
            pi = self.partition(list_to_sort, low, high)
            self.quick_sort(low, pi - 1, list_to_sort)
            self.quick_sort(pi + 1, high, list_to_sort)

        # return list_to_sort


    # Radix sort
    def counting_sort(self, list_to_sort, exp):  # n + k
        output = [0] * len(list_to_sort)
        count = [0] * 10

        for i in range(0, len(list_to_sort)):
            index = list_to_sort[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = len(list_to_sort) - 1
        while i >= 0:
            index = list_to_sort[i] // exp
            output[count[index % 10] - 1] = list_to_sort[i]
            count[index % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, len(list_to_sort)):
            list_to_sort[i] = output[i]

        # return list_to_sort


    def radix_sort(self, list_to_sort=None):  # n*log(n)
        if list_to_sort is None:
            list_to_sort = [value for value in self.test_list]

        maximum = max(list_to_sort)
        exp = 1
        while maximum / exp >= 1:
            self.counting_sort(list_to_sort, exp)
            exp *= 10

        negative_numbers = []
        for index in range(len(list_to_sort) - 1, -1, -1):
            if "-" in str(list_to_sort[index]):
                negative_numbers.insert(0, list_to_sort[index])
                list_to_sort.remove(list_to_sort[index])

        list_to_sort = negative_numbers + list_to_sort
        # return list_to_sort

        # Credits for Radix Sort:
        # This code was adapted from Mohit Kumra and Patrick Gallagher's one.
        # https://www.geeksforgeeks.org/radix-sort/


    # Shell sort
    def shell_sort(self, list_to_sort=None):
        if list_to_sort is None:
            list_to_sort = [value for value in self.test_list]

        gap = len(list_to_sort) // 2
        while gap > 0:
            iteration = gap

            while iteration < len(list_to_sort):
                index = iteration - gap

                while index >= 0:
                    if list_to_sort[index + gap] > list_to_sort[index]:
                        break
                    else:
                        self.swap(list_to_sort, index + gap, index)

                    index -= gap

                iteration += 1

            gap = gap // 2

        # return list_to_sort

        # Credits for Shell Sort:
        # This code was adapted from Illion's one.
        # https://www.geeksforgeeks.org/shellsort/


    # Heap Sort
    def heapify(self, list_to_sort, length, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < length and list_to_sort[largest] < list_to_sort[left]:
            largest = left

        if right < length and list_to_sort[largest] < list_to_sort[right]:
            largest = right

        if largest != i:
            self.swap(list_to_sort, i, largest)
            self.heapify(list_to_sort, length, largest)


    def heap_sort(self, list_to_sort=None):
        if list_to_sort is None:
            list_to_sort = [value for value in self.test_list]

        length = len(list_to_sort)

        for i in range(length // 2 - 1, -1, -1):
            self.heapify(list_to_sort, length, i)

        for j in range(length - 1, 0, -1):
            self.swap(list_to_sort, j, 0)
            self.heapify(list_to_sort, j, 0)

        # return list_to_sort

        # Credits for Heap Sort:
        # This code was adapted from Mohit Kumra's one.
        # https://www.geeksforgeeks.org/heap-sort/


# Define user inputs, such as the initial size, the increment and
# the number of iterations.
initial_list_size = int(input("Insert initial size:\t"))
incremental_size = int(input("\nInsert incremental size:\t"))
number_iterations = int(input("\nInsert number of iterations:\t"))

# Create the random list with the initial size, with numbers from 0 to 50 as test.
random_list = [randint(-10000, 10000) for i in range(initial_list_size)]

# Create a list with the row names for tabulate.
# In it, we will store the name of the sorts and, further, their respective times.
# Algorithm refers to the sample size.
row_names = [["Algorithm"], ["Insertion sort"], ["Bubble sort"], ["Selection sort"],
             ["Merge sort"], ["Quick sort"], ["Radix sort"], ["Shell sort"], ["Heap sort"]]

# Create a list with the column names for tabulate.
# We start with Iteration and follow up with the list of instances, from 1 to the established n_int.
col_names = ["Iteration"] + [str(i) for i in range(1, number_iterations + 1)]

# Run all methods and time them.
for i in range(number_iterations):

    list_timed = Sorting(random_list)
    size = len(random_list)

    # Append the sample size to row_names, in the Algorithms list.
    row_names[0].append(str(size))

    start = time.time()
    list_timed.insertion_sort()
    row_names[1].append(f"{round(time.time() - start, 4)} sec")

    start = time.time()
    list_timed.bubble_sort()
    row_names[2].append(f"{round(time.time() - start, 4)} sec")

    start = time.time()
    list_timed.selection_sort()
    row_names[3].append(f"{round(time.time() - start, 4)} sec")

    start = time.time()
    list_timed.merge_sort()
    row_names[4].append(f"{round(time.time() - start, 4)} sec")

    start = time.time()
    list_timed.quick_sort(0, size - 1)
    row_names[5].append(f"{round(time.time() - start, 4)} sec")

    start = time.time()
    list_timed.radix_sort()
    row_names[6].append(f"{round(time.time() - start, 4)} sec")

    start = time.time()
    list_timed.shell_sort()
    row_names[7].append(f"{round(time.time() - start, 4)} sec")

    start = time.time()
    list_timed.heap_sort()
    row_names[8].append(f"{round(time.time() - start, 4)} sec")

    # Add the increment to the random_list for each instance
    random_list += [randint(-10000, 10000) for a in range(incremental_size)]

# Print the table from tabulate.
# The rows are derived from row_names, and the columns are derived from col_names.
print("\nRESULTS:\n", tabulate(row_names, headers=col_names))