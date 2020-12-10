class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    #***************GET HEIGHT & GET BALANCE********************************
    def getHeight(self, root): 
        if not root: 
            return 0
        return root.height 
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right)
    #*****GETTING THE MINIMUM VALUE*****************************************
    def getMinValueNode(self, root): 
        current = root
        #LEFTMOST LEAF
        while(current.left is not None):
            current = current.left
    
        return current
    #**********************FINDING THE NUMBER OF  NODES IN THE TREE*******************************
    def nodeCount(self,root):
        if (root == None): 
            return 0
        
        res = 0
        if (root): 
            res += 1
        
        res += (self.nodeCount(root.left) + self.nodeCount(root.right))  
        return res  
    #**************ROTATIONS*************************************************
    def leftRotate(self, old_root): 
        new_root = old_root.right 
        Tmp = new_root.left 
        #ROTATION 
        new_root.left = old_root 
        old_root.right = Tmp 
        #HEIGHT UPDATE
        old_root.height = 1 + max(self.getHeight(old_root.left),self.getHeight(old_root.right)) 
        new_root.height = 1 + max(self.getHeight(new_root.left),self.getHeight(new_root.right)) 

        return new_root 
  
    def rightRotate(self, old_root): 
  
        new_root = old_root.left 
        Tmp = new_root.right 
  
        #ROTATION
        new_root.right = old_root 
        old_root.left = Tmp
        #HEIGHT UPDATE
        old_root.height = 1 + max(self.getHeight(old_root.left),self.getHeight(old_root.right)) 
        new_root.height = 1 + max(self.getHeight(new_root.left),self.getHeight(new_root.right)) 
  
        # Return the new root 
        return new_root 
    #**************INSERTION & DELETION*************************************
    def insertNodeAVLTree(self, root, key): 
        #NORMAL BST
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insertNodeAVLTree(root.left, key) 
        else: 
            root.right = self.insertNodeAVLTree(root.right, key) 
        #HEIGHT UPDATE
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
  
        #BALANCE FACTOR
        balance = self.getBalance(root) 
        #BALANCING
        #CASE 1 -LEFT LEFT
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
        #CASE 2- RIGHT RIGHT 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
        #CASE 3 LEFT RIGHT
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
        #CASE 4- RIGHT LEFT
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
    #****************DELETION*******************************************
    def deleteNodeAVLTree(self, root, key): 
        #BST DELETE
        if not root: 
            return root 
        elif key < root.val: 
            root.left = self.deleteNodeAVLTree(root.left, key) 
        elif key > root.val: 
            root.right = self.deleteNodeAVLTree(root.right, key) 
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.getMinValueNode(root.right) 
            root.val = temp.val 
            root.right = self.deleteNodeAVLTree(root.right,temp.val)
            
        if root is None: 
            return root 
        #HEIGHT UPDATE
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right)) 
        #BALANCE FACTOR
        balance = self.getBalance(root) 
        #HEIGHT BALANCING
        #CASE1-LEFT LEFT
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
        #CASE2-RIGHT RIGHT 
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
        #CASE3-LEFT RIGHT 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
        #CASE4-RIGHT LEFT
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
        return root 
    #*******************PRINTING****************************************************
    def preorder(self, root): 
        if not root: 
            return
        print("{0} ".format(root.val), end="") 
        self.preorder(root.left) 
        self.preorder(root.right)

    def postOrder(self,root):
        if not root:
            return
        self.postOrder(root.left) 
        self.postOrder(root.right)
        print("{0} ".format(root.val), end="")

    def inOrder(self,root):
        if not root:
            return
        self.inOrder(root.left)
        print("{0} ".format(root.val), end="") 
        self.inOrder(root.right)

    def levelorder(self,root):
        h = self.getHeight(root)
        for i in range(1, h+1):
            self.printGivenLevel(root,i)  
        
    def printGivenLevel(self,root,level):
        if root is None:
            return
        if level == 1:
            print("{0} ".format(root.val), end="") 

        elif level > 1 :
            self.printGivenLevel(root.left , level-1)
            self.printGivenLevel(root.right , level-1)
    #*******************PRINTING****************************************************
"""
myTree = AVLTree() 
root = None
for i in range(0,15):
    root = myTree.insertNodeAVLTree(root,i)
  

print("***************************")
myTree.inOrder(root)
  
# Delete 
key = 10
root = myTree.deleteNodeAVLTree(root, key)
print()
myTree.inOrder(root)
print()
myTree.levelorder(root)
print()
x = myTree.nodeCount(root)
print(x)
"""