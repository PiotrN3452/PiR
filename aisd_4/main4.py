import sys
import random
import numpy as np
from collections import deque

sys.setrecursionlimit(10**6)

def create_hamiltonian_graph(nodes, saturation):
    adjacency_matrix = np.zeros((nodes, nodes), dtype=int)

    hamiltonian_cycle = list(range(nodes))
    random.shuffle(hamiltonian_cycle)
    for i in range(nodes - 1):
        adjacency_matrix[hamiltonian_cycle[i], hamiltonian_cycle[i + 1]] = 1
        adjacency_matrix[hamiltonian_cycle[i + 1], hamiltonian_cycle[i]] = 1
    adjacency_matrix[hamiltonian_cycle[-1], hamiltonian_cycle[0]] = 1
    adjacency_matrix[hamiltonian_cycle[0], hamiltonian_cycle[-1]] = 1

    num_edges = int((nodes * (nodes - 1) / 2) * saturation)

    while np.sum(adjacency_matrix) / 2 < num_edges:
        u, v = random.sample(range(nodes), 2)
        if u != v and adjacency_matrix[u, v] == 0:
            adjacency_matrix[u, v] = 1
            adjacency_matrix[v, u] = 1

    for node in range(nodes):
        while np.sum(adjacency_matrix[node]) % 2 != 0:
            neighbor = random.choice(np.nonzero(adjacency_matrix[node])[0])
            adjacency_matrix[node, neighbor] = 0
            adjacency_matrix[neighbor, node] = 0
            cycle_nodes = random.sample(range(nodes), 3)
            adjacency_matrix[cycle_nodes[0], cycle_nodes[1]] = 1
            adjacency_matrix[cycle_nodes[1], cycle_nodes[0]] = 1
            adjacency_matrix[cycle_nodes[1], cycle_nodes[2]] = 1
            adjacency_matrix[cycle_nodes[2], cycle_nodes[1]] = 1

    return adjacency_matrix


def create_non_hamiltonian_graph(nodes, saturation):
    adjacency_matrix = np.zeros((nodes, nodes), dtype=int)
    
    num_edges = int((nodes * (nodes - 1) / 2) * saturation)

    edges_added = 0
    while edges_added < num_edges:
        u, v = random.sample(range(nodes), 2)
        if u != v and adjacency_matrix[u, v] == 0:
            adjacency_matrix[u, v] = 1
            adjacency_matrix[v, u] = 1
            edges_added += 1

    # Isolate one node to ensure the graph is non-Hamiltonian
    isolated_node = random.choice(range(nodes))
    for i in range(nodes):
        if adjacency_matrix[isolated_node, i] == 1:
            adjacency_matrix[isolated_node, i] = 0
            adjacency_matrix[i, isolated_node] = 0

    return adjacency_matrix


def display_adjacency_matrix(adjacency_matrix):
    print(adjacency_matrix)





def main():
    global actions
    global adjacency_matrix
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
            adjacency_matrix = create_hamiltonian_graph(nodes, saturation)
            print("Macierz sąsiedztwa:")
            display_adjacency_matrix(adjacency_matrix)
        elif sys.argv[1] == "--non-hamilton":
            adjacency_matrix = create_non_hamiltonian_graph(nodes, saturation)
            print("Macierz sąsiedztwa")
            display_adjacency_matrix(adjacency_matrix)
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
