#!/usr/bin/env ruby

require 'test/unit/assertions'
include Test::Unit::Assertions

# @param {Integer} n
# @return {String}
def count_and_say(n)
    sequence = [1]

    while n > 1
        new_sequence = []
        count = 1
        digit = sequence[0]

        for i in 1..sequence.length
            next_digit = sequence[i]
            if digit != next_digit
                new_sequence.append(count)
                new_sequence.append(digit)
                digit = next_digit
                count = 1
            else
                count += 1
            end
        end

        sequence = new_sequence
        n -= 1
    end

    sequence.join
end

puts count_and_say(1)
puts count_and_say(2)
puts count_and_say(3)