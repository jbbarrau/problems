"""
The third question is a brain teaser: if 1000 couples are to give birth to male and female babies(50% change each), 
and they would keep giving birth until they have a girl, what's the boy to girl ratio in 20 years

http://www.careercup.com/question?id=5101786763362304

-> Response

50 / 50

Every year one couple out of 2 does a girl the other one a boy
--> Partition remains 50/50
The next iteration half of the couples remain. Same story. One of two does a boy, the other a girl.
--> Partition remains 50/50

etc... until we don't have any couple anymore


"""



class Population:

    def __init__(self,couples):
        self.couples = couples        
    
    @classmethod
    def prob_to_get_a_girl_after_year(cls, n):
        if n == 1:
            return 0.5
        if n == 0:
            return 0
        return Population.prob_to_get_a_girl_after_year(n-1) + (0.5) ** n