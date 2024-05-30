import sys
import random
import numpy as np
from collections import deque

sys.setrecursionlimit(10**6)

class GraphGenerator:
    def __init__(self, nodes, saturation):
        self.nodes = nodes
        self.saturation = saturation
        self.adjacency_matrix = np.zeros((nodes, nodes), dtype=int)

    def create_hamiltonian_graph(self):
        self._initialize_hamiltonian_cycle()
        num_edges = int((self.nodes * (self.nodes - 1) / 2) * self.saturation)
        self._add_random_edges(num_edges)
        self._ensure_even_degree()
        return self.adjacency_matrix

    def create_non_hamiltonian_graph(self):
        num_edges = int((self.nodes * (self.nodes - 1) / 2) * self.saturation)
        self._add_random_edges(num_edges)
        self._isolate_random_node()
        return self.adjacency_matrix

    def _initialize_hamiltonian_cycle(self):
        hamiltonian_cycle = list(range(self.nodes))
        random.shuffle(hamiltonian_cycle)
        for i in range(self.nodes - 1):
            self.adjacency_matrix[hamiltonian_cycle[i], hamiltonian_cycle[i + 1]] = 1
            self.adjacency_matrix[hamiltonian_cycle[i + 1], hamiltonian_cycle[i]] = 1
        self.adjacency_matrix[hamiltonian_cycle[-1], hamiltonian_cycle[0]] = 1
        self.adjacency_matrix[hamiltonian_cycle[0], hamiltonian_cycle[-1]] = 1

    def _add_random_edges(self, num_edges):
        edges_added = np.sum(self.adjacency_matrix) // 2
        while edges_added < num_edges:
            u, v = random.sample(range(self.nodes), 2)
            if u != v and self.adjacency_matrix[u, v] == 0:
                self.adjacency_matrix[u, v] = 1
                self.adjacency_matrix[v, u] = 1
                edges_added += 1

    def _ensure_even_degree(self):
        for node in range(self.nodes):
            while np.sum(self.adjacency_matrix[node]) % 2 != 0:
                neighbor = random.choice(np.nonzero(self.adjacency_matrix[node])[0])
                self.adjacency_matrix[node, neighbor] = 0
                self.adjacency_matrix[neighbor, node] = 0
                cycle_nodes = random.sample(range(self.nodes), 3)
                self.adjacency_matrix[cycle_nodes[0], cycle_nodes[1]] = 1
                self.adjacency_matrix[cycle_nodes[1], cycle_nodes[0]] = 1
                self.adjacency_matrix[cycle_nodes[1], cycle_nodes[2]] = 1
                self.adjacency_matrix[cycle_nodes[2], cycle_nodes[1]] = 1

    def _isolate_random_node(self):
        isolated_node = random.choice(range(self.nodes))
        for i in range(self.nodes):
            if self.adjacency_matrix[isolated_node, i] == 1:
                self.adjacency_matrix[isolated_node, i] = 0
                self.adjacency_matrix[i, isolated_node] = 0

    def display_adjacency_matrix(self):
        print(self.adjacency_matrix)






def main():
    global actions
    global nodes
    global saturation

    if len(sys.argv) < 2 or (sys.argv[1] != "--hamilton" and sys.argv[1] != "--non-hamilton"):
        print("Wrong argument: expected value <--hamilton> or <--non-hamilton>")
        sys.exit(1)
    
    if sys.argv[1] == "--hamilton":
        input_data = sys.stdin.read().strip().split()
        if not input_data:
            print("Error: no arguments provided")
            sys.exit(1)
        
        input_data = process_input(input_data)
        nodes = input_data[0]
        if int(nodes) <= 10:
            print("Error: Expected nodes value greater than 10")
            sys.exit(1)
        
        if len(input_data) > 1:
            saturation = input_data[1]
            if saturation != str(0.3) and saturation != str(0.7):
                print("Error: Expected saturation value of 0.3 or 0.7")
                sys.exit(1)
        else:
            print("Error: not enough arguments provided")
            sys.exit(1)
        
        try:
            nodes = int(nodes)
        except ValueError:
            print("Input data error: expected integer value for nodes")
            sys.exit(1)
        
        try:
            saturation = float(saturation)
        except ValueError:
            print("Input data error: expected float value for saturation")
            sys.exit(1)

        graph = "graph_placeholder"
        actions_start(actions, graph)
        
        print(f"nodes> {nodes}")
        print(f"saturation> {saturation}")
        
    if sys.argv[1] == "--non-hamilton":
        input_data = sys.stdin.read().strip().split('\n')
        input_data = process_input(input_data)
        saturation = 0.5
        if input_data:
            try:
                nodes = int(input_data[0])
            except ValueError:
                print("Error: invalid node number")
                sys.exit(1)
            print(f"nodes> {nodes}")
            print(f"saturation> {saturation}")
        else:
            print("Error: no nodes number")
        
        graph = "graph_placeholder"
        actions_start(actions, graph)
         
def process_input(input_data):
    action_list = []
    to_delete = []

    for index in range(len(input_data) - 1, -1, -1):
        value = input_data[index].lower()

        if value == "print" and "print" not in action_list:
            action_list.append("print")
            to_delete.extend([i for i, x in enumerate(input_data) if x.lower() == "print"])
        
        if value == "export" and "export" not in action_list:
            action_list.append("export")
            to_delete.extend([i for i, x in enumerate(input_data) if x.lower() == "export"])

        elif value == "euler" and "euler" not in action_list:
            action_list.append("euler")
            to_delete.extend([i for i, x in enumerate(input_data) if x.lower() == "euler"])

        elif value == "hamilton" and "hamilton" not in action_list:
            action_list.append("hamilton")
            to_delete.extend([i for i, x in enumerate(input_data) if x.lower() == "hamilton"])
        
    for index in sorted(set(to_delete), reverse=True):
        del input_data[index]
    
    global actions
    actions = action_list
    return input_data

def actions_start(act, graph):
    if "print" in act:
        if sys.argv[1] == "--hamilton":
            graph_generator = GraphGenerator(nodes, saturation)
            graph_generator.create_hamiltonian_graph()
            print("Hamiltonian Graph Adjacency Matrix:")
            graph_generator.display_adjacency_matrix()

        elif sys.argv[1] == "--non-hamilton":
            graph_generator = GraphGenerator(nodes, saturation)
            graph_generator.create_non_hamiltonian_graph()
            print("Non-Hamiltonian Graph Adjacency Matrix:")
            graph_generator.display_adjacency_matrix()
            
    if "euler" in act:
        print("euler")
        print(graph)
    if "hamilton" in act:
        print("hamilton")
        print(graph)
    if "export" in act:
        print("export")
        print(graph)
if __name__ == "__main__":
    main()
