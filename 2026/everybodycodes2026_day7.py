fname='day7part1.txt'
fname='day7part2.txt'
# fname='day7example1.txt'
fname='day7example3.txt'

with open(fname) as fp: data = fp.read().splitlines()

start='0'
maxcon=0
clouds=dict()
for row in data:
    temp=row.split(', ')
    id=str(temp[0].split('=')[1])
    energy=int(temp[1].split('=')[1])
    connections=[a for a in temp[2].split('=')[1].split(',')]
    # print(id,energy,connections)
    if len(connections)>maxcon: 
        start=id
        maxcon=len(connections)
    clouds[id]=[energy,connections]

# print(clouds)
# print(start)

if fname[-5:]=='1.txt': 
    strength=5
else:
    strength=10

# targets=[start]
# while strength>0:
#     nexttargets=[]
#     for target in targets:
#         clouds[target][0]+=strength
#         for next in clouds[target][1]:
#             nexttargets.append(next)
#     strength-=1
#     targets=[a for a in nexttargets]


# total = sum([a[0] for a in clouds.values()])
# print(total)

### PART 3 ###

start='2'
targets=[start]
listoftargets=[targets]
explodestrength=10
impulses=[strength]
explodelim=100
# print(sum(impulses))
stage=1
while sum(impulses)>0:
   
    nexttargets=[]
    explodetargets=[]
    for idx,targets in enumerate(listoftargets):
        for target in targets:
            if target in clouds.keys():
                clouds[target][0]+=impulses[idx]
                for next in clouds[target][1]:
                    nexttargets.append(next)
        impulses[idx]-=1
        if impulses[idx]<0: impulses[idx]=0
        targets=[a for a in nexttargets]
    listoftargets[0]=targets
    print('')
    print(stage)
    print(clouds)
    print(impulses)
    print(listoftargets)
    stage+=1

    # explode stuff
    exploded=[]
    explodetargets=[]
    for cloud in clouds.keys():
        if clouds[cloud][0]>=explodelim:
            impulses.append(explodestrength)
            explodetargets.append(clouds[cloud][1])
            exploded.append(cloud)

    for explodetarget in explodetargets:
        listoftargets.append(explodetarget)

    for explode in exploded:
        del clouds[explode]

    for cloud in clouds.keys():
            for explode in exploded:
                if explode in clouds[cloud][1]:
                    clouds[cloud][1].remove(explode)
    print(exploded)

#need to propagate target lists after the explosion, they don't just keep coming from the same source over and over

print(clouds)

total = sum([a[0] for a in clouds.values()])
print('Part 3',total)

