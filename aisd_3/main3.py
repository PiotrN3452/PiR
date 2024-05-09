import sys
import random
import numpy as np
from collections import deque
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
        print(nodes_to_visit)

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

def type_of_graph(input_data):
    if input_data[0] in ["list","matrix","table"]:
        
        return input_data[0]
    else:
        print("Input data error: expecter value for type")
        sys.exit(1)
        
def main():
    global reprezentation
    global adjacency_matrix
    if  sys.argv[1] != "--generate" and sys.argv[1] != "--user-provided":
        print("Wrong argument: expected value <--argument> or <--user-provided>")
        sys.exit(1)
    

    if sys.argv[1] == "--generate":
        input_data = []
        input_data = sys.stdin.read().split()
        if not input_data[0]:
            print("Error: no arguments provided")
            sys.exit(1)
        print(input_data)
        input_data = actions(input_data)
        print(input_data)
        nodes = input_data[1]
        if len(input_data) > 2:
            saturation = input_data[2]
            if input_data[0] in ["list","matrix","table"]:
                reprezentation = input_data[0]
            else:
                print("Input data error: expecter value for type")
                sys.exit(1)
        else:
            print("Input data error: expected value for saturation")
            sys.exit(1)
        print("nodes> " + nodes)
        if saturation:
            print("saturation> " + saturation)
        nodes = int(nodes)
        saturation = int(saturation)
        graph = DirectedGraph(nodes)
        graph.generate_tree()
        adjacency_matrix = graph.adjacency_matrix_as_numpy()
        print(adjacency_matrix)
        print(reprezentation)
        print(actions)
        actions_start(actions,graph)

    if sys.argv[1] == "--user-provided":
        
        input_data = sys.stdin.read().strip().split('\n')
        reprezentation = type_of_graph(input_data)
        input_data.pop(0)
        input_data = actions(input_data)
        print(input_data)
        nodes = len(input_data)
        graph = DirectedGraph(nodes)
        for i, line in enumerate(input_data):
            successors = list(map(int, line.split()))
            for successor in successors:
                graph.add_edge(i, successor-1)  # Subtracting 1 to adjust to 0-based indexing
        
        adjacency_matrix = graph.adjacency_matrix_as_numpy()
        print(adjacency_matrix)
        print(reprezentation)
        actions_start(actions,graph)
        
        

def successor_list(adjacency_matrix):
    for i in range(1, adjacency_matrix.shape[0] + 1):
        successors = []
        for j in range(1, adjacency_matrix.shape[1] + 1):
            if adjacency_matrix[i - 1, j - 1] == 1:
                successors.append(j)
        print(f"{i} --> {successors}")

def edge_list(adjacency_matrix):
    edge_list = []
    for i in range(adjacency_matrix.shape[0]):
        for j in range(adjacency_matrix.shape[1]):
            if adjacency_matrix[i, j] == 1:
                edge_list.append([i + 1, j + 1])
    print(np.array(edge_list))
        
def actions(input_data):
    action_list = []
    to_delete = []

    # Reverse iterate to handle actions in the order they appear when processed
    for index in range(len(input_data) - 1, -1, -1):
        value = input_data[index].lower()

        if value == "print" and "print" not in action_list:
            action_list.append("print")
            to_delete.extend([i for i, x in enumerate(input_data) if x.lower() == "print"])

        elif value == "breath-first_search" and "breath-first_search" not in action_list:
            action_list.append("breath-first_search")
            to_delete.extend([i for i, x in enumerate(input_data) if x.lower() == "breath-first_search"])

        elif value == "depth-first_search" and "depth-first_search" not in action_list:
            action_list.append("depth-first_search")
            to_delete.extend([i for i, x in enumerate(input_data) if x.lower() == "depth-first_search"])

        elif value == "sort" and "sort" not in action_list:
            action_list.append("sort")
            to_delete.extend([i for i, x in enumerate(input_data) if x.lower() == "sort"])

        elif value == "tarjan" and "tarjan" not in action_list:
            action_list.append("tarjan")
            to_delete.extend([i for i, x in enumerate(input_data) if x.lower() == "tarjan"])

        elif value == "kahn" and "kahn" not in action_list:
            action_list.append("kahn")
            to_delete.extend([i for i, x in enumerate(input_data) if x.lower() == "kahn"])

        elif value == "find":
            try:
                # Assuming the next two values are integers as required
                find_obj = ["find", int(input_data[index + 1]), int(input_data[index + 2])]
                action_list.append(find_obj)
                # Mark indices for deletion
                to_delete.extend([index, index + 1, index + 2])
            except (IndexError, ValueError):
                print("error: no correct edge info after find action")
                sys.exit(1)

    # Delete marked indices from input_data in reverse order to not mess up the indices
    for index in sorted(set(to_delete), reverse=True):
        del input_data[index]
    global actions
    actions =  action_list
    return input_data

