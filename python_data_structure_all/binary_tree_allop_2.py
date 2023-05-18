import binarytree
from binarytree import tree
from binarytree import Node

nodes = [23,12,3,21,43,56,44]

binary_tree=binarytree.build(nodes)

def bin_tree_traverse():
    print(binary_tree)

def bin_tree_length():
    print("The length of the tree is: ",len(binary_tree))

def bin_tree_height():
    print("The height of the tree is: ",binary_tree.height)

def bin_tree_left():
    print("The left node of the binary tree is: ",binary_tree.left)

def bin_tree_right():
    print("The right node of the binary tree is: ",binary_tree.right)

def bin_tree_isPerfect():
    if(binary_tree.is_perfect==True):
        print("Binary tree is perfect")
    else:
        print("Binary tree is not perfect")
       # binary_tree.

def bin_tree_inorder():
    print(binary_tree.inorder)

def bin_tree_isSymmetric():
    if(binary_tree.is_symmetric==True):
        print("Binary tree is symmetric")
    else:
        print("Binary tree is not symmetric")

def bin_tree_isComplete():
    if(binary_tree.is_complete==True):
        print("Binary Tree is complete")
    else:
        print("Binary tree is not complete")

def bin_tree_isBalanced():
    if(binary_tree.is_balanced==True):
        print("Binary Tree is balanced")
    else:
        print("Bianry Tree is not balanced")

def bin_tree_isStrict():
    if(binary_tree.is_strict==True):
        print("Strict Binary Tree")
    else:
        print("Not Strict Binary Tree")

def bin_tree_isBST():
    if(binary_tree.is_bst==True):
        print("Binary Tree is BST")
    else:
        print("Bianry Tree is not BST")

def bin_tree_maxHeap():
    print("Maxheap is: ")
    if(binary_tree.left.is_max_heap==True):
        bin_tree_left()
    else:
        bin_tree_right()

def bin_tree_levels():
    print(binary_tree.levels)

def bin_tree_getItem():
    n=int(input("Enter the index: "))
    print("Element at index",n,"is: ",binary_tree.__getitem__(n))

def bin_tree_delete():
    n=int(input("Enter index to be deleted: "))
    if(n>len(binary_tree)):
        print("Not possible")
    else:
        binary_tree.__delitem__(n)
        print("Item at index",n,"deleted")

def insert_tree():
    n=int(input("Enter element: "))
    binary_tree.val=n
    print("Inserted")

# def insert_at_nodes():
#     n=int(input("Enter values for node: "))
#     Node.value=n
#     print("Inserted")






while (True):
    ch = int(input("Enter choice: "))

    if (ch == 0):
        bin_tree_traverse()
    elif(ch==1):
        bin_tree_length()
    elif(ch==2):
        bin_tree_height()
    elif(ch==3):
        bin_tree_left()
    elif(ch==4):
        bin_tree_right()
    elif(ch==5):
        bin_tree_isPerfect()
    elif(ch==6):
        bin_tree_inorder()
    elif(ch==7):
        bin_tree_isSymmetric()
    elif(ch==8):
        bin_tree_isComplete()
    elif(ch==9):
        bin_tree_isBalanced()
    elif(ch==10):
        bin_tree_isBalanced()
    elif(ch==11):
        bin_tree_isBST()
    elif(ch==12):
        bin_tree_maxHeap()
    elif(ch==13):
        bin_tree_isStrict()
    elif(ch==14):
        bin_tree_levels()
    elif(ch==15):
        bin_tree_getItem()
    elif(ch==16):
        bin_tree_delete()
    elif(ch==17):
        insert_tree()
    elif(ch==18):
        insert_at_nodes()

    elif(ch==20):
        exit(0)
    else:
        print("Wrong Choice")