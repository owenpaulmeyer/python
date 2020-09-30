class Empty:
    def isempty(self):
        return True
    
    def __str__(self):
        return '[]'
    
    
class Node:
    def __init__(self, head, tail = Empty()):
        self.head = head
        self.tail = tail
        
    def isempty(self):
        return False
    
    def __str__(self):
        return str(self.head) + ', ' + str(self.tail)
    

def attatch_tail(node, tail):
    node.tail = tail
    return node
        

def append(head, alist):
    return Node(head, alist)
    
def reverse(alist):
    head = alist
    tail = alist.tail
    reversed = Empty()
    
    while not tail.isempty():
        reversed = attatch_tail(head, reversed)
        head = tail
        tail = head.tail
    return attatch_tail(head, reversed)


ll = Empty()
for n in range(1,6):
    ll = append(n, ll)
    
print(ll)
revs = reverse(ll)
print(revs)
        

        
