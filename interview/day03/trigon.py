import sys

if __name__ == "__main__":
    str1 = ''.join(sys.stdin.readline().strip().split())
    str2 = sys.stdin.readline().strip()
    count = 0
    for i in range(len(str1) - len(str2)):
        if str1[i:i+len(str2)] == str2:
            count += 1
    print(count)