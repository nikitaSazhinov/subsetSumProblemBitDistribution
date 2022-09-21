import pandas as pd
from generate import generateData
from tree import runBB
import numpy as np


def generateMSData(index):
    # Multiset data
    instances = [S_3, S_2, S_1, S_0, S_N1, S_N2, S_N3] = generateData(multiset = True)

    counter = 0
    data = []
    for instance in instances:
        recursions = []
        for i in instance:
            print("SOLVING ", i)
            print("ITERATION", counter)
            recursions.append(runBB(i))
            counter += 1
        data.append(recursions)
        
    for i in data:
        print(i)

    filename_raw = "datasheets/multiset/recursions_ms_raw_" + str(index) + ".xlsx"
    excelData = pd.DataFrame({"S-3":data[0], "S-2": data[1], "S-1": data[2], "S-0": data[3], "S-N1": data[4], "S-N2": data[5], "S-N3": data[6]})
    excelData.to_excel(filename_raw, sheet_name='recursions', index=False)

    print("\n")

    filename_graph = "datasheets/multiset/recursions_ms_graph_" + str(index) + ".xlsx"
    ax = ["S-3", "S-2", "S-1", "S-0", "S-N1", "S-N2", "S-N3"]
    excelGraph = pd.DataFrame({"S-3":data[0], "S-2": data[1], "S-1": data[2], "S-0": data[3], "S-N1": data[4], "S-N2": data[5], "S-N3": data[6]})
    for i in range(0, 7*1000):
        s = pd.Series([np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN], index = ax)
        excelGraph = excelGraph.append(s,ignore_index=True)
    for i in range(0,7):
        excelGraph[ax[i]] = excelGraph[ax[i]].shift(periods = 1000*i)
    excelGraph.to_excel(filename_graph, sheet_name='recursions', index=False)

def generateSData(index):
    # Set data
    instances = [S_3, S_2, S_1, S_0, S_N1, S_N2, S_N3] = generateData(multiset = False)

    data = []
    dataI = []
    counter = 0
    for instance in instances:
        recursions = []
        instances_arr = []
        for i in instance:
            # print("COUNTER ", counter)
            recursionCount = runBB(i)
            # print(i)
            recursions.append(recursionCount)
            instances_arr.append(i)
            counter += 1
        data.append(recursions)
        dataI.append(instances_arr)
        print(data)

    for i in data:
        print(i)

    filename_raw = "datasheets/set/recursions_s_raw_" + str(index) + ".xlsx"
    excelData = pd.DataFrame({
    "S-3-INSTANCES": dataI[0], "S-3-RECURSIONS":data[0],
    "S-2-INSTANCES": dataI[1],"S-2-RECURSIONS": data[1], 
    "S-1-INSTANCES": dataI[2],"S-1-RECURSIONS": data[2],
    "S-0-INSTANCES": dataI[3],"S-0-RECURSIONS": data[3],
    "S-N1-INSTANCES": dataI[4],"S-N1-RECURSIONS": data[4],
    "S-N2-INSTANCES": dataI[5],"S-N2-RECURSIONS": data[5],
    "S-N3-INSTANCES": dataI[6],"S-N3-RECURSIONS": data[6],
    })
    excelData.to_excel(filename_raw, sheet_name='recursions', index=False)

    # print("\n")

    filename_graph = "datasheets/set/recursions_s_graph_" + str(index) + ".xlsx"
    ax = ["S-3", "S-2", "S-1", "S-0", "S-N1", "S-N2", "S-N3"]
    excelGraph = pd.DataFrame({
    "S-3-INSTANCES": dataI[0], "S-3-RECURSIONS":data[0],
    "S-2-INSTANCES": dataI[1],"S-2-RECURSIONS": data[1], 
    "S-1-INSTANCES": dataI[2],"S-1-RECURSIONS": data[2],
    "S-0-INSTANCES": dataI[3],"S-0-RECURSIONS": data[3],
    "S-N1-INSTANCES": dataI[4],"S-N1-RECURSIONS": data[4],
    "S-N2-INSTANCES": dataI[5],"S-N2-RECURSIONS": data[5],
    "S-N3-INSTANCES": dataI[6],"S-N3-RECURSIONS": data[6],
    })
    for i in range(0, 7*1000):
        s = pd.Series([np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN], index = ax)
        excelGraph = excelGraph.append(s,ignore_index=True)
    for i in range(0,7):
        excelGraph[ax[i]] = excelGraph[ax[i]].shift(periods = 1000*i)
    excelGraph.to_excel(filename_graph, sheet_name='recursions', index=False)


# generateMSData('1k')
generateSData('1k-new')