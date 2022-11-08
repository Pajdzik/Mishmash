# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Boolean}
def is_balanced(root)
    def depth(node)
        return 0 if node.nil?
        return [depth(node.left), depth(node.right)].max + 1
    end

    def balanced?(node)
        return true if node.nil?

        lh = depth(node.left)
        rh = depth(node.right)

        return false if (lh - rh).abs > 1
        return balanced?(node.left) && balanced?(node.right)
    end

    return balanced?(root)
end