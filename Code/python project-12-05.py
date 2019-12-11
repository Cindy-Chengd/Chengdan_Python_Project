#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:28:08 2019

@author: chengdan

import os
pwd
os.chdir("/Users/chengdan/Desktop/Python Project")


import pandas as pd
data0 = pd.read_csv("gencode.v25.annotation.TP53.txt",sep="\t",header=None)
data0.shape
data0.head
type(data0)
data = data0.iloc[:,:8]
data

data.head()
data.tail()
help(data.drop)
data=data.drop(labels=1,axis=1)
data.shape
data=data0.drop(labels=[1,8],axis=1)
data.shape
data.head
data[2].value_counts()

data.columns()
data.columns.values()


data.head()

data.columns
type(data.columns)
data.columns.values
data.columns.values.tolist()

data.index.values.tolist()

data.head(n=10)
data10 = data.head(n=10)
type(data10)
data10[3]

data.iloc[:10,2]

data.head()


###################################################################

CDS0 = pd.read_csv("CCDS.20160908.txt",sep="\t")

CDS0.shape

CDS0.head()

CDS0.iloc[:,-1].value_counts()

CDS0.columns.values.tolist()

CDS0.match_type.value_counts()

CDS0.ccds_status.value_counts()

import numpy as np

# only take ccds_status=public, match_type=identical
np.logical_and(CDS0.iloc[:,5]=="Public",CDS0.iloc[:,-1]=="Identical")

idx = np.logical_and(CDS0.iloc[:,5]=="Public",CDS0.iloc[:,-1]=="Identical")

type(idx)

len(idx)

#count how many match
idx.value_counts()

temp = CDS0[idx,:]


#confirmation
temp.match_type.value_counts()

temp.ccds_status.value_counts()

#Drop "match_type" and "ccds_status" columns
temp1=temp.drop("match_type", axis=1)
temp1.shape

temp2=temp1.drop("ccds_status", axis=1)
temp2.shape

#check the drop
temp2.columns.values.tolist()


#combine coding
CDS=CDS0.loc[np.logical_and(CDS0.iloc[:,5]=="Public",CDS0.iloc[:,-1]=="Identical")].drop("ccds_status", axis=1).drop("match_type", axis=1)

CDS=CDS0.loc[np.logical_and(CDS0.iloc[:,5]=="Public",CDS0.iloc[:,-1]=="Identical")].drop(["ccds_status","match_type"], axis=1)

#CDS.columns.values.tolist()
Out[104]: 
['#chromosome',
 'nc_accession',
 'gene',
 'gene_id',
 'ccds_id',
 'cds_strand',
 'cds_from',
 'cds_to',
 'cds_locations']#

#example gene1:
tmp=CDS.iloc[0,-1]
type(tmp)   str
len(tmp)  195


#deplete "[]" and split by ", "
tmp.strip("[").strip("]").split(", ")

#check
type(tmp1)   list
len(tmp1)    13

#calculate the length of exon
tmp2=tmp1[0]   '925941-926012'
tmp2.split("-")['925941', '926012']


list(map(int,tmp2.split("-")))
np.diff(list(map(int,tmp2.split("-"))))[0]
#Out[135]: 71

#loop

[np.diff(list(map(int,tmp1[i].split("-"))))[0]+1 for i in range(13)]

range()

[np.diff(list(map(int,tmp1[i].split("-"))))[0]+1 for i in range(len(tmp1))]

sum([np.diff(list(map(int,tmp1[i].split("-"))))[0]+1 for i in range(len(tmp1))])


#programm
def sum_exon(tmp):
    tmp1=tmp.strip("[").strip("]").split(", ")
    Lcds=sum([np.diff(list(map(int,tmp1[i].split("-"))))[0]+1 for i in range(len(tmp1))])
    return(Lcds)

#test
sum_exon(tmp)    2046

tmp=CDS.iloc[1,-1]
sum_exon(tmp)     2250

#loop

CDS_N=list(map(sum_exon,CDS.cds_locations))

#check
type(CDS_N)
len(CDS_N)
CDS_N[0:9]
sum(CDS_N)

#count gene number
CDS.gene.value_counts()
















#cds = pd.read_csv(".../CCDS.20160908.txt",sep="\t") #34297
#cds = pd.read_csv(".../CCDS.20160908.txt",sep="\t") #34297
#cds = cds[cds.match_type=="Identical"] #34031
#cds = cds[cds.ccds_status=="Public"] #32533
#cds = cds.drop(labels="match_type",axis=1) #(32533, 10)
#cds.columns.values.tolist()
##Out[155]: 
##['#chromosome',
## 'nc_accession',
## 'gene',
## 'gene_id',
## 'ccds_id',
## 'ccds_status',
## 'cds_strand',
## 'cds_from',
## 'cds_to',
## 'cds_locations'


