import sys
import random
import numpy as np

sys.setrecursionlimit(10**6)

class DirectedGraph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, source, target):
        self.adjacency_matrix[source][target] = 1

    def has_cycle(self):
        visited = [False] * self.num_nodes
        stack = [False] * self.num_nodes

        for node in range(self.num_nodes):
            if not visited[node]:
                if self.has_cycle_util(node, visited, stack):
                    return True
        return False

    def has_cycle_util(self, node, visited, stack):
        visited[node] = True
        stack[node] = True

        for neighbor in range(self.num_nodes):
            if self.adjacency_matrix[node][neighbor] == 1:
                if not visited[neighbor]:
                    if self.has_cycle_util(neighbor, visited, stack):
                        return True
                elif stack[neighbor]:
                    return True

        stack[node] = False
        return False

    def generate_tree(self):
        # Tworzenie drzewa - łączenie losowych wierzchołków w sposób zapewniający acykliczność
        nodes_to_visit = list(range(1, self.num_nodes))
        random.shuffle(nodes_to_visit)

        for node in nodes_to_visit:
            parent = random.choice(range(node))
            self.add_edge(parent, node)

    def adjacency_matrix_as_numpy(self):
        return np.array(self.adjacency_matrix)

    
def main():
    

    if  sys.argv[1] != "--generate" and sys.argv[1] != "--user-provided":
        print("Wrong argument: expected value <--argument> or <--user-provided>")
        sys.exit(1)
    

    if sys.argv[1] == "--generate":
        input_data = []
        input_data = sys.stdin.read().split()
        if not input_data[0]:
            print("Error: no arguments provided")
            sys.exit(1)
        nodes = input_data[0]
        if len(input_data) > 1:
            saturation = input_data[1]
        else:
            print("Input data error: expected value for saturation")
        print("nodes> " + nodes)
        if saturation:
            print("saturation> " + saturation)
        nodes = int(nodes)
        saturation = int(saturation)
        graph = DirectedGraph(nodes)
        graph.generate_tree()
        adjacency_matrix = graph.adjacency_matrix_as_numpy()
        print(adjacency_matrix)

    if sys.argv[1] == "--user-provided":
        input_data = sys.stdin.read().strip().split('\n')
        nodes = len(input_data)
        graph = DirectedGraph(nodes)
        for i, line in enumerate(input_data):
            successors = list(map(int, line.split()))
            for successor in successors:
                graph.add_edge(i, successor-1)  # Subtracting 1 to adjust to 0-based indexing

        adjacency_matrix = graph.adjacency_matrix_as_numpy()
        print(adjacency_matrix)

if __name__ == "__main__":
    main()
