import time
kongre = ["samsun", "amasya"]
for i in kongre:
    print(i.upper())

for i in kongre:
    print(i.lower())

for i in kongre:
    print(i.title())

m = "MARMARA"
cntm = m.center(15)
print(cntm, "selam")

cntm = m.center(15, "*")
print(cntm)

cntm = " MAYİS 19"
cntm = m.center(13, "1")
print(cntm)

m = "A"
cntm = m.rjust(3, "#")
print(cntm)

ikibit = "11"
print("2 bit ", ikibit)
print("4 bit ", ikibit.zfill(4))

s = "MARMARA"
print(s.replace("A", "X"))
print(s)

