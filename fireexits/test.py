import fireexits

# room1 = fireexits.Room(0,[-1])
# room2 = fireexits.Room(1,[0,2])
# room3 = fireexits.Room(2,[4])
# room4 = fireexits.Room(3,[0])
# room5 = fireexits.Room(4,[3])
# room6 = fireexits.Room(5,[4])

# rooms = [room1,room2,room3,room4,room5,room6]


room1 = fireexits.Room(0,[1])
room2 = fireexits.Room(1,[2])
room3 = fireexits.Room(2,[0,3,5])
room4 = fireexits.Room(3,[4,6])
room5 = fireexits.Room(4,[-1,2])
room6 = fireexits.Room(5,[4])
room7 = fireexits.Room(6,[-1])

rooms = [room1,room2,room3,room4,room5,room6,room7]

test = fireexits.Floor(rooms)
print test.IsSecure()