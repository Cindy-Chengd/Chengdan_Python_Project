# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:33:44 2019
for Cindy<3
@author: Hua&Dan
"""

import numpy as np
import pandas as pd

def sum_exon(cds_locations):
    cds_locations = cds_locations.strip("[").strip("]").split(", ")
    Lcds = sum([np.diff(list(map(int,cds_locations[i].split("-"))))[0]+1 for i in range(len(cds_locations))])
    return(Lcds)

def test_sum_exon():
    
    cds0 = pd.read_csv("./CCDS.20160908.txt",sep="\t") #34297
    
    cds = cds0[np.logical_and(cds0.match_type=="Identical", cds0.ccds_status=="Public")].drop(['match_type','ccds_status'],axis=1)
    
    cds_len = list(map(sum_exon,cds.cds_locations))
    
    cds["cds_len"] = cds_len
    
    cds.columns.values.tolist()
    
    cds.sort_values(by=["cds_len"],ascending=False,inplace=True)
    
    cds["dup"] = cds.duplicated(subset=["gene"],keep="first")
    
    cds = cds[cds.dup==False].drop(labels="dup",axis=1)
    
    total_len_cds = sum(cds.cds_len)
    
    print("Number of protein-coding genes counted: ",cds.shape[0])
    print("Total length of human CDS (of longest transcripts) is: ",total_len_cds, "bp")
    
    assert total_len_cds == 32899880