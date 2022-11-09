# @param {Integer} n
# @return {Integer}

def climb_stairs_bf(n)
    return 0 if n < 0
    return 1 if n == 0
    return climb_stairs(n - 1) + climb_stairs(n - 2)
end

def climb_stairs_cache(n)
    cache = {
        0 => 0,
        1 => 1,
        2 => 2
    }

    def count(n, cache)
        return 0 if n < 0
        return 1 if n == 0
        return cache[n] if cache.key?(n)
        c = count(n - 1, cache) + count(n - 2, cache)
        cache[n] = c
        return c
    end

    return count(n, cache)
end

def climb_stairs(n)
    return 0 if n <= 0
    return 1 if n == 1
    return 2 if n == 2

    count = 0
    one_step = 1
    two_steps = 2

    (3..n).each {
        puts "#{n}: #{count}"
        count = one_step + two_steps
        one_step, two_steps = two_steps, count
    }

    return count
end