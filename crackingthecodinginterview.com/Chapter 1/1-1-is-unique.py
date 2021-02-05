# Implement an algorithm to determine if a string has all unique characters. 

def isUnique(input):
    map = {}

    for c in input:
        if c in map:
            return False
        else:
            map[c] = True

    return True

def isUnique2(input):
    input = sorted(input)

    for idx in range(len(input) - 1):
        if input[idx] == input[idx + 1]:
            return False

    return True

if __name__ == "__main__":
    input1 = "abcde"
    print(input1 + ": " + str(isUnique2(input1)))

    input1 = "ababa"
    print(input1 + ": " + str(isUnique2(input1)))
