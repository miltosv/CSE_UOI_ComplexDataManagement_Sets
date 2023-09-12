# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Miltiades Vasiliades 2944

# %%
import pymorton
from itertools import islice
from copy import deepcopy
import sys
# Miltiades Vasiliades 2944
# %%
# Miltiades Vasiliades 2944
coords_p=sys.argv[1]
offsets_p=sys.argv[2]
polygons = []
mbrs = []
mbr_centres=[]
z_curves=[]
prev_start=0
with open(coords_p) as coordinates:
    with open(offsets_p) as offsets:
        for offset in offsets:
            pointers = [ int(x) for x in offset.split(sep=',') ]
            prev_start=pointers[1]
            polygon = [line.strip().split(sep=',') for line in islice(coordinates,pointers[1]-prev_start, pointers[2]-pointers[1]+1)]
            max_x = max(map(lambda x: x[0], polygon))
            min_x = min(map(lambda x: x[0], polygon))
            max_y = max(map(lambda x: x[1], polygon))
            min_y = min(map(lambda x: x[1], polygon))
            mbrs.append([pointers[0],[min_x,max_x,min_y,max_y]])
            centre = [(float(max_x)+float(min_x))/2,(float(max_y)+float(min_y))/2]
            #mbr_centres.append(centre)
            z_curves.append([pointers[0],pymorton.interleave_latlng(centre[1],centre[0])])
z_curves.sort(key = lambda x: x[1])
mbrs = [mbrs[i] for i in [idx[0] for idx in z_curves]]
del mbr_centres



# %%
Tree = []
B = 20
queue = []
lvl = 0
isnonleaf = 0
node_id = 0
for i in range(0,len(mbrs),B):
    #print(i,B+i)
    #node = []
    nodeentries = mbrs[i:i+B]
    queue.append((node_id,nodeentries,lvl))
    Tree.append([isnonleaf,node_id,nodeentries])
    node_id = node_id + 1
    #print(queue[0])
print(len(queue),' nodes at level ',lvl)
## This fixes occupancy
if len(queue)>=2 and len(queue[-1][1])<8:
    print('size is for ',queue[-1][0], 'is', len(queue[-1][1]), '< 8 redirstributing using',queue[-2][0])
    difference = 8 - len(queue[-1][1])
    to_be_moved = queue[-2][1][-difference:]
    while to_be_moved:
        queue[-1][1].insert(0,to_be_moved.pop())
    del queue[-2][1][-difference:]
    print('new sizes are', queue[-1][0] ,'size:', len(queue[1][1]), queue[-2][0],'size:', len(queue[-2][1]))

# %%
isnonleaf = 1
how_many_nodes = 0
changelvl = False
reachedRoot=False
node = []
while len(queue)>1:
    i = 0
    e = []
    while i<20 and queue:
        if queue[0][2] == lvl:
            e = queue.pop(0)
            bounding = [x[1] for x in e[1]]
            xs = [item for sublist in [x[:2] for x in bounding] for item in sublist]
            ys = [item for sublist in [x[2:] for x in bounding] for item in sublist]
            max_x = max(xs)
            min_x = min(xs)
            max_y = max(ys)
            min_y = min(ys)
            node.append([e[0],[min_x,max_x,min_y,max_y]])
            i = i + 1
        else:
           changelvl=True
           break
    if node:
        queue.append((node_id,node,lvl+1))
        if len(queue)!=1:
            Tree.append([isnonleaf,node_id,node])
        node_id = node_id + 1
        how_many_nodes = how_many_nodes + 1
        node = []
    
    if changelvl:
        lvl = lvl + 1
        print(how_many_nodes,' nodes at level ', lvl)
        how_many_nodes =0
        node = []
        changelvl = False    

    if len(queue)>=2 and len(queue[1][1])<8 and queue[0][2]==queue[1][2]:
        print('size is for ',queue[1][0], 'is', len(queue[1][1]), '< 8 redirstributing using',queue[0][0])
        difference = 8 - len(queue[1][1])
        to_be_moved = queue[0][1][-difference:]
        while to_be_moved:
            queue[1][1].insert(0,to_be_moved.pop())
        del queue[0][1][-difference:]
        print('new sizes are', queue[1][0] ,'size:', len(queue[1][1]), queue[0][0],'size:', len(queue[0][1]))

print(len(queue),'nodes at root,',queue[0][2],'level')
root=queue.pop()
Tree.append([isnonleaf,root[0],root[1]])
  


# %%
with open('Rtree.txt','w') as output:
    [output.write(str(item)+'\n') for item in Tree]


# %%



