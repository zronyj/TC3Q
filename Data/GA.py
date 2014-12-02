import random, string

# Creates the first generation
def first_gen(population=100,dimension=10,interval=1,tipo=0):
    unit = []
    for j in range(population):
        chromosome = []
        if tipo == 0:
            for i in range(dimension): chromosome.append(random.random()*interval)
        elif tipo == 1:
            for i in range(dimension): chromosome.append(int(random.random()*interval))
        unit.append(chromosome)
    return unit

# Makes crossovers between chromosomes
def recombine(unit, frac_point=3):
    while frac_point >= len(unit[0]) or frac_point == 0:
        print "Fracture point out of range.\n\n Recalculating ...\n\n"
        frac_point = int(random.random()*len(unit[0]))
    offsprings = []
    for i in range(len(unit)):
        for j in range(i+1,len(unit)):
            offsprings.append( unit[i][:frac_point] + unit[j][frac_point:] )
    return unit + offsprings

# Introduces mutations in the chromosomes
def mutation(unit, mut_factor=0.1, interval=1):
    total = int(random.random()*mut_factor)
    for i in range(total):
        mutant = int(random.random()*len(unit))
        gene = int(random.random()*len(unit[mutant]))
        if type(unit[mutant][gene]) == float:
            unit[mutant][gene] = random.random()
        elif type(unit[mutant][gene]) == int:
            unit[mutant][gene] = int(random.random()*interval)
    return unit

# Deletes chromosomes which are the same (everyone is unique!)
def multi_del(unit):
    unique = [unit[0]]
    for i in unit:
        ctrl = 0
        for j in unique:
            if i != j:
                ctrl += 1
        if ctrl == len(unique):
            unique.append(i)
    return unique

# Function defining which chromosome is the best (CHANGES FOR DIFFERENT APPLICATIONS)
def scoring(chromosome):
    ctrl = 0
    for i in chromosome:
        ctrl += i
    return ctrl

# Kills the chromosomes which are too weak
def natural_sel(unit, limit=10):
    scores = []
    for i in unit:
        scores.append(scoring(i))
    top = []
    for j in range(limit):
        high = 0
        posi = 0
        for k in list(set(range(len(scores))) - set(top)):
            if scores[k] > high:
                high = scores[k]
                posi = k
        top.append(posi)
    best = []
    for l in range(len(top)):
        best.append(unit[top[l]])
    return best

# Just something to visualize the best chromosome
def results(unit):
    print "*"*60
    print "\t\t\tResults"
    print "*"*60
    print "\n\tScore\tChromosome\n"
    for i in range(len(unit)):
        print "\t" + str(scoring(unit[i])) + "\t" + str(unit[i])
    print "\n" + "*"*60

# Commented genetic algorithm
def GAv(initial_pop=100, generations=5, chrom_len=10, interval=1, kind=1, mut=0.1, expected=50, final_pop=10):
    print "*"*60 + "\n\t\tGenetic Algorithm\n" + "*"*60 + "\n\n"
    print "- Creating first population:", initial_pop
    unit = first_gen(initial_pop, chrom_len, interval, kind)
    for i in range(generations):
        print "\n\n- Making generation:", i+1, "\n"
        unit = recombine(unit, int(random.random()*chrom_len))
        print "-- Recombined!\tPopulation:", len(unit)
        unit = mutation(unit, mut, interval)
        print "-- Mutated!\tMutants:",int(len(unit)*mut)
        unit = multi_del(unit)
        print "-- Filtered!\tPopulation:", len(unit)
        unit = natural_sel(unit, expected)
        print "-- Selected!\tPopulation:", len(unit)
    unit = natural_sel(unit, final_pop)
    print "\n\n- Final population:", len(unit)
    print "\n-Process finished!\n\n" + "*"*60
    results(unit)
    return unit

def GA(initial_pop=100, generations=5, chrom_len=10, interval=1, kind=1, mut=0.1, expected=50, final_pop=10):
    unit = first_gen(initial_pop, chrom_len, interval, kind)
    for i in range(generations):
        unit = recombine(unit, int(random.random()*chrom_len))
        unit = mutation(unit, mut)
        unit = multi_del(unit)
        unit = natural_sel(unit, expected)
    unit = natural_sel(unit, final_pop)
    return unit
