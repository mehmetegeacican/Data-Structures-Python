from bst import *
from random import randint
import random
from timeit import default_timer as timer
import time

#GENERATING A NUMBER NUMBER LIST
numList = []
while(len(numList) < 15000):
    numList.append(randint(0,15000))

print("Time Analysis of Binary Search Tree - part 1")
print("--------------------------------------------")
print("Tree Size-----------Times Elapsed")
#CONSTRUCT A TREE
r = Node(randint(0,1500))
start = timer()
for i in range(0,15000):   
    if i % 1500 == 0 and i != 0:
        end = timer()
        print("  ",i,"        ", 1000*(end-start))
    r = insertBST(r,randint(0,15000) + i)
print("--------------------------------------------")

print("Time Analysis of Binary Search Tree - part 2")
print("--------------------------------------------")
print("Tree Size-----------Times Elapsed")
#DELETE FROM THE TREE
start = timer()
for i in range(15000,0,-1):
    
    if i % 1500 == 0 and i != 15000:
        end = timer()
        print("  ",i,"        ", 1000*(end-start))
    r = deleteNodeBST(r,randint(0,15000))
print("--------------------------------------------")