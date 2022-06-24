# import pandas as pd
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

for i in data:
    print(i)

# print(data[4])
# rs = []
# for i in S_0:
#     # print(i)
#     # print("Sum: ", sum(i))
    
#     rs.append(runBB(i))
# print(rs)
[2853, 1230, 758, 499, 232, 68, 43, 19, 14, 6, 3, 1]
[3081, 1611, 959, 498, 143, 104, 41, 28, 9, 5, 2, 1]
[2104, 1451, 798, 291, 144, 77, 57, 22, 9, 5, 3, 1]
# for i in range (0,6):
#     for j in range(0, i*len(data[i])):
#         data[i].insert(0, None)
#         data[i].append(None)

# excelData = pd.DataFrame({"S-3":data[0], "S-2": data[1], "S-1": data[2], "S-0": data[3], "S-N1": data[4], "S-N2": data[5], "S-N3": data[6]})
# excelData.to_excel('best_so_far.xlsx', sheet_name='recursions', index=False)


# list1 = [10,20,30,40]
# list2 = [40,30,20,10]
# col1 = "X"
# col2 = "Y"
# data = pd.DataFrame({col1:list1,col2:list2})
# data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)