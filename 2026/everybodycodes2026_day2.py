fname='day2part1.txt'
fname='day2part2.txt'
fname='day2part3.txt'
#fname='day2example2.txt'
#fname='day2example1.txt'
#fname='day2example3.txt'

with open(fname) as fp: data = fp.read().splitlines()

total=0
for row in data:
    if fname!='day2part2.txt' and fname!='day2part3.txt':
        hard = ['1','2','3','4','5']
    else:
        hard = ['1','2','3','4','5','6','7','8','9']
    print(hard)
    repeat=True
    while repeat:
        test = []
        for pair in row.split(' '): 
            left = hard.index(pair[0])
            right = hard.index(pair[2])
            op = pair[1]

            if op == '<':
                if left<right:
                    hard[left],hard[right]=hard[right],hard[left]
                    test.append(True)
                else:
                    test.append(False)
            elif op == '>':
                if left>right:
                    hard[left],hard[right]=hard[right],hard[left]
                    test.append(True)
                else:
                    test.append(False)
            else: print('ruh roh')
        repeat &= any(test)
    a=int(''.join(hard))
    total+=a
print(total)
