from util import time_it

@time_it
def binary_search(number_list, target_number):
    
    left_idx = 0
    right_idx = len(number_list) - 1
    mid_idx = 0
    
    while left_idx <= right_idx:
        
        mid_idx = (left_idx + right_idx) // 2

        mid_number = number_list[mid_idx]
        
        if mid_number == target_number:
            return mid_idx
        
        if mid_number < target_number:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1
    
    return -1


if __name__ == '__main__':
    numbers = [1, 5, 4, 15, 16, 48, 94, 112, 151, 164, 198, 179]
    
    
    index_number = binary_search(numbers, 112) 
    print(f'number found at index {index_number}') 
    

    
