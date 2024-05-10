import sys
import random
import numpy as np
from collections import deque

from graph_class import DirectedGraph
from action_for_use import *
sys.setrecursionlimit(10**6) 
     
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
        
        input_data = actions(input_data)
        
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
        try:
            nodes = int(nodes)
        except:
            print("Input data error: expecter value for nodes")
            sys.exit(1)
        saturation = int(saturation)
        graph = DirectedGraph(nodes)
        graph.generate_tree()
        adjacency_matrix = graph.adjacency_matrix_as_numpy()
        actions_start(actions,graph)

    if sys.argv[1] == "--user-provided":
        
        input_data = sys.stdin.read().strip().split('\n')
        reprezentation = type_of_graph(input_data)
        input_data.pop(0)
        input_data = actions(input_data)
        nodes = len(input_data)
        graph = DirectedGraph(nodes)
        for i, line in enumerate(input_data):
            successors = list(map(int, line.split()))
            for successor in successors:
                graph.add_edge(i, successor-1)  # Subtracting 1 to adjust to 0-based indexing
        
        adjacency_matrix = graph.adjacency_matrix_as_numpy()
        actions_start(actions,graph)
         
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

        elif value == "export" and "export" not in action_list:
            action_list.append("export")
            to_delete.extend([i for i, x in enumerate(input_data) if x.lower() == "export"])

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

            

def actions_start(act,graph):
    if "print" in act:
        if reprezentation == "matrix":
            print(adjacency_matrix)
        if reprezentation == "list":
            successor_list(adjacency_matrix)
            
        if reprezentation == "table":
            edge_list(adjacency_matrix)
            
    for action in act:
        if isinstance(action, list) and action[0] == 'find':
            find(adjacency_matrix,actions)
    if "breath-first_search" in act:
        print("bfs:", graph.breath_first_traversal())
    if "depth-first_search" in act:
        print("dfs:", end=" ")
        dfs(adjacency_matrix)
        print()
    if "export" in act:
        latex_code = adjacency_matrix_to_tikz(adjacency_matrix)
        print(latex_code)
    if "kahn" in act:
        print("Topological order (kahn):" ,graph.kahn_topological_sort())
    if "tarjan" in act:
        topological_order = tarjan(adjacency_matrix)
        print("Topological order (tarjan):", topological_order)
    
                    
            
if __name__ == "__main__":
    main()
    
