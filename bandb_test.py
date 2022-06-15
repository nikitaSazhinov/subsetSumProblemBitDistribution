"""
    Problem:

    Given a vector of ints/floats V, find the number of
    length 3 subsets which have a sum < X.
    
    Assume that V contains no duplicates.
"""

def num_subsets(V, X, N):
    global count
    count = 0

    def branch_bound(V, X, N, i=0, s=0, t=0):
        """
            Recursive branch-and-bound algorithm for subset sum.

            V, X, N: inputs based on the problem (N is subset size)
            i: current item index in V
            s: current sum
            t: number of items taken from V

            Result is located in count variable defined above.
        """
        # Number of items taken is N -> valid subset found
        # Update overall count and return
        if t == N:
            global count
            count += 1
            return

        # Depth limit for search; abort
        elif i == len(V):
            return

        else:
            # Take the current item *only* if it meets the constraint
            print(s + V[i])
            if s + V[i] == X:
                branch_bound(V, X, N, i+1, s+V[i], t+1)

            # Always try *not taking* the current item
            branch_bound(V, X, N, i+1, s, t)

    # Run branch-and-bound
    branch_bound(V, X, N)

    # Return the number of valid subsets found
    return count

if __name__ == '__main__':
    # Sample with answer = 6
    # Subsets: [1,2,3], [1,2,4], [1,2,5], [1,3,4], [1,3,5], [2,3,4]
    V = [2545, 1026, 664, 402, 227, 66, 56, 22, 11, 4, 2, 1]
    X = sum(V)/2
    print('Valid subsets: {0}'.format(num_subsets(V, X, 6)))

    # Larger problem with negative numbers and unsorted
    # Max subset size is 10
    # V = [-10, 5, 4, 52, 77, 134, 22, 100, -59, 2, 16, 81, 3, 8, 21]
    # X = 150
    # print('Valid subsets: {0}'.format(num_subsets(V, X, 10)))
