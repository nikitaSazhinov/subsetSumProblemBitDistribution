import random
from algorithms import karmarkarKarp
from algorithms import greedyPartition
from tree import runBBWithSolutions
    
def randomBits(word_size):
    number = 0
    for bit in random.sample(range(word_size), word_size):
        number |= 1 << bit
    min = int((number)/2)    
    return random.randint(min, number)  #+1 in min 
    

def generateSingleInstance(template, size):
    sample = []
    for i in template:
        sample.append(randomBits(i))
    instance = random.sample(sample, size)
    return instance

def generateTemplatesInstance(multiset):
    
    # Multiset, 14
    strictTemplate6 = [1,1,1,1,1,4,4,4,5,9,13,17,21,23]
    strictTemplate5 = [1,1,2,2,3,4,5,5,6,9,12,15,18,22]
    strictTemplate4 = [1,1,2,4,4,5,6,7,9,10,11,13,15,17]
    strictTemplate3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] # boundary
    strictTemplate2 = [3,3,4,4,5,6,7,9,9,9,10,11,12,13]
    strictTemplate1 = [6,6,6,6,6,7,7,7,8,8,8,10,10,10]
    strictTemplate0 = [7,7,7,7,7,7,7,8,8,8,8,8,8,8]

    # Set, 14
    sstrictTemplate6 = [1,1,2,2,3,3,3,3,4,9,13,17,20,26]
    sstrictTemplate5 = [1,1,2,2,3,4,5,5,6,9,12,15,18,22]
    sstrictTemplate4 = [1,1,2,4,4,5,6,7,9,10,11,13,15,17]
    sstrictTemplate3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] # boundary
    sstrictTemplate2 = [3,3,4,4,5,6,7,9,9,9,10,11,12,13]
    sstrictTemplate1 = [6,6,6,6,6,7,7,7,8,8,8,10,10,10]
    sstrictTemplate0 = [7,7,7,7,7,7,7,8,8,8,8,8,8,8]

    templates = []
    if multiset:
        templates = [
            strictTemplate6,
            strictTemplate5,
            strictTemplate4,
            strictTemplate3,
            strictTemplate2,
            strictTemplate1,
            strictTemplate0
        ]
    else: 
         templates = [
            sstrictTemplate6,
            sstrictTemplate5,
            sstrictTemplate4,
            sstrictTemplate3,
            sstrictTemplate2,
            sstrictTemplate1,
            sstrictTemplate0
        ]

    instances = []

    for template in templates:
        instance = []
        
        # Check for duplicates
        if not multiset:
            flag = False
            while not flag:
                
                instance = generateSingleInstance(template, len(strictTemplate3))
                s_instance = set(instance)
                if len(instance) == len(s_instance):
                    flag = True
        else:
            instance = generateSingleInstance(template, 14)
        
        instances.append(sorted(instance, reverse=True)) #Reverse should be true for biggest elements first
    return instances


def generateData(multiset):

    S_3 = []
    S_2 = []
    S_1 = []
    S_0 = []
    S_N1 = []
    S_N2 = []
    S_N3 = []

    for i in range(0, 1000):
        templateInstance = generateTemplatesInstance(multiset)
        S_3.append(templateInstance[0])
        S_2.append(templateInstance[1])
        S_1.append(templateInstance[2])
        S_0.append(templateInstance[3])
        S_N1.append(templateInstance[4])
        S_N2.append(templateInstance[5])
        S_N3.append(templateInstance[6])
    
    return S_3, S_2, S_1, S_0, S_N1, S_N2, S_N3

print("GENERATING INSTANCES")
# templateInstance = generateTemplatesInstance(multiset = False)
# bb = (runBBWithSolutions(templateInstance[5])["val"])
# gr = greedyPartition(templateInstance[5])
# print("BB: ", bb, "GR: ", gr)

# data for: 1.5