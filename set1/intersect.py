# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Miltiades Vasiliades 2944

# %%
from copy import deepcopy


# %%
R_sorted_path='R_sorted.tsv'
S_sorted_path='S_sorted.tsv'
intersection_out_path='RintersectS.tsv'
S=[]
R=[]
out=[]
R_prev=[]
S_prev=[]
with open(intersection_out_path,'w') as output:
    with open(R_sorted_path,'r',newline='\n') as R_sorted:
        with open(S_sorted_path,'r',newline='\n') as S_sorted:
            for R in R_sorted:
                R=R.split()
                if R_prev == R:
                    continue
                R_prev = deepcopy(R)
                while True:
                    if S == R:
                        output.write(R[0]+'\t'+R[1]+'\n')
                        S_prev = deepcopy(S)
                        break 
                    elif S < R:
                        S_prev = deepcopy(S)
                        while True:
                            S = S_sorted.readline()
                            S = S.split()
                            if S != S_prev:
                                break
                        continue
                    elif S > R:
                        S_prev = deepcopy(S)
                        break 


# %%



