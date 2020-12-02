from stack import *
from queue import *

print("Hello, Welcome to Stack and Queue trial")
s = Stack()
q = Queue()
dec = 0
print("*******************************************")
print("1-Push to Stack")
print("2-Pop from Stack")
print("3-Enqueue to Queue")
print("4-Dequeue from Queue")
print("5-Print Stack")
print("6-Print Queue")
print("7-Quit")
print("*******************************************")
while(dec < 8 or dec >= 0 ):
    dec = int(input("What woul you like to do:(Please Enter desired numbers):"))
    
    if(dec == 1):
        new_data = input("What is the number or the person that you'd like to add: ")
        s.push(new_data)
    elif(dec == 2):
        s.pop()
    elif(dec == 3):
        new_data = input("What is the number or the person that you'd like to add: ")
        q.enqueue(new_data)
    elif(dec == 4):
        q.dequeue()
    elif(dec == 5):
        print("************STACK***************************")
        s.printStack()
        print("********************************************")
    elif(dec == 6):
        print("*****************QUEUE**********************")
        q.printQueue()
        print("*******************************************")
    elif(dec == 7):
        print("Thank you, Goodbye")
        print("********************************************")
        break
    else:
        print("Please put a decision number between 1 and 7")