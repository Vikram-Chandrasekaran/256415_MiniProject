class Stack:
    def __init__(self):
        self.elements=[]
    def push(self,number):
        self.elements.append(number)
        print(str(number)+" is pushed successfully")
    def pop(self):
        popped_element = self.elements.pop()
        print(str(popped_element)+" is popped successfully")
    def size(self):
        print("The number of elements in the stack is "+str(len(self.elements)))
    def clear(self):
        while(size()!=0):
            pop()
        print("The stack has no elements")
