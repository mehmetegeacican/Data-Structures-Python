from avltree import *
import random

#THE TREE
size = 8000
#RANDOM TREE
myTree = AVLTree() 
root = None
#ASCENDING TREE
ascTree = AVLTree()
ascroot = None
#DESCENDING TREE
descTree = AVLTree()
descroot = None
#NODE COUNT
x = myTree.nodeCount(root)
y = ascTree.nodeCount(ascroot)
z =  descTree.nodeCount(descroot)
#SCREEN
print("--------------------------------------------")
print("Height Analysis of AVL Tree")
print("--------------------------------------------")
print("size----random----ascend----descend---")
while(x < size):
    i = random.randint(0,size*10)
    root = myTree.insertNodeAVLTree(root,i)
    x = myTree.nodeCount(root)
    hr = myTree.getHeight(root)
    ascroot = ascTree.insertNodeAVLTree(ascroot,x)
    y = ascTree.nodeCount(ascroot)
    ha = ascTree.getHeight(ascroot)
    descroot = descTree.insertNodeAVLTree(descroot,size - y)
    z = descTree.nodeCount(descroot)
    hd = descTree.getHeight(descroot)
    if z % 1000 == 0:
        print(z,"----",hr," ---- ",ha,"------",hd)
print("--------------------------------------------")