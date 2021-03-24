#!/usr/bin/env python3

# Given a reai number between 0 and 1 (e.g., 0.72) that is passed in as a double,
# print the binary representation. If the number cannot be represented accurately
# in binary with at most 32 characters, print "ERROR."

def double_to_string(d):
    res = ["0."]

    while d > 0:
        if len(res) > 32:
            return "Error"

        d = d * 2

        if d >= 1.0:
            res.append("1")
            d -= 1
        else:
            res.append("0")

    return "".join(res)

def run_and_print(n):
    print("{}: {}".format(n, double_to_string(n)))

if __name__ == "__main__":
    run_and_print(0.5)
    run_and_print(0.8)
    run_and_print(0.75)
    run_and_print(0.99)
    run_and_print(0.625)