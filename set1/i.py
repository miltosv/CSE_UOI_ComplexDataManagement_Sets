R_sorted_path='R_sorted.tsv'
S_sorted_path='S_sorted.tsv'
intersection_out_path='R_S.tsv'
S=''
R=''
out=''
with open(intersection_out_path,'a') as output:
    with open(R_sorted_path,'r',newline='\n') as R_sorted:
        with open(S_sorted_path,'r',newline='\n') as S_sorted:
            while True:
                R_temp = deepcopy(R)
                while True:
                    R = R_sorted.readline()
                    R = R.split()
                    if (not R == R_temp) or (not R):
                        break
                S_temp = deepcopy(S)
                while True:
                    S = S_sorted.readline()
                    S = S.split()
                    if (not S == S_temp) or (not S):
                        break
                if (not R) and (not S):
                    break
                if R == S:
                    output.write(R[0]+'\t'+R[1]+'\n')
                else:
                    continue