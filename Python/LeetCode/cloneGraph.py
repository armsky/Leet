"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

NOTE: To travel through a graph has two methods: BFS or DFS
"""
# NOTE: Both of these two methods need a dict to store the relationship with node and cloned_node, instead of
# a visited list in BFS/DFS

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        def DFS(input, clone):
            if input in clone:
                return clone[input]
            cloned_node = UndirectedGraphNode(input.label)
            clone[input] = cloned_node
            for neighbor in input.neighbors:
                cloned_node.neighbors.append(DFS(neighbor, clone))
            return cloned_node

        def BFS(node):
            clone = {}
            stack = [node]
            new_node = UndirectedGraphNode(node.label)
            clone[node] = new_node
            while stack:
                node = stack.pop()
                for neighbor in node.neighbors:
                    if neighbor not in clone:
                        new_neighbor = UndirectedGraphNode(neighbor.label)
                        clone[neighbor] = new_neighbor
                        clone[node].neighbors.append(new_neighbor)
                        stack.append(neighbor)
                    else:
                        clone[node].neighbors.append(clone[neighbor])
            return new_node

        return DFS(node, {}) # or return BFS(node)

solution = Solution()
print solution.cloneGraph()

