#!/bin/python3
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        in_order = []
        queue = [root]

        while queue:
            node = queue.pop(0)

            in_order.append(str(node.val) if node else '-')

            if not node:
                continue

            queue.append(node.left)        
            queue.append(node.right)
        
        return ','.join(in_order)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        root_value = nodes.pop(0)
        if root_value == "-":
            return None
        root = TreeNode(int(root_value))
        queue = [root]

        while queue:
            node = queue.pop(0)
            lv = nodes.pop(0)
            if lv != "-":
                left = TreeNode(int(lv))
                node.left = left
                queue.append(left)

            rv = nodes.pop(0)
            if rv != "-":
                right = TreeNode(int(rv))
                node.right = right
                queue.append(right)
        
        return root

        
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    ser = Codec().serialize(root)
    rr = Codec().deserialize(ser)
    print(rr)