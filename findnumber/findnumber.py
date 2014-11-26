# http://www.careercup.com/question?id=5722969366069248
# Let's we search the first index of the digit. Neighbors are 0,+1,-1
# Time: O(n) in worst case / O(log n) in average case - Space: O(n)
# Example of array [1,2,2,1,0,-1,0,0,1,2]

class IntegerArray:


    def __init__(self,listofnumbers):
        self.listofnumbers = listofnumbers
        
    
    def GetNumberBasic(self,num):
        i = 0
        for number in self.listofnumbers:
            if number == num:
                return i
            i += 1
        return -1
            
            
    def GetNumber(self,num):
        i = 0
        while i < len(self.listofnumbers):
            if self.listofnumbers[i] == num:
                return i
            else:  
                i += abs(num-self.listofnumbers[i])
        return -1