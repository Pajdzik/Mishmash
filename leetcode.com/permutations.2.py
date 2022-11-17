class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def generate_permutation(sequence: list[int], visited: list[bool]):
            if len(sequence) == len(nums):
                result.append(sequence.copy())
            else:
                for i, num in enumerate(nums):
                    if not visited[i]:
                        new_sequence = [*sequence, num]
                        new_visited = visited.copy()
                        new_visited[i] = True
                        generate_permutation(new_sequence, new_visited)

        generate_permutation([], [False for _ in range(len(nums))])

        return result
    
if __name__ == "__main__":
    Solution().permute([1, 2, 3])