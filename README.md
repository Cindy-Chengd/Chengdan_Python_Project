# Python_Project_Dan_Cheng

Object: In this project, I'll try to calculate the total length of coding sequences of all protein-coding genes in human genome.

Data: I'll use the "txt" file cotaining the information (including chromosome number, nc_accession, gene, gene_id, ccds_id, ccds_status, cds_strand, cds_from, cds_to, cds_locations, match_type) of all protein-coding genes as original data. 

Methods: Firstly, I'll process the original data: 
1. read ".txt" file into "csv" file.
2. only use the data with column "ccds_status" == "Public" and column "match_type" == "Identical"
3. take the data from the column "cds_locations", change the data type from "string" to "integer"
4. calculate the length of coding sequences for one gene
5. use loop to calculate the length of coding sequences for each gene
6. add up the length of coding sequences for each gene to get the total length of coding sequences for all genes
Test:

This project will use many python knowledge I learnt in this course, including python data types, python data structures, python functions, python packages...
This project is very interesting and useful and will resolve a problem I meet in my research work.



     
                                      
