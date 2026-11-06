fname='day8part1.txt'
# fname='day8part2.txt'
# fname='day8part3.txt'
# fname='day8example1.txt'
fname='day8example2.txt'

def calculateEnergy(trees,direction):
    # direction=(1,1)
    # if data[0][-1]=='↘':
    #     direction=(1,1)
    # print(data[0][-1])
    # print(direction)
    # trees=data[0:]
    # print(len(trees))
    shadows=[[0 for a in range(len(trees[0]))] for b in range(len(trees))]
    res=[['.' for a in range(len(trees[0]))] for b in range(len(trees))]
    # print(trees)
    print(direction)
    total=0


    if direction==(1,1):
        for i,row in enumerate(trees):
            for j,pos in enumerate(row):
                if pos!='.':
                    if i>0 and j>0:
                        shadows[i][j]=max(shadows[i-direction[0]][j-direction[1]]-1,int(trees[i][j]))
                    else:
                        shadows[i][j]=int(trees[i][j])
                    # print(int(trees[i][j]),shadows[i][j])
                    if int(trees[i][j])>=shadows[i-direction[0]][j-direction[1]]:
                        res[i][j]=trees[i][j]
                        total+=1

    elif direction==(1,-1):
            for i,row in enumerate(trees):
                for j,pos in enumerate(row):
                    if pos!='.':
                        if i>0 and j<(len(trees[0])-1):
                            shadows[i][j]=max(shadows[i-direction[0]][j-direction[1]]-1,int(trees[i][j]))
                        else:
                            shadows[i][j]=int(trees[i][j])
                        # print(int(trees[i][j]),shadows[i][j])
            for i,row in enumerate(trees):
                for j,pos in enumerate(row):
                    if pos!='.':
                        if i>0 and j<(len(trees[0])-1):
                            if int(trees[i][j])>=shadows[i-direction[0]][j-direction[1]]:
                                res[i][j]=trees[i][j]
                                total+=1
                        elif i==0 or j==len(trees[0])-1:
                            res[i][j]=trees[i][j]
                            total+=1

    elif direction==(0,-1):
                for i,row in enumerate(trees):
                    for j,pos in enumerate(row):
                        if pos!='.':
                            if j<(len(trees[0])-1):
                                shadows[i][j]=max(shadows[i-direction[0]][j-direction[1]]-1,int(trees[i][j]))
                            else:
                                shadows[i][j]=int(trees[i][j])
                            # print(int(trees[i][j]),shadows[i][j])
                for i,row in enumerate(trees):
                    for j,pos in enumerate(row):
                        if pos!='.':
                            if j<(len(trees[0])-1):
                                if int(trees[i][j])>=shadows[i-direction[0]][j-direction[1]]:
                                    res[i][j]=trees[i][j]
                                    total+=1
                            elif j==len(trees[0])-1:
                                res[i][j]=trees[i][j]
                                total+=1

   
    for row in shadows:
        print(''.join(str(a) for a in row))
    print('')
    for row in res:
        print(''.join(a for a in row))    
    print(total)
    print('')
    return total


with open(fname) as fp: data = fp.read().splitlines()

### PART 1 ###

direction=(1,1)
print(calculateEnergy(data,(1,1)))

### PART 2 ###
directions=[(1,1), (1,-1), (0,-1), (-1,-1), (-1,1), (0,1)]
total=0
for direction in directions:
    total+=calculateEnergy(data,direction)
print(total)






# if data[0][-1]=='↘':
#     direction=(1,1)
# print(data[0][-1])
# print(direction)
# trees=data[0:]
# print(len(trees))
# shadows=[[0 for a in range(len(trees[0]))] for b in range(len(trees))]
# res=[['.' for a in range(len(trees[0]))] for b in range(len(trees))]
# print(trees)
# total=0
# for i,row in enumerate(trees):
#     for j,pos in enumerate(row):
#         if pos!='.':
#             if i>0 and j>0:
#                 shadows[i][j]=max(shadows[i-direction[0]][j-direction[1]]-1,int(trees[i][j]))
#             else:
#                 shadows[i][j]=int(trees[i][j])
#             # print(int(trees[i][j]),shadows[i][j])
#             if int(trees[i][j])>=shadows[i-direction[0]][j-direction[1]]:
#                 res[i][j]=trees[i][j]
#                 total+=1
# for row in shadows:
#     print(''.join(str(a) for a in row))

# for row in res:
#     print(''.join(a for a in row))
# print('')
# print(total)



    