# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import ast
import sys
import time
import heapq


# %%
transactions_path = sys.argv[1]
queries_path = sys.argv[2]
transactions = []
with open(transactions_path) as tf:
    for line in tf:
        transaction = ast.literal_eval(line)
        transactions.append(transaction)


# %%
def setify(sequence):
    seq = sorted(sequence,
    #reverse=True
    )
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

# %% [markdown]
# def inverted_index_creator():
#     global transactions
#     inverted = {}
#     for t in range(len(transactions)):
#         ts = transactions[t]
#         ts = setify(ts)
#         for item in ts:
#             if item in inverted:
#                 inverted[item].append(t)
#             else:
#                 inverted[item] = [t]
#     return inverted

# %%
def count_trf_in_transaction(trf,transaction):
    tr = setify(transaction)
    #print(tr)
    for item in tr:
        if item in trf:
            trf[item] = trf[item] + 1
        else:
            trf[item] = 1


# %%
def count_occ_of_item_in_transaction(occ,transaction,t):    
    for item in transaction:
        if item in occ:            
            if t in occ[item]:
                occ[item][t] = occ[item][t] + 1
            else:
                occ[item][t] = 1
        else:
            occ[item] = {t : 1}


# %%
def count_trf_occ_of_item_all_transactions():
    global transactions
    trf = {}
    occ = {}
    for t in range(len(transactions)):
        tr = transactions[t]
        count_trf_in_transaction(trf,tr)
        count_occ_of_item_in_transaction(occ,tr,t)
    return (trf,occ)
trf_occ = count_trf_occ_of_item_all_transactions()
trf = trf_occ[0]
occ = trf_occ[1]


# %%
#print(trf[0])
#print(occ[15][5])


# %%
ratio = {}
T = len(transactions)
for i in trf:
    ratio[i] = T/trf[i]


# %%
def write_dict_to_file(dct,name):
    global ratio
    with open(name,mode='w',newline='\n') as fp:
        for k in sorted(dct):
            fp.write(str(k)+':')
            list_of_lists = [list(elem) for elem in dct[k].items()]
            fp.write(str(ratio[k])+', ')
            fp.write(str(list_of_lists))
            fp.write('\n')       

write_dict_to_file(occ,'invfileocc.txt')


# %%
def rel(t,q):
    result = 0.0
    query = setify(q)
    for item in query:
        if t in occ[item]:
            result += occ[item][t] * ratio[item]
    return result


# %%
queries = []

with open(queries_path) as qf:
    for line in qf:
        q = ast.literal_eval(line)
        queries.append(q)


# %%
def merge(l1,l2):
    import copy
    lst1 = copy.deepcopy(l1)
    lst2 = copy.deepcopy(l2)
    res = []
    if lst1 and (not lst2):
        res = lst1
        return res
    elif lst2 and (not lst1):
        res = lst2
        return res
    if not(lst1 and lst2):
        return []        
    i = 0
    j = 0
    while i<len(lst1) and j<len(lst2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        elif lst1[i] == lst2[j]:
            res.append(lst1[i])
            i += 1
            j += 1
        else:
            res.append(lst2[j])
            j +=1
    
    if i<len(lst1):
        res = res + lst1[i:]
        return res
    if j<len(lst2):
        res = res + lst2[j:]
        return res

#print(merge([],[2,9,99]))


# %%
def inverted_relevance(query):
    contain = [list(occ[x].keys()) for x in query]
    merged = []
    #print(query)
    while contain:
        merged = merge(merged,contain.pop())
    
    #print(merged)
    if not merged:
        return []
    topk = []
    for transaction in merged:
        score = rel(transaction,query)
        heapq.heappush(topk,[-score,transaction])
    #print(topk[0])
    return topk


# %%
def naive(query):
    global transactions
    global trf
    def counter(t):
        count = {}
        for i in t:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return count
    #print(query)
    topk = []
    for t in range(len(transactions)):
        count = {}
        count = counter(transactions[t])
        #print(count)
        #break
        score = 0.0
        for item in query:
            if item in count:
                score += count[item]*ratio[item]
        if score>0:
            heapq.heappush(topk,[-score,t])
    return topk
def test_naive():
    testresult = naive(queries[0])
    i = 2
    while testresult and i>0:
        r = heapq.heappop(testresult)
        r[0] = -r[0]
        print(r)
        i -= 1
#test_naive()


# %%
def ask(queryID,method,k):
    global transactions
    global queries
    methods={
        0 : naive,
        1 : inverted_relevance
    }

    def printtopk(topk,k):
        while topk and k>0:
            r = heapq.heappop(topk)
            r[0] = -r[0]
            print(r)
            k -= 1


    if method > -1:    
        if queryID == -1:
            t1 = time.time()
            for query in queries:
                methods[method](query)
            t2 = time.time()
            print('Time Elapsed method',methods[method].__name__,'is',t2-t1,'for all the queries in the file')
        else:        
            t1 = time.time()
            results = methods[method](queries[queryID])
            t2 = time.time()
            printtopk(results,k)
            print('Time Elapsed method',methods[method].__name__,'is',t2-t1)

    elif method == -1:
        if queryID == -1:
            for method in methods:
                t1 = time.time()
                for query in queries:
                    methods[method](query)
                t2 = time.time()
                print('Time Elapsed method',methods[method].__name__,'is',t2-t1,'for all the queries in the file')
        else:
            for method in methods:        
                t1 = time.time()
                methods[method](queries[queryID])
                t2 = time.time()
                print('Time Elapsed method',methods[method].__name__,'is',t2-t1)


# %%
#ask(-1,-1,2)
ask(int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))

# %%



