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

thousandyears=1000*365*24*3600
class Player:
    def __init__(self,name):
        self.name=name
        self.times=[[-1*thousandyears,-1*thousandyears,-1*thousandyears,-1*thousandyears]]
        self.sums=[[-1*thousandyears,-1*thousandyears,-1*thousandyears,-1*thousandyears]]

    def calc_sums(self):
        for i in range(1,len(self.times)):
            self.sums[i][1]=self.times[i][1]
            self.sums[i][2]=self.times[i][1]+self.times[i][2]
            self.sums[i][3]=self.times[i][1]+self.times[i][2]+self.times[i][3]


fname='day4part3.txt'
# fname='day4example3.txt'
# fname='day4example3withties.txt'

with open(fname) as fp: data = fp.read().splitlines()

# find total results and players, will go through list twice but whatever
nquest=0
npart=0
nid=0
for row in data:
    id=int(row.split(' ')[0].split('=')[1])
    part=int(row.split(' ')[-2].split('=')[1])
    quest=int(row.split(' ')[1].split('=')[1])
    if id>nid: nid=id
    if part>npart: npart=part
    if quest>nquest: nquest=quest

#create player instances, initialize all result vectors to -1000*365*24*3600 seconds (1000 years)
Players=[Player(0)]

for i in range(1,nid+1):
    Players.append(Player(i))
for player in Players:
    for n in range(1,nquest*npart+1):
        player.times.append([-1*thousandyears,-1*thousandyears,-1*thousandyears,-1*thousandyears])
        player.sums.append([-1*thousandyears,-1*thousandyears,-1*thousandyears,-1*thousandyears])
  
for row in data:
    id=int(row.split(' ')[0].split('=')[1])
    time=int(row.split(' ')[-1].split('=')[1])
    part=int(row.split(' ')[-2].split('=')[1])
    quest=int(row.split(' ')[1].split('=')[1])
    Players[id].times[quest][part]=time
    
for player in Players:
    player.calc_sums()

ranks=dict()
for quest in range(1,nquest+1):
    for part in range(1,npart+1):
        temp=[]
        for player in Players:
            temp.append([player.name,player.sums[quest][part]])
        temp=temp[1:]
        temp=sorted(temp,key=lambda x: (x[1] if x[1]>0 else -1*x[1]))
        points=part*50
        tiecount=0
        scores=[]
        prevtime=thousandyears
        for i,a in enumerate(temp):
            if i>0:
                if a[1]==prevtime:
                    tiecount+=1
                else:
                    points-=1+tiecount
                    if points<0: points=0
                    tiecount=0
            if a[1]>0:
                scores.append(points)
            else:
                scores.append(0)
            
            prevtime=a[1]
        ranks[(quest,part)]=[]
        for i,a in enumerate(temp):
            ranks[(quest,part)].append([a[0],scores[i]])

totals=[0 for a in range(len(Players))]
for vals in ranks.values():
    for pair in vals:
        totals[pair[0]]+=pair[1]

totals=sorted(totals,reverse=True)

checksum=0
prevtotal=thousandyears
rank=1
tiecount=0
for i,a in enumerate(totals):
    if i>0:
        if a==prevtotal:
            tiecount+=1
        else:
            rank+=1+tiecount
            tiecount=0
    prevtotal=a
    checksum+=a*rank
print('Part 3',checksum)
