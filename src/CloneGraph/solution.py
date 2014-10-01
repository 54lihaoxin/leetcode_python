# Clone Graph
# 
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
# 
# 
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
# 
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# 
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
# 
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
# 
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/


from CommonClasses import *    # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        
        if node == None:
            return None
        
        q = [node]
        duplicates = {node:UndirectedGraphNode(node.label)}
        visited = set([node])
        
        while len(q) > 0:
            n = q.pop(0)
            if n not in duplicates:
                duplicates[n] = UndirectedGraphNode(n.label)
            for neighbor in n.neighbors:
                if neighbor not in visited:                    
                    visited.add(neighbor)
                    q.append(neighbor)
                if neighbor not in duplicates:
                    duplicates[neighbor] = UndirectedGraphNode(neighbor.label)
                duplicates[n].neighbors.append(duplicates[neighbor])
                    
        return duplicates[node]
    