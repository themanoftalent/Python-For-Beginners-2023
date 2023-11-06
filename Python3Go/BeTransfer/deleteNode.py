#delete a node from a signly linked list, wiht only information being you only have the current node
class LinkedListNode:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __repr__(self):
        return "{}".format(self.value)

def delete_node(nodeToDelete):
    next_node = nodeToDelete.next
    if next_node:
        nodeToDelete.value = next_node.value
        nodeToDelete.next = next_node.next
    else:
        raise Exception("cannot delete the last node")
    
a = LinkedListNode(5)
b = LinkedListNode(1)
c = LinkedListNode(9)
a.next = b
b.next = c
delete_node(b)
print( a)
print ("next is",a.next)
print (b)
print ("next is",b.next)
