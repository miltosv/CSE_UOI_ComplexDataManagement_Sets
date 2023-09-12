# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Miltiades Vasiliades 2944

# %%
import ast
import time
import sys

# %%

#queries_path='queries.txt'
#transactions_path='transactions.txt'

transactions_path=sys.argv[1]
queries_path=sys.argv[2]
qnum = int(sys.argv[3])
method = int( sys.argv[4])

transactions = []
with open(transactions_path) as tf:
    for line in tf:
        transaction = ast.literal_eval(line)
        transactions.append(transaction)

queries = []

with open(queries_path) as qf:
    for line in qf:
        q = ast.literal_eval(line)
        queries.append(q)

# %%
def naive_query(questions):
    questions = sorted(questions)
    results = []
    for t in range(len(transactions)):
        st = transactions[t]
        st = sorted(st)
        contains = False
        i = 0
        for q in questions:
            if contains:
                contains = False
            while i < len(st):
                if st[i] < q:
                    i += 1
                elif st[i] == q:
                    contains = True
                    i += 1
                else:
                    break
            if not contains:
                break
        if contains:
            results.append(t)                                   
    
    return set(results)


# %%
def setify(sequence):
    seq = sorted(sequence,reverse=True)
    previous = seq.pop(0)
    out = []
    out.append(previous)
    for number in seq:
        if number == previous:
            continue
        else:
            out.append(number)
            previous = number
    return out
#setify([3,4,9,9,9,9,9,9,9,9,9,9,9,4,0])


# %%
def mapbit(sequence):
    seq = setify(sequence)
    bitmap = ['0']
    bitmap = bitmap * (seq[0]+1)
    for item in seq:
        bitmap[item] = '1'
    bitmap.reverse()
    return ''.join(bitmap)

#mapbit([0,1])


# %%
sigfile = [int(mapbit(ts),2) for ts in transactions]
with open('sigfile.txt',mode = 'w') as sf:
    sf.write('\n'.join([str(x) for x in sigfile]))     


# %%
def sigfile_query(questions):
    global sigfile
    results = []
    query_signature = int(mapbit(questions), 2)
    for t in range(len(sigfile)):
        if (query_signature & (~sigfile[t]) ) == 0:
            results.append(t)
    return set(results)
#sigfile_query(queries[0])


# %%
def create_bitslice():
    global transactions
    bitslices = {}
    for t in range(len(transactions)):
        tr = setify(transactions[t])
        for element in tr:
            if element in bitslices:
                bitslices[element] = bitslices[element] + pow(2,t)
            else:
                bitslices[element] = pow(2,t)
    return bitslices
def write_dict_to_json(dct,name,sep):
    import json
    with open(name,mode='w') as f:
        f.write(json.dumps(dct,sort_keys=True,separators=sep))

def write_dict_to_csv(dct,name):
    with open(name,mode='w',newline='\n') as fp:
        import csv    
        writer = csv.writer(fp)
        for key, value in sorted(dct.items()):
            writer.writerow([key, value])


# %%
bitslices = create_bitslice()
#write_dict_to_json(bitslices,'bitslice.txt',('\n', ':'))
write_dict_to_csv(bitslices,'bitslice.txt')


# %%
def bitslice_query(questions):
    global bitslices
    results = []
    queryAND = '1'*len(transactions)
    queryAND = int(queryAND,2)
    #print(queryAND)
    for q in questions:
        queryAND = queryAND & bitslices[q]

    queryAND = format(queryAND, 'b')[::-1]
    for i in range(len(queryAND)):
        if int(queryAND[i]):
            results.append(i)
    return set(results)       
#bitslice_query(queries[0])


# %%
def inverted_index_creator():
    global transactions
    inverted = {}
    for t in range(len(transactions)):
        ts = transactions[t]
        ts = setify(ts)
        for item in ts:
            if item in inverted:
                inverted[item].append(t)
            else:
                inverted[item] = [t]
    return inverted
            


# %%
inverted_index = inverted_index_creator()
#write_dict_to_file(inverted_index,'invfile.txt',(",",':'))
write_dict_to_csv(inverted_index,'invfile.txt')


# %%
def join_merge_intersect(L1,L2):
    from copy import deepcopy
    L1 = deepcopy(L1)
    L2 = deepcopy(L2)
    i = 0
    j = 0
    result = []
    while i<len(L1) and j<len(L2):
        if L1[i] < L2[j]:
            i += 1
        elif L1[i] == L2[j]:
            result.append(L1[i])
            i += 1
            j += 1
        else:
            j +=1
    return result
#join_merge_intersect([1,3,4,5],[1,3,4,6])


# %%
def inverted_query(questions):
    global inverted_index
    results = []
    q = setify(questions)
    intermediate = [sorted(inverted_index[i]) for i in q]
    if len(intermediate) == 1:
        results = intermediate.pop()
    elif len(intermediate) >= 2:
        #print('at least 2')
        L1 = intermediate.pop()
        L2 = intermediate.pop()
        results = join_merge_intersect(L1,L2)
        while len(intermediate):
            #print('more than 2')
            results = join_merge_intersect(results,intermediate.pop())
    return set(results)
#print(inverted_query(queries[0]))


# %%
def ask(queryID,method):
    methods = {
        0 : naive_query,
        1 : sigfile_query,
        2 : bitslice_query,
        3 : inverted_query
    }
    if method > -1:    
        if queryID == -1:
            for query in queries:
                print(methods[method](query))
        else:        
            t1 = time.time()
            print(methods[method](queries[queryID]))
            t2 = time.time()
            print('Time Elapsed method',methods[method].__name__,'is',t2-t1)

    elif method == -1:
        if queryID == -1:
            for method in methods:
                t1 = time.time()
                for query in queries:
                    #print(methods[method](query))
                    methods[method](query)
                t2 = time.time()
                print('Time Elapsed method',methods[method].__name__,'is',t2-t1,'for ALL QUERIES')
        else:
            for method in methods:        
                t1 = time.time()
                methods[method](queries[queryID])
                t2 = time.time()
                print('Time Elapsed method',methods[method].__name__,'is',t2-t1)


# %%


        
ask(qnum,method)



'''
ask(0,0)
ask(0,1)
ask(0,2)
ask(0,3)
'''



# %%



