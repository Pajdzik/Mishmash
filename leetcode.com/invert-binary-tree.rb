# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val = 0, left = nil, right = nil)
        @val = val
        @left = left
        @right = right
    end
end

# @param {TreeNode} root
# @return {TreeNode}
def invert_tree(root)
    def invert_node(node)
        return if node.nil?

        node.left, node.right = node.right, node.left
        invert_node(node.left)
        invert_node(node.right)
    end

    invert_node(root)
    return root
end