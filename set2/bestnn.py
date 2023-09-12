# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import ast
import heapq
import sys
#Miltiades Vasiliades

# %%
rfile = sys.argv[1]
qfile = sys.argv[2]
Rtree = []
results = []
query = []
k = 3
with open(rfile,'r') as rf:
    for line in rf:
        line = ast.literal_eval(line)
        Rtree.append(line)
del line,rf,rfile


# %%
def dist(q,mbr):
    from math import sqrt
    q = [float(item) for item in q]
    mbr = [float(item) for item in mbr]
    x=q[0]
    y=q[1]
    mxmin = mbr[0]
    mxmax = mbr[1]
    mymin = mbr[2]
    mymax = mbr[3]
    dx = 0
    dy = 0
    if x < mxmin:
        dx = mxmin - x
    if x > mxmax:
        dx = x - mxmax
    if y < mymin:
        dy = mymin - y
    if y > mymax:
        dy = y - mymax
    return sqrt( dx**2 + dy**2 )


# %%

def kNN_search(root_id,query,topk):
    k = topk
    global Rtree
    nn = []
    #heapq.heapify(H)
    distance = 99999999999999999999999999999999999999
    pq = []
    heapq.heapify(pq)
    isobject = 0
    for entry in Rtree[root_id][2]:
        #print(entry)
        ds = dist(query,entry[1])
        heapq.heappush(pq,[ds,entry,isobject])
        #heapq.heappush(pq,[ds,Rtree[root_id][0],Rtree[root_id][1]])
        #print(query)
        #print(pq[0])
    while k:
        e = pq[0]
        if e[2] == 1:
            heapq.heappop(pq)
        idx =e[1][0]
        #print(e[1][0],Rtree[e[1][0]][0])
        if Rtree[idx][0] == 1: #if entry shows not leaf
            isobject = 0
            n = Rtree[idx][2]
            #print('n', n)
            for entry in n:
                #print(entry)
                ds = dist(query,entry[1])
                if ds<distance:
                    #print(ds,entry)
                    heapq.heappush(pq,[ds,entry,isobject])

        else:
            isobject = 1
            n = Rtree[idx][2]
            for entry in n:
                ds = dist(query,entry[1])
                if ds<distance:
                    heapq.heappush(pq,[ds,entry,isobject])
                    nn = entry[0]
                    distance = ds
        k = k - 1
    print(nn)
    #heapq.heappush(H,pq[0][3][0])
    #print(H[0])
    #distance = pq[0][0]
    #print(distance)
    #while pq and dist(query,heapq)<

    



counter = 0
root_id = Rtree[-1][1]
with open (qfile,'r') as qf:
    query = qf.readline().split()
    kNN_search(root_id,query,k)
    print(counter,'(',len(results),'): ',results)
    
    while True:
        query = qf.readline().split() 
        counter = counter + 1
        if query:
            kNN_search(query,root_id)
            print(counter,'(',len(results),'): ',results)
            
        else:
            break
    


# %%



