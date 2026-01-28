lp = open('Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.new.md', 'r', encoding='utf-8').readlines()
pl = open('Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.new.md', 'r', encoding='utf-8').readlines()

lp_count = sum(1 for l in lp if l.startswith('- '))
pl_count = sum(1 for l in pl if l.startswith('- '))

print(f'Lengxuan→Polski: {lp_count} entries')
print(f'Polski→Lengxuan: {pl_count} entries')
print(f'Difference: {abs(lp_count - pl_count)}')
