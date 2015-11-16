from node import Node

def find_max_in_bintree(croot):
    _max = croot.data
    if croot.left:
        _max = max(_max, find_max_in_bintree(croot.left))
    if croot.right:
        _max = max(_max, find_max_in_bintree(croot.right))
    return _max


def find_max_in_bintree_nonrec1(root):
    # copy tree?
    stack = []
    stack.append(root)
    cmax = root.data
    
    #import pdb; pdb.set_trace()
    # alternatively we can take off the edges...
    visited = set([])
    while len(stack):
        cnode = stack[-1]
        visited.add(cnode)
        if cnode.left and cnode.left not in visited:
            stack.append(cnode.left)
        else:
            cnode = stack.pop(-1)
            cmax = max(cmax, cnode.data)
            if cnode.right and cnode.right not in visited:
                stack.append(cnode.right)
    
    return cmax


def find_max_in_bintree_nonrec2(root):
    stack = []
    stack.append(root)
    cmax = root.data
    
    #import pdb; pdb.set_trace()
    while len(stack):
        cnode = stack[-1]
        if cnode.left:
            stack.append(cnode.left)
            cnode.left = None
        else:
            cnode = stack.pop(-1)
            cmax = max(cmax, cnode.data)
            if cnode.right:
                stack.append(cnode.right)
                cnode.right = None
    
    return cmax

"""
        1
      /   \
     3     5
    / \
   2   9

def get_tree():
    tree_root = Node(data=1)
    lvl1_node0 = tree_root.left = Node(data=3)
    lvl1_node1 = tree_root.right = Node(data=5)
    lvl2_node0 = lvl1_node0.left = Node(data=2)
    lvl2_node1 = lvl1_node0.right = Node(data=9)
    return tree_root

tree_root = Node(data=1)
lvl1_node0 = tree_root.left = Node(data=3)
lvl1_node1 = tree_root.right = Node(data=5)
lvl2_node0 = lvl1_node0.left = Node(data=2)
lvl2_node1 = lvl1_node0.right = Node(data=9)
print find_max_in_bintree(tree_root) # print 9
print find_max_in_bintree_nonrec1(tree_root)
print find_max_in_bintree_nonrec2(tree_root)

"""
