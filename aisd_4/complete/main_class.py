import random
import numpy as np

class GraphGenerator:
    def __init__(self, nodes, saturation):
        self.nodes = nodes
        self.saturation = saturation
        self.adjacency_matrix = np.zeros((nodes, nodes), dtype=int)

    def create_hamiltonian_graph(self):
        self._initialize_hamiltonian_cycle()
        num_edges = int((self.nodes * (self.nodes - 1) / 2) * self.saturation)
        additional_edges = num_edges - self.nodes 
        self._add_random_edges(additional_edges)
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
                potential_nodes = [i for i in range(self.nodes) if i != node and np.sum(self.adjacency_matrix[i]) % 2 != 0]
                if not potential_nodes:
                    continue  
                neighbor = random.choice(potential_nodes)
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
        stack = [0]
        
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
        
        if len(cycle) != np.sum(self.adjacency_matrix) // 2 + 1:
            return None

        return cycle
    
    def _is_eulerian(self):
        def is_connected():
            visited = [False] * self.nodes
            non_zero_degree_nodes = [i for i in range(self.nodes) if np.sum(self.adjacency_matrix[i]) > 0]
            if not non_zero_degree_nodes:
                return True
            
            def dfs(v):
                visited[v] = True
                for u in range(self.nodes):
                    if self.adjacency_matrix[v, u] > 0 and not visited[u]:
                        dfs(u)
            
            dfs(non_zero_degree_nodes[0])
            return all(visited[i] for i in non_zero_degree_nodes)
        
        if not is_connected():
            return False
        
        for node in range(self.nodes):
            if np.sum(self.adjacency_matrix[node]) % 2 != 0:
                return False
        
        return True
    
    def find_hamiltonian_cycle(self):
        path = [-1] * self.nodes
        path[0] = 0 
        if not self._hamiltonian_cycle_util(path, 1):
            return None
        return [x + 1 for x in path]

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