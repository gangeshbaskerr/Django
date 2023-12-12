class Graph:
    def __init__(self):
        self.edge_list = {}

    def transform_edges(self):
        return [(start, end, weight) for (start, end), weight in self.edge_list.items()]

    def sort_edges(self):
        edge_tuples = self.transform_edges()
        sorted_edges = sorted(edge_tuples, key=lambda x: x[2])
        return sorted_edges