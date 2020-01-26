class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightSibling = None

class PairingHeap:
    def __init__(self, rootval):
        self.root = Node(rootval)

    def Merge(self, root):
        if root.value < self.root.value:
            self.root.rightSibling = root.leftChild
            root.leftChild = self.root
            self.root = root

        else:
            root.rightSibling = self.root.leftChild
            self.root.leftChild = root

        return self.root

    def Insert(self, value):
        Newnode = Node(value)
        self.Merge(Newnode)

    def FindMinimum(self):
        return self.root.value

    def ExractMinimum(self):
        stop = False
        out = self.root.value
        x = self.root.leftChild
        siblings = []
        while not stop:
            y = x.rightSibling
            x.rightSibling = None
            siblings.append(x)
            x = y
            if x == None:
                stop = True


        #pass1
        siblings2 = []
        for j in range(0, len(siblings), 2):
            x1 = siblings[j]
            try:
                x2 = siblings[j+1]
            except:
                siblings2.append(x1)
                x2 = None
            if x2 is None:
                break
            if x1.value < x2.value:
                x2.rightSibling = x1.leftChild
                x1.leftChild = x2
                siblings2.append(x1)
            else:
                x1.rightSibling = x2.leftChild
                x2.leftChild = x1
                siblings2.append(x2)

        #pass2
        for i in range(1, len(siblings2)):
            starter = 0
            if starter == 0:
                x1 = siblings2[-i]
                starter = 1
            x2 = siblings2[-(i+1)]
            if x1.value < x2.value:
                x2.rightSibling = x1.leftChild
                x1.leftChild = x2
                x1 = x1
            else:
                x1.rightSibling = x2.leftChild
                x2.leftChild = x1
                x1 = x2
        self.root = x1
        return out




    def Print(self):
        x = self.root
        print('Root Node:', end='')
        print(x.value)
        print('\r')
        def Print(node, leftchild, rightsibling):
            if leftchild is not None:
                print("'" + str(node.value) + "'", 'Left Child:', end='')
                print(leftchild.value)
                print('\r')
                Print(leftchild, leftchild.leftChild, leftchild.rightSibling)
            if rightsibling is not None:
                print("'" + str(node.value) + "'", 'Right Sibling:', end='')
                print(rightsibling.value)
                print('\r')
                Print(rightsibling, rightsibling.leftChild, rightsibling.rightSibling)
        Print(x, x.leftChild, x.rightSibling)



Ob1 = PairingHeap(3)
Ob1.Insert(1)
Ob1.Insert(2)
Ob1.Insert(4)
Ob1.Insert(5)
print('Minimum Before Extraction:')
print(Ob1.FindMinimum())
print('---------------------------')
Ob1.ExractMinimum()
Ob1.Print()
print('---------------------------')
print('Minimum After Extraction:')
print(Ob1.FindMinimum())

