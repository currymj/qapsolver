import sys
import itertools

#n offices, n professors

#matrix of distances d[i][j]  that is the distances of two offices
#matrix of affinities a[i][j] that is the affinities of people

#we need to pair up people to offices

#perms is list of permutations. perm[0] = 2 means person 0 gets office 2

#generate a list of all permutations

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                #nb str[0:1] works in both string and list contexts
                yield perm[:i] + str[0:1] + perm[i:]

def solve(n, a, d):

    perms = list(itertools.permutations(range(n)))
    optVal = None
    optPerm = None

    for perm in perms:
        val = 0
        for i in range(0,n):
            for j in range(0,n):
                val = val + a[i][j]*d[perm[i]][perm[j]]
        if optVal == None or val < optVal:
            optVal = val
            optPerm = perm
    return optVal, optPerm

pfile = open(sys.argv[1], 'r') #sys.argv[1]

n = int(pfile.readline())

pfile.readline()

a = []

for i in range(n):
    l = pfile.readline().split()
    l2 = []
    for s in l:
        l2.append(int(s))
    a.append(l2)
    
b = []

pfile.readline()

for i in range(n):
    l = pfile.readline().split()
    l2 = []
    for s in l:
        l2.append(int(s))
    b.append(l2)

    #print(n)
    #print(a)
    #print(b)

print(solve(n, a, b))
