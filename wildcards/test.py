from wildcards import Generator


gen = Generator("0?1?")
gen1 = Generator("01?")
gen2= Generator("01")
gen3= Generator("01?0???100?1")
gen4= Generator("???????")

print gen.Combinations()
print gen1.Combinations()
print gen2.Combinations()
print gen3.Combinations()
print gen4.Combinations()



