class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None
    #***************************PRINTING*********************************************
    def printList(self):
        #PRECAUTION
        if self.last is None:
            print("The list is empty")
            return
        #TRAVERSING
        tmp = self.last.next
        while tmp:
            print(tmp.data)
            tmp = tmp.next
            if tmp == self.last.next:
                break
 
#****************************************PRINTING***********************************
#****************************COUNT THE LENGTH
    def getLength(self):
        #PRECAUTION--LIST IS Null
        count = 0
        if self.last is None:
            return count
        #TRAVERSING
        node = self.last.next
        while node:
            count += 1
            node = node.next
            if node == self.last.next:
                return count
#***************************************ADDITION***************************************
    #ADDITION TO THE EMPTY LIST
    def addtoEmptyList(self,new_data):
        #PRECAUTION
        if self.last is not None:
            return self.last

        #CONSTRUCTION OF THE NEW NODE
        new_node = Node(new_data)
        self.last = new_node

        #CREATING THE CIRCULAR LINK
        self.last.next = self.last
        return self.last
    #ADDITION TO THE BEGINNING OF THE LIST
    def addToBeginning(self,new_data):
        #PRECAUTIONS
        if(self.last == None):
            self.addtoEmptyList(new_data)
        else:
            #CONSTRUCTION OF THE NEW NODE
            new_node = Node(new_data)
            #PLACING
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node
 
            return self.last
    
    #ADDING AFTER A SPECIFIC ONE
    def addAfter(self,prev_data,new_data):
        #PRECAUTION
        if (self.last == None):
            return None
        #CONSTRUCTION OF THE NEW NODE
        new_node = Node(new_data)
        tmp = self.last.next

        while tmp:
            if (tmp.data == prev_data):
                new_node.next = tmp.next
                tmp.next = new_node
 
                if (tmp == self.last):
                    self.last = new_node
                    return self.last
                else:
                    return self.last
            tmp = tmp.next
            if (tmp == self.last.next):
                print(prev_data, "is not present in the list")
                break
#***********************DELETION********************************************
#DELETING THE HEAD
    def deleteHead(self):
        prev = self.last
        nxt = self.last
        #tmp = self.last

        #PRECAUTION
        if prev is None:
            print("List is empty")
            return None
        #PRECAUTION-ONE NODE ONLY
        if prev.next is None:
            self.head = None
            return None
        #TRAVERSING
        while(prev.next != self.last):
            prev = prev.next
            nxt = prev.next
        # NOW PREVIOUS IS THE LAST NODE  
        # NOW NXT IS THE HEAD OF THE CIRCULAR LINKED LIST
        # SKIP THE HEAD TO ADJUST IT
        #tmp is for memory management if you require
        #prev.next = tmp
        prev.next = nxt.next
  
        #ADJUST THE HEAD NODE
        self.last = prev.next

        return self.last
#DELETING THE DESIRED NODE
    def deleteNode(self,del_node_data):
        prev = self.last
        nxt = self.last
        #PRECAUTION
        if prev is None:
            print("List is empty")
            return None
        #IF THE DESIRED NODE WAS THE LAST/HEAD
        if(prev.data == del_node_data):
            self.deleteHead()
            return self.last
        #TRAVERSING
        while(prev is not None):
            if(prev.next.data == del_node_data):
                prev.next = nxt.next
                return self.last
            prev = prev.next
            nxt = prev.next
        return self.last
            
        




 
