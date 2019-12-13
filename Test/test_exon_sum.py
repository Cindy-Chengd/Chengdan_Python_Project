
#Test the function: sum_exon_final()


import pytest
import pandas as pd
import numpy as np
import cal_sum_exon

file_path = "./CCDS.20160908_origin.txt"

#use the appropirate pandas read function for your source data file.
data0 = pd.read_csv(file_path,sep="\t") #34297
cds = data0[np.logical_and(data0.match_type=="Identical", data0.ccds_status=="Public")].drop(['match_type','ccds_status'],axis=1)

def test_function():
    assert cal_sum_exon.sum_exon_final(cds)
