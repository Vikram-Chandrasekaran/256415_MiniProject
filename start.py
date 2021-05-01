from stack_prog import Stack
from queue_prog import Queue
print("___________________________")
print("Welcome to Data Structures")
print("___________________________")
while(True):
    print("Please select a data structure")
    print(" 1. Stack \n 2.Queue \n 3. Binary Search Tree \n 4. Exit")
    op = int(input())
    s=Stack()
    q=Queue()
    if(op==1):
        while(True):
            print(" 1. Push \n 2. Pop \n 3. Check size \n 4. Clear the stack 5. Exit\n")
            in_op = int(input())
            if(in_op==1):
                print("Enter the number to be pushed")
                s.push(int(input()))
            elif(in_op==2):
                s.pop()
            elif(in_op==3):
                s.size()
            elif(in_op==4):
                s.clear()
            elif(in_op==5):
                break
    if(op==2):
        while(True):
            print(" 1. Enqueue \n 2. Dequeue \n 3. Check size \n 4. Clear the queue 5. Exit\n")
            in_op = int(input())
            if(in_op==1):
                print("Enter the number to be enqueued")
                q.enqueue(int(input()))
            elif(in_op==2):
                q.dequeue()
            elif(in_op==3):
                q.size()
            elif(in_op==4):
                q.clear()
            elif(in_op==5):
                break
    # if(op==3):

    if(op==4):
        break;
print("Thanks for using this application!")