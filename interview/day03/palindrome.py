

def longest_palindrome(s):
    s = '#'.join(list(s))
    length = len(s)
    r_side = 0
    r_side_center = 0
    half_len = [0 for _ in s]
    center = 0
    longest_half = 0
    for i in range(len(s)):
        need_calc = True
        if r_side > i:
            l_center = r_side_center * 2 - i
            half_len[i] = half_len[l_center]
            if i + half_len[i] > r_side:
                half_len[i] = r_side - i
            if i + half_len[l_center] < r_side:
                need_calc = False
        if need_calc:
            while i - 1 - half_len[i] > 0 and i + 1 + half_len[i] < length:
                if s[i + 1 + half_len[i]] == s[i - 1 - half_len[i]]:
                    half_len[i] += 1
                else:
                    break
        r_side = i + half_len[i]
        r_side_center = i
        if half_len[i] > longest_half:
            center = i
            longest_half = half_len[i]
    return s[center - longest_half + 1: center + longest_half + 1]


def longest_v2(s):
    s = '#'.join(list(s))
    max_half_length = 0
    center = 0
    for i in range(len(s)):
        half_len = 1
        while i - half_len >= 0 and i + half_len <= len(s) -1 and s[i - half_len] == s[i + half_len]:
            half_len += 1
        if half_len > max_half_length:
            max_half_length = half_len
            center = i
    sub = s[center - max_half_length + 1: center + max_half_length]
    return ''.join(sub.split('#'))



# while True:
#     try:
#         line = input()
#         if not line:
#             break
#         res = longest_palindrome(line)
#         print(res)
#     except:
#         break

if __name__ == '__main__':
    # print(longest_palindrome('ABBAKK'))
    print(longest_v2('ABBAkk'))