def find(adjacency_matrix, actions):
    for action in actions:
        if isinstance(action, list) and action[0] == 'find':
            edge = (action[1], action[2])  # Krawędź jako para wierzchołków
            if adjacency_matrix[edge[0]-1, edge[1]-1] == 1:  # Sprawdź, czy krawędź istnieje w macierzy
                print(f"True: edge {edge[0]}, {edge[1]} exists in the graph")
            else:
                print(f"False: edge {edge[0]}, {edge[1]} does not exist in the graph")
def dfs_util(graph, u, visited): 
    visited[u] = True
    print(u+1)  # Wyświetlenie wierzchołka, który jest odwiedzany
    for v in range(len(graph)):
        if graph[u][v] == 1 and not visited[v]:
            dfs_util(graph, v, visited)
            
def dfs(graph):
    visited = [False] * len(graph)
    for u in range(len(graph)):
        if not visited[u]:
            dfs_util(graph, u, visited)

def tarjan(adjacency_matrix):
    num_nodes = len(adjacency_matrix)
    colors = ['white'] * num_nodes
    L = []  
    S = []  

    # Funkcja pomocnicza do sprawdzania, czy istnieją białe następniki dla danego wierzchołka
    def has_white_successor(u):
        for v in range(num_nodes):
            if adjacency_matrix[u][v] == 1 and colors[v] == 'white':
                return True
        return False

    # Funkcja pomocnicza do wyboru białego wierzchołka startowego
    def choose_starting_node():
        for u in range(num_nodes):
            if colors[u] == 'white' and not has_white_successor(u):
                return u
        return None

    # Funkcja pomocnicza do cofania się do szarego poprzednika na ścieżce
    def backtrack_to_gray_predecessor(u):
        for v in range(num_nodes):
            if adjacency_matrix[v][u] == 1 and colors[v] == 'gray':
                return v
        return None

    # Funkcja główna do wykonywania sortowania topologicznego
    def tarjan_util(u):
        while u is not None:
            colors[u] = 'gray'

            
            while has_white_successor(u):
                for v in range(num_nodes):
                    if adjacency_matrix[u][v] == 1 and colors[v] == 'white':
                        u = v
                        break
                colors[u] = 'gray'

            
            colors[u] = 'black'
            S.append(u)

           
            u = backtrack_to_gray_predecessor(u)

    
    u = choose_starting_node()
    while u is not None:
        tarjan_util(u)
        u = choose_starting_node()  #

    
    while S:
        L.append(S.pop() + 1) 

    return L            

def actions_start(act,graph):
    if "print" in act:
        if reprezentation == "matrix":
            print(adjacency_matrix)
        if reprezentation == "list":
            successor_list(adjacency_matrix)
            print(adjacency_matrix)
        if reprezentation == "table":
            edge_list(adjacency_matrix)
            print(adjacency_matrix)
    for action in act:
        if isinstance(action, list) and action[0] == 'find':
            find(adjacency_matrix,actions)
    if "breath-first_search" in act:
        print(graph.breath_first_traversal())
    if "depth-first_search" in act:
        dfs(adjacency_matrix)
    if "sort" in act:
        pass
    if "kahn" in act:
        print(graph.kahn_topological_sort())
    if "tarjan" in act:
        topological_order = tarjan(adjacency_matrix)
        print("Topological order:", topological_order)
    
                    
            
if __name__ == "__main__":
    main()
    print(actions)
