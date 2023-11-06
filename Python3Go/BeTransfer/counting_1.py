def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] = count[A[k]]+1
    return count


def dictCounting(A):
    dict = {}
    for a in A:
        if a in dict:
            dict[a] += 1
        else:
            dict[a] = 1
    return dict


def count(dict, m):
    if m in dict:
        return dict[m]
    return 0


# Test
A = [1, 4, 8, 7]
dict = dictCounting(A)

print('Telling us dictionary: ', dict)
print('Counting the dictionary: ', count(dict, 7))
print(count(dict, 15))
