def isoscore(iso,vote):
    while len(iso) < len(vote):
            for i in range(len(iso)):
                    iso.append(iso[i])
    iso=iso[len(iso)-len(vote):]
    score=0
    for i in range(len(iso)):
        score+=int(vote[i])*int(iso[i])**(len(iso)-i-1)
    return score

### PART 1 ###

fname='day3part1.txt'
#fname='day3example1.txt'

with open(fname) as fp: data = fp.read().splitlines()

total=0
for row in data:
    iso = [str(a) for a in row.split(' ')[0].split('-')[1]]
    vote = [str(a) for a in row.split(' ')[1]]   
    total+=isoscore(iso,vote)
print('Part 1',total)

### PART 2 ###

fname='day3part2.txt'
#fname='day3example2.txt'

with open(fname) as fp: data = fp.read().splitlines()

total=0
for row in data:
    iso = [str(a) for a in row.split(' ')[0].split('-')[1]]
    vote = [str(a) for a in row.split(' ')[1]]
    total+=isoscore(iso,vote)
print('Part 2',total)

### PART 3 ###

fname='day3part3.txt'
#fname='day3example3.txt'

with open(fname) as fp: data = fp.read().splitlines()

total=0
for row in data:
    iso = [str(a) for a in row.split(' ')[0].split('-')[1]]
    vote = [str(a) for a in row.split(' ')[1]]
    isValid=True
    max=row.split(' ')[1]
    test=isoscore(iso,vote)
    for i in range(int(max)):
        testvote=[a for a in str(i)]
        cand = isoscore(iso,testvote)
        if cand==test:
            isValid=False
            break
    if isValid:
        total+=test
print('Part 3',total)
