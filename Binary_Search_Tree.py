from __future__ import print_function
import random



class Node(object):

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    '''Insert function works as follows: 1. Checks if self.data is empty and if yes self.data = data
    2. Proceeds to check to which "child" data belongs to with recursion'''
    def insert(self, data):
        if self.data:
            if data < (self.data - 3):
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > (self.data + 3):
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    """Some functions are not useful for this particular program. (lookup,delete,compare_trees)"""
    def lookup(self, data, parent=None):
        """Lookup node containing data

        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent


    def delete(self, data):
        """Delete node containing data

        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # if node has no children, just remove it
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.data = None
            elif children_count == 1:
                # if node has 1 child
                # replace node by its child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data
            else:
                # if node has 2 children
                # find its successor
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # replace node data by its successor data
                node.data = successor.data
                # fix successor's parent node child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def compare_trees(self, node):
        """Compare 2 trees

        @param node tree to compare
        @returns True if the tree passed is identical to this tree
        """
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res


    def tree_data(self):
        """Generator to get the tree nodes data

        """
        # we use a stack to traverse the tree in a non-recursive way
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                # we are returning so we pop the node and we yield it
                node = stack.pop()
                yield node.data
                node = node.right

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.data))
            if self.right:
                self.right.inorder()

    def children_count(self):
        """Return the number of children

        @returns number of children: 0, 1, 2
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def height(self):
        return 1 + max(self.left.height() if self.left is not None else 0,
                       self.right.height() if self.right is not None else 0)


random.seed(1019336)

# BST Generation from random numbers

root = Node(random.randint(1,604800)/60)
'''The tree root is created. Essentially it is just a node and
   the only one we can directly access '''
# 60 sec * 60 min * 24 hours * 7 days = N sec/week
for i in range(0,100000,1):
    root.insert(random.randint(1,604800)/60)

# Tree Ready.

print("BST height is equal to h = " + str(root.height()) + " \nTheoretical values: \nMin height is hmin = log2(100000) = 16.6096405 "
                                                      "\nMax height is hmax = 100000")
