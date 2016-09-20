# Author: Yuze Ma
# Date: Sept, 19th, 2016
# This code is made for Lab 3, Checkpoint 3

bpop = int(input('Number of bunnies ==> '))
print(bpop)
fpop = int(input('Number of foxs ==> '))
print(fpop)



def population_of_bunnies_for_the_next_year(bpop,fpop):
	bpop_next = (10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop
	return bpop_next 

def population_of_foxes_for_the_next_year(bpop,fpop):
	fpop_next = 0.4 * fpop + 0.02 * fpop * bpop
	return fpop_next

print('Yaer 1:', bpop, fpop)

bpop_1 = int(population_of_bunnies_for_the_next_year(bpop,fpop))
fpop_1 = int(population_of_foxes_for_the_next_year(bpop,fpop))

print('Yaer 2:', bpop_1, fpop_1)

bpop = int(population_of_bunnies_for_the_next_year(bpop_1,fpop_1))
fpop = int(population_of_foxes_for_the_next_year(bpop_1,fpop_1))

print('Yaer 3:', bpop, fpop)

bpop_1 = int(population_of_bunnies_for_the_next_year(bpop,fpop))
fpop_1 = int(population_of_foxes_for_the_next_year(bpop,fpop))

print('Yaer 4:', bpop_1, fpop_1)

bpop = int(population_of_bunnies_for_the_next_year(bpop_1,fpop_1))
fpop = int(population_of_foxes_for_the_next_year(bpop_1,fpop_1))

print('Yaer 3:', bpop, fpop)

