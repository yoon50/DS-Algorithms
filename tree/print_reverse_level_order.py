from node import Node

def print_reverse_level_order(root):
    """
    Put in the right child followed by the left child of the
    recently popped parent. Place parent in the stack.

    Once we have processed all the nodes, then 
    we will pop each element from the stack and print the data.
    """
    if root is None:
        return
    queue = [root]
    stack = []

    while len(queue):
        cnode = queue.pop(0)
        stack.append(cnode)
        if cnode.right:
            queue.append(cnode.right)
        if cnode.left:
            queue.append(cnode.left)
        
    while len(stack):
        node = stack.pop(-1)
        print node.data, 
    print



"""
        1
      /   \
     3     5
    / \
   2   9
"""

tree_root = Node(data=1)
lvl1_node0 = tree_root.left = Node(data=3)
lvl1_node1 = tree_root.right = Node(data=5)
lvl2_node0 = lvl1_node0.left = Node(data=2)
lvl2_node1 = lvl1_node0.right = Node(data=9)

# print
# 2 9 3 5 1
print_reverse_level_order(tree_root)



