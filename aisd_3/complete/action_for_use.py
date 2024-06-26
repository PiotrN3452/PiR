import sys
import numpy as np

def type_of_graph(input_data):
    if input_data[0] in ["list","matrix","table"]:
        
        return input_data[0]
    else:
        print("Input data error: expecter value for type")
        sys.exit(1)
        
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
    
def find(adjacency_matrix, actions):
    for action in actions:
        if isinstance(action, list) and action[0] == 'find':
            edge = (action[1], action[2])  
            if adjacency_matrix[edge[0]-1, edge[1]-1] == 1: 
                print(f"True: edge {edge[0]}, {edge[1]} exists in the graph")
            else:
                print(f"False: edge {edge[0]}, {edge[1]} does not exist in the graph")
def dfs_util(graph, u, visited): 
    visited[u] = True
    print(u+1, end=' ') 
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

    # funkcja pomocnicza do sprawdzania czy istnieja biale nastepniki dla wierzcholka
    def has_white_successor(u):
        for v in range(num_nodes):
            if adjacency_matrix[u][v] == 1 and colors[v] == 'white':
                return True
        return False

    #funkcja pomocnicza do wyboru bialego wierzcholka poczatkowego    
    def choose_starting_node():
        for u in range(num_nodes):
            if colors[u] == 'white' and not has_white_successor(u):
                return u
        return None

    #funkcja pomocnicza do cofania sie do szarego poprzednika
    def backtrack_to_gray_predecessor(u):
        for v in range(num_nodes):
            if adjacency_matrix[v][u] == 1 and colors[v] == 'gray':
                return v
        return None

     #funkcja glowna do wykonania tarjana
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

def adjacency_matrix_to_tikz(adjacency_matrix):
    rows, cols = np.shape(adjacency_matrix)
    tikz_code = "\\documentclass{article}\n"
    tikz_code += "\\usepackage{tikz}\n"
    tikz_code += "\\begin{document}\n\n"
    tikz_code += "\\begin{figure}[ht]\n"
    tikz_code += "  \\centering\n"
    tikz_code += "  \\begin{tikzpicture}\n"
    tikz_code += "    \\tikzstyle{vertex}=[draw, circle, minimum size=20pt, inner sep=0pt]\n"
    
    # Add vertices
    for i in range(rows):
        tikz_code += f"    \\node[vertex] (v{i+1}) at ({360*i/rows}:2) {{{i+1}}};\n"
    
    # Add edges
    for i in range(rows):
        for j in range(cols):
            if adjacency_matrix[i][j] == 1:
                tikz_code += f"    \\draw[-latex] (v{i+1}) -- (v{j+1});\n"
    
    tikz_code += "  \\end{tikzpicture}\n"
    tikz_code += "\\end{figure}\n"
    tikz_code += "\\end{document}\n"
    
    return tikz_code       
