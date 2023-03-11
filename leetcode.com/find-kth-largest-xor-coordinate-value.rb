#!/usr/bin/env ruby

'''
You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the kth largest value (1-indexed) of all the coordinates of matrix.
'''

'''
5 2
1 6

The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
'''

# @param {Integer[][]} matrix
# @param {Integer} k
# @return {Integer}
def kth_largest_value(matrix, k)
    xor_array = get_xor_array(matrix)
    get_kth_value(xor_array, k)
end

def get_xor_array(matrix)
    res = Array.new(matrix.length) { Array.new(matrix[0].length, 0) }
    matrix.each_with_index do |row, i|
        row.each_with_index do |col, j|
            if i == 0 && j == 0
                res[i][j] = matrix[i][j]
            elsif i == 0
                res[i][j] = res[i][j-1] ^ matrix[i][j]
            elsif j == 0
                res[i][j] = res[i-1][j] ^ matrix[i][j]
            else
                res[i][j] = res[i-1][j] ^ res[i][j-1] ^ res[i-1][j-1] ^ matrix[i][j]
            end
        end
    end
    res
end

def get_kth_value(xor_array, k)
    xor_array.flatten.sort[-k]
end