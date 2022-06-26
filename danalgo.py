def findbest(set, position, currentv):
    global best
    global recursions
    global flag

    recursions=recursions+1


    var1 = currentv + set[position]
    var2 = currentv

    if abs(target - var1) < abs(target - best):
        best = var1
        if best == target:
            flag = True
        #print(bestvalue)

    if position+1 < len(set) and var2 < target and not flag:
    #if position + 1 < len(set):
        findbest(set, position+1, var2)

    if position+1 < len(set) and var1 < target and not flag:
        findbest(set, position+1, var1)


def runDaan(arr):
    
    global target
    target =  round(sum(arr)/2)

    global flag
    global recursions
    global best

    best = 99999999999
    recursions = 0
    flag =False

    global numSolutions
    numSolutions = 0

    print("Arr: ", arr)
    print("Target: ", target)
    print("Solutions: ", numSolutions)

    findbest(arr, 0, 0)
    return recursions
