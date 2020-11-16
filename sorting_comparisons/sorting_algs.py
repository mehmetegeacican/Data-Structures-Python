from timeit import default_timer as timer
import time
#Selection Sort--THE SORTING ALGORITHM
def selectionS(A):
    # TRAVERSING THROUGH ALL ELEMENTS**************
    for i in range(len(A)):         
        #INDING THE MINIMUM ELEMENT IN UNSORTED ARRAY**************
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
        #SWAP        
        A[i], A[min_idx] = A[min_idx], A[i]
    return A
#SELECTION SORT MODIFICATION-- IN ORDER TO NOT ALTER THE ARRAY BUT MAKE A NEW ARRAY FROM THE SORTED ONE 
def selectionSort(A):
    #DEFINING A SORTED ARRAY*********************
    sortedArray = [0]*len(A)
    #ADJUSTING THE NUMBERS TO THE LIST*************
    for i in range(len(A)):
        sortedArray[i] = A[i]
    startTime = timer()

    selectionS(sortedArray)

    endTime = timer()
    print("The time that the process took was(Selection Sort):")
    print(1000*(endTime-startTime))
    return sortedArray
#Bubble Sort -- THE SORTING ALGORITHM
def bubbleS(A):    
    # TRAVERSE THROUGH ALL ELEMENTS
    for i in range(len(A)): 
        swapped = False
        for j in range(0, len(A)-i-1): 
            if A[j] > A[j+1] : 
                A[j], A[j+1] = A[j+1], A[j] 
                swapped = True
        if not swapped: 
            break
    return A
#BUBBLE OSRT MODIFICATION -- IN ORDER TO RETURN A SORTED ARRAY WITHOUT MODIFYING THE UNSORTED ONE
def bubbleSort(A):
    #DEFINING A SORTED ARRAY*********************
    sortedArray = [0]*len(A)
    #ADJUSTING THE NUMBERS TO THE LIST*************
    for i in range(len(A)):
        sortedArray[i] = A[i]
    startTime = timer()
    bubbleS(sortedArray)
    endTime = timer()
    print("The time that the process took was(Bubble Sort):")
    print(1000*(endTime-startTime))
    return sortedArray
#Insertion Sort -- THE SORTING ALGORITHM
def insertionS(A): 
    # Traverse through 1 to len(arr) 
    
    for i in range(1, len(A)): 
        key = A[i]

        #SHIFTING 
        j = i-1
        while j >= 0 and key < A[j] : 
                A[j + 1] = A[j] 
                j = j -1 
        A[j + 1] = key
    return A
#INSERTION SORT MODIFICATION -- IN ORDER TO RETURN A SORTED ARRAY WITHOUT MODIFYING THE GIVEN ONE
def insertionSort(A):
    #DEFINING A SORTED ARRAY*********************
    sortedArray = [0]*len(A)
    #ADJUSTING THE NUMBERS TO THE LIST*************
    for i in range(len(A)):
        sortedArray[i] = A[i]
    startTime = timer()
    insertionS(sortedArray)
    endTime = timer()
    print("The time that the process took was(Insertion Sort):")
    print(1000*(endTime-startTime))
    return sortedArray
#HEAP SORT -- A MORE EFFICIENT ALGORITHM
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapS(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

def heapSort(A):
    #DEFINING A SORTED ARRAY*********************
    sortedArray = [0]*len(A)
    #ADJUSTING THE NUMBERS TO THE LIST*************
    for i in range(len(A)):
        sortedArray[i] = A[i]
    startTime = timer()
    heapS(sortedArray)
    endTime = timer()
    print("The time that the process took was(Heap Sort):")
    print(1000*(endTime-startTime))
    return sortedArray
