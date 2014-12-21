"""
Given a binary search tree and a number n, write a program to find the greatest number in the binary search tree less than or equal to N.
Given the following tree construction, what is the output for N=44?

http://www.careercup.com/question?id=5765237112307712

Time complexity = O(log n)

"""

class BST:
    def __init__(self,key,leftTree,rightTree):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree
        
    def greatestNumberLessThanOrEqualTo(self,N):
        if self.key == N:
            return self.key
        elif self.key > N:
            if self.leftTree is None:
                return -1
            return self.leftTree.greatestNumberLessThanOrEqualTo(N)
        elif self.key < N:
            if self.rightTree is None:
                return self.key
            return self.rightTree.greatestNumberLessThanOrEqualTo(N)