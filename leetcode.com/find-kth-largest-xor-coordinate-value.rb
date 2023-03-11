#!/usr/bin/env ruby

# @param {Integer[][]} matrix
# @param {Integer} k
# @return {Integer}
def kth_largest_value(matrix, k)
    get_xor_array(matrix)
    get_kth_value(matrix, k)
end

def get_xor_array(matrix)
    matrix.each_with_index do |row, i|
        row.each_with_index do |col, j|
            matrix[i][j] ^= matrix[i][j-1] if j > 0
            matrix[i][j] ^= matrix[i-1][j] if i > 0
            matrix[i][j] ^= matrix[i-1][j-1] if i > 0 && j > 0
        end
    end
end

def get_kth_value(xor_array, k)
    xor_array.flatten.sort[-k]
end