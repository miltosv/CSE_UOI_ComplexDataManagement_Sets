# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Miltiades Vasiliades 2944

# %%
import sys
#MILTIADES VASILIADES 2944
def load_nodes(inputfile):
    nodes = []
    with open('out.txt',mode='r') as infile:
        for line in infile:
            line = line.split()
            #print (line)
            ID = line[0]
            X = line[1]
            Y = line[2]
            nei = line[3:]
            #print(nei)
            nei = [nei[x:x+2] for x in range(0, len(nei), 2)]
            #print(nei)
            node = [ID,X,Y,nei]
            #print(node)
            nodes.append(node)

    return nodes


# %%
def dijkstra_generator(start):
    import heapq
    global nodes
    iterations = 0
    SPD = []
    #path = []
    visited  = []
    SPD = [99999999999 for node in nodes]
    path = [[] for node in nodes]
    visited = [False for node in nodes]
    Q = []
    SPD[start] = 0
    heapq.heappush(Q,(SPD[start],str(start)))    
    while Q:
        v = heapq.heappop(Q)
        v = int(v[1])
        iterations = iterations + 1
        visited[v] = True
        yield (v,path[v],SPD[v])
        for u in nodes[v][3]:
            u_ptr = int(u[0])
            if (not visited[u_ptr]) and SPD[u_ptr] > SPD[v] + float(u[1]):
                SPD[u_ptr] = SPD[v] + float(u[1])
                path[u_ptr] = path[v] + [(v,u_ptr)]
                path.append(u_ptr)
                heapq.heappush(Q,(SPD[u_ptr],str(u[0])))
        


# %%
def best_place(lstofentries):
    global nodes
    import heapq
    best = []
    generators =  [dijkstra_generator(entry) for entry in lstofentries]
    #print(len(generators))
    distances = [[9999 for entry in entries]for node in nodes]
    paths = [ [[]for entry in entries] for node in nodes]

    S = []
    upper_bound = [9999 for node in nodes]
    lower_bound = [0 for node in nodes]
    #print(paths[-1])
    #print(len(distances),distances[-1])
    #while True:
    run = []
    for j in range (len(generators)):
        pairs = next(generators[j])
        #print(pairs,j)
        distances[pairs[0]][j] = pairs[2]
        paths[pairs[0]][j] = pairs[1]
        run.append([pairs[0],pairs[2]])
    bound = 9999
    nextorun = 0
    if 9999 not in distances[pairs[0]]:
        cost = max(distances[pairs[0]])
        heapq.heappush(best,(cost,pairs[0]))
    for i in range(len(run)):
        if run[i][1]<bound:
            bound = run[i][1]
            nextorun = run[i][0]
    print(bound,nextorun)    
    while not best:
        run = []
        
            #print(distances[pairs[0]])
            if 9999 not in distances[pairs[0]]:
                cost = max(distances[pairs[0]])
                heapq.heappush(best,(cost,pairs[0]))
        print(run)
        S.append(run)
    

    

        
        

    #print(best[0])

entries = [0,1,6,5]
nodes = load_nodes('out.txt')
#best_place(entries)
entries = sys.argv[1:]
best_place(entries)


# %%



