import binarytree
from binarytree import tree
from binarytree import *

node = [3,23,4,2,6,9]
node1=[3,23,4,2,6,9]

trs=binarytree.build(node)
trs2=binarytree.build(node1)
print(trs)
#print(trs.__setitem__(2,2))

print(trs.left)
print(trs.leaf_count)
print(trs2)
print(trs.__getitem__(1))
print(trs.is_perfect)
root=Node(0)
print(binarytree.get_parent(trs,trs.left.left))
print(trs.__setitem__(1,trs.left.left))
print(trs)
print(trs.height)
print(len(trs))
print(trs.size)
print(trs.leaf_count)
print(trs.inorder)
print(trs.left.is_max_heap)
trs.i
#print(trs.__delitem__(5))

