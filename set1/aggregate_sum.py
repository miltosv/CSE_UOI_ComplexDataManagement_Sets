# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Miltiades Vasiliades 2944

# %%
from copy import deepcopy


# %%
def readfile(filepath,table):
    with open(filepath) as R_file:
        for line in R_file:
            table.append([int(i) if i.isdigit() else i for i in line.split()])


# %%
def mergeSort(table
#,output
):
    if len(table) > 1:
        pivot = len(table) // 2
        L = table[:pivot]
        R = table[pivot:]
        mergeSort(R)
        mergeSort(L)

        i = k = j = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                table[k] = L[i]
                i = i + 1
            else:
                table[k] = R[j]
                j = j + 1
            k = k + 1
        while i < len(L):
            table[k] = L[i]
            i = i + 1
            k = k + 1
        while j < len(R):
            table[k] = R[j]
            j = j + 1
            k = k + 1


# %%
def aggregateSortedTable(table):
    aggregate = []
    if len(table)>1:
        aggregate.append(deepcopy(table[0]))
    j = 0
    for i in range(1,len(table)):
        if table[i][0] == aggregate[j][0]:
            aggregate[j][1] = aggregate[j][1] + deepcopy(table[i][1])
        else:
            aggregate.append(deepcopy(table[i]))
            j = j + 1
    return aggregate


# %%
def slow_sum(table):
    mergeSort(R_table)
    R_sum_slow = aggregateSortedTable(R_table)
    return R_sum_slow


# %%
def write_sum(table):
    with open('Rgroupby.tsv',mode='w')as output:
        for item in table:
            output.write(item[0]+'\t'+str(item[1])+'\n')


# %%
def mergeAggregate(table
#,output
):
    if len(table) > 1:
        pivot = len(table) // 2
        L = table[:pivot]
        R = table[pivot:]
        mergeAggregate(R)        
        mergeAggregate(L)
        i = k = j = 0
        while i < len(L) and j < len(R):
            if L[i][0] == R[j][0]:
                table[k][0] = L[i][0]
                table[k][1] = L[i][1] + R[j][1]
                i = i + 1
                j = j + 1
            else:
                k = k + 1
                if L[i] < R[j]:
                    table[k] = L[i]
                    i = i + 1                    
                else:
                    table[k] = R[j]
                    j = j + 1
        while i < len(L):
            if L[i][0] == table[k][0]:
                table[k][1] = table[k][1] + L[i][1]
            else:
                table[k] = L[i]
                k = k + 1
            i = i + 1
        while j < len(R):
            if R[j][0] == table[k][0]:
                table[k][1] = table[k][1] + R[j][1]
            else:
                table[k] = R[j]            
                k = k + 1
            j = j + 1


# %%


R_path = 'R.tsv'
R_sum = 'R_groupby_sum.tsv'
R_table=[]
R_sum = []



readfile(R_path,R_table)

#mergeSortAggregate(R_table)

R_sum = slow_sum(R_table)

write_sum(R_sum)


# %%



