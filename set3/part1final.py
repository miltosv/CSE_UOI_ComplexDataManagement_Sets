#Miltiades Vasiliades 2944

import sys
def write_nodes_to_output(nodes):
    with open('out.txt',mode='w')as out:
        for entry in nodes:
            flattened = [val for sublist in entry[3] for val in sublist]
            out.write(" ".join(entry[:3])+' ')
            out.write(" ".join(flattened))
            out.write('\n')

nodes = []
edge = ''
cal_edge = 'cal.cedge'
cal_node = 'cal.cnode'
with open(cal_node) as node_f:
    for node in node_f:
        node = node.split()
        adj = []
        node.append(adj)
        nodes.append(node)

with open(cal_edge) as edge_f:
    for edge in edge_f:
        edge = edge.split()

        source_edge = edge[2:]
        nodes[int(edge[1])][3].append(source_edge)        

        source_node = edge[1:2]
        dest_node = edge[2:3]
        edge = edge[3:]
        edge[0:0] = source_node

        nodes[int(dest_node[0])][3].append(edge)

write_nodes_to_output(nodes)