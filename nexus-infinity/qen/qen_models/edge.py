class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def __str__(self):
        return "Edge between {} and {}".format(self.node1.id, self.node2.id)

# Example usage:
node1 = Node("Node 1")
node2 = Node("Node 2")
edge = Edge(node1, node2)
print("Edge:", edge)
