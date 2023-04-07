#!/usr/bin/env ruby

# @param {Integer} n
# @return {Boolean}
def is_power_of_three(n)
    return false if n <= 0
    biggest_power_of_three = 3 ** 19
    biggest_power_of_three % n == 0
end