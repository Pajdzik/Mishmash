# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors: list['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, root: Node) -> Node:
        if not root:
            return None
        
        visited = {}

        def copy(node: Node) -> Node:
            node_copy = Node(node.val)
            visited[node_copy.val] = node_copy

            for neighbor in node.neighbors:
                neighbor_copy = visited[neighbor.val] if neighbor.val in visited else copy(neighbor)

                node_copy.neighbors.append(neighbor_copy)
                

            return node_copy

        return copy(root)

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors.append(node2)
    node1.neighbors.append(node4)

    node2.neighbors.append(node1)
    node2.neighbors.append(node3)

    node3.neighbors.append(node2)
    node3.neighbors.append(node4)

    node4.neighbors.append(node1)
    node4.neighbors.append(node2)

    clone = Solution().cloneGraph(node1)
    print(clone.val)