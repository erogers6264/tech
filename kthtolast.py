

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

def kth_to_last_node(k, current_node):
    node_count = 1
    after_counting_node = current_node
    
    # Iterate through the list to count elements
    while current_node.next is not None:
        node_count += 1
        current_node = current_node.next
        
    # Position of kth to last is the difference from total element count
    kth_to_last = node_count - k
    
    # Iterate again only until kth to last
    for i in range(kth_to_last):
        after_counting_node = after_counting_node.next
    
    # Return that value
    return after_counting_node.value
    

print kth_to_last_node(2, a)
# returns the node with value "Devil's Food" (the 2nd to last node)