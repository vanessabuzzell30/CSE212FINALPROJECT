class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes

    def findv(self, lookval):
        if lookval < self.data:
            if self.left is None:
                return str(lookval)+" is not Found"
            return self.left.findv(lookval)
        elif lookval > self.data:
            if self.right is None:
                return str(lookval)+" is not Found"
            return self.right.findv(lookval)
        else:
            return str(self.data) + " is found"
# Print the tree

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
print(root.findv(7))
print(root.findv(14))
# output shoud be 7 is not Found and 14 is found
