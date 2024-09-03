def max_rewards(teams):
    def recurse(teams):
        if len(teams) == 1:
            return teams[0]

        mid = len(teams) // 2
        left_half = teams[:mid]
        right_half = teams[mid:]
        max_left = max(left_half)
        max_right = max(right_half)
        reward_left_elim = max_left + recurse(right_half)
        reward_right_elim = max_right + recurse(left_half)
        return max(reward_left_elim, reward_right_elim)

    return recurse(teams)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0]) 
    teams = list(map(int, data[1:]))  
    
    print(max_rewards(teams))

if __name__ == "__main__":
    main()
