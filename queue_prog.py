class Queue:
    def __init__(self):
        self.elements = []
    def enqueue(self,number):
        self.elements.insert(0,number)
    def dequeue(self):
        self.elements.pop()
    def size(self):
        print("The size of the queue is "+len(self.elements))
    def clear(self):
        while(size()!=0):
            dequeue()
        print("The queue is empty")

        