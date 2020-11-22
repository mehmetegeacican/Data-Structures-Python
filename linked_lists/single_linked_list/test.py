from linked_list import *
# Start with the empty list
llist = LinkedList()
#FIRST INITIALIZATIONS
llist.head = Node("A")
second = Node("B")
third = Node("C")
llist.head.next = second; # Link first node with second
second.next = third; # Link second node with the third node
#INSERTIONS
llist.insertfromHead("D")
llist.insertfromTail("X")

llist.insertAfter(third,"Y")

#PRINTING
llist.printList()

llist.deleteHead()
llist.deleteNode("Y")
llist.deleteTail()
llist.deleteListOOP()
print("*******************")
llist.printList()
print("***********************")
for i in range(0,20):
    llist.insertfromTail(i)
llist.printList()
print("***********************")
llist.deleteList()
llist.insertfromHead(100)
for i in range(0,20):
    llist.insertfromTail(i)
print(llist.listLength())
llist.printList()
foundNode = llist.searchNode(45)
indexNode = llist.searchNode(10)
print(indexNode.data)
llist.reverse()
print("****REVERSED **")
llist.printList()