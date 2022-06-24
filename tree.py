import copy
from ctypes import c_int16
from os import curdir
from select import select
import sys

class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
    #   self.parent = None
      self.data = data

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
            print("Found ", root.data)
            return
        
        self.countSolutions(root.right, target)
        recursions += 1


        

    def newDepthFirst(self, root, target, current):
        print("")

    def depthFirst(self, root, target):
              
        global recursions
        global flag
        global best
        global numSolutions
        goRightFlag = False

        if (abs(sum(root.data) - target) < best):
            best = abs(sum(root.data) - target)
            # print("Current best:", best ,"with data", root.data)
        # print("Partial sum", sum(root.data), "data", root.data)
        # print(best)
       
        if not root or root == None: return
        
        if root.left == None or root.right == None: 
            return #hmmm...
  
        
        # If subset sum is equal to target we found the subset
        # Idea for solution: if found you not supposed to stop. You supposed to backtrack to parent and go next branch.
        if (sum(root.data) == target):
            flag = True
            numSolutions += 1
            print("FOUND RESULT ", root.data)
            return root.data

        # # #Skip branch if sum higher than target
        if ((sum(root.data) > target)):
            root.left = None
            root.right = None
            # print("PRUNING BRANCH WITH SUM", sum(root.data), "AND DATA", root.data)
            # self.depthFirst(root.right, target)
            return


        # DFS
        if ( (flag == False)):
            if (sum(root.data) < target):
                self.depthFirst(root.left, target)  
                # if (sum(root.data) < target):  
                self.depthFirst(root.right, target)
                

        # Count the recursions
        recursions += 1

    
    def bAndB_stack(self, root):
        # print("root data", root.data)
        stack = []

        def addToStack(root):
            if (root.left == None or root.right == None):
                return
            
            stack.append(root.data)
            addToStack(root.left)
            addToStack(root.right)
        addToStack(root)
        return stack
        # print(stack)
    
    # def BBForReal(self, root, target):
    #     best = 9999999999999
    #     stack = []
    #     stack.append(root.data)

    #     while (stack is not []):
    #         cur = stack.pop()
    #         if (sum(cur) < best)


 #Auxiliary function to display tree, useful for debugging (works best with len < 6)
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
     
        
      

def runBB(arr):
    root = Node([])
    root.construct(0, arr)
    target =  sum(arr)/2
    # root.display()

    global flag
    global recursions
    global best

    best = 99999999999
    recursions = 0
    flag =False

    global numSolutions
    numSolutions = 0
    # root.depthFirst(root, target)

    root.countSolutions(root, target)
    # print("num ", numSolutions)
    return numSolutions

testArr = sorted([1,2,6,12,19,35,115,247,305,563,1534,3828], reverse=True)
#print(testArr)
arr = [2188, 2045, 892, 501, 192, 69, 36, 29, 9, 5, 3, 1]
# print("Array: ", arr)
# print("Full sum: ", sum(arr))
# print("Target: ",  sum(arr)/2)
# print("")
# print("--------------------------------------------------------")
# print("")
# print("RECURSIONS: ", runBB(arr))
#[1,2,6,12,19,35,115,247,305,563,1534,3828]
# Use the insert method to add nodes

# root = Node([])
# #arr = [5,4,3,2]#[103, 90, 86, 79, 67, 65, 57, 56, 43, 41, 40, 39]
# #arr = [123, 120, 86, 82, 76, 72, 63, 55, 49, 47, 46, 31]
# arr = [332, 256, 195, 145, 100, 64, 44, 42, 30, 23, 15, 14]

# root.construct(0, arr)
# #root.display()
# target =  sum(arr)/2
# print("target: ", target)
# global recursions
# recursions = 0
# root.depthFirst(root,target)
#print("# of recursions: ",recursions)


