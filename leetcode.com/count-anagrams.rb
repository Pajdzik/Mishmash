#!/usr/bin/env ruby

require 'set'

$limit = 10**9 + 7

# @param {String} s
# @return {Integer}
def count_anagrams(s)
    res = 1
    s.split(" ").each do |word|
        count = permutation_count(word)
        res = (res * count) % $limit
    end

    res
end

def permutation_count(s)
    counter = Hash.new(0)

    s.each_char do |c|
        counter[c] += 1
    end

    all_permutations = factorial(s.length)
    duplicate_permutations = 1
    counter.values.each do |v|
        duplicate_permutations = modulo_multiply(duplicate_permutations, factorial(v))
    end

    modulo_multiply(all_permutations, inverse_modulo(duplicate_permutations))
end

$factorial_cache = Array.new(10**5 + 1, 0)
def factorial(n)
    return 1 if n <= 1
    return $factorial_cache[n] if $factorial_cache[n] > 0

    res = modulo_multiply(n, factorial(n-1))
    $factorial_cache[n] = res

    return res
end

def modulo_multiply(a, b)
    (a % $limit) * (b % $limit) % $limit
end

def inverse_modulo(n)
    quick_power(n, $limit - 2)
end

def quick_power(base, exponent)
    res = 1
    while exponent > 0 do
        if exponent & 1 == 1
            res = (res * base) % $limit
        end

        base = (base * base) % $limit
        exponent >>= 1
    end
    
    res
end

if __FILE__ == $0
    puts count_anagrams("too hot")
    puts count_anagrams("b okzojaporykbmq tybq zrztwlolvcyumcsq jjuowpp")
end