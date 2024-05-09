import sys
import random
import numpy as np
from collections import deque
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
    def breath_first_traversal(self):
        # Find the first node with outgoing edges to use as the root, adjusted for 1-based indexing
        start_node = None
        for i in range(1, self.num_nodes + 1):
            if any(self.adjacency_matrix[i - 1]):  # Adjust index for 0-based internal representation
                start_node = i
                break

        if start_node is None:
            return []  # No suitable root node found, return empty list

        visited = [False] * (self.num_nodes + 1)  # Adjust size for 1-based indexing
        traversal_order = []
        queue = deque()
        queue.append(start_node)
        visited[start_node] = True

        while queue:
            current_node = queue.popleft()
            traversal_order.append(current_node)

            for neighbor in range(1, self.num_nodes + 1):  # Adjust loop for 1-based indexing
                if self.adjacency_matrix[current_node - 1][neighbor - 1] == 1 and not visited[neighbor]:  # Adjust indices for 0-based internal representation
                    queue.append(neighbor)
                    visited[neighbor] = True

        return traversal_order   

    def kahn_topological_sort(self):
        # Calculate in-degree for each node
        in_degree = [0] * (self.num_nodes + 1)  # Adjust size for 1-based indexing
        for i in range(1, self.num_nodes + 1):
            for j in range(1, self.num_nodes + 1):
                if self.adjacency_matrix[i-1][j-1] == 1:  # Adjust indices for 0-based internal representation
                    in_degree[j] += 1

        # Queue for nodes with no incoming edges
        queue = deque()
        for i in range(1, self.num_nodes + 1):
            if in_degree[i] == 0:
                queue.append(i)

        topological_order = []
        while queue:
            node = queue.popleft()
            topological_order.append(node)

            # For each node m with an edge e from n to m
            for m in range(1, self.num_nodes + 1):
                if self.adjacency_matrix[node-1][m-1] == 1:  # Adjust indices for 0-based internal representation
                    # Remove edge e from the graph
                    in_degree[m] -= 1
                    # If m has no other incoming edges then insert m into S
                    if in_degree[m] == 0:
                        queue.append(m)

        # Check if topological sorting is possible (i.e., all nodes are processed)
        if len(topological_order) != self.num_nodes:
            print("Error: the graph has at least one cycle")
            return None
        else:
            return topological_order