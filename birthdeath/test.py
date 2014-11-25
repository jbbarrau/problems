import birthdeath


people = [\
    (1901,1923),\
    (1921,1985),\
    (1927,1928),\
    (1945,1999),\
    (1977,1952),\
    (1942,1987),\
    (1943,1978),\
]    


test = birthdeath.Demography(people)
print test.MaxYearOfPopulation()