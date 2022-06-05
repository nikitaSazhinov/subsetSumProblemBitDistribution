import pandas as pd
from generate import generateData
from tree import runBB

instances = [S_3, S_2, S_1, S_0, S_N1, S_N2, S_N3] = generateData()
#print(S_N3)

data = []
for instance in instances:
    recursions = []
    for i in instance:
        recursions.append(runBB(i))
    data.append(recursions)

print(data)

excelData = pd.DataFrame({"S-3":data[0], "S-2": data[1], "S-1": data[2], "S-0": data[3], "S-N1": data[4], "S-N2": data[5], "S-N3": data[6]})
excelData.to_excel('recursions_0.xlsx', sheet_name='recursions', index=False)


# list1 = [10,20,30,40]
# list2 = [40,30,20,10]
# col1 = "X"
# col2 = "Y"
# data = pd.DataFrame({col1:list1,col2:list2})
# data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)