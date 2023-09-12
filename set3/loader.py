# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
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


