class BST:
    def __init__(self,data):
        self.data=data
        self.left_node=None
        self.right_node=None
    def add(self,number):
        if self.data!=None:
            if self.data > number:
                if self.left_node==None:
                    self.left_node=BST(number)
                else:
                    self.left_node.add(number)
            else:
                if self.right_node==None:
                    self.right_node=BST(number)
                else:
                    self.right_node.add(number)
        else:
            self.data=number
    def search(self,number):
        if self.data == number:
            return True
        if number < self.data:
            if self.left_node == None:
                return False
            return self.left_node.search(number)
        if number > self.data:
            if self.right_node == None:
                return False
            return self.right_node.search(number)
