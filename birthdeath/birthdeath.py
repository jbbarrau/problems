# http://www.careercup.com/question?id=5153263227764736
# Time: O(n) - Space: O(1)
# Sorting of the keys of demographyevolution is always on less than 100 elements. So it does not depend on n, the population.

class Demography:

    def __init__(self,people):
    
        # people is a list of tuple (birthyear,deathyear)
        # E.g: [(1912,1946),(1922,1949)]
        
        self.demographyevolution = {}
        
        for (birthyear,deathyear) in people:
            if not birthyear in self.demographyevolution.keys():
                self.demographyevolution[birthyear] = 0
            if not deathyear in self.demographyevolution.keys():
                self.demographyevolution[deathyear] = 0
            self.demographyevolution[birthyear] += 1
            self.demographyevolution[deathyear] -= 1
            
    def MaxYearOfPopulation(self):
        population = 0
        maxpop = 0
        maxyear = 1900
        for year in sorted(self.demographyevolution.keys()):
            population += self.demographyevolution[year]
            if population > maxpop:
                maxpop = population
                maxyear = year
                
        return maxyear