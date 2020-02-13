
def merge_sort(l):
    if len(l) <= 1:
        return l
    half = len(l) // 2
    first = merge_sort(l[:half])
    second = merge_sort(l[half:])
    sorted_l = []
    i = 0
    j = 0
    while i < len(first) or j < len(second):
        if i < len(first) and j < len(second):
            if first[i] <= second[j]:
                sorted_l.append(first[i])
                i += 1
            else:
                sorted_l.append(second[j])
                j += 1
        elif i < len(first):
            sorted_l.append(first[i])
            i += 1
        else:
            sorted_l.append(second[j])
            j += 1
    return sorted_l


if __name__ == '__main__':
    l1 = [3, 2, 6, 9, 1, 3, 1, 3, 5, 3, 4]
    print(merge_sort(l1))