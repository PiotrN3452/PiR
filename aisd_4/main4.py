import sys
import random
import numpy as np
from collections import deque

sys.setrecursionlimit(10**6)

def main():
    global actions
    global adjacency_matrix

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
        
        if len(input_data) > 1:
            saturation = input_data[1]
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
        
        if input_data:
            try:
                nodes = int(input_data[0])
            except ValueError:
                print("Error: invalid node number")
                sys.exit(1)
            print(f"nodes> {nodes}")
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
        print("print")
        print(graph)
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
