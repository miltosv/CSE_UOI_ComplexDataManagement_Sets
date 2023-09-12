# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Miltiades Vasiliades 2944

# %%
R_sorted_path='R_sorted.tsv'
S_sorted_path='S_sorted.tsv'
union_out_path='RunionS.tsv'
S=''
R=''
out=''
with open(union_out_path,'w',newline='\n') as output:
    with open(R_sorted_path,'r',newline='\n') as R_sorted:
        with open(S_sorted_path,'r',newline='\n') as S_sorted:
            R = R_sorted.readline()
            S = S_sorted.readline()
            R_temp = ''
            S_temp = S
            while R and S:
                while R == R_temp:
                    R=R_sorted.readline()
                if R < S:
                    output.write(R)
                    R_temp = R
                    R = R_sorted.readline()
                elif R>S:
                    output.write(S)
                    S_temp = S
                    S = S_sorted.readline()
                    while S == S_temp:
                        S = S_sorted.readline()
                elif R==S:
                    output.write(R)
                    R_temp = R
                    R = R_sorted.readline()
                    S_temp = S
                    S = S_sorted.readline()
                    while S == S_temp:
                        S = S_sorted.readline()
            while R:
                output.write(R)
                R_temp = R
                R = R_sorted.readline()
                while R == R_temp:
                    R = R_sorted.readline()
            
            while S:
                output.write(S)
                S_temp = S
                S = S_sorted.readline()
                while S == S_temp:
                    S = S_sorted.readline()
                    

            
                


# %%
r1='aa 34'
r2='bb 33'
r3=''
r1>r3


# %%



