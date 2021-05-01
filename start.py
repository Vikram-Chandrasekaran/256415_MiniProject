from stack_prog import Stack
from queue_prog import Queue
from binary_search_tree_prog import BST
print("___________________________")
print("Welcome to Data Structures")
print("___________________________")
while(True):
    print("Please select a data structure")
    print(" 1. Stack \n 2. Queue \n 3. Binary Search Tree \n 4. Exit")
    op = int(input())
    s = Stack()
    q = Queue()
    bst = BST(None)
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
    if(op==3):
        while(True):
            print(" 1. Add \n 2. Search \n 3. Exit\n")
            in_op = int(input())
            if(in_op==1):
                print("Enter the number to be added to the BST")
                bst.add(int(input()))
            elif(in_op==2):
                print("Enter the number to be searched in the BST")
                if(bst.search(int(input()))):
                    print("Number is found")
                else:
                    print("Number is not found")
            elif(in_op==3):
                break
    if(op==4):
        break
print("Thanks for using this application!")