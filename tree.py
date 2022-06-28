class TreeNode:
    
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent    
            level += 1
            
        return level
            

    def print_tree(self, level):
        spaces = ' ' * self.get_level() * 2
        prefix = spaces + '|__' if self.parent else ""
        
        print(prefix, self.data)
        if self.children and self.get_level() < level:
            for child in self.children:
                # print(child.data, end='    ')
                child.print_tree(level)    
 

def build_product_tree():
    root = TreeNode('Electronics')
    labtop = TreeNode('Labtop')      
    labtop.add_child(TreeNode('Mac'))  
    cellphone = TreeNode('Cellphone')
    tv = TreeNode('TV')
    
    tv.add_child(TreeNode('SAMSUNG'))
    tv.add_child(TreeNode('LG'))
    

    root.add_child(labtop)
    root.add_child(cellphone)
    root.add_child(tv)
     
    return root
if __name__ == '__main__':
    root = build_product_tree() 
    root.print_tree(2)
    print(root.get_level())