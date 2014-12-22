"""

An efficient way to sort patient files in an array of just 3 types 'High-importance', 'Mid-importance', 'Low-importance' 
which are in an arbitrary order (unsorted). 

The output preference should start with the highest. 

1. High-importance 
2. Mid-importance 
3. Low-importance 

Time/Space complexity: O(n)

http://www.careercup.com/question?id=5080405046722560

""" 

class PatientFile:

    def __init__(self,priority):
        self.priority = priority
        
    def __cmp__(self,other):
        map = { "High": 1,\
                "Mid": 2,\
                "Low": 3,\
            }  
        return cmp(map[self.priority],map[other.priority])
        
    def __str__(self):
        return self.priority
    
    
    
class PatientList:
    def __init__(self,files):
        self.files = files
        
    def __str__(self):
        return str([str(file) for file in self.files])
        
    def sort(self):
                
        i = 0                   # Index of list traversing
        l = 0                   # Index of already sorted smaller items
        h = len(self.files) - 1 # Index of already sorted larger items

        
        while i <= h:
        
            # If is greater than pivot - Swap it with item at the end of the list - Final position for self.files[i]
            # End of the list (3rd partition) does not need to be sorted anymore
            # Potentially, new item self.files[i] coming from swap needs to be sorted. i is not incremented
            if self.files[i] > PatientFile("Mid"):   
                buf = self.files[i] 
                self.files[i] = self.files[h]
                self.files[h] = buf
                                
                h -= 1
                
            # If is less - Swap it with item just after the end of 1st partition
            # Beginning of the list (1st partition does not need to be sorted anymore
            # Since we already traverse the new swapped item previously we know it is a mid value.
            # Thus, we are in the 2nd partition with index i. We can increment i
            # Remark: We have to increment i. l should not get greater than i
            elif self.files[i] < PatientFile("Mid"):
                buf = self.files[i]
                self.files[i] = self.files[l]
                self.files[l] = buf
                
                l += 1
                i += 1
                
            # It is equal - Keep it in the middle of the list (2nd partition) and visit next item
            else:
                i += 1
                
                
            print "-- 1st partition index:", l
            print "-- 2nd partition index:", i
            print "-- 3rd partition index:", h
            print self
