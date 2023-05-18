import binarytree
from binarytree import *

nodes=[]


def nodes_insert():
    n = int(input("Enter elements: "))
    nodes.append(n)
    print("Element inserted ",n)

def nodes_delete_from_beggining():
    nodes.pop(0)
    print('Item Deleted')

def bin_tree_build():
    return binarytree.build(nodes)

def bin_tree_traverse():
    print(bin_tree_build())


def bin_tree_right():
    bin=bin_tree_build()
    print(bin.right)

bin=bin_tree_build()

def bin_tree_left():
    print(bin.left)
    print(bin.right)



while(True):
    ch=int(input("Enter ch: "))

    if(ch==1):
        nodes_insert()
    elif(ch==2):
        nodes_delete_from_beggining()
    elif(ch==3):
        bin_tree_traverse()
    elif(ch==4):
        print(nodes)
    elif(ch==5):
        bin_tree_build()
    elif(ch==6):
        bin_tree_left()
    elif(ch==7):
        bin_tree_right()
    elif(ch==10):
        exit(0)
