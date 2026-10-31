fname='day4part1.txt'
#fname='day4example1.txt'

with open(fname) as fp: data = fp.read().splitlines()

results=dict()

for row in data:
    id=row.split(' ')[0].split('=')[1]
    time=int(row.split(' ')[-1].split('=')[1])
    if id not in results.keys():
        results[id]=time
    else:
        results[id]+=time

sumtimes=sorted(list(results.values()))
total=0
for i,val in enumerate(sumtimes):
    total+=(i+1)*val
print('Part 1',total)

## PART 2 ##

fname='day4part2.txt'
#fname='day4example2.txt'

with open(fname) as fp: data = fp.read().splitlines()

results=dict()

for row in data:
    id=row.split(' ')[0].split('=')[1]
    time=int(row.split(' ')[-1].split('=')[1])
    #parts=int(row.split(' ')[-2].split('=')[1])
    if id not in results.keys():
        results[id]=[time,1]
    else:
        results[id]=[results[id][0]+time,results[id][1]+1]
maxval=0
for test in results.values():
    if test[1]>maxval:
        maxval=test[1]

summary=sorted(list(results.values()),key=lambda x: (maxval-x[1],x[0]))
total=0
for i,val in enumerate(summary):
    total+=(i+1)*val[0]
print('Part 2',total)

## PART 3 ##

fname='day4part3.txt'
fname='day4example3.txt'

with open(fname) as fp: data = fp.read().splitlines()

results=dict()

for row in data:
    id=row.split(' ')[0].split('=')[1]
    time=int(row.split(' ')[-1].split('=')[1])
    part=int(row.split(' ')[-2].split('=')[1])
    quest=int(row.split(' ')[1].split('=')[1])
    #print(id,quest,part,time)
    if (quest,part) not in results.keys():
        results[(quest,part)]=[[id,time]]
        #print(results)
    else:
        temp=list(results[(quest,part)])
        temp.append([id,time])
        results[((quest,part))]=temp

scores=dict()      
for val in results.values():
    #print(val)
    a=sorted(val,key=lambda x: (x[1]))
    print(a)