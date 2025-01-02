#part one

left = []
right = []
totalArr = []
total = 0
s = open("first.txt", "r")
s=s.read()
s=s.split("\n")
left=[]
right=[]
for line in s:
    l,r = map(int,line.split("   "))
    left.append(l)
    right.append(r)
left = sorted(left, key=abs,reverse=False)
right = sorted(right, key=abs,reverse=False)

for i in range(0, len(left), 1):
    totalArr.append(abs(left[i] - right[i]))
    total += totalArr[i]

print(total)
