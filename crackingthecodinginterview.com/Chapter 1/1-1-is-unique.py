# Implement an algorithm to determine if a string has all unique characters. 

def is_unique(input):
    map = {}

    for c in input:
        if c in map:
            return False
        else:
            map[c] = True

    return True

def is_unique2(input):
    input = sorted(input)

    for idx in range(len(input) - 1):
        if input[idx] == input[idx + 1]:
            return False

    return True

if __name__ == "__main__":
    input1 = "abcde"
    print(input1 + ": " + str(is_unique2(input1)))

    input1 = "ababa"
    print(input1 + ": " + str(is_unique2(input1)))
