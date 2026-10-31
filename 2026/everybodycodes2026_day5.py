fname='day5part1.txt'
fname='day5part2.txt'
fname='day5part3.txt'
# fname='day5example1.txt'

with open(fname) as fp: data = fp.read().splitlines()

map=[]
for row in data:
    temp=[]
    for c in row:
        temp.append(c)
    map.append(temp)
    

def isLand(row,col,maxrow,maxcol):
    # corners are always not land
    rowdirs=[]
    coldirs=[]
    if (row==0 and (col==0 or col==maxcol)) or (row==maxrow and (col==0 or col==maxcol)):
        pass
    # edges have to index only in the possible direction
    elif row==0 and col!=0 and col!=maxcol: #top row
        rowdirs=[0,1]
        coldirs=[-1,0,1]
    elif row==maxrow and col!=0 and col!=maxcol: #bottom row
        rowdirs=[-1,0]
        coldirs=[-1,0,1]
    elif row!=0 and row!=maxcol and col==0: #left column
        rowdirs=[-1,0,1]
        coldirs=[0,1]
    elif row!=0 and row!=maxcol and col==maxcol: #right column
        rowdirs=[-1,0,1]
        coldirs=[-1,0]
    else:
        rowdirs=[-1,0,1]
        coldirs=[-1,0,1]
    landcount=0
    already=False
    for rowoffset in rowdirs:
        for coloffset in coldirs:
            if map[row+rowoffset][col+coloffset]=='1' or map[row+rowoffset][col+coloffset]=='#':
                if rowoffset!=0 or coloffset!=0:
                    landcount+=1
            if map[row+rowoffset][col+coloffset]=='#':
                already=True
    if landcount>=5 and already:
        map[row][col]='#'

def isSand(row,col,maxrow,maxcol):
    # corners are always not land
    rowdirs=[]
    coldirs=[]
    isSand=False
    isEdge=False
    if (row==0 and (col==0 or col==maxcol)) or (row==maxrow and (col==0 or col==maxcol)):
        isEdge=True
    # edges have to index only in the possible direction    
    elif row==0 and col!=0 and col!=maxcol: #top row
        rowdirs=[0,1]
        coldirs=[-1,0,1]
        isEdge=True
    elif row==maxrow and col!=0 and col!=maxcol: #bottom row
        rowdirs=[-1,0]
        coldirs=[-1,0,1]
        isEdge=True
    elif row!=0 and row!=maxcol and col==0: #left column
        rowdirs=[-1,0,1]
        coldirs=[0,1]
        isEdge=True
    elif row!=0 and row!=maxcol and col==maxcol: #right column
        rowdirs=[-1,0,1]
        coldirs=[-1,0]
        isEdge=True
    else:
        rowdirs=[-1,0,1]
        coldirs=[-1,0,1]
    sandcount=0
    
    for rowoffset in rowdirs:
        for coloffset in coldirs:
            if map[row][col]=='#' and map[row+rowoffset][col+coloffset]=='=':
                sandcount+=1
            elif map[row][col]=='#' and map[row+rowoffset][col+coloffset]!='#':
                isSand=True
            elif map[row][col]=='#' and isEdge:
                isSand=True

    if sandcount>=5 or isSand:
        map[row][col]='='

def isTree(row,col,maxrow,maxcol):
    padding=2
    
    rowdirs=[-2,-1,0,1,2]
    coldirs=[-2,-1,0,1,2]

    if row-padding<0 or row+padding>maxrow:
        return
    if col-padding<0 or col+padding>maxcol:
        return

    count=0
    for rowoffset in rowdirs:
        for coloffset in coldirs:
            notCorner=False
            if rowoffset not in [-2,2] or coloffset not in [-2,2]:
                notCorner=True
            
            if (map[row][col]=='#' 
                and (map[row+rowoffset][col+coloffset]=='#' or map[row+rowoffset][col+coloffset]=='@')
                and notCorner):
                count+=1
        if count==21:
            map[row][col]='@'

def growTree(row,col,maxrow,maxcol,cmap):
    padding=1
    
    rowdirs=[-1,0,1]
    coldirs=[-1,0,1]

    if row-padding<0 or row+padding>maxrow:
        return
    if col-padding<0 or col+padding>maxcol:
        return

    count=0
    for rowoffset in rowdirs:
        for coloffset in coldirs:                        
            if (cmap[row][col]=='#' 
                and cmap[row+rowoffset][col+coloffset]=='@'):
                count+=1
        if count>=4:
            map[row][col]='@'

def countLand(c):
    count=0
    for row in map:
        count+=row.count(c)
    return count

def printMap():
    for row in map:
        for c in row:
            print(c,end='')
        print('')    

### PART 1 ###

#seed the center
maxrows=len(map)
maxcols=len(map[0])

map[(maxrows-1)//2][(maxcols-1)//2]='#'

while True:
    startCount=countLand('#')
    for row in range(maxrows):
        for col in range(maxcols):
            isLand(row,col,maxrows-1,maxcols-1)
    endCount=countLand('#')
    if startCount==endCount:
        break

print('Part 1',countLand('#'))

### PART 2 ###

while True:
    startCount=countLand('=')
    for row in range(maxrows):
        for col in range(maxcols):
            isSand(row,col,maxrows-1,maxcols-1)
    endCount=countLand('=')
    if startCount==endCount:
        break

print('Part 2',countLand('='))

### PART 3 ###

for row in range(maxrows):
    for col in range(maxcols):
        isTree(row,col,maxrows-1,maxcols-1)

cmap=tuple(tuple(a) for a in map)
for row in range(maxrows):
    for col in range(maxcols):
        growTree(row,col,maxrows-1,maxcols-1,cmap)

cmap=tuple(tuple(a) for a in map)
for row in range(maxrows):
    for col in range(maxcols):
        growTree(row,col,maxrows-1,maxcols-1,cmap)

print('Part 3',countLand('@'))
