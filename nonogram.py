f = open("nonogram.in", "r")
n = int(f.readline())
m = int(f.readline())
print(n, m)
conjs = []
next_free_idx = n*m + 1
for i in range(n):
    rule = list(map(int, (f.readline().split())))
    print(rule)
    # number of additional variables for each number in rule
    r_vars = n - sum(rule) - len(rule) + 2
    print(r_vars)
    # Part 1
    for j in range(len(rule)):
        # for each number in rule at least one of its additional variables is True
        conjs.append(' '.join([str(k) for k in range(next_free_idx+j*r_vars, next_free_idx+(j+1)*r_vars)]))
        # for each number in rule at most one of its additional variables is True
        for k in range(next_free_idx+j*r_vars, next_free_idx+(j+1)*r_vars):
            for l in range(k+1, next_free_idx+(j+1)*r_vars):
                conjs.append('-'+str(k)+' -'+str(l))
    # Part 2
    for j in range(len(rule)-1):
        offset = next_free_idx+j*r_vars
        # if var[offset+k] is True then var[offset+r_vars+k] or var[offset+r_vars+k+1] or var[offset+r_vars+k+2] or ...
        # we can ignore var[offset] because var[offset+r_vars] or var[offset+r_vars+1] or ... is already in part 1
        for k in range(1, r_vars):
            conjs.append('-'+str(offset+k)+' '+' '.join([str(offset+r_vars+l) for l in range(k, r_vars)]))
        # there is no need to do same things backwards because of part 1 (exactly one is true)
    # Part 3
    for j in range(m):
        # In this part we relate cells with our additional variables
        corr = []
        s = 1
        for idx, v in enumerate(rule):
            e = s+v-1
            for k in range(r_vars):
                if e+k >= j+1 >= s+k:
                    corr.append(str(next_free_idx+idx*r_vars+k))
            s = e+2
        print(corr)
        # var[i*m+j] is True if and only if disjunction of corresponding additional variables is True
        conjs.append('-'+str(i*m+j+1)+' '+' '.join(corr))
        for x in corr:
            conjs.append(str(i*m+j+1)+' -'+x)
    next_free_idx += r_vars*len(rule)
for i in range(m):
    rule = list(map(int, (f.readline().split())))
    print(rule)
    # number of additional variables for each number in rule
    r_vars = m - sum(rule) - len(rule) + 2
    print(r_vars)
    # Part 1
    for j in range(len(rule)):
        # for each number in rule at least one of its additional variables is True
        conjs.append(' '.join([str(k) for k in range(next_free_idx+j*r_vars, next_free_idx+(j+1)*r_vars)]))
        # for each number in rule at most one of its additional variables is True
        for k in range(next_free_idx+j*r_vars, next_free_idx+(j+1)*r_vars):
            for l in range(k+1, next_free_idx+(j+1)*r_vars):
                conjs.append('-'+str(k)+' -'+str(l))
    # Part 2
    for j in range(len(rule)-1):
        offset = next_free_idx+j*r_vars
        # if var[offset+k] is True then var[offset+r_vars+k] or var[offset+r_vars+k+1] or var[offset+r_vars+k+2] or ...
        # we can ignore var[offset] because var[offset+r_vars] or var[offset+r_vars+1] or ... is already in part 1
        for k in range(1, r_vars):
            conjs.append('-'+str(offset+k)+' '+' '.join([str(offset+r_vars+l) for l in range(k, r_vars)]))
        # there is no need to do same things backwards because of part 1 (exactly one is true)
    # Part 3
    for j in range(n):
        # In this part we relate cells with our additional variables
        corr = []
        s = 1
        for idx, v in enumerate(rule):
            e = s+v-1
            for k in range(r_vars):
                if e+k >= j+1 >= s+k:
                    corr.append(str(next_free_idx+idx*r_vars+k))
            s = e+2
        print(corr)
        # var[i*n+j] is True if and only if disjunction of corresponding additional variables is True
        conjs.append('-'+str(i*n+j+1)+' '+' '.join(corr))
        for x in corr:
            conjs.append(str(i*n+j+1)+' -'+x)
    next_free_idx += r_vars*len(rule)
print(conjs)
f.close()
# prepare input for minisat
mf = open('minisat.in', 'w')
total_vars = next_free_idx - 1
print("total vars: ", total_vars)
mf.write('p cnf '+str(total_vars)+' '+str(len(conjs)))
for c in conjs:
    mf.write('\n')
    mf.write(c)
mf.close()

