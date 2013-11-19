# given a pair of cost matrices
# compute matrix L as given in li et al for a given 1..n
# solve linear assignment problem (using the Hungarian method)


from munkres import Munkres, print_matrix
    

def minpdp(v,w):
    # computes a permutation with minimum permuted dot product of vectors v and w
    # pairs largest with smallest, next largest with next smallest, and so on and so on
    #perm = [None for n in range(len(v))]
    #vperm = sorted(range(n), key=lambda k: v[k])
    #wperm = sorted(range(n), key=lambda k: w[k],reverse=True)
    vs = sorted(v)
    ws = sorted(w,reverse=True)
    return reduce(lambda x,y:x+y, [vs[i] * ws[i] for i in range(len(v))])
    

    
def lb(a,b):
    n = len(a)

    l = [ [minpdp([a[i][ind] for ind in range(n) if ind != i],[b[j][ind] for ind in range(n) if ind != j]) for j in range(n)] for i in range(n) ]

    # now solve linear assignment problem on l
    m = Munkres()

    indices = m.compute(l)

    print indices

    total = 0
    for row, column in indices:
        val = l[row][column]
        total += val
        print '(%d, %d) -> %d' % (row,column,val)
    return total
