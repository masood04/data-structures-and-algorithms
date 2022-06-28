class Graph:
    def __init__(self, edeges, ):
        self.edeges = edeges
        self.graph_dict = dict()
        
        for start, end in self.edeges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
                 
        print("Graph DICT: ", self.graph_dict)
    
    def get_paths(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                
                for p in new_paths:
                    paths.append(p)
    

        return paths
    
    
    
if __name__ == '__main__':
    routes = [
        ('Paris', 'Mumbai'),
        ('Mumbai', 'NYC'),
        ('Paris', 'Yazd'),
        ('Yazd', 'Taft')
    ]    
    
    route_groups = Graph(routes)
    
    print(route_groups.get_paths('Paris', 'Taft'))
    