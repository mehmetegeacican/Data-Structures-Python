from random import seed
from random import randint
from sorting_algs import *
from sorting_algs_divcon import *


#TAKING THE SIZE PARAMETER
decision = 'y'
while decision == 'y':
	val = input("Enter your value: ")
	size = int(val)
	#ARRAY DEFINITON
	A = [0]*size
	# generate some integers
	for i in range(len(A)):
		A[i] = randint(0, len(A))

	print("UNSORTED********")
	dec = input("Would you like to print the array?(y/n)")
	if dec == 'y':
		print(A)
	print("UNSORTED********\n")

	print("PRINTING THE RUNTIME OF EACH USED ALGORITHM*****************")
	print("SELECTION*******")
	selectArr = selectionSort(A)
	print("SELECTION*******\n")

	print("BUBBLE*******")
	bubbleArr = bubbleSort(A)
	print("BUBBLE*******\n")

	print("INSERTION*******")
	insertArr = insertionSort(A)
	print("INSERTION*******\n")

	print("MERGE*******")
	mergeArr = mergeSort(A)
	print("MERGE*******\n")

	print("QUICK*******")
	quickArr = quickSort(A)
	print("QUICK*******\n")

	print("HYBRID*******")
	hybArr = hybridSort(A)
	print("HYBRID*******\n")

	print("HEAP*******")
	heap = heapSort(A)
	print("HEAP*******\n")


	deci = input("Would you like to print the Array?(y/n)")
	if deci == 'y':
		print(quickArr)
	decision = input("Do you want to continue(y/n)?")




