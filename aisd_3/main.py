import sys
import sys

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

print(actions(["find","1","1","sort","1","prInt","pRINT","find","2","kahn","3","kahn","kAHN"]))
print(actions)