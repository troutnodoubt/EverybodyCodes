fname='day9part1.txt'
fname='day9part2.txt'
# fname='day9part3.txt'
# fname='day9example1.txt'
# fname='day9example2.txt'

with open(fname) as fp: data = fp.read().splitlines()

### PART 1 ###

total=0
for row in data:
    growth=int(row.split(', ')[1].split('=')[1])
    limit=int(row.split(', ')[2].split('=')[1])
        
    branches=[1]
    time=1
    nodes=0
    while True:
        # print(time,branches,nodes)
        branches=[a+1 for a in branches]
        time+=1
        a=len(branches)
        for i in range(a):
            if branches[i]>=growth:
                temp=branches[i]//2
                branches[i]=temp
                branches.append(temp)
                branches.append(1)
                nodes+=1
        if sum(branches)+nodes>=limit:
            break
        
    total+=time
print('Part 1',total)

## PART 2 ##
total=0
for row in data:
    growth=int(row.split(', ')[1].split('=')[1])
    limit=int(row.split(', ')[2].split('=')[1])
        
    branches=[1]
    hassplit=[False]
    time=1
    nodes=0
    while True:
        branches=[a+1 for a in branches]
        time+=1
        a=len(branches)
        for i in range(a):
            if branches[i]>=growth:
                temp=branches[i]//2
                branches[i]=temp
                branches.append(temp)
                branches.append(1)
                if hassplit[i]:
                    hassplit.append(True)
                else:
                    hassplit.append(False)
                hassplit.append(False)

                if not hassplit[i]:
                    hassplit[i]=True
                nodes+=1
       
        if hassplit.count(False)>=limit:
            break

    total+=time
print('Part 2',total)

    