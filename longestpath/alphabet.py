"""

given matrix like : 

a b e d 
b c f e 
a b d d 

find the longest path of consecutive alphabets given a starting alphabet. 
You can move in all 8 directions
for eg a->b(right)->c(down)->d(diagnal down) len = 4 , find max such len

http://www.careercup.com/question?id=5727802043138048

Time/space complexity: O(n^2)

"""


class LettersMatrix:
    
    def __init__(self, matrix):
        self.height = len(matrix)
        self.length = len(matrix[0])
        self.matrix = matrix
        
        self.startingnodes = []
        self.graph = {}
        
        for i in range(0, self.height):
            for j in range(0, self.length):
                if self.matrix[i][j] == 'a':
                    self.startingnodes.append((i,j))
                    self.explore((i,j))
                
                
    def explore(self, (i, j)):
        successors = []
        if i > 0 and i < self.height - 1:
            if j > 0 and j < (self.length - 1):            
                neighbors = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
            elif j > 0: 
                neighbors = [(i-1,j-1),(i-1,j),(i,j-1),(i+1,j-1),(i+1,j)]
            elif j < (self.length - 1):
                neighbors = [(i-1,j),(i-1,j+1),(i,j+1),(i+1,j),(i+1,j+1)]
        elif i > 0:
            if j > 0 and j < (self.length - 1):            
                neighbors = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1)]
            elif j > 0: 
                neighbors = [(i-1,j-1),(i-1,j),(i,j-1)]
            elif j < (self.length - 1):
                neighbors = [(i-1,j),(i-1,j+1),(i,j+1)]
        elif i < (self.height - 1):
            if j > 0 and j < (self.length - 1):            
                neighbors = [(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
            elif j > 0: 
                neighbors = [(i,j-1),(i+1,j-1),(i+1,j)]
            elif j < (self.length - 1):
                neighbors = [(i,j+1),(i+1,j),(i+1,j+1)]

        for (k,l) in neighbors:
            if ord(self.matrix[k][l]) == ord(self.matrix[i][j]) + 1:
                successors.append((k,l))
            
        self.graph[(i,j)] = successors
        for successor in successors:
            self.explore(successor)
            
    
    def longest_graph_path(self):
        return self.max_path_length(self.startingnodes)
    
    def max_path_length(self,nodelist):
        path_lengths = []
        for node in nodelist:
            successors = self.graph[node]
            if successors == []:
                path_lengths.append(1)
            else:
                path_lengths.append(1 + self.max_path_length(successors))
        return max(path_lengths)
                
                

        