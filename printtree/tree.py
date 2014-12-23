"""


Give a tree (any tree, can be a binary. I told the interviewer that I assume it is binary tree and he said that is fine). Print the tree content on the screen one tree level per line 
i.e. 
if a tree is like this: 
a 
/ \ 
b c 
/ / 
e f 
The output would be 
a 
bc 
ef 


http://www.careercup.com/question?id=5169384622391296

"""



class N:
    def __init__(self,value,children):
        self.value = value
        self.children = children
    

        
class Tree:
    def __init__(self,graph,root):
    
        graph.delete(root)
        return N(root, [Tree(graph.delete(root),child) for child in graph[root]])

        
        
    def printit(self):
        pass
        