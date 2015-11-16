from node import Node

def get_height_of_bintree(croot):
    if croot is None:
        return -1
    return 1 + max(
        get_height_of_bintree(croot.left),
        get_height_of_bintree(croot.right))

def get_height_of_bintree_nonrec1(root):
    # using stack implementation
    if root is None:
        return -1
    
    max_height = 0
    clvl = 0
    stack = [root]
    while len(stack):
        cnode = stack[-1]
        if cnode.left:
            stack.append(cnode.left)
            clvl += 1
            cnode.left = None
        else:
            cnode = stack.pop(-1)
            max_height = max(max_height, clvl)
            clvl -= 1
            if cnode.right:
                stack.append(cnode.right)
                clvl += 1
                cnode.right = None
    return max_height 


def get_height_of_bintree_nonrec2(root):
    if root is None:
        return -1
    # Level order search version...
    queue = [root]
    lvl = 0
    count = 1

    # import pdb; pdb.set_trace()
    while len(queue):
        next_count = 0
        for i in range(count):
            node = queue.pop(-1)
            if node.left:
                queue.append(node.left)
                next_count += 1
            if node.right:
                queue.append(node.right)
                next_count += 1
        if next_count:
            lvl += 1
            count = next_count
    
    return lvl



def get_height_of_bintree_nonrec3(root):
    """Level order traversal with marker for end of level"""
    if root is None:
        return -1
    queue = [root, None]
    lvl = 0

    while len(queue):
        # go through the queue
        # when we encounter None object (end of level marker)
        # we have finished processing that level
        # if we have any remaining nodes in the next level
        # then we also append the level marker and increment level
        node = queue.pop(0)
        if node is None:
            if len(queue):
                queue.append(None)
                lvl += 1
        else:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return lvl


"""
        1
      /   \
     3     5
    / \
   2   9
"""

def get_tree():
    tree_root = Node(data=1)
    lvl1_node0 = tree_root.left = Node(data=3)
    lvl1_node1 = tree_root.right = Node(data=5)
    lvl2_node0 = lvl1_node0.left = Node(data=2)
    lvl2_node1 = lvl1_node0.right = Node(data=9)
    return tree_root

print get_height_of_bintree(get_tree()) # 2
print get_height_of_bintree_nonrec1(get_tree()) #2
print get_height_of_bintree_nonrec2(get_tree()) #2
print get_height_of_bintree_nonrec3(get_tree()) #2
