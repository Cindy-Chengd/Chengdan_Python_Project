"""
Calculate total length of human CDS
"""

import pandas as pd

import numpy as np

data0 = pd.read_csv("CCDS.20160908_origin.txt",sep="\t")

data1 = np.logical_and(data0.iloc[:,5]=="Public",data0.iloc[:,-1]=="Identical")

cds=data2.drop(["match_type", "ccds_status"],axis=1)

tmp = cds.iloc[0,-1]

tmp1 = tmp.strip("[").strip("]").split(", ")

def sum_exon(tmp):
    """
    Calculate the total length of exon for a gene
    
    """
    tmp1 = tmp.strip("[").strip("]").split(", ")
    cds_len = sum([np.diff(list(map(int,tmp1[i].split("-"))))[0]+1 
    for i in range(len(tmp1))])
    return(cds_len)


cds_len_list = list(map(sum_exon,cds.cds_locations))

total_cds_len = sum(cds_len_list)

print("Total length of human CDS is: ",total_cds_len)

