f = open("input.txt")
print (f.read())
with open("input.txt", "r") as f:
    print(max(list(map(sum, [list(map(int, x.split("\n"))) for x in f.read().rstrip("\n").split("\n\n")]))))
