# Given two lists of Strings with the same set of elements and no duplicates within the list, 
# find out the minimum number of contiguous swaps that are required to get from one list to another.
# Example 
# S = ["B","C","A","D"] 
# D = ["C","D","A","B"]


# B C A D
# C B A D
# C A B D
# C A D B
# C D A B


# contiguous swaps means - you can only swap adjacent elements.

def min_contiguous_swap(S, D):
    swaps = 0
    S = list(S)
    for i in range(len(S)):
        if S[i] != D[i]:
            swap_id = S.index(D[i])
            while swap_id > i:
                S[swap_id],S[swap_id-1] = S[swap_id-1],S[swap_id]
                swaps += 1
                swap_id -= 1
    return swaps
# Test the function
S = ["B","C","A","D"]
D = ["C","D","A","B"]
print(min_contiguous_swap(S, D))