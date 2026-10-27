fname='day1part3.txt'
#fname='day1example1.txt'

with open(fname) as fp: data = fp.read().splitlines()

data=[int(a) for a in data[0].split(',')]
maxdata=max(data)

# Generate perfect squares until greater than maxdata
squares=[8]
i=5
while squares[-1] <= maxdata:
    squares.append(i*i-1)
    i+=2

#print(squares)

total=0
for cones in data:
    
    test=8
    i=0
    while cones > test:
        #print(i,squares[i])
        test=squares[i]
        i+=1
 #   print(cones,test,test-cones)
    total+=test-cones

print(total)