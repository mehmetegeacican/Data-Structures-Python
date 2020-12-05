class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key 
#******INSERTION TO THE BST************************************************* 
def insertBST(root, key): 
    if root is None: 
        return Node(key) 
    else: 
        if root.val == key: 
            return root 
        elif root.val < key: 
            root.right = insertBST(root.right, key) 
        else: 
            root.left = insertBST(root.left, key) 
    return root
#***********INSERTION TO BST************************************************************
#************TRAVERSAL**************************************************************** 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
#***************LEVEL ORDER************************************************
def height(node):
    if node is None:
        return 0
    else :
        leftHeight = height(node.left)
        rightHeight = height(node.right)
        #RETURN THE LARGEST HEIGHT OF THE SUBTREES
        if leftHeight > rightHeight :
            return leftHeight+1
        else:
            return rightHeight+1
#**********************HEIGHT OF THE TREE****************************************************
#**********************FINDING THE NUMBER OF  NODES IN THE TREE*******************************
def nodeCount(root):
    if (root == None): 
        return 0
      
    res = 0
    if (root): 
        res += 1
      
    res += (nodeCount(root.left) + 
            nodeCount(root.right))  
    return res  
#**********************FINDING THE NUMBER OF NODES IN THE TREE*******************************
#**********************FINDING THE REQUIRED NUMBER OF NODES IN ORDER TO MAKE IT A FULL BINARY TREE***************
def nodesRequired(root):
    h = height(root)
    numberOfNodes = nodeCount(root)
    fullTreeNodeReq = 2**h - 1
    return fullTreeNodeReq-numberOfNodes
#**********************PRINT GIVEN LEVEL*****************************************************
def printGivenLevel(root , level):
    if root is None:
        return
    if level == 1:
        print(root.val)

    elif level > 1 :
        printGivenLevel(root.left , level-1)
        printGivenLevel(root.right , level-1)
#*******************PRINT GIVEN LEVEL*********************************************************
#*******************LEVEL ORDER TRAVERSAL***************************************************
def levelorder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root,i)  
#********* LEVEL ORDER TRAVERSAL********************************************************************
#******************************GETFULLNODES***************************************************
def getfullCount(root): 
    if root is None: 
        return 0  
    res = 0
    if (root.left and root.right): 
        res += 1
    res += (getfullCount(root.left) + 
            getfullCount(root.right))  
    return res
def fullTreeLevel(root):
    fullNode = getfullCount(root)
    h = height(root)
    for x in range(h,0,-1):
        full = 2**x-1
        if fullNode >= full:
            print("the full level tree level :",x)
            return x

#******MIRRORRING A TREE***************************************************************
def mirrorLevels(root,level):
    if root is None:
        return
    if level == 1:
        print(root.val)
    elif level > 1:
        mirrorLevels(root.right,level-1)
        mirrorLevels(root.left,level-1)

def mirrorPrint(root):
    h = height(root)
    for i in range(1,h+1):
        mirrorLevels(root,i)

def mirrorTree(root):  
    if (root is None): 
        return
    else:   
        tmp = root           
        #SUBTREE RECURSION
        mirrorTree(root.left)  
        mirrorTree(root.right)  
        #SWAPPING THE LEFT AND RIGHT
        temp = root.left  
        root.left = root.right  
        root.right = temp  
#******MIRRORING A TREE****************************************************************
#*********SEARCHING IN A BST***********************************************************
def searchBST(root,key):
    if root is None or root.val == key:
        #found = True
        #if root is None:
            #found = False
        return root
    
    if root.val < key:
        return searchBST(root.right,key)
       
    return searchBST(root.left,key)
#*********SEARCHING IN A BST***********************************************************
#***************DELETING FROM A BST****************************************************
#THE MINIMUM VALUE
def minValueNode(node):
    current = node
 
    #LEFTMOST LEAF
    while(current.left is not None):
        current = current.left
 
    return current

def deleteNodeBST(root, key):
    #NULL CASE
    if root is None:
        return root
    #RECURSION
    if key < root.val:
        root.left = deleteNodeBST(root.left, key)
    elif(key > root.val):
        root.right = deleteNodeBST(root.right, key)
    else:
        # ONLY ONE CHILD NODE
        if root.left is None:
            tmp = root.right
            root = None
            return tmp
 
        elif root.right is None:
            tmp = root.left
            root = None
            return tmp
        # NODE WITH TWO CHILDREN
        tmp = minValueNode(root.right)
        root.val = tmp.val
        root.right = deleteNodeBST(root.right, tmp.val) 
    return root
#***************DELETING FROM A BST****************************************************
"""
r = Node(50)
r = insertBST(r,40)
r = insertBST(r,60)
r = insertBST(r,30)
r = insertBST(r,55)
r = insertBST(r,45)
levelorder(r)
print("---------------------------------")
mirrorPrint(r)
print("********************************")
fullTreeLevel(r)"""
