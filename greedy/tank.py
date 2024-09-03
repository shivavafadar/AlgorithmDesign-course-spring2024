import math

number = int(input())

for _ in range(number):
    result = 0
    tanks = int(input())
    tank = list(map(int, input().split()))
    duplicate_count_dict = {item: tank.count(item) for item in set(tank)}
    if 1 in list(duplicate_count_dict.keys()):
        result = math.ceil(duplicate_count_dict[1] / 2)
    for key in duplicate_count_dict.keys():
        if key == 1:
            pass
        else:
            result += duplicate_count_dict[key]

    print(result)
