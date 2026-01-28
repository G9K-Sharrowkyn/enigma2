import sys
lines = sys.stdin.readlines()
count = sum(1 for l in lines if l.startswith('- '))
print(f'Entries: {count}')
