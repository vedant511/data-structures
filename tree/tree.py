class TreeNode(object):
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self, item):
        if self.root is None:
            self.root = TreeNode(item)
        else:
            self._put(item, self.root)
        self.size += 1

    def _put(self, item, node):
        if item < node.data:
            if node.left is None:
                node.left = TreeNode(item, parent=node)
            else:
                self._put(item, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(item, parent=node)
            else:
                self._put(item, node.right)

    def search(self, item):
        if self.root is None:
            return False
        else:
            self._search(item, self.root)

    def _search(self, item, node):
        if node is None:
            return False
        elif item == node.data:
            return node
        elif item < node.data:
            return self._search(item, node.left)
        else:
            return self._search(item, node.right)

    def __contains__(self, item):
        if self._search(item, self.root):
            return True
        else:
            return False

    def delete(self, item):
        if self.root is None:
            return False
        elif self.size == 1 and self.root.data == item:
            pass
        # TODO: Implement the delete node procedure
