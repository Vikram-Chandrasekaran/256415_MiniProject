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
