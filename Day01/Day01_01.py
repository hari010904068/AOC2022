f = open("input.txt")
#print (f.read().rstrip("\n").split("\n\n"))
#print (f.read())
#solution one liner
#print('6616\n7349\n7758\n1591\n6068\n9217\n6924\n6766'.split("\n"))
#l = ['6616', '7349', '7758', '1591', '6068', '9217', '6924', '6766']
##l1 =(map(int,l))
# l2 = (list(l1))
# print(max(l2))
# print(max(list((map(sum,l2)))))
# with open("input.txt", "r") as f:
#     print(max(list(map(sum, [list(map(int, x.split("\n"))) for x in f.read().rstrip("\n").split("\n\n")]))))

t=0
x=open("in.txt", "r").read().split("\n\n")
print(x)


for i in x:
    t=max(t,sum([int(r) for r in i.splitlines()]))


print(t)