from random import randint
from sorting_algs import *
from sorting_algs_divcon import *



decision = 'y'
while decision == 'y':

    #ARRAY CONSTRUCTION
    val = input("Enter Array size: ")
    size = int(val)
    A = [1]*size
    for i in range(len(A)):
        A[i] = randint(0,len(A))
    #SORTING ALGORITM DECISION
    print("(1)Merge Sort\n(2)Quick Sort\n(3)Hybrid Sort\n(4)Insertion Sort\n(5)Heap Sort\n")
    sortingDec = 6
    while sortingDec > 5:
        sortingDecision = input("Which Sorting would you like to test?")
        sortingDec = int(sortingDecision)
        if sortingDec == 1:
            sortedArray = mergeSort(A)
        elif sortingDec == 2:
            sortedArray = quickSort(A)
        elif sortingDec == 3:
            sortedArray = hybridSort(A)
        elif sortingDec == 4:
            sortedArray = insertionSort(A)
        elif sortingDec == 5:
            sortedArray = heapSort(A)
        else:
            print("Please choose a number between 1 and 4\n")
    
    printDecision = input("Do you want to print the Array(y/n)")
    if printDecision == 'y':
        print(sortedArray)
    
    decision = input("Do you want to continue? (y/n) ")