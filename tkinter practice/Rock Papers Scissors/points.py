uw = int(input("enter value: "))
ul = int(input("enter value: "))
cw = int(input("enter value: "))
cl = int(input("enter value: "))


f = open("rsp.txt", "w")
f.write(f"{uw}{ul}{cw}{cl}")
f.close()

r = open("rsp.txt", "r")
x = r.read()

uw = (f"{x[0]}+{x[1]}")
ul = (f"{x[2]}+{x[3]}")
cw = (f"{x[4]}+{x[5]}")
cl = (f"{x[6]}+{x[7]}")

print(uw, ul, cw, cl)