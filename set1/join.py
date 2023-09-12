# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Miltiades Vasiliades 2944
# Set #1
# %% [markdown]
# 

# %%
R_sorted_path='R_sorted.tsv'
S_sorted_path='S_sorted.tsv'
join_out_path='RjoinS.tsv'
max_buffer=0
buffer = []
S = ''
with open(join_out_path,'a') as output:
    with open(R_sorted_path,'r') as R_sorted:
        with open(S_sorted_path,'r') as S_sorted:
            for R in R_sorted:
                R_split=R.split()
                if len(buffer) == 0 and S:
                        S_split = S.split()
                        if R_split[0]==S_split[0]:
                            output.write(str(R_split[0]+'\t'+R_split[1]+'\t'+S_split[1]+'\n'))
                            buffer.append(S_split)
                        elif R_split[0]<S_split[0]:
                            continue
                elif(len(buffer)!=0):
                    #print(buffer)
                    if R_split[0] == buffer[0][0]:
                        for tpl in buffer:
                            output.write(str(R_split[0]+'\t'+R_split[1]+'\t'+tpl[1]+'\n'))
                        continue
                    else:
                        max_buffer = max(len(buffer),max_buffer)
                        buffer.clear()
                        continue
                while True:
                    S = S_sorted.readline()
                    if not S:
                        break
                    S_split=S.split()
                    if R_split[0]==S_split[0]:                            
                        output.write(str(R_split[0]+'\t'+R_split[1]+'\t'+S_split[1]+'\n'))
                        buffer.append(S_split)
                    else:
                        break                                               

print("Max Bufffer size for this operation:", max_buffer)              
                
                


