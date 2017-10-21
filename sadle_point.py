
# coding: utf-8

# In[8]:

def saddle_point(matrx):
    row_min=[min(val) for val in matrx]
    col_max=[max(val) for val in zip(*matrx)]
    sad_pt=set(row_min).intersection(col_max)
    if len(sad_pt):
        return("saddle_pt==>",sad_pt.pop())
    else:
        return "No Saddle point"
if __name__=='__main__':
    n = int(input().strip())
    m = int(input().strip())
    for i in range(n):
        matrx[i] = [int(j) for j in input().strip().split(" ")][:m]
    print(saddle_point(matrx))






