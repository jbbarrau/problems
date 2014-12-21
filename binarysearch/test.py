from binarysearch import BST



tree = BST(40,\
            BST(20,\
                BST(10,
                    BST(5,None,None),\
                    BST(15,None,None),\
                ),\
                BST(30,
                    BST(20,None,None),\
                    BST(35,None,None),\
                ),\
            ),\
            BST(80,\
                BST(60,
                    BST(50,None,None),\
                    BST(70,None,None),\
                ),\
                BST(100,
                    BST(90,None,None),\
                    BST(110,None,None),\
                ),\
            )\
        )
        
print tree.greatestNumberLessThanOrEqualTo(5)
print tree.greatestNumberLessThanOrEqualTo(1115)
print tree.greatestNumberLessThanOrEqualTo(73)
print tree.greatestNumberLessThanOrEqualTo(51)