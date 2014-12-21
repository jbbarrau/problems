"""

Replace wild cards with all possible combinations of zeros and ones using recursion.

http://www.careercup.com/question?id=6332042201530368

Average: O(log n)
Worst case: O(n)

E.g: "011?"

"""


class Generator:
    def __init__(self,pattern):
        self.pattern = pattern
        self.combinations = []
        
    def Combinations(self):
        index = self.pattern.find('?')
        
        if index == -1:
            return [self.pattern]
        else:
            head = self.pattern[:index]
            tail = self.pattern[index+1:]
            combinations = []
            for combination in Generator(tail).Combinations():
                combinations.append(head+"0"+combination)
                combinations.append(head+"1"+combination)
            return combinations
        
        
        