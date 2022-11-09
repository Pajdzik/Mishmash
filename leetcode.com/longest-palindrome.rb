# @param {String} s
# @return {Integer}
def longest_palindrome(s)
    map = s.chars.tally
    total_count = 0
    even_used = false

    map.each do |letter, count|
        if !even_used and count.odd? then
            total_count += 1 
            even_used = true
        end
        total_count += (count/2)*2
    end

    total_count
end
