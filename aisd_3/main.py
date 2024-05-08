import sys
def actions_f(input_data):
    global actions
    actions = []
    for_itr = input_data
    for i in reversed(for_itr):
        if "print" not in actions:
            if i.lower() == "print":
                actions.append("print")
                for j in range(len(input_data),0,-1):
                    j -= 1
                    element = input_data[j]
                    if element.lower() == "print":
                        del input_data[j]
        if "breath-first search" not in actions:
            if i.lower() == "breath-first search":
                actions.append("breath-first search")
                for j in range(len(input_data),0,-1):
                    j -= 1
                    element = input_data[j]
                    if element.lower() == "breath-first search":
                        del input_data[j]    
        if "depth-first search" not in actions:
            if i.lower() == "depth-first search":
                actions.append("depth-first search")
                for j in range(len(input_data),0,-1):
                    j -= 1
                    element = input_data[j]
                    if element.lower() == "depth-first search":
                        del input_data[j]
        if "sort" not in actions:
            if i.lower() == "sort":
                actions.append("sort")
                for j in range(len(input_data),0,-1):
                    j -= 1
                    element = input_data[j]
                    if element.lower() == "sort":
                        del input_data[j]            
        if "tarjan" not in actions:
            if i.lower() == "tarjan":
                actions.append("tarjan")
                for j in range(len(input_data),0,-1):
                    j -= 1
                    element = input_data[j]
                    if element.lower() == "tarjan":
                        del input_data[j]            
        if "kahn" not in actions:
            if i.lower() == "kahn":
                actions.append("kahn")
                for j in range(len(input_data),0,-1):
                    j -= 1
                    element = input_data[j]
                    if element.lower() == "kahn":
                        del input_data[j]       
        if i.lower() == "find":
            find_obj = ["find"]
            help_list = [x.lower() for x in input_data]
            try:
                find_obj.append(int(input_data[help_list.index("find") + 1]))
                find_obj.append(int(input_data[help_list.index("find") + 2]))
                del input_data[help_list.index("find") + 2]
                del input_data[help_list.index("find") + 1]
                del input_data[help_list.index("find")]
            except:
                print("error: no corect edge info after find action ")
                sys.exit(1)
            
            actions.append(find_obj)
        
    return input_data

lista = ['matrix', '2', 'find', '3', '5', 'PrInt', 'prINT']
print(actions_f(lista))
print(actions)