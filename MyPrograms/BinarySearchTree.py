'''
The given classes can be used to created a BST, first we have to create nodes and instatiate the tree
then use the insert function to add the nodes, then the option is to simply searach or traverse in-order
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root == None:
            self.root = node
        else:
            added = False
            current = self.root
            while added != True:
                if current.data < node.data and current.right == None: # Used in case new node is larger than current and right node is empty
                    current.right = node
                    added = True
                elif current.data > node.data and current.left == None: # Used in case new node is smaller than current and left node is empty
                    current.left = node
                    added = True
                elif current.data < node.data and current.right != None:
                    current = current.right
                elif current.data > node.data and current.left != None:
                    current = current.left

    def search(self, data):
        current = self.root
        found = False
        path = []
        while found == False:
            if current.data == data:
                path.append(current.data)
                found = True
            elif current.data < data and current.right != None:
                path.append(current.data)
                current = current.right
            elif current.data > data and current.left != None:
                path.append(current.data)
                current = current.left
            elif current.data < data and current.right == None: # if  node / None means that there is no more nodes to left to check so not in
                path.append(current.data)
                path.append("Not found")
                break
            elif current.data > data and current.left == None: # if  node \ None means that there is no more nodes to right to check so not in
                path.append(current.data)
                path.append("Not found")
                break

        return path

    def in_order(self, current): # LOL recursion taken of 
        if current:
            self.in_order(current.left)
            print(current.data)
            self.in_order(current.right)


if __name__ == "__main__":
    n1 = Node(50)                                                   #   50 / 100 \ 150
    n2 = Node(100)                                                  #  25/\75    125/\175
    n3 = Node(150)                                                  # Current tree
    n4 = Node(25)                                                   # Preorder: 100,50,25,75,150,175
    n5 = Node(75)                                                   # In-order: 25,50,75,100,125,150,175
    n6 = Node(125)                                                  # Postorder: 25,75,50,125,175,150,100
    n7 = Node(175) 
    l = BSTree()
    l.insert(n2)
    l.insert(n1)
    l.insert(n3)
    l.insert(n4)
    l.insert(n5)
    l.insert(n6)
    l.insert(n7)
    print(l.in_order(n2))


