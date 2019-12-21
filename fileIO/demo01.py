
import glob
import csv

# pyfiles = glob.glob('*.py')
# print(pyfiles)
#
# result = glob.escape('/Users/yaowu')
# print(result)

with open('../LICENSE', 'rt') as f:
    print(f.read(10))

with open('../LICENSE', 'rt') as f:
    print(f.buffer.read(10))