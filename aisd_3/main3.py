import sys
import random

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

    def print_adjacency_matrix(self):
        for row in self.adjacency_matrix:
            print(" ".join(map(str, row)))

    
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
        graph.print_adjacency_matrix()

if __name__ == "__main__":
    main()
