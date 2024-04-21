import sys

def UI(node, insert):

    # Data as heredoc
    if not sys.stdin.isatty():
        input_data = sys.stdin.read().split()
        try:
            data = [int(x) for x in input_data[0:]]
            node = ' '.join(str(data[0]))
            insert = ' '.join(str(x) for x in data[1:])
        except EOFError:
            print("Error reading input.")
        print("nodes> " + str(node))
        print("insert> " + str(insert))
    
    # user input 
    elif node == None and insert == []:
        node = input("nodes> ")
        while not node.isdigit():
            print("Error: expected nodes as single integer")
            node = input("nodes> ")

        while True:
            insert = input("insert> ")
            input_data = insert.split()
            #print(input_data)
            for x in input_data:
                if not x.isdigit():
                    a = False
                else:
                    a = True
            if a == True:
                break
            else:
                print("Error: expected insert as a sequence of integers separated by a single space")
                    
        input_data = [int(num) for num in input_data]
        print(input_data)

def main():
    # Command-line arguments: python script.py --tree <tree_type> optional: < *.txt or <<< "data"
    if sys.argv[1] != "--tree": 
        print("Usage: python script.py --tree <tree_type>")
        sys.exit(1)

    tree_type = str(sys.argv[2])
    node = None
    insert = []

    try: 
        if tree_type != "BST" and tree_type != "AVL":
            raise ValueError("tree_type error: expected value <BST> or <AVL>")
        else:
            UI(node, insert)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()