#!/bin/python3
# https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        cache = { }

        for path_data in paths:
            data = path_data.split(' ')

            parent_dir = data[0]

            for i in range(1, len(data)):
                file_name, file_content = data[i].split('(')
                file_content = file_content.removesuffix(")")

                full_path = parent_dir + "/" + file_name
                if file_content in cache:
                    cache[file_content].append(full_path)
                else:
                    cache[file_content] = [ full_path ]

        result = []
        for paths in cache.values():
            if len(paths) > 1:
                result.append(paths)

        return result

if __name__ == "__main__":
    assert(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]) \
        == [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]])
        