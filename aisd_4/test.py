import numpy as np
import random

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

    def find_eulerian_cycle(self):
        if not self._is_eulerian():
            return None
        
        adj_matrix_copy = self.adjacency_matrix.copy()
        cycle = []
        stack = [0]  # Start from the first node
        
        while stack:
            u = stack[-1]
            found_edge = False
            for v in range(self.nodes):
                if adj_matrix_copy[u, v] > 0:
                    stack.append(v)
                    adj_matrix_copy[u, v] -= 1
                    adj_matrix_copy[v, u] -= 1
                    found_edge = True
                    break
            if not found_edge:
                cycle.append(stack.pop())
        
        return cycle

    def _is_eulerian(self):
        for node in range(self.nodes):
            if np.sum(self.adjacency_matrix[node]) % 2 != 0:
                return False
        return True

# Przykład użycia
nodes = 6
saturation = 0.5
graph_gen = GraphGenerator(nodes, saturation)
graph_gen.create_hamiltonian_graph()
graph_gen.display_adjacency_matrix()
eulerian_cycle = graph_gen.find_eulerian_cycle()
print("Eulerian Cycle:", eulerian_cycle)
