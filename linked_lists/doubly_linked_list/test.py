from double_linked_list import *

llist = DoublyLinkedList()
llist.insertHead(16)
llist.insertHead("head")
llist.insertTail("Tail")
llist.insertTail("TAİL2")
llist.insertIndex(123,llist.head.next)
llist.deleteNode(llist.head.next)
llist.printList()
print("*******************")
