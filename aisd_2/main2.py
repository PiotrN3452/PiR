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

    def inorder(self, values = None):
        if values is None:
            values = []
        if self.left:
            self.left.inorder(values)
        values.append(self.key)
        if self.right:
            self.right.inorder(values)
        return values

    def preorder(self, values = None):
        if values is None:
            values = []
        values.append(self.key)
        if self.left:
            self.left.preorder(values)
        if self.right:
            self.right.preorder(values)
        return values

    def postorder(self, values = None):
        if values is None:
            values = []
        if self.left:
            self.left.postorder(values)
        if self.right:
            self.right.postorder(values)
        values.append(self.key)
        return values

    def min(self):
        if self.left:
            return self.left.min()
        return self.key

    def max(self):
        if self.right:
            return self.right.max()
        return self.key
    
    def remove(self, key, parent=None):
        if int(key) < self.key:
            if self.left:
                self.left.remove(key, self)
        elif int(key) > self.key:
            if self.right:
                self.right.remove(key, self)
        else:
            if self.left and self.right:  # wezel z dwoma potomkami - jako korzen w podrzewie przyjety jest maksymalny element w lewym podrzewie
                successor = self.left.max()
                self.key = successor
                self.left.remove(successor, self)
            elif parent is None:  # korzen z jednym lub bez potomka
                if self.left:
                    self.key = self.left.key
                    self.left = self.left.left
                    self.right = self.left.right
                elif self.right:
                    self.key = self.right.key
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    self.key = None
            elif parent.left == self:  # wezel z lewym potomkiem
                parent.left = self.left if self.left else self.right
            elif parent.right == self:  # wezel z prawym potomkiem
                parent.right = self.left if self.left else self.right
        

def min_max(arr):
    tree = TreeNode(arr[0])
    for key in arr[1:]:
        tree.insert(key)

    min = tree.min()
    max = tree.max()

    print("Min:", min)
    print("Max:", max)

def traverse(arr):

    tree = TreeNode(arr[0])
    for key in arr[1:]:
        tree.insert(key)
    
    x = tree.inorder()

    if len(x) % 2 == 0:
        median = (x[len(x)//2] + x[(len(x)//2)-1]) / 2
    else:
        median = x[len(x)//2]
    print("Sorted:", tree.inorder())
    print("Median: " + str(median))
    print("Pre-order:", tree.preorder())
    print("In-order:", tree.inorder())
    print("Post-order:", tree.postorder())

def remove_node(arr, rnodes): 
    tree = TreeNode(arr[0])
    for key in arr[1:]:
        tree.insert(key)
    
    for rnode in rnodes:
        tree.remove(rnode)

    print("Pre-order:", tree.preorder())
    print("In-order:", tree.inorder())
    print("Post-order:", tree.postorder())

def delete(arr): #usuwanie drzewa BST z wykorzystaniem post-order - tak jak na wykladzie
    tree = TreeNode(arr[0])
    for key in arr[1:]:
        tree.insert(key)
    
    x = tree.postorder()
    y = str(x)
    print("deleting: " + y)
    while x:
        x.pop()
    if x == []:
        print("Tree succesfully removed")

### to dla drzewa BST

def UI(node, insert,tree_type):
    action_list = {'1':'Help', '2':'Print', '3':'FindMinMax', '4':'Remove', '5':'Delete', '6':'Export', '7':'Rebalace', '8': 'Exit'}
    help = '''
Help            Show this massage
Print           Prints the tree using In-order, Pre-order, Post-order
FindMinMax      Finds minimal and maximal value
Remove          Remove elements from tree
Delete          Delete the whole tree
Export          Export the tree to tikzpicture
Rebalance       Rebalance the tree
Exit            Exit the program
'''

    # dane jako heredoc
    if not sys.stdin.isatty():
        input_data = sys.stdin.read().split()
        try:
            data = []
            for x in input_data: #ignorowanie powtarzajacych sie wezlow
                if x.isdigit():
                    value = int(x)
                    if value not in data:
                        data.append(value)
        
            node = str(len(data))
            insert = ' '.join(str(x) for x in data)

        except ValueError:
            print("Invalid input format")
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
            index = input_data.index(action_list['4']) + 1
            #print(input_data)
            #print(len(input_data))
            rnodes = []
            while index < len(input_data) and input_data[index].isdigit():
                rnodes.append(input_data[index])
                index += 1
            print("Removing nodes:", rnodes)
            remove_node(data, rnodes)
        if action_list['5'] in input_data:
            delete(data)
        if action_list['6'] in input_data:
            print(help)
        if action_list['7'] in input_data:
            print(help)    
        if action_list['8'] in input_data:
            sys.exit(0)
    
    # user input 
    #else:
    #    node = input("nodes> ")
    #    while not node.isdigit():
    #        print("Error: expected nodes as single integer")
    #        node = input("nodes> ")

    #    while True:
    #        insert = input("insert> ")
    #        input_data = insert.split()
    #        #print(input_data)
    #        for x in input_data:
    #            if not x.isdigit():
    #                a = False
    #            else:
    #                a = True
    #        if a == True:
    #            break
    #        else:
    #            print("Error: expected insert as a sequence of integers separated by a single space")

    #    node = int(node)            
    #    input_data = [int(num) for num in input_data]
    #    if node != len(input_data):
    #        print("Error: nodes value do not match insert amount")
    #        sys.exit(1)

    #    while True:
    #        action = input("action> ")
    #        if action == action_list['1']:
    #            print(help)
    #        elif action == action_list['2']:
    #            print("tutaj funkcja print")
    #        elif action == action_list['3']:
    #            print("tutaj funkcja remove")
    #        elif action == action_list['4']:
    #            print("tutaj funkcja delete")
    #        elif action == action_list['5']:
    #            print("tutaj funkcja export") 
    #        elif action == action_list['6']:
    #            print("tutaj funkcja rebalance")
    #        elif action == action_list['7']:
    #            sys.exit(0)
    #        else:
    #            print('Error: unknown command. Use "Help" to see all commands')


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