from heightAnalysis import *
from avltree import *

myTree = AVLTree()
root = None
print("****INSERTION AND DELETION****")
print()
numbers = [5, 10, 15, 60, 8,40, 2, 30, 17, 12, 74]
for number in numbers:
    root = myTree.insertNodeAVLTree(root,number)

print("----THE PRE ORDER AFTER INSERTION----")
myTree.preorder(root)
print()

deletions = [30, 10, 8, 74, 5]

for deletion in deletions:
    root = myTree.deleteNodeAVLTree(root,deletion)

print("----THE PRE ORDER AFTER DELETION-----")
myTree.preorder(root)