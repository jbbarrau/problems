"""

Write a java program logic to find whether list is circular 
linked list or not?

http://www.careercup.com/question?id=5095169533673472

Time/Space complexity: O(n)

"""


class Node:

    def __init__(self,value,node):
        self.value = value
        self.successor = node
        
    def isCircular(self):
        node = self.successor
        while node != None:
            if node.value == self.value:
                return True   
            node = node.successor
        return False