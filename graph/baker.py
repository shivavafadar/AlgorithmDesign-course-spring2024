N = int(input())
bread_requests = list(map(int, input().split()))
relationships = [input() for _ in range(N)]


replacements = []
for item in relationships:
    temp = []
    for i in range(len(item)):
        if item[i] == "1":
            temp.append(i)

    if len(temp) > 1:
        replacements.append(temp)

def merge_lists(lists):
    merged = []
    while lists:
        first, *rest = lists
        first = set(first)

        lf = -1
        while len(first) > lf:
            lf = len(first)

            rest2 = []
            for r in rest:
                if first.intersection(set(r)):
                    first |= set(r)
                else:
                    rest2.append(r)
            rest = rest2

        merged.append(sorted(first))
        lists = rest
    return merged


merged_lists = merge_lists(replacements)
def constrained_sort(lst, index_groups):
    for indexes in index_groups:
        # Extract the elements to be sorted
        elements = [lst[i] for i in indexes]
        # Sort the extracted elements
        elements.sort()
        # Place the sorted elements back in their original positions
        for i, val in zip(indexes, elements):
            lst[i] = val
    return " ".join(map(str, lst))


sorted_lst = constrained_sort(bread_requests, merged_lists)
print(sorted_lst)

