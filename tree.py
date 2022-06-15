import copy
from ctypes import c_int16
from os import curdir
from select import select
import sys

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
        

    def newDepthFirst(self, root, target, current):
        print("")

    def depthFirst(self, root, target):
        if not root: return
        if root.left == None or root.right == None: return #hmmm...
        
        global recursions
        global flag

        # Count the recursions
        recursions += 1

        # If subset sum is equal to target we found the subset
        if (sum(root.data) == target):
            flag = True
            return root.data

        # #Skip branch if sum higher than target
        if ((sum(root.data) > target)  & (flag == False)):
            return

        # DFS
        if ((root.left is not None) & (root.right is not None)):
            if ((sum(root.data) < target) & (flag == False)):
                self.depthFirst(root.left, target)
                self.depthFirst(root.right, target)


   
    # def bAndB_stack(self, root):
    #     # print("root data", root.data)
    #     stack = []

    #     def addToStack(root):
    #         if (root.left == None or root.right == None):
    #             return
            
    #         stack.append(root.data)
    #         addToStack(root.left)
    #         addToStack(root.right)
    #     addToStack(root)
    #     return stack
    #     # print(stack)
    
    # def BBForReal(self, root, target):
    #     best = 9999999999999
    #     stack = []
    #     stack.append(root.data)

    #     while (stack is not []):
    #         cur = stack.pop()
    #         if (sum(cur) < best)
     
        
      

def runBB(arr):
    root = Node([])
    root.construct(0, arr)
    target =  sum(arr)/2

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

#runBB([103, 90, 86, 79, 67, 65, 57, 56, 43, 41, 40, 39])
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


 # Auxiliary function to display tree, useful for debugging (works best with len < 6)
    # def display(self):
    #     lines, *_ = self._display_aux()
    #     for line in lines:
    #         print(line)

    # def _display_aux(self):
    #     """Returns list of strings, width, height, and horizontal coordinate of the root."""
    #     # No child.
    #     if self.right is None and self.left is None:
    #         line = '%s' % self.data
    #         width = len(line)
    #         height = 1
    #         middle = width // 2
    #         return [line], width, height, middle

    #     # Only left child.
    #     if self.right is None:
    #         lines, n, p, x = self.left._display_aux()
    #         s = '%s' % self.data
    #         u = len(s)
    #         first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
    #         second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
    #         shifted_lines = [line + u * ' ' for line in lines]
    #         return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    #     # Only right child.
    #     if self.left is None:
    #         lines, n, p, x = self.right._display_aux()
    #         s = '%s' % self.data
    #         u = len(s)
    #         first_line = s + x * '_' + (n - x) * ' '
    #         second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
    #         shifted_lines = [u * ' ' + line for line in lines]
    #         return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    #     # Two children.
    #     left, n, p, x = self.left._display_aux()
    #     right, m, q, y = self.right._display_aux()
    #     s = '%s' % self.data
    #     u = len(s)
    #     first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    #     second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    #     if p < q:
    #         left += [n * ' '] * (q - p)
    #     elif q < p:
    #         right += [m * ' '] * (p - q)
    #     zipped_lines = zip(left, right)
    #     lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    #     return lines, n + m + u, max(p, q) + 2, n + u // 2
