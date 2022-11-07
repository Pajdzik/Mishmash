require 'set'

# @param {Integer[][]} image
# @param {Integer} sr
# @param {Integer} sc
# @param {Integer} color
# @return {Integer[][]}
def flood_fill(image, sr, sc, color)
    queue = [[sr, sc]]
    visited = Set.new
    ex_color = image[sr][sc]

    while queue.length > 0 do
        r, c = *queue.pop()
        next if !(r.between?(0, image.length - 1) and c.between?(0, image[0].length))
        next if visited.include?([r, c])
        next if image[r][c] != ex_color
            
        queue << [r + 1, c]
        queue << [r, c + 1]
        queue << [r - 1, c]
        queue << [r, c - 1]

        image[r][c] = color
        visited << [r, c]
    end

    return image
end

puts flood_fill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)