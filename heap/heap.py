from copy import deepcopy
class BinHeap(object):
    """ Classical implementation of Heap Data Structure
        Not performing any resizing here directly since 
        we're using Python lists.
    """
    def __init__(self, comparator, arr=[]):
        self.arr = deepcopy(arr)
        self.size = len(arr)
        self.is_higher_priority = comparator
        if arr:
            self.heapify()

    def insert(self, key):
        self.arr.append(key)
        self.size += 1
        self.percolate_up(idx=self.size-1)

    def get_root(self):
        return self.arr[0]

    def delete_root(self):
        root = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop(-1)
        self.size -= 1
        self.percolate_down(idx=0)
        return root
  
    def heapify(self):
        first_nonleaf_idx = (self.size - 2) / 2
        for idx in range(first_nonleaf_idx, -1, -1):
            self.percolate_down(idx)

    def percolate_up(self, idx):
        # compare current node with the current parent
        # and if current node is of higher priority,
        # swap
        arr = self.arr
        node = arr[idx]
        p_idx = (idx - 1) / 2
        while p_idx >= 0:
            parent = arr[p_idx]
            if self.is_higher_priority(node, parent):
                arr[p_idx] = node
                arr[idx] = parent
                idx = p_idx
                p_idx = (p_idx - 1) / 2
            else:
                break

    def percolate_down(self, idx):
        # heapifying the heap rooted at idx
        node = self.arr[idx]
        first_child_idx = 2 * idx + 1
        
        while first_child_idx < self.size:
            # find which child to compare with
            priority_child_idx = first_child_idx
            second_child_idx = first_child_idx + 1
            if second_child_idx < self.size:
                if self.is_higher_priority(self.arr[second_child_idx],
                                           self.arr[first_child_idx]):
                    priority_child_idx = second_child_idx
            child = self.arr[priority_child_idx]
            # if our node is of higher priority
            # we don't need to proceed anymore
            if self.is_higher_priority(node, child):
                break
            else:
                # otherwise swap the node with child
                # and update the location, and the
                # expected location of the first child
                self.arr[idx] = child
                self.arr[priority_child_idx] = node
                idx = priority_child_idx
                first_child_idx = 2 * idx + 1


class MinBinHeap(BinHeap):
    def __init__(self, arr=[]):
        comparator = lambda x, y: x < y
        super(MinBinHeap, self).__init__(comparator, arr)

    def get_min(self):
        return self.get_root()

    def delete_min(self):
        return self.delete_root()


class MaxBinHeap(BinHeap):
    def __init__(self, arr=[]):
        comparator = lambda x, y: x > y
        super(MaxBinHeap, self).__init__(comparator, arr)

    def get_max(self):
        return self.get_root()

    def delete_max(self):
        return self.delete_root()



arr = [1, 5, 14, 2, 10, 21, 18, 3, 11, 8, 7, 12]
minheap = MinBinHeap(arr)
print minheap.arr

