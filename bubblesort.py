import random

a = random.sample(range(1, 100), 99)


def bubbleSort(arr):
    while True:
        for index in range(len(arr) - 1):
            isSorted = True
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                isSorted = False
        if isSorted:
            return arr


print(bubbleSort(a))
