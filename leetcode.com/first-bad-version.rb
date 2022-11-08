# The is_bad_version API is already defined for you.
# @param {Integer} version
# @return {boolean} whether the version is bad
# def is_bad_version(version):

# @param {Integer} n
# @return {Integer}
def first_bad_version(n)
    lowest = 0
    highest = n

    while true do
        v = (lowest + highest) / 2
        is_bad = is_bad_version(v)
        return v if is_bad && (v == 1 || !is_bad_version(v - 1))

        if is_bad then
            highest = v - 1
        else
            lowest = v + 1
        end
    end
end