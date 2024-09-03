def calculate_total_balloons(mid, left_kids_count, right_kids_count):
    total_balloons = mid

    # Calculate left balloons
    if left_kids_count >= mid - 1:
        total_balloons += (mid - 1) * mid // 2 + left_kids_count - (mid - 1)
    else:
        total_balloons += left_kids_count * (left_kids_count + 1) // 2

    # Calculate right balloons
    if right_kids_count >= mid - 1:
        total_balloons += (mid - 1) * mid // 2 + right_kids_count - (mid - 1)
    else:
        total_balloons += right_kids_count * (right_kids_count + 1) // 2

    return total_balloons

def find_max_balloons(n, m, k):
    left_kids_count = k - 1
    right_kids_count = n - k
    
    # Start with the maximum possible number of balloons for the specific child
    max_balloons = 1
    while True:
        current_total_balloons = calculate_total_balloons(max_balloons, left_kids_count, right_kids_count)
        
        if current_total_balloons <= m:
            max_balloons += 1
        else:
            break

    return max_balloons - 1

def main():
    n, m, k = map(int, input().split())
    result = find_max_balloons(n, m, k)
    print(result)

if __name__ == "__main__":
    main()
