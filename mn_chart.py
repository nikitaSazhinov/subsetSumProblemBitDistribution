# import pandas as pd
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

n = 12
mRange = range(24 , 128)


def sumsToX(numsum, size):
    # build a list/array of random numbers
    numbers = []
    for _ in range(size):
        numbers.append(random.random())
    # print(numbers)
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
        template = sumsToX(i, 12)
        templates.append(template)
    return templates

templates = generateTemplates()

for i in templates:
    print(i)
    print("SUM/MEAN: ", sum(i), sum(i)/12)

instances = []
for i in templates:
    instances.append(
        {
        "instance": generateSingleInstance(i, 12),
        "template": i,
        "m/n": (sum(i)/12)/12
        }
        )

# print(instances[200])
# print(instances[30])
# print(runBB(instances[4]))
alo = []
for i in instances:
    print("current instance: ", i["instance"])
    alo.append(
        {
        "recursions": runBB(i["instance"]),
        "m/n": i["m/n"]
        }
        )

print(alo[)

