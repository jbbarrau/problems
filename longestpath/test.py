from alphabet import LettersMatrix

matrix = [\
    ['a','b','e','d'],\
    ['b','c','f','e'],\
    ['a','b','d','d'],\
    ]
    
    
matrix = LettersMatrix(matrix)

#print matrix.graph

print matrix.longest_graph_path()