import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import seaborn as sns

file_ref=sys.argv[1]
file_qry=sys.argv[2]

def sharedPCs(v1,v2):
    vc1_vcs=list(set(v1))
    vc2_vcs=list(set(v2))
    
    inter=list(set(vc1_vcs)&set(vc2_vcs))
    # Shared vcs dir
    vc1_dir={}
    for vc in vc1_vcs:
        vc1_dir[vc]=1
    vc2_dir={}
    for vc in vc2_vcs:
        vc2_dir[vc]=1
        
    vc1_n=0
    vc2_n=0
    for vc in inter:
        if vc1_dir.get(vc)!=None:
            vc1_n+=1
        if vc2_dir.get(vc)!=None:
            vc2_n+=1
            
    vc1_sh=vc1_n/float(len(vc1_vcs))
    vc2_sh=vc2_n/float(len(vc2_vcs))

    try:
        return np.average([vc1_sh,vc2_sh])
    except:
        return 0

# Reading test files
refs_dir={}
queries_dir={}
with open(file_ref) as inFile:
    for line in inFile:
        toks=line.strip().split('\t')
        refs_dir[toks[0]]=toks[1:]
with open(file_qry) as inFile:
    for line in inFile:
        toks=line.strip().split('\t')
        queries_dir[toks[0]]=toks[1:]

X=[]
for uv1 in queries_dir.keys():
    X.append([])
    for uv2 in refs_dir.keys():
        X[-1].append(sharedPCs(queries_dir[uv1],refs_dir[uv2]))

with open('vMatch_matrix.txt','w') as outFile:
    for h in range(len(X[0])):
        outFile.write(list(refs_dir.keys())[h]+'\t')
    outFile.write('\n')
    for i in range(len(X)):
        outFile.write(list(queries_dir.keys())[i]+'\t')
        for j in range(len(X[0])):
            outFile.write(str(X[i][j])+'\t')
        outFile.write('\n')

sns.clustermap(X,vmin=0,vmax=0.8,cmap=plt.cm.Blues,col_cluster=True,row_cluster=True)
plt.savefig('vMatch_heatmap.png')
