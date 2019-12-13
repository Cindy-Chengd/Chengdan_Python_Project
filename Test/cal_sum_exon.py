
#Define the function: sum_exon_final

import numpy as np
import pandas as pd

"""
Calculate total CDS length of one gene
"""

def sum_exon(cds_locations):
    cds_locations = cds_locations.strip("[").strip("]").split(", ")
    Lcds = sum([np.diff(list(map(int,cds_locations[i].split("-"))))[0]+1 for i in range(len(cds_locations))])
    return(Lcds)



"""
Calculate total CDS length of all genes
"""

def sum_exon_final(cds):
    cds_len = list(map(sum_exon,cds.cds_locations))    
    total_cds_len = sum(cds_len)
    print("Total length of human CDS is: ",total_cds_len)
    return(total_cds_len)
