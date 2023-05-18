import binarytree
from binarytree import tree

nodes = []

def nodes_insert():
    n = int(input("Enter elements: "))
    nodes.append(n)
    print("Element inserted ",n)

# def nodes_insert_at_beginning():
#     n=int(input("Enter the element to be inserted "))
#     nodes.insert(0,n)
#     print ("value inserted ",n)
#
# def nodes_insert_at_end():
#     n=int(input("Enter the element to be inserted "))
#     nodes.insert(len(nodes),n)
#     print ("value inserted ",n)
#
# def nodes_insert_at_specific_loc():
#     n=int(input("Enter the element to be inserted "))
#     m=int(input("Enter the index "))
#     nodes.insert(m,n)

def nodes_delete_by_element():
    n=int(input("Enter the element to be deleted: "))
    nodes.remove(n)
    print ("Item deleted",n)

# def nodes_delete_by_index():
#     n=int(input("Enter the index"))
#     nodes.pop(n)
#     print ("Item deleted at index ",n)

def nodes_delete_from_beggining():
    nodes.pop(0)
    print('Item Deleted')

# def nodes_delete_from_end():
#     nodes.pop(-1)
#     print ("Item Deleted")


def nodes_traverse():
    print(nodes)

def bin_tree_build():
    return binarytree.build(nodes)

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

binary_tree=bin_tree_build()

while (True):
    ch = int(input("Enter choice: "))

    if(ch==0):
        bin_tree_build()
    elif (ch == 1):
        nodes_insert()
    elif(ch==2):
        nodes_delete_from_beggining()
    elif(ch==3):
        nodes_delete_by_element()
    elif(ch==4):
        nodes_traverse()
    elif(ch==5):
        bin_tree_traverse()
    elif(ch==6):
        bin_tree_left()
    elif(ch==7):
        bin_tree_right()

    elif(ch==30):
        exit(0)



