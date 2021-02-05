# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string. 

def urlify1(input):
    return input.replace(" ", "%20")

def urlify(input):
    space_count = sum(map(lambda c : 1 if c == ' ' else 0, input))
    result_len = len(input) + (space_count * 2)
    result = list('\0' * result_len)

    rdx = 0
    for idx in range(len(input)):
        if input[idx] == ' ':
            result[rdx + 0] = '%'
            result[rdx + 1] = '2'
            result[rdx + 2] = '0'
            rdx += 2
        else:
            result[rdx] = input[idx]

        rdx += 1

    return''.join(result)

if __name__ == "__main__":
    input = "a bcd e"
    print("{}: {}".format(input, urlify(input)))

    input = "abcde"
    print("{}: {}".format(input, urlify(input)))
