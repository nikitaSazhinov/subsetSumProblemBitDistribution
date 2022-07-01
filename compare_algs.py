from algorithms import karmarkarKarp
from algorithms import greedyPartition
from generate import generateTemplatesInstance
from tree import runBBWithSolutions
import pandas as pd


#MS First
data = []
for index in range(0,7):
    bb_res = []
    greedy_res = []
    kk_res = []
    for i in range(0,100):
        instances = generateTemplatesInstance(multiset=True)
        i = instances[index]
        bb_res.append(runBBWithSolutions(i)["val"])
        greedy_res.append(greedyPartition(i))
        kk_res.append(karmarkarKarp(i))
    data.append([bb_res, greedy_res, kk_res])


counter = 0 
ax = ["S-3", "S-2", "S-1", "S-0", "S-N1", "S-N2", "S-N3"]
for val in data:
    filename_raw = "datasheets/compare/compare_algs_" + ax[counter] + ".xlsx"
    excelData = pd.DataFrame({"BB":val[0], "GR": val[1], "KK": val[2]})
    excelData.to_excel(filename_raw, sheet_name='data', index=False)
    counter += 1

# Sets
data = []
for index in range(0,7):
    bb_res = []
    greedy_res = []
    kk_res = []
    for i in range(0,100):
        instances = generateTemplatesInstance(multiset=False)
        i = instances[index]
        bb_res.append(runBBWithSolutions(i)["val"])
        greedy_res.append(greedyPartition(i))
        kk_res.append(karmarkarKarp(i))
    data.append([bb_res, greedy_res, kk_res])



counter = 0 
ax = ["S-3", "S-2", "S-1", "S-0", "S-N1", "S-N2", "S-N3"]
for val in data:
    filename_raw = "datasheets/compare/compare_set_algs_" + ax[counter] + ".xlsx"
    excelData = pd.DataFrame({"BB":val[0], "GR": val[1], "KK": val[2]})
    excelData.to_excel(filename_raw, sheet_name='data', index=False)
    counter += 1
