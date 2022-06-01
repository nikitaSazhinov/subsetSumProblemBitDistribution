import random
from re import template
from typing import Set
from algorithms import karmarkarKarp
from algorithms import greedyPartition
    
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




for i in range(0, 1):
   templateInstance = generateTemplatesInstance()

   print(templateInstance[6])
   print(templateInstance[2])

   print("Greedy: ", greedyPartition(templateInstance[6]))
   print("Greedy: ", greedyPartition(templateInstance[3]))
