import pandas as pd
from tree import runBB
import math
import random


def randomBits(word_size):
    number = 0
    for bit in random.sample(range(word_size), word_size):
        number |= 1 << bit
    min = int((number)/2)    
    return random.randint(min+1, number)  #+1 in min 
    

def generateSingleInstance(template, n):
    sample = []
    for i in template:
        sample.append(randomBits(i))
    instance = random.sample(sample, n)
    return instance

n = 16
mRange = range(32 , 256)

def sumsToX(numsum, size):
    # build a list/array of random numbers
    numbers = []
    for _ in range(size):
        numbers.append(random.random())

    # normalise the original list using the sum
    normalised = []
    for n in numbers:
        normalised.append( numsum * (n / sum(numbers)))
    normalisedRounded = []
    for i in normalised:
        normalisedRounded.append(math.ceil(i))
    # print(normalisedRounded)

    return normalisedRounded


    # sumsToX(16, 24)

def generateTemplates():
    templates = []
    for i in mRange:
        template = sumsToX(i, 16)
        templates.append(template)
    return templates

templates = generateTemplates()


instances = []
for i in templates:
    for j in range(0,5):
        instances.append(
            {
            "instance": generateSingleInstance(i, 16),
            "template": i,
            "m/n": (sum(i)/16)/16
            }
            )


data = []
for i in instances:
    data.append(
        {
        "solutions": runBB(i["instance"]),
        "m/n": i["m/n"]
        }
        )

print(data)

excelData = pd.DataFrame(data)
excelData.to_excel('mnchart.xlsx', sheet_name='solutions', index=False)

