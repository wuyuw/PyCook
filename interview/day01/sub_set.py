
def fix_binary_string(val, setlen):
    binary = bin(val).replace('0b', '')
    fix_string = '0' * (setlen - len(binary))
    return fix_string + binary


def get_set_by_binary(val, collection):
    lst = list(collection)
    binary = fix_binary_string(val, len(lst))
    sub = []
    for i in range(len(lst)):
        if binary[i] == '1':
            sub.append(lst[i])
    return sub


def find_max_by_len(collection):
    val = 0
    for i in range(len(set(collection))):
        val |= (1 << i)
    return val


def find_all_subset(collection):
    max_int = find_max_by_len(collection)
    for i in range(max_int+1):
        print(i)
        print(get_set_by_binary(i, collection))



if __name__ == '__main__':
    # print(fix_binary_string(3, 4))
    # print(find_max_by_len([1, 2, 3, 4, 5]))
    find_all_subset(['a', 'b', 'c'])
