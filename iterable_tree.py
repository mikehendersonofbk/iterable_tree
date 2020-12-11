import math

class Node: 
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

class IterableTree:
    def __init__(self, from_arr = None, root = None):
        if root is None and from_arr is not None:
            self.root = self._build_tree(sorted(from_arr))
        else:
            self.root = root

        self.it = root

    def _build_tree(self, arr):
        if len(arr) == 0 or arr == None:
            return None
        middle = math.floor(len(arr) / 2)

        root = Node(arr[middle])
        root.left = self._build_tree(arr[:middle])
        root.right = self._build_tree(arr[middle + 1:])

        return root

    def _traverse(self, root, progress = []):
        # reached leaf nodes, just return
        if root == None:
            return

        # print left child, current, right child
        # print('DEBUG:: val: {}'.format(root.val))
        # if root.left is not None:
        #     print('DEBUG:: left: {}'.format(root.left.val))
        # if root.right is not None:
        #     print('DEBUG:: right: {}'.format(root.right.val))
        self._traverse(root.left, progress)
        progress.append('{}'.format(root.val))
        self._traverse(root.right, progress)
        
    def traverse_and_print(self, delimiter = ','):
        progress = []
        self._traverse(self.root, progress)
        print(delimiter.join(progress))

    def reset_iterator(self):
        self.it = self.root

    def _next(self, root):
        if root == None:
            return

        if root.left is not None:
            yield from self._next(root.left)
        yield root.val
        if root.right is not None:
            yield from self._next(root.right)

        return

    # use a generator to yield next node in tree
    def next(self):
        for n in self._next(self.root):
            yield n


if __name__ == '__main__':
    tree = IterableTree([1, 2, 3, 4, 5])
    # print tree traversal to make sure it was built correctly
    tree.traverse_and_print()

    for val in tree.next():
        print(val)
