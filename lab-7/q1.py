# Q1. Implement preoder, inorder and postorder traversal using stacks (not recursion).
# create an input file to read the graph, for e.g.:
# 5, 1, 2 # 5's left child is 1, right child is 2
# 1, 4, # 1's left child is 4
# 2, , 9 # 2's right child is 9
# 3, 6, 8
# You can use any alternative format for the graph file as well.

class TreeNode():
    def __init__(self,data):
        
        self.data = data
        self.left = None
        self.right = None

    def Leftinsert(self, leftnode):
        self.left = leftnode
    
    def Rightinsert(self, rightnode):
        self.right = rightnode
    
    def printTree(self):
        print(self.data, end=" ")
        if (self.left):
            self.left.printTree()
        if(self.right):
            self.right.printTree()
    
def preOrderTraversal(root):
    if root == None:
        return
    
    stack = []
    stack.append(root)
    
    while(len(stack)>0):

        tn = stack.pop()
        print(tn.data,end=' ')

        if tn.right != None:
            stack.append(tn.right)

        if tn.left != None:
            stack.append(tn.left)

def inOrderTraversal(root):
    if root == None:
        return
    stack = []
    tn  = root

    while True:
        if(tn != None):
            stack.append(tn)
            tn = tn.left
        elif(len(stack)>0 and tn == None):
            tn = stack.pop()

            print(tn.data, end = " ")
            tn = tn.right
        else:
            break

def postOrderTraversal(root):
    if root is None:
        return
    
    stack = []
    stack2 = []

    stack.append(root)
    while(stack):
        treenode = stack.pop()
        stack2.append(treenode)

        if(treenode.left):
            stack.append(treenode.left)

        if(treenode.right):
            stack.append(treenode.right)

    while(stack2):

        treenode = stack2.pop()

        print(treenode.data, end = " ")


g = TreeNode(1)
g1 = TreeNode(5)
g2 = TreeNode(6)
g3 = TreeNode(7)
g4 = TreeNode(8)
g5 = TreeNode(9)
g.Leftinsert(g1)
g.Rightinsert(g2)
g1.Leftinsert(g3)
g3.Rightinsert(g4)
g4.Leftinsert(g5)
print("Tree : ")
g.printTree()
print("\n")
print("Inorder travelsal : ")
inOrderTraversal(g)
print("\n")
print("Preorder travelsal : ")
preOrderTraversal(g)
print("\n")
print("Postorder travelsal : ")
postOrderTraversal(g)