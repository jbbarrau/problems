from tree import Tree


graph = {\
            'a': ['b','c','d'],\
            'b': ['e','f'],\
            'c': [],\
            'd': ['g','h','i','j'],\
            'e': ['k','l'],\
            'f': [],\
            'g': ['m'],\
            'h': ['p'],\
            'i': ['q'],\
            'j': ['r'],\
            'k': [],\
            'l': [],\
            'm': ['n'],\
            'n': ['o'],\
            'o': [],\
            'p': [],\
            'q': [],\
            'r': [],\
}          
testtree = Tree(graph,'a')