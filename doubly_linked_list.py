


class Node:
    
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
        

class DoublyLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        
    def insert_at_begening(self, data):
        if not self.head:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
        
    def print_list(self):
        if self.head is None:
            print('your linked list is empty')
            return 
        
        itr = self.head
        
        lstr = ''
        while itr:
            lstr += str(itr.data) + '--->'
            
            itr = itr.next
        print(lstr)
    
    def get_last_node(self):
        itr = self.head
        
        while itr.next:
            itr = itr.next
        
        return itr
    
    
    def print_reverse(self):
        if not self.head:
            print('your linked list is empty')
            
        last_node = self.get_last_node()
        itr = last_node
        
        lstr = ''
        while itr:
            lstr += itr.data + '--->'
            itr = itr.prev
        
        print('backward print: ', lstr)
            
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return 

        itr = self.head
        
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None, itr)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def count_lenght(self):
        count = 0
        itr = self.head
        
        while itr:
            count += 1
            itr = itr.next
            
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.count_lenght():
            raise Exception('invalid index')
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        
        while itr:
            
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1
            
    def insert_at(self, index, data):
        if index < 0 or index >= self.count_lenght():
            raise Exception('invalid index')
        
        if index == 0:
            self.insert_at_begening(data)
            return

        count = 0
        itr = self.head
        
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                
                itr.next = node
                break 
                
            itr = itr.next
            count += 1

    # def insert_after_value(self, data_after, data_to_insert):
    #     if data_after == self.head.data:
    #         self.insert_at_begening(data_to_insert)
        
    #     itr = self.head
        
    #     while itr:
    #         if itr.data == data_after:
    #             itr.next = Node(data_to_insert, itr.next)
    #             break
    #         itr = itr.next            

    # def remove_by_value(self, data):
    #     if self.head is None:
    #         return
        
    #     if self.head.data == data:
    #         self.head = self.head.next
    #         return
        
    #     itr = self.head
        
    #     while itr.next:
            
    #         if itr.next.data == data:
    #             itr.next = itr.next.next

    #             break
            
    #         itr = itr.next
            

    
if __name__ == '__main__':
    # ll = LinkedList()
    # ll.insert_values([i for i in range(10)])
    # print(ll.count_lenght())
    # ll.insert_at_begening(5)
    # ll.insert_at_end(51)
    
    # ll.print_list()
    
    # ll.remove_at(7)
    # ll.insert_at(3, 69)
    # ll.insert_after_value(69, 21)
    # ll.insert_at(0, 36)
    # print(ll.count_lenght())
    
    # ll.print_list()     
    
    
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_list()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_list()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_list()
    ll.remove_by_value("figs")
    ll.print_list()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_list()
