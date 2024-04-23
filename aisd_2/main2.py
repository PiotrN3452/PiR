import sys


### to dla drzewa BST
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def insert(self,key):
        if key < self.key:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key)
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.key)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key) 

    def min(self):
        if self.left:
            self.left.min()
        if self.left is None:
            print(self.key)

    def max(self):
        if self.right:
            self.right.max()
        if self.right is None:
            print(self.key)

def min_max(arr):
    tree = TreeNode(arr[0])
    for key in arr[1:]:
        tree.insert(key)

    print("Min: ")
    tree.min()
    print("Max: ")
    tree.max()

def traverse(arr):

    tree = TreeNode(arr[0])
    for key in arr[1:]:
        tree.insert(key)
    
    print("Preorder:")
    tree.preorder()
    print("Inorder:")
    tree.inorder()
    print("Postorder:")
    tree.postorder()

### to dla drzewa BST

def UI(node, insert,tree_type):
    action_list = {'1':'Help', '2':'Print', '3':'FindMinMax', '4':'Remove', '5':'Delete', '6':'Export', '7':'Rebalace', '8': 'Exit'}
    help = '''
Help        Show this massage
Print       Prints the tree using In-order, Pre-order, Post-order
Remove      Remove elements from tree
Delete      Delete the whole tree
Export      Export the tree to tikzpicture
Rebalance   Rebalance the tree
Exit        Exit the program
'''

    # Data as heredoc
    if not sys.stdin.isatty():
        input_data = sys.stdin.read().split()
        try:
            data = [int(x) for x in input_data if x.isdigit()]
            #node = ' '.join(str(data[0]))
            node = str(len(data))
            insert = ' '.join(str(x) for x in data[0:])
        except EOFError:
            print("Error reading input.")
        print("nodes> " + node)
        print("insert> " + insert)

        if action_list['1'] in input_data:
            print(help)
        if action_list['2'] in input_data:
            if tree_type == "BST":
                traverse(data)
            else:
                sys.exit(1)
        if action_list['3'] in input_data:
            min_max(data)
        if action_list['4'] in input_data:
            print(help)
        if action_list['5'] in input_data:
            print(help)
        if action_list['6'] in input_data:
            print(help)
        if action_list['7'] in input_data:
            print(help)    
        if action_list['8'] in input_data:
            sys.exit(0)
    
    # user input 
    else:
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

        node = int(node)            
        input_data = [int(num) for num in input_data]
        if node != len(input_data):
            print("Error: nodes value do not match insert amount")
            sys.exit(1)

        while True:
            action = input("action> ")
            if action == action_list['1']:
                print(help)
            elif action == action_list['2']:
                print("tutaj funkcja print")
            elif action == action_list['3']:
                print("tutaj funkcja remove")
            elif action == action_list['4']:
                print("tutaj funkcja delete")
            elif action == action_list['5']:
                print("tutaj funkcja export") 
            elif action == action_list['6']:
                print("tutaj funkcja rebalance")
            elif action == action_list['7']:
                sys.exit(0)
            else:
                print('Error: unknown command. Use "Help" to see all commands')


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
            UI(node, insert,tree_type)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()