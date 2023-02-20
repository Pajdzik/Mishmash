#!/usr/bin/env ruby

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
# @return {String[]}
def binary_tree_paths(root)
    def dfs(path, result)
        node = path[-1]
        if !node
            path.pop
            return
        end

        if !node.left and !node.right
            printed_path = path.map(&:val).join("->")
            result.push(printed_path)
            path.pop
        else
            dfs([*path, node.left], result)
            dfs([*path, node.right], result) 
        end
    end

    result = []
    path = [root]
    dfs(path, result)
    
    result
end