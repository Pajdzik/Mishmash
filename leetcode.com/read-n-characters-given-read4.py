#!/bin/python3
# https://leetcode.com/problems/read-n-characters-given-read4/

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
curr = 0
def read4(buf4: list[str]) -> int:
    global curr
    s = "ab"
    i = 0
    for i in range(curr, min(curr + 4, len(s))):
        buf4[i % 4] = s[i]
        curr += 1

    return i + 1

class Solution:
    def read(self, buf: list[str], n: int):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        bytes_read = 4
        read_total = 0

        while read_total < n and bytes_read != 0:
            buf_4 = [None] * 4
            bytes_read = read4(buf_4)

            for i in range(0, bytes_read):
                if read_total + i >= n:
                    return n

                buf[read_total + i] = buf_4[i]
            read_total += bytes_read

        return read_total
        
buf = [None] * 40
Solution().read(buf, 1)