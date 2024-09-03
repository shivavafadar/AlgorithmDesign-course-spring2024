iteration = int(input())

for _ in range(iteration):
    unique_flowers, number_clients = map(int, input().split())
    flowers = list(map(int, input().split()))

    for _ in range(number_clients):
        l, r = map(int, input().split())
        ranges = flowers[l - 1:r]
        if len(ranges) == 1:
            print("sad")
        else:
            if sum(ranges) - len(ranges) >= 2:
                print("happy")
            else:
                print("sad")

