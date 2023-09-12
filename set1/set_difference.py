# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Miltiades Vasiliades 2944

# %%
from copy import deepcopy


# %%
R_sorted_path='R_sorted.tsv'
S_sorted_path='S_sorted.tsv'
intersection_out_path='RdifferenceS.tsv'
S=[]
R=[]
out=[]
R_prev=''
S_prev=''
with open(intersection_out_path,'w') as output:
    with open(R_sorted_path,'r',newline='\n') as R_sorted:
        with open(S_sorted_path,'r',newline='\n') as S_sorted:
            S = S_sorted.readline()
            S = S.split()
            R = R_sorted.readline()
            R = R.split()
            while R and S:
                while R == R_prev:
                    R = R_sorted.readline()
                    R = R.split()
                while S == S_prev:
                    S = S_sorted.readline()
                    S = S.split()                
                if R == S:
                    R_prev = deepcopy(R)
                    S_prev = deepcopy(S)
                    R = (R_sorted.readline()).split()
                    S = (S_sorted.readline()).split()
                elif R < S:
                    output.write(R[0]+'\t'+R[1]+'\n')
                    R_prev= deepcopy(R)
                    R = (R_sorted.readline()).split()
                elif R > S:
                    S_prev = deepcopy(S)
                    S = (S_sorted.readline()).split()
            while R:                     
               output.write(R[0]+'\t'+R[1]+'\n')
               R_prev = deepcopy(R)
               while R == R_prev and R:
                    R = R_sorted.readline()
                    R = R.split()     


# %%



