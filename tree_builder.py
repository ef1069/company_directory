class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # Case 1: Empty Tree
        if self.root is None:
            print("Tree is empty. Cannot insert without root")
            return
        
        # Start from root if not part of recursive call
        if current_node is None:
            current_node = self.root

        # Case 2: Found parent node
        if current_node.name == manager_name:
            if side == "left" and current_node.left is None:
                current_node.left = EmployeeNode(employee_name)
                print(f"{employee_name} added under {manager_name} on the left.")
                return True

            elif side == "right" and current_node.right is None:
                current_node.right = EmployeeNode(employee_name)
                print(f"{employee_name} added under {manager_name} on the right.")
                return True
            else:
                print(f"{manager_name} already has a {side} subordinate.")
                return True

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else: 
                return

        indent = "  " * level
        print(f"-{node.name}")

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)

# Test your code here









# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")