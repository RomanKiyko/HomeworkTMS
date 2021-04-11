st = str(input())
centr = st[int(len(st) / 2)]
print(centr)
if centr == st[0]:
    print(st[1:-1])