# Merge Sort or divide and conquer
# Time: O(n log n)
# Space: O(n) - Note: can be Log n, but this is harder to write
D = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    m = len(arr) // 2
    l = arr[:m]
    r = arr[m:]

    l = merge_sort(l)
    r = merge_sort(r)
    L,R = 0,0
    l_len = len(l)
    r_len = len(r)

    sorted_arr = [0] * n
    i = 0
    while l<l_len and r < r_len:
        if l[L] < r[R]:
            sorted_arr[i] = l[L]
            L += 1
        else:
            sorted_arr[i] = r[R]
            R += 1
        i += 1
    while L < l_len:
        sorted_arr[i] = l[L]
        L += 1
        i += 1
    while R < r_len:
        sorted_arr[i] = r[R]
        R += 1
        i += 1
    return sorted_arr
merge_sort(D)


