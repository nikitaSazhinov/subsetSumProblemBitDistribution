
import copy
from ctypes import c_int16
from os import curdir
from select import select
import sys

class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.parent = None
      self.data = data
      self.state = "created"
      self.path = []

    def initRoot(self, target):
        depth = 11 #12?
        self.state = "active"

        def dfs(root, counter):
            if not root or root == None: return
            if counter <= depth: return

            if root.state == "created": #maybe init should be null instead of created
                root.state = "active"
            
            if (sum(root.data) > target): #Best?
                 root.state = "dead"
                 root.left = None
                 root.right = None
                 dfs(root.parent, target, counter - 1)
            elif ((root.state == "dead" and root.right.state == "dead") or (counter == depth)):
                #record path and vals here
                root.state = "dead"
                root.left = None
                root.right = None
                root.path.pop()
                dfs(root.parent, target, counter - 1)
            elif (root.left is None):
                print("")
                #create left child

    def createNode(left, parent, path):
        depth = parent.depth + 1
        node = Node(





            
        )
    # Construct subset tree
    def construct(self, counter, arr):
        
        newSubset = copy.deepcopy(self.data)
        
        # Depth of tree is equal to length of tree
        if counter == len(arr) : return
        # if counter is not 0: self.parent = Node(self.data)
        # Right child = current subset
        self.right = Node(newSubset)
        # Left child = current subtree + next element
        self.left = Node(newSubset + [arr[counter]])

        counter += 1

        # Recursively construct tree
        self.left.construct(counter,arr)
        self.right.construct(counter, arr)
        

    def newDepthFirst(self, root, target, current):
        print("")

    def depthFirst(self, root, target):
              
        global recursions
        global flag
       
        if not root or root == None: return
        
        if root.left == None or root.right == None: 
            return #hmmm...
  
        # Count the recursions
        recursions += 1

        # If subset sum is equal to target we found the subset
        # Idea for solution: if found you not supposed to stop. You supposed to backtrack to parent and go next branch.
        if (sum(root.data) == target):
            flag = True
            # print("FOUND")
            # print("Arr: ", root.data)
            # print("Value: ", sum(root.data))
            return root.data

        # #Skip branch if sum higher than target
        if ((sum(root.data) > target) ):
            # print("2 much")
            root.left = None
            # root.right = None
            # self.depthFirst(root.right, target)
            return

        # DFS
        if ((root.left is not None)):
            if ( (flag == False)):
                #self.depthFirst(root.left, target)
                self.depthFirst(root.right, target)
                if (sum(root.data) < target):
                    self.depthFirst(root.left, target)

    
def runBB(arr):
    root = Node([])
    root.construct(0, arr)
    target =  sum(arr)/2
    # print("Target: ", target)
    global flag
    global recursions
    # global current
    # current = 0
    # best = 99999999999

    recursions = 0
    flag =False

    
    # s = root.bAndB_stack(root)
    

    root.depthFirst(root, target)

    #print("Solution: ", root.depthFirst(root,target))
    #print(recursions)
    return recursions

testArr = sorted([1,2,6,12,19,35,115,247,305,563,1534,3828], reverse=True)
#print(testArr)
print(runBB([2188, 2045, 892, 501, 192, 69, 36, 29, 9, 5, 3, 1]))
