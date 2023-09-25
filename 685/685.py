class Solution:
    def __init__(self):
        self.parents = []

    def findRedundantDirectedConnection(self, edges):
        nodesCount = len(edges)
        self.parents = [i for i in range(nodesCount + 1)]
        conflict = -1
        cycle = -1

        def findAncestor(node):
            while self.parents[node] != node:
                node = self.parents[node]
            return node

        for i in range(nodesCount):
            edge = edges[i]
            node1, node2 = edge[0], edge[1]
            if self.parents[node2] != node2:
                conflict = i
            else:
                if conflict < 0 and cycle < 0:
                    ancestor1 = findAncestor(node1)
                    ancestor2 = findAncestor(node2)
                    if ancestor1 == ancestor2:
                        cycle = i
                self.parents[node2] = node1

        if conflict < 0:
            redundant = [edges[cycle][0], edges[cycle][1]]
            return redundant

        conflictEdge = edges[conflict]

        def containsCycle(node):
            tempNode = node
            while self.parents[node] != node:
                if self.parents[node] == tempNode:
                    return True
                node = self.parents[node]
            return False

        if containsCycle(conflictEdge[1]):
            redundant = [0, conflictEdge[1]]
            redundant[0] = self.parents[conflictEdge[1]]
            return redundant
        else:
            redundant = [conflictEdge[0], conflictEdge[1]]
            return redundant
