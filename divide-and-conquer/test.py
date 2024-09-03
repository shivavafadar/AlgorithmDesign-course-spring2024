def find_permutation(n, m):
    if m < n - 1 or m > n * (n - 1) // 2:
        return -1
    
    perm = list(range(1, n + 1))
    
    calls_needed = m - (n - 1)
    i = 0
    
    while calls_needed > 0 and i < n - 1:
        if calls_needed >= (i + 1):
            perm[:i + 2] = reversed(perm[:i + 2])
            calls_needed -= (i + 1)
        i += 1
    
    if merge_sort_count(perm) == m:
        return perm
    else:
        return -1

def merge_sort_count(arr):
    count = 0
    size = 1
    n = len(arr)
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size
            right = min(left + 2 * size, n)
            merged = merge(arr[left:mid], arr[mid:right])
            arr[left:right] = merged
            count += 1
        size *= 2
    return count

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def main():
    n, m = map(int, input().split())
    result = find_permutation(n, m)
    if isinstance(result, list):
        print(" ".join(map(str, result)))
    else:
        print(result)

if __name__ == "__main__":
    main()
