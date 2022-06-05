import random
from re import template
from typing import Set
from algorithms import karmarkarKarp
from algorithms import greedyPartition
# from tree import Node
    
def randomBits(word_size):
    number = 0
    for bit in random.sample(range(word_size), word_size):
        number |= 1 << bit
    min = int((number)/2)    
    return random.randint(min, number) 
    

def generateSingleInstance(template):
    sample = []
    for i in template:
        sample.append(randomBits(i))
    instance = random.sample(sample, 12)
    return instance

def generateTemplatesInstance():

    strictTemplate6 = [1,1,1,1,1,4,4,5,9,13,17,21]
    strictTemplate5 = [1,1,2,2,3,4,5,6,9,12,15,18]
    strictTemplate4 = [1,1,2,4,4,5,6,7,9,11,13,15]
    strictTemplate3 = [1,2,3,4,5,6,7,8,9,10,11,12] # boundary
    strictTemplate2 = [3,3,4,4,5,6,7,8,8,9,10,11]
    strictTemplate1 = [4,4,5,5,6,6,7,7,8,8,9,9]
    strictTemplate0 = [6,6,6,6,6,6,7,7,7,7,7,7]

    templates = [
        strictTemplate6,
        strictTemplate5,
        strictTemplate4,
        strictTemplate3,
        strictTemplate2,
        strictTemplate1,
        strictTemplate0
    ]

    instances = []

    for template in templates:
        instances.append(sorted(generateSingleInstance(template), reverse=True))
    return instances


def generateData():

    S_3 = []
    S_2 = []
    S_1 = []
    S_0 = []
    S_N1 = []
    S_N2 = []
    S_N3 = []

    for i in range(0, 20):
        templateInstance = generateTemplatesInstance()
        S_3.append(templateInstance[0])
        S_2.append(templateInstance[1])
        S_1.append(templateInstance[2])
        S_0.append(templateInstance[3])
        S_N1.append(templateInstance[4])
        S_N2.append(templateInstance[5])
        S_N3.append(templateInstance[6])

    return S_3, S_2, S_1, S_0, S_N1, S_N2, S_N3
    #print(templateInstance[6])
    #print(templateInstance[5])

    #print("Greedy: ", greedyPartition(templateInstance[6]))
    #print("Greedy: ", greedyPartition(templateInstance[5]))
