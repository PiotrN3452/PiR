import sys

class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if not node:
            return AVLTreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # Rotacje, jeśli drzewo staje się niezrównoważone
        if balance > 1:
            if key < node.left.key:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        if balance < -1:
            if key > node.right.key:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _remove(self, node, key):
        key = int(key)
        if not node:
            return node

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._remove(node.right, temp.key)

        if node is None:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1:
            if self._get_balance(node.left) >= 0:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        if balance < -1:
            if self._get_balance(node.right) <= 0:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def min(self):
        if not self.root:
            return None
        return self._min_value_node(self.root).key

    def _max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def max(self):
        if not self.root:
            return None
        return self._max_value_node(self.root).key

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def inorder(self):
        result = []
        self._inorder_traverse(self.root, result)
        return result

    def _inorder_traverse(self, node, result):
        if node:
            self._inorder_traverse(node.left, result)
            result.append(node.key)
            self._inorder_traverse(node.right, result)

    def preorder(self):
        result = []
        self._preorder_traverse(self.root, result)
        return result

    def _preorder_traverse(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_traverse(node.left, result)
            self._preorder_traverse(node.right, result)

    def postorder(self):
        result = []
        self._postorder_traverse(self.root, result)
        return result

    def _postorder_traverse(self, node, result):
        if node:
            self._postorder_traverse(node.left, result)
            self._postorder_traverse(node.right, result)
            result.append(node.key)
    def bst_to_tikz(self):
        tikz_code = []

        def traverse(node, level=0):
            if node:
                tikz_code.append('  ' * level + f"node {{{node.key}}}")  # Add node with key
                if node.left:
                    tikz_code.append('  ' * level + "child {")
                    traverse(node.left, level + 1)
                    tikz_code.append('  ' * level + "}")
                if node.right:
                    tikz_code.append('  ' * level + "child {")
                    traverse(node.right, level + 1)
                    tikz_code.append('  ' * level + "}")

        if self.root:
            tikz_code.append("\\documentclass{standalone}")
            tikz_code.append("\\usepackage{tikz}")
            tikz_code.append("\\begin{document}")
            tikz_code.append("\\begin{tikzpicture}[level distance=10mm, every node/.style={circle, draw}]")
            tikz_code.append("\\node {" + str(self.root.key) + "}")
            traverse(self.root, 1)
            tikz_code.append(";")  # Add semicolon at the end of the last subtree
            tikz_code.append("\\end{tikzpicture}")
            tikz_code.append("\\end{document}")
        return "\n".join(tikz_code)
    
    def _delete_tree_postorder(self, node):
        if node:
            self._delete_tree_postorder(node.left)
            self._delete_tree_postorder(node.right)
            del node

    def delete_tree_postorder(self):
        self._delete_tree_postorder(self.root)
        self.root = None
        
def create_avl_tree(arr):
    avl_tree = AVLTree()
    for key in arr:
        avl_tree.insert(key)
    return avl_tree


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
    def delete_tree_postorder(self):
        if self:
            if self.left:
                self.left.delete_tree_postorder()
            if self.right:
                self.right.delete_tree_postorder()
            del self
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


def create_tree(arr):
    if not arr:
        return None
    tree = TreeNode(arr[0])
    for key in arr[1:]:
        tree.insert(key)
    return tree

def min_max(tree):
    if not tree:
        return

    min = tree.min()
    max = tree.max()

    print("Min:", min)
    print("Max:", max)

def traverse(tree):
    if not tree:
        return
    
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

def remove_node(tree, rnodes): 
    if not tree:
        return
    for rnode in rnodes:
        tree.remove(rnode)
        

    print("Pre-order:", tree.preorder())
    print("In-order:", tree.inorder())
    print("Post-order:", tree.postorder())

def delete(tree): #usuwanie drzewa BST z wykorzystaniem post-order - tak jak na wykladzie
    if not tree:
        return
    x = tree.postorder()
    y = str(x)
    tree.delete_tree_postorder()
    print("deleting: " + y)
    if x == []:
        print("Tree succesfully removed")

def bst_to_tikz(root):
    tikz_code = []

    def traverse(node, level=0):
        if node:
            tikz_code.append('  ' * level + f"node {{{node.key}}}")  # Add node with key
            if node.left:
                tikz_code.append('  ' * level + "child {")
                traverse(node.left, level + 1)
                tikz_code.append('  ' * level + "}")
            if node.right:
                tikz_code.append('  ' * level + "child {")
                traverse(node.right, level + 1)
                tikz_code.append('  ' * level + "}")

    tikz_code.append("\\documentclass{standalone}")
    tikz_code.append("\\usepackage{tikz}")
    tikz_code.append("\\begin{document}")
    tikz_code.append("\\begin{tikzpicture}[level distance=10mm, every node/.style={circle, draw}]")
    tikz_code.append("\\node {" + str(root.key) + "}")
    traverse(root, 1)
    tikz_code.append(";")  # Add semicolon at the end of the last subtree
    tikz_code.append("\\end{tikzpicture}")
    tikz_code.append("\\end{document}")

    return "\n".join(tikz_code)





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
    global tree_type_c
    tree_type_c = tree_type
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

        if tree_type == "BST":
            array = create_tree(data) # stworzenie drzewa BST
        elif tree_type == "AVL":
            array = create_avl_tree(data) 
        else: 
            print("Error: wrong type of tree")
            sys.exit(1)
        if action_list['1'] in input_data:
            print(help)
        if action_list['2'] in input_data:
            traverse(array)
        if action_list['3'] in input_data:
            min_max(array)
        if action_list['4'] in input_data:
            index = input_data.index(action_list['4']) + 1
            rnodes = []
            while index < len(input_data) and input_data[index].isdigit():
                rnodes.append(input_data[index])
                index += 1
            print("Removing nodes:", rnodes)
            remove_node(array, rnodes)
        if action_list['5'] in input_data:
            delete(array)
        if action_list['6'] in input_data:
            if tree_type == "AVL":
                print(array.bst_to_tikz())
            else:
                tikz_picture = bst_to_tikz(array)
                print(tikz_picture)
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