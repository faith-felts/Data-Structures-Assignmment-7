class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
     self.root = None

    def insert(self, parent_name, new_value, side, current_node=None):
      if self.root is None:
        print("Tree is empty. Cannot insert without root")
        return
    
      if current_node is None:
        current_node = self.root 
    
      if current_node.name == parent_name: 
        if side == "left" and current_node.left is None:
          current_node.left = DoctorNode(new_value) 
          print(f"{new_value} added under {parent_name} on the left.") 
          return True 
        elif side == "right" and current_node.right is None: 
          current_node.right = DoctorNode(new_value) 
          print(f"{new_value} added under {parent_name} on the right.") 
          return True 
        else: 
          print(f"{parent_name} already has a {side} subordinate.") 
          return True
      found_left = False
      found_right = False
      
      if current_node.left:
        found_left = self.insert(parent_name, new_value, side, current_node.left)
      
      if current_node.right and not found_left:
        found_right = self.insert(parent_name, new_value, side, current_node.right)
      
      if not(found_left or found_right):
        if current_node == self.root:
          print(f"Parent node {parent_name} not found in the tree")
        return False
      
      return True
        
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)
   
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)
 
    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]



tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")
tree.insert("Dr. Croft", "Dr. Goldsmith", "right") 
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right") 
tree.insert("Dr. Phan", "Dr. Morgan", "left")


print("Preorder:", tree.preorder(tree.root))
print("Inorder:", tree.inorder(tree.root))
print("Postorder:", tree.postorder(tree.root))

  # Test your DoctorTree and DoctorNode classes here
