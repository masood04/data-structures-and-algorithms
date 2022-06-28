
def bubble_sort(elements):
    size = len(elements)
    
    for i in range(size - 1):
        
        swapped = False
        
        for j in range(size - i- 1):
            if elements[j] > elements[j + 1]:
                
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True
        
        if not swapped:
            break
    
    
    
    
    
if __name__ == '__main__':
    elements = [45, 78, 14, 84, 21, 32, 98, 42]

    
    bubble_sort(elements)
    print(elements)


