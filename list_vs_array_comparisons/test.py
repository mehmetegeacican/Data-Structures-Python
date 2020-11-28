from linked_list import *
from linked_list_sort import *
import random
from math import ceil, floor


print("HELLO WELCOME TO LIST VS ARRAY COMPARISONS")
size = input("ENTER THE SIZE OF ARRAY (SIZES OF 100 TO 5000 IS ADVISED)")
llist = LinkedList()
A = [None]*int(size)
for i in range(len(A)):
    A[i] = i + random.randint(0,len(A))
    llist.insertfromTail(random.randint(0,len(A)))

decision = True
while(decision):
    print("What do you want to compare?")
    compDec = 0
    print("1-INSERTION\n")
    print("2-DELETION\n")
    print("3-SORTING\n")
    print("4-MERGE SORT\n")
    print("5-FIND INDEX\n")
    print("6-QUIT\n")
    compDec = int(input("Your decision: "))
    if compDec == 1:
        #HEAD INSERTION
        insertToArrayHead(A,random.randint(0,len(A)))
        start = timer()
        llist.insertfromHead(random.randint(0,len(A)))
        end = timer()
        print("the insertion to the Linked List Head took", float_round(1000*(end-start), 5, ceil))
        #TAIL INSERTION
        insertToTailArray(A,random.randint(0,len(A)))
        start2 = timer()
        llist.insertfromTail(random.randint(0,len(A)))
        end2 = timer()
        print("the insertion to the Linked List Tail took", float_round(1000*(end2-start2), 5, ceil))

    elif compDec == 2:
        #HEAD DELETION
        deleteFromHead(A)
        start = timer()
        llist.deleteHead()
        end = timer()
        print("the deletion of the Linked List Head took", float_round(1000*(end-start), 5, ceil))
        #TAIL DELETION
        deleteFromEnd(A)
        start = timer()
        llist.deleteTail()
        end = timer()
        print("the deletion of the Linked List Tail took", float_round(1000*(end-start), 5, ceil))

    elif compDec == 3:
        #SORTING ARRAY
        A = insertionSort(A)
        #SORTING LIST
        llist2 = linked_list_sort(llist)
        
    
    elif compDec == 4:
        #MERGE SORT
        A = mergeSort(A)
        startMergeSort = timer()
        llist2 = llist.mergeSort_linked_list(llist.head)
        endMergeSort = timer()
        print("the merge sort of the Linked List Tail took", float_round(1000*(endMergeSort-startMergeSort), 5, ceil))
        
    elif compDec == 5:
        #SEARCHING AN INDEX IN ARRAY
        i = random.randint(0,len(A))
        start = timer()
        searchArrayIndex(A,i)
        end = timer()
        print("the search in Array took", float_round(1000*(end-start),5,ceil))
        start_list = timer()
        llist.findNodeByIndex(i)
        end_list = timer()
        print("The search in Linked List took",float_round(1000*(end_list-start_list),5,ceil))

    elif compDec == 6:
        decision = False
    
    elif compDec > 6 or compDec < 1:
        print("Please Enter a Number between 1 and 4")
        print("*************************************")
    

