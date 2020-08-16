vMatch
========

Tool to explore bacteriophage phylogeny based on protein clusters

<b>Requirements:</b>
* Python (tested v3.6.7)
* Numpy (tested v1.17.0)

<b>Usage:</b> 
```
vMatch.py <genomes_ref> <genomes_queries>
```

<genomes_ref>: File containing associated PCs per reference genome (one genome per line) <br />
<genomes_queries>: File containing associated PCs per query genome (one genome per line) <br />


<b>Output:</b>

```
<vMatch_matrix.txt>
```

<vMatch_matrix.txt>: Matrix containing fraction of shared PCs between genomes (reference genomes as columns)
