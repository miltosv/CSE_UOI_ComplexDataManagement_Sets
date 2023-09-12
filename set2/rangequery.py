# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Miltiades Vasiliades 2944

# %%
import ast
import sys
# Miltiades Vasiliades 2944
# %%
rfile = sys.argv[1]
qfile = sys.argv[2]
Rtree = []
results = []
query = []
with open(rfile,'r') as rf:
    for line in rf:
        line = ast.literal_eval(line)
        Rtree.append(line)
    
# Miltiades Vasiliades 2944

# %%
def intersects(query,mbr):
    qx_low=query[0]
    qy_low=query[1]
    qx_high=query[2]
    qy_high=query[3]

    x_low = mbr[0]
    x_high = mbr[1]
    y_low = mbr[2]
    y_high = mbr[3]
    
    return not (x_high <= qx_low or x_low >= qx_high or y_high <= qy_low or y_low >= qy_high)
def range_search(query,node):
    global Rtree  
    global results
    if Rtree[node][0] == 0: #if it's leaf
        for entry in Rtree[node][2]:
            location_id = entry[0]
            mbr = entry[1]
            if intersects(query,mbr):
                results.append(location_id)
    else: #if not leafnode
        for entry in Rtree[node][2]:
            node_id = entry[0]
            mbr = entry[1]
            #print('mbr', mbr)
            #print('query',query)
            if intersects(query,mbr):
                range_search(query,Rtree[node_id][1])
counter = 0
root_id = Rtree[-1][1]
with open (qfile,'r') as qf:
    query = qf.readline().split()
    #query = ['-170.707084', '-14.287277', '-170.844179',  '-14.373776']
    range_search(query,root_id)
    print(counter,'(',len(results),'): ',results)
    results =[]
    while True:
        query = qf.readline().split() 
        counter = counter + 1
        if query:
            range_search(query,root_id)
            print(counter,'(',len(results),'): ',results)
            results=[]
            
        else:
            break
    


# %%



