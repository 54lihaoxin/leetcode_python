
# Definition for a undirected graph node
class UndirectedGraphNode:
        
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __repr__(self):
        return '[{0}]'.format(self.label)
    
    # hxl: sample input: '{0,1,2#1,2#2,2}'
    @staticmethod
    def getGraphFromString(s):
        s = s[1:-1].split('#')
        d = {}
        root = None
        for nodeStr in s:
            nodeVal = nodeStr.split(',')[0]
            d[nodeVal] = UndirectedGraphNode(nodeVal)
            if root == None:
                root = d[nodeVal]
        for nodeStr in s:
            nodes = nodeStr.split(',')
            cur = d[nodes[0]]
            print cur.label, nodes[1:]
            for neighbor in nodes[1:]:
                cur.neighbors.append(d[neighbor])
        return root
