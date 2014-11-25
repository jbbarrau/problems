# http://www.careercup.com/question?id=5145121580384256
# n is the number of balls (n = 3^d)
# Time: O(log n) - Space: O(n)

class BallSet:

    def __init__(self,ballset):
        
        #ballset is list of 81 weights
        #the index is the identifier of the ball
        # 81 = 3 * 3 * 3 * 3
       
        self.pickedlist = []
        listlength = len(ballset)
        inputlist = ballset
        while listlength != 1:
            listlength = listlength/3
            firstpart = inputlist[0:listlength]
            secondpart = inputlist[listlength:2*listlength]
            thirdpart = inputlist[2*listlength:3*listlength]
            remaininglist, listnumber = self.minimumweight(firstpart,secondpart,thirdpart)
            self.pickedlist.append(listnumber)
            inputlist = remaininglist
        
    def GetBallId(self):
        multiplier = 27
        index = 0
        for i in self.pickedlist:
            index += i * multiplier
            multiplier /= 3       
        return index
        
    def minimumweight(self,a,b,c):
        # a,b,c are sublists: We use the fact that 2 of the lists of the same weight whereas one is lighter
        if self.sum(a) < self.sum(b):
            return (a,0)
        elif self.sum(b) < self.sum(c):
            return (b,1)
        elif self.sum(c) < self.sum(a):
            return (c,2)
        
    def sum(self,list):
        totalWeight = 0
        for weight in list:
            totalWeight += weight
        return totalWeight