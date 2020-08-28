""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkNode(node, min, max):
    if node == None:
        return True

    if not (min < node.data < max):
        return False

    return checkNode(node.left, min, node.data) and checkNode(node.right, node.data, max)

def checkBST(node):
    return checkNode(node, -99999, 99999)