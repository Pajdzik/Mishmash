# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    left = 0
    right = s.length - 1

    while left < right do
        if !s[left].match?(/[A-Za-z0-9]/) then
            left += 1
        elsif !s[right].match?(/[A-Za-z0-9]/) then
            right -= 1
            next
        else
        return false if s[left].downcase != s[right].downcase

        left += 1
        right -= 1
        end
    end

    return true
end
