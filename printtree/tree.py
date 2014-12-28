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
    
    	children = graph[root]
    	del graph[root]
    	
    	self.node = N(root, [Tree(graph,child).node for child in children])

        
        
    def __str__(self):

		level = {}
		string = ''
		level[0] = [self.node]
		
		while level.keys() != []:
		
			currentdepth = max(level)
			newdepth = currentdepth + 1
			
			for node in level[currentdepth]:
				if not newdepth in level:
					level[newdepth] = []
				level[newdepth] += node.children
			
			for node in level[currentdepth]:
				string += str(node.value)+' '
			string += '\n'
			del level[currentdepth]
			
		return string 
        
        