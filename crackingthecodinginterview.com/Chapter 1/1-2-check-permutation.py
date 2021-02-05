# Given two strings, write a method to decide if  one is a permutation of the other.

def is_permutation1(word, other_word):
    sorted_word = sorted(word)
    sorted_other_word = sorted(other_word)

    return sorted_word == sorted_other_word

def is_permutation(word, other_word):
    hist = get_histogram(word)
    other_hist = get_histogram(other_word)

    for key in hist.keys():
        if key not in other_hist or hist[key] != other_hist[key]:
            return False

    return True

def get_histogram(word):
    hist = {}
    
    for c in word:
        if c in hist:
            hist[c] = hist[c] + 1
        else:
            hist[c] = 1

    return hist


if __name__ == "__main__":
    input1 = "abcde"
    input2 = "abcee"
    print("{}, {}: {}".format(input1, input2, is_permutation(input1, input2)))

    input1 = "abcde"
    input2 = "ecbad"
    print("{}, {}: {}".format(input1, input2, is_permutation(input1, input2)))
