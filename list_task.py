# Remove equal adjacent elements
#
# Example input: [1, 2, 2, 3]
# Example output: [1, 2, 3]
def remove_adjacent(lst):
    res = []
    
    for i in lst:
        if len(res) == 0 or res[-1] != i:
            res.append(i)
    
    return res

print(remove_adjacent([1, 2, 2, 3]))

# Merge two sorted lists in one sorted list in linear time
#
# Example input: [2, 4, 6], [1, 3, 5]
# Example output: [1, 2, 3, 4, 5, 6]
def linear_merge(lst1, lst2):
    res = []

    i, j = 0, 0

    while i < len(lst1) or j < len(lst2):
        if i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                res.append(lst1[i])
                i += 1
            else:
                res.append(lst2[j])
                j += 1
        else:
            if i < len(lst1):
                res.append(lst1[i])
                i += 1
            if j < len(lst2):
                res.append(lst2[j])
                j += 1
    
    return res

print(linear_merge([2, 4, 6], [1, 3, 5]))
