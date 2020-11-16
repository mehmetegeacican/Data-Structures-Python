#THESE ARE THE SORTING ALGORITHMS THAT USE DIVIDE&CONQUER TYPE OF APPROACH
from timeit import default_timer as timer
from timeit import Timer
from sorting_algs import insertionS
#QUICKSORT
#PARTITION FUNCTION
def partition(arr, low, high):
    pivot_index = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
        
        if arr[j] <= pivot:
            pivot_index += 1
            arr[pivot_index], arr[j] = arr[j], arr[pivot_index]
 
    arr[pivot_index+1], arr[high] = arr[high], arr[pivot_index+1]
    return (pivot_index+1)

#QUICKSORT FUNCTION 
def quickS(A, low, high):
    if len(A) == 1:
        return arr
    if low < high:
        pi = partition(A, low, high)
        quickS(A, low, pi-1)
        quickS(A, pi+1, high)
#QUICKSORT MODIFICATION-- IN ORDER TO NOT ALTER THE ARRAY BUT MAKE A NEW ARRAY FROM THE SORTED ONE 
def quickSort(A):
    #DEFINING A SORTED ARRAY*********************
    sortedArray = [0]*len(A)
    #ADJUSTING THE NUMBERS TO THE LIST*************
    for i in range(len(A)):
        sortedArray[i] = A[i]

    startTime = timer()
    quickS(sortedArray,0,len(sortedArray)-1)
    endTime = timer()
    print("The time that the process took was(Quick Sort):")
    print(1000*(endTime-startTime))
    return sortedArray
#MERGE SORT************************************************************************

#MERGE FUNCTION
def merge(A, left, mid, right): 
    # create temp arrays
    n1 = mid - left + 1
    n2 = right- mid 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = A[left + i] 
  
    for j in range(0 , n2): 
        R[j] = A[mid + 1 + j] 
  
    # Merge the Left and Right Arrays
    i = 0 # Initial index of first subarray 
    j = 0 # Initial index of second subarray 
    k = left # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            A[k] = L[i] 
            i += 1
        else: 
            A[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements if there are any left
    while i < n1: 
        A[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        A[k] = R[j] 
        j += 1
        k += 1
#MERGE SORT FUNCTION
def mergeS(A,left,right):
    
    if left < right: 
  
        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        mid = (left+(right-1))//2
  
        # Sort first and second halves 
        mergeS(A, left, mid) 
        mergeS(A, mid+1, right) 
        merge(A, left, mid, right)
 
#MERGE SORT MODIFICATION--IN ORDER TO CREATE A NEW SORTED ARRAY WITH MERGE SORT
def mergeSort(A):
    #DEFINING A SORTED ARRAY*********************
    sortedArray = [0]*len(A)
    #ADJUSTING THE NUMBERS TO THE LIST*************
    for i in range(len(A)):
        sortedArray[i] = A[i]

    startTime = timer()
    mergeS(sortedArray,0,len(sortedArray)-1)
    endTime = timer()
    print("The time that the process took was(Merge Sort):")
    print(1000*(endTime-startTime))
    return sortedArray

#HYBRID SORT
def hybridS(A,low,high):
    if len(A) == 1:
        return A
    elif len(A) <= 10:
        insertionS(A)
    else:
        if low < high:
            pi = partition(A,low,high)
            quickS(A,low,pi-1)
            quickS(A,pi+1,high)

def hybridSort(A):
    #DEFINING A SORTED ARRAY*********************
    sortedArray = [0]*len(A)
    #ADJUSTING THE NUMBERS TO THE LIST*************
    for i in range(len(A)):
        sortedArray[i] = A[i]

    startTime = timer()
    hybridS(sortedArray,0,len(sortedArray)-1)
    endTime = timer()
    print("The time that the process took was(Hybrid Sort):")
    print(1000*(endTime-startTime))
    return sortedArray
Arr= [64, 25, 12, 22, 11,34,54,12,54,32,12,43,23,34,22,4,56,7,4,8,0,1,23,23345,456546,87967874,123123217,67678754,58763432,1231] 

'''
print("UNSORTED*********")
print(Arr)
print("UNSORTED********\n")

print("QUICK-SORT*********")
quickArr = quickSort(Arr)
print(quickArr)
print("QUICK-SORT********\n")

print("MERGE-SORT*********")
mergeArr = mergeSort(Arr)
print(mergeArr)
print("MERGE-SORT********\n")

print("UNSORTED*********")
print(Arr)
print("UNSORTED********\n")
'''
