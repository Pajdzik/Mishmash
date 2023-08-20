def solution(n):
    if n <= 3:
        return 1

    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    def ways(n, max_val):
        if cache[n][max_val] != -1:
            return cache[n][max_val]
        # invalid sequence (sum of sequence > n)
        if n < 0:
            return 0
        # found a valid sequence
        if n == 0:
            return 1

        count = 0
        for i in range(1, min(n, max_val) + 1):
            # i is included in the sequence, n is decreased by i
            # let's see if the rest of the sequence can be formed
            # max_val is i - 1 because we need strict monotonicity
            count += ways(n-i, i-1)

        cache[n][max_val] = count
        return count
    return ways(n, n) - 1


def test(n, expected):
    answer = solution(n)
    print(f"n: {n}, answer: {answer}, expected: {expected}")
    assert answer == expected


if __name__ == "__main__":
    test(3, 1)
    test(4, 1)
    test(5, 2)
    test(200, 487067745)

'''
3 => 1: [1]
  (2 1)

4 => 1: [1]
  (3 1)

5 => 2: [2]
  (4 1), (3 2)

6 => 3: [2 1]
  (5 1), (4 2)
  (3 2 1)

7 => 4: [3 1]
  (6 1), (5 2), (4 3)
  (4 2 1)

8 => 5: [3 2]
  (7 1), (6 2), (5 3)
  (5 2 1), (4 3 1)

9 => 7: [4 3]
  (8 1), (7 2), (6 3), (5 4)
  (6 2 1), (5 3 1), (4 3 2)

10 => 8: [4 3 1]
  (9 1), (8 2), (7 3), (6 4)
  (6 3 1), (5 4 1), (5 3 2)
  (4 3 2 1)

11 => 10: [5 4 1]
  (10 1), (9 2), (8 3), (7 4), (6 5)
  (7 3 1), (6 4 1), (6 3 2), (5 4 2)
  (5 3 2 1)

12 => 12: [5 5 2]
  (11 1), (10 2), (9 3), (8 4), (7 5)
  (8 3 1), (7 4 1), (7 3 2), (6 5 1), (6 4 2)
  (6 3 2 1), (5 4 2 1)
'''

'''
3:
#
##

---------
4:
#
#
##

---------
5:
#
#
#
##

#
##
##
---------
6:
#
#
#
#
##

#
#
##
##

#
##
###
---------
7:
#
#
#
#
#
##

#
#
#
##
##

#
##
##
##

#
#
##
###
---------
8:
#
#
#
#
#
#
##

#
#
#
#
##
##

#
#
##
##
##

#
##
##
###
---------
9:
#
#
#
#
#
#
#
##

#
#
#
#
#
##
##

#
#
#
##
##
##

#
##
##
##
##

#
#
##
##
###

#
##
###
###
---------
10:

#
#
#
#
#
#
#
#
##
91

#
#
#
#
#
#
##
##
82

#
#
#
#
##
##
##
73

#
#
##
##
##
##
64

#
##
##
##
###
541

#
#
#
#
#
##
###
'''
