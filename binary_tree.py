class BinarySearchTreeNode:
    
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
        
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
            
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    

    def in_order_traversal(self):
        elemnts = []
        
        if self.left:
            elemnts += self.left.in_order_traversal()

        elemnts.append(self.data)
        
        if self.right:
            elemnts += self.right.in_order_traversal()

        
        return elemnts
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            
            if self.left:
                return self.left.search(val)
            
            else:
                return False
            
            
        if val > self.data:
            
            if self.right:
                return self.right.search(val)
            
            else:
                return False
            
            
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
            
    def find_min(self):
        if self.left is None:
            return self.data
        
        else:
            return self.left.find_min()
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)    
        
        else:
            if not self.left and not self.right:
                return None
            
            if not self.left:
                return self.right
            
            if not self.right:
                return self.left
            
            min_val = self.find_min()
            self.data = min_val
            
            self.right = self.right.delete(min_val)

        return self
    
    
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root



if __name__ == '__main__':
    numbers = [71, 548, 1548, 124, 15, 115, 84, 23]

    root = build_tree(numbers)
    print(root.in_order_traversal())
    print(root.search(548))
    root.delete(548)
    print('after deleting element 548: ', root.in_order_traversal())
    
    
