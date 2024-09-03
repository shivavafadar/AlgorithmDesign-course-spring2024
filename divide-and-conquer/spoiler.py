def count_crossing_subarrays(w, k, left, mid, right):
    count = 0
    # Compute suffix sums for the left half
    suffix_sums = []
    suffix_total = 0
    for i in range(mid, left - 1, -1):
        suffix_total += w[i]
        suffix_sums.append(suffix_total)
    
    # Compute prefix sums for the right half
    prefix_sums = []
    prefix_total = 0
    for j in range(mid + 1, right + 1):
        prefix_total += w[j]
        prefix_sums.append(prefix_total)
    
    # Count valid crossing subarrays
    for s_sum in suffix_sums:
        for p_sum in prefix_sums:
            if abs(s_sum + p_sum) > k:
                count += 1
    
    return count

def count_subarrays(w, k, left, right):
    if left == right:
        # Single element subarray case
        return 1 if abs(w[left]) > k else 0

    if left < right:
        mid = (left + right) // 2
        left_count = count_subarrays(w, k, left, mid)
        right_count = count_subarrays(w, k, mid + 1, right)
        cross_count = count_crossing_subarrays(w, k, left, mid, right)
        return left_count + right_count + cross_count
    return 0

def process_input():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        w = list(map(int, data[index:index + n]))
        index += n
        
        result = count_subarrays(w, k, 0, n - 1)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    process_input()
