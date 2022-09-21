from algorithms import karmarkarKarp
from algorithms import greedyPartition
from generate import generateTemplatesInstance
from tree import runBBWithSolutions
import pandas as pd
import math


# Sets
data = []
for index in range(0,7):
    bb_gr = []
    bb_kk = []
    for i in range(0,100):
        instances = generateTemplatesInstance(multiset=False)
        i = instances[index]
        bb = runBBWithSolutions(i)["val"]
        gr = greedyPartition(i)
        kk = karmarkarKarp(i)
        bb_gr.append(abs(bb - gr))
        bb_kk.append(abs(bb - kk))

    data.append(bb_gr)
    data.append(bb_kk)


for i in data:
    print(i)



counter = 0 
ax = ["S-3", "S-2", "S-1", "S-0", "S-N1", "S-N2", "S-N3"]
filename_raw = "datasheets/compare_set_algs_descr" + ".xlsx"

excelData = pd.DataFrame({})
for i in data:
    s = pd.Series(i)
    excelData = excelData.append(s,ignore_index=True)
    counter += math.floor(0.5)
excelData.to_excel(filename_raw, sheet_name='data', index=False)
