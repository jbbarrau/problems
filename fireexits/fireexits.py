# http://www.careercup.com/question?id=5649261284818944
#There are multiple rooms in a floor. There are one or more fire exits. Each door can be designed with 
#an option of pull or push. For fire safety, a door should be designed so as to open (push) towards the fire exit.
#Design a data structure to represent the floor and door design.  
#A person could start from any room and moves towards fire exit. 
#Write an algorithm to check if all the doors are designed to be pushed towards fire exit
# v = vertex / e = edge
# Time: O(v^2) - Space: O(v + e)

class Floor:

    def __init__(self,rooms):
    
        self.outsideworld = Room(-1,[])
        self.rooms = rooms
        
    def IsSecure(self):
        Yes = True
        for room in self.rooms:
            self.visitedrooms = []
            print "Path out of",room.index,":"
            Yes = Yes and self.IsThereAPathOut(room)
        return Yes
        
    def IsThereAPathOut(self,room):
            self.visitedrooms.append(room.index)
            if -1 in room.reachablerooms:
                print "-->",-1
                return True
            else:
                result = False
                for adjacentindex in room.reachablerooms: 
                    if not adjacentindex in self.visitedrooms:
                        result = result or self.IsThereAPathOut(self.rooms[adjacentindex])
                        if result:
                            print "-->",adjacentindex
                return result
            
class Room:
    def __init__(self,index,reachablerooms):
        self.index = index
        
        #Reachable rooms are rooms which can be accessed from another room thanks to a push door
        self.reachablerooms = reachablerooms    