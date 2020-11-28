from linked_list import *
import random
from timeit import default_timer as timer
import time
from math import ceil, floor
#**********************************FOR FLOATING***********************
def float_round(num, places = 0, direction = floor):
    return direction(num * (10**places)) / float(10**places)
#********************************************LINKED LIST INSERTION SORT*****************************************************************************
def linked_list_place(self,new_data):

    curr = self.head
    minimum = -1
    #ADD TO THE BEGINNING IF THERE IS NO NODE OR ONLY ONE NODE WHICH IS BIGGER THAN THE NEW NODE
    if curr is None or curr.data >= new_data:
        self.insertfromHead(new_data)
        minimum = new_data
    else:
        while curr is not None:
            #ADD THE MINIMUM NUMBER IF IT HAS BEEN ENCOUNTERED
            if(curr.next != None and
                curr.next.data >= new_data):
                    self.insertAfter(curr,new_data)
                    break
            #THE NEW NUMBER WAS BIGGER THAN THE PREVIOUS DATAS THEREFORE ADD TO THE TAIL 
            elif(curr.next is None and curr.data < new_data):
                self.insertfromTail(new_data)
                break
            curr = curr.next

def linked_list_sort(self):
    llist = LinkedList()
    curr = self.head
    startTime = timer()
    while(curr is not None):
        linked_list_place(llist,curr.data)
        curr = curr.next
    endTime = timer()
    print("The time that the process took was(Insertion Sort Linked-list):")
    print(1000*(endTime-startTime))
    return llist
#*****************************************************************LINKED LIST INSERTION SORT*****************************************************************************************
#*****************************************************************ARRAY INSERTION SORT****************************************************************************
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
    print("The time that the process took was(Insertion Sort Array):")
    print(1000*(endTime-startTime))
    return sortedArray
#ARRAY INSERTION
def insertToArrayHead(A,new_data):
    start = timer()
    new_size = len(A)+ 1
    A2 = [None]*new_size
    A2[0] = new_data
    for i in range(1,len(A)):
        A2[i] = A[i-1]
    end = timer()
    print("the insertion to Array ( Beginning) took", float_round(1000*(end-start), 5, ceil))
    return A2
def insertToTailArray(A,new_data):
    start = timer()
    new_size = len(A)+ 1
    A2 = [None]*new_size
    A2[new_size-1] = new_data
    for i in range(0,len(A)):
        A2[i] = A[i]
    end = timer()
    print("the insertion to Array(to the end) took", float_round(1000*(end-start), 5, ceil))
    return A2
def deleteFromHead(A):
    start = timer()
    new_size = len(A)-1
    A2 = [None]*new_size
    x = A[0]
    for i in range(1,len(A)):
        A2[i-1] = A[i]
    end = timer()
    print("the Deletion to Array(from the beginning) took", float_round(1000*(end-start), 5, ceil))
    return A2
def deleteFromEnd(A):
    start = timer()
    new_size = len(A)-1
    A2 = [None]*new_size
    x = A[new_size]
    for i in range(0,new_size):
        A2[i] = A[i]
    end = timer()
    print("the Deletion to Array(from the end) took", float_round(1000*(end-start), 5, ceil))
    return A2
def searchArrayIndex(A,i):
    if i < 0 or i >= len(A):
        print("Out of range,there is no index like this")
        return -1 
    return A[i]   
#*****************************************************************ARRAY INSERTION&DELETION&SEARCHBYINDEX&SORT**********************************************************************************
#*****************************************************************ARRAY MERGE SORT***************************************************************************
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
    print("The time that the process took was(Merge Sort Array):",float_round(1000*(endTime-startTime),5,ceil))
    return sortedArray
#*****************************************************************ARRAY MERGE SORT*******************************************************************************



