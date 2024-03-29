import copy

# Greedy. Returns absolute difference of sums between two partitions.
def greedyPartition(input):
    p1 = []
    p2 = []
    inputCopy = copy.deepcopy(input)
    for i in range(0, len(inputCopy)):

        if (len(p1) != len(p2)):
            smallerList = p1 if (len(p1) < len(p2)) else p2
            smallerList.append(inputCopy[i])
        else:     
            if (sum(p1) > sum(p2)):
                p2.append(inputCopy[i])  
            else:
                p1.append(inputCopy[i])
        
    return  abs(sum(p1) - sum(p2)) #abs(sum(p1) - round(sum(input)/2)) #abs(sum(p1) - sum(p2)) #p1, p2
    

def karmarkarKarp(input):
    # p1 = []
    # p2 = []
    inputCopy = copy.deepcopy(input)

    for i in range(0, len(input) - 1):
        difference = abs(inputCopy[0] - inputCopy[1])
        inputCopy.pop(0)
        inputCopy.pop(0)
        inputCopy.append(difference)
    
    return inputCopy[0] #p1, p2

