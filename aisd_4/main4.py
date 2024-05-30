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
    def find_hamiltonian_cycle(self):
        path = [-1] * self.nodes
        path[0] = 0  # Start from the first node
        
        if not self._hamiltonian_cycle_util(path, 1):
            return None
        path.append(path[0])  # Make it a cycle by returning to the starting node
        return path
    def _hamiltonian_cycle_util(self, path, pos):
        if pos == self.nodes:
            if self.adjacency_matrix[path[pos - 1], path[0]] == 1:
                return True
            else:
                return False
        
        for v in range(1, self.nodes):
            if self._is_safe(v, path, pos):
                path[pos] = v
                if self._hamiltonian_cycle_util(path, pos + 1):
                    return True
                path[pos] = -1
        
        return False  
    def _is_safe(self, v, path, pos):
        if self.adjacency_matrix[path[pos - 1], v] == 0:
            return False
        if v in path:
            return False
        return True


    def adjacency_matrix_to_tikz(self, filename="graph.tex"):
        preamble = r"""
\documentclass{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1]
"""
        tikz_code = self._generate_tikz_code()
        postamble = r"""
\end{tikzpicture}
\end{document}
"""
        full_code = preamble + tikz_code + postamble

        with open(filename, "w") as file:
            file.write(full_code)

        print(f"TikZ code has been written to {filename}")

    def _generate_tikz_code(self):
        node_positions = self._generate_node_positions()
        num_nodes = self.adjacency_matrix.shape[0]
        tikz_code = ""

        # Add nodes
        for i, (x, y) in enumerate(node_positions, start=1):
            tikz_code += f"\\node[circle, draw] ({i}) at ({x:.2f}, {y:.2f}) {{{i}}};\n"

        # Add edges
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if self.adjacency_matrix[i, j] != 0:
                    tikz_code += f"\\draw ({i+1}) -- ({j+1});\n"

        return tikz_code

    def _generate_node_positions(self):
        angle_step = 2 * np.pi / self.nodes
        radius = 3
        return [(radius * np.cos(i * angle_step), radius * np.sin(i * angle_step)) for i in range(self.nodes)]



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
        
        if sys.argv[1] == "--hamilton":
            graph_generator = GraphGenerator(nodes, saturation)
            x = graph_generator.create_hamiltonian_graph()
            eulerian_cycle = graph_generator.find_eulerian_cycle()
            print("Eulerian Cycle:", eulerian_cycle)

        elif sys.argv[1] == "--non-hamilton":
            graph_generator = GraphGenerator(nodes, saturation)
            graph_generator.create_non_hamiltonian_graph()
            eulerian_cycle = graph_generator.find_eulerian_cycle()
            print("Eulerian Cycle:", eulerian_cycle)
    if "hamilton" in act:
        if sys.argv[1] == "--hamilton":
            graph_generator = GraphGenerator(nodes, saturation)
            graph_generator.create_hamiltonian_graph()
            hamiltonian_cycle = graph_generator.find_hamiltonian_cycle()
            print("Hamiltonian Cycle:", hamiltonian_cycle)

        elif sys.argv[1] == "--non-hamilton":
            graph_generator = GraphGenerator(nodes, saturation)
            graph_generator.create_non_hamiltonian_graph()
            hamiltonian_cycle = graph_generator.find_hamiltonian_cycle()
            print("Hamiltonian Cycle:", hamiltonian_cycle)

    if "export" in act:
        graph_generator.adjacency_matrix_to_tikz()
if __name__ == "__main__":
    main()
