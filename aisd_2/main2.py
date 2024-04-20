import sys

def UI():
    # Jeśli dane zostały przekazane jako wejście za pomocą przekierowania strumienia wejściowego (heredoc)
    if not sys.stdin.isatty():
        input_data = sys.stdin.read().split()
        try:
            data = [int(x) for x in input_data[1:]]
        except EOFError:
            print("Error reading input.")
        print("nodes> " + str(input_data[0]))
        print("insert> " + str(input_data))
    # W przeciwnym razie, gdy użytkownik wprowadza dane ręcznie
    else:
        node = input("nodes> ")
        while not node.isdigit():
            print("Error: expected nodes as integer")
            node = input("nodes> ")

        while True:
            insert = input("insert> ")
            input_data = insert.split()
            try:
                input_data = [int(num) for num in input_data]
                break  # Wyjście z pętli, jeśli dane są poprawne
            except ValueError:
                print("Error: expected insert as a sequence of numbers separated by a space")

        

        print(input_data)

def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if sys.argv[1] != "--tree": #len(sys.argv) != 3 or 
        print("Usage: python script.py --tree <tree_type>")
        sys.exit(1)

    tree_type = str(sys.argv[2])
    
    try: 
        if tree_type != "BST" and tree_type != "AVL":
            raise ValueError("tree_type error: expected value <BST> or <AVL>")
        UI()
    except ValueError as e:
        print(e)

    # Perform sorting using the specified algorithm
    #sorted_data = tree(data, tree_type)

    # Print the sorted data
    #print("Sorted data:", sorted_data[0:10])

if __name__ == "__main__":
    main()