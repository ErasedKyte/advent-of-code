left = []
right = []
totalArr = []
total = 0
s = open("first/first.txt", "r")
s=s.read()
s=s.split("\n")
left=[]
right=[]

for line in s:
    l,r = map(int,line.split("   "))
    left.append(l)
    right.append(r)

for i in range(0, len(left)-1, 1):
    x=0
    for j in range(0,len(right)-1,1):
        if left[i] == right[j]:
            x += 1
    total += x*left[i]
print(total)