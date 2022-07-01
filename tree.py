import copy

class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

    # Construct subset tree
    def construct(self, counter, arr):
        
        newSubset = copy.deepcopy(self.data)
        
        # Depth of tree is equal to length of tree
        if counter == len(arr) : return

        # Right child = current subset
        self.right = Node(newSubset)
        # Left child = current subtree + next element
        self.left = Node(newSubset + [arr[counter]])

        counter += 1
       
        # Recursively construct tree
        self.left.construct(counter,arr)
        self.right.construct(counter, arr)
       
    def countSolutions(self, root, target):
        global numSolutions
        global recursions

        if (recursions > 4096): return

        if not root or root == None: return
        if (root.left == None) or (root.right == None):
            return

        self.countSolutions(root.left, target)

        if (sum(root.data) == target):
            numSolutions += 1
            # print("Found ", root.data)
            return
        
        self.countSolutions(root.right, target)
        recursions += 1

    def depthFirst(self, root, target):
              
        global recursions
        global flag
        global best
        global numSolutions
        global solution

        if root.left == None: return 
        left = sum(root.left.data)
        right = sum(root.right.data)

        if (abs(target - left) < abs(target - best)):
            best = left
            solution = root.left.data
            if best == target:
                print("Found: ", root.left.data, "with sum", left)
                solution = root.left.data
                numSolutions += 1
                flag = True  # COMMENT IF YOU WANT ALG TO NOT HALT ON PERFECT SOLUTION
        
        if right < target and not flag:
            self.depthFirst(root.right, target)
        
        if left < target and not flag:
            self.depthFirst(root.left, target)

        # Count the recursions
        recursions += 1
    

def runBB(arr):
    root = Node([])
    root.construct(0, arr)
    target =  round(sum(arr)/2)


    global flag
    global recursions
    global best

    best = 99999999999
    recursions = 0
    flag =False

    global numSolutions
    numSolutions = 0
    # print("Arr: ", arr)
    # print("Target: ", target)
    root.depthFirst(root, target)
    # print("Solutions: ", numSolutions)

    return recursions

def runBBWithSolutions(arr):
    root = Node([])
    root.construct(0, arr)
    target =  round(sum(arr)/2)


    global flag
    global recursions
    global best

    best = 99999999999
    recursions = 0
    flag =False

    global solution
    solution = []
    
    global numSolutions
    numSolutions = 0
    # print("Arr: ", arr)
    # print("Target: ", target)
    root.depthFirst(root, target)
    # print("Solutions: ", numSolutions)
    
    remaining = list(set(arr) - set(solution))
    print("sol", solution)
    val = abs(sum(solution) - sum(remaining))  #abs(sum(solution) - target) #abs(best - sum(remaining))

    return {"val":val, "sol":solution}
