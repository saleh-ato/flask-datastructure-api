class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    
    def print_ll(self):
        ll_string=""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} -> "
            node = node.next_node
            
        ll_string += " None"
        print(ll_string)
    
    def insert_begining(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        #? down
        # new_node = Node(data, self.head)
        # self.head = new_node
        else:
            new_node = Node(data, self.head)
            self.head = new_node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_begining(data)
            return
        # if self.last_node is None:
            # print("last node is none")
            # node = self.head
            # while node.next_node:
            #     print("iter", node.data)
            #     node = node.next_node
            
            # node.next_node = Node(data, None)
            # self.last_node = node.next_node
        # else:
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node
        
ll = LinkedList()
ll.insert_begining("data4")
ll.insert_begining("data+four")
ll.insert_begining("data3")
ll.insert_begining("data2")
ll.insert_begining("data1")

ll.print_ll()
# ll.insert_begining("data-new")
# ll.print_ll()
ll.insert_at_end("data-end1")
# ll.insert_at_end("data-end2")
# ll.insert_at_end("data-end3")
ll.print_ll()