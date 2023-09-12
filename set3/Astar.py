#MILTIADES VASILIADES 2944

import sys
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
def calc_dist(x1,y1,x2,y2):
    from math import sqrt
    dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    return dist
def A_star(start,end):
    import heapq
    global nodes    
    iterations = 0
    SPD = [99999999999 for node in nodes]
    path = [[] for node in nodes]
    visited = [False for node in nodes]
    dist = []
    for i in range(len(nodes)):
        args  = (nodes[end][1],nodes[end][2],nodes[i][1],nodes[i][2])
        args = tuple(map(float,args))
        dst = calc_dist(args[0],args[1],args[2],args[3])
        dist.append(dst)    
    Q = []
    SPD[start] = 0
    heapq.heappush(Q,(SPD[start]+dist[start],str(start)))
    while Q:
        #print(Q)
        v = heapq.heappop(Q)
        v = int(v[1])
        iterations = iterations + 1
        visited[v] = True
        if v == end:
            print('iterations',iterations)
            print('distance',SPD[end])
            return path[end]        
        for u in nodes[v][3]:
            u_ptr = int(u[0])

            if (not visited[u_ptr]) and ( SPD[u_ptr] > (SPD[v] + float(u[1]) ) ):
               SPD[u_ptr] = SPD[v] + float(u[1])
               path[u_ptr] = path[v] + [(v,u_ptr)]
               heapq.heappush(Q, ( (SPD[u_ptr] + dist[u_ptr]) ,str(u[0])))

nodes = load_nodes('out.txt')
print(A_star(int(sys.argv[1]),int(sys.argv[2])))