from linkedlist import Node

linkedlist = Node(1,Node(2,Node(3,Node(4,None))))
linkedlist = Node(1,Node(2,Node(3,Node(1,None))))

print linkedlist.isCircular()