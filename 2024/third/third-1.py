import re
file = open("2024/third/third.txt", "r")
f = file.read()
x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)",f )
y = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)",f )

def findMul():
    total = 0
    for i in range(len(x)):
        x[i]=x[i].replace("mul(", "").replace(")", "").split(",") 
        total += int(x[i][0]) * int(x[i][1])
    print(total)
            
def enableMul():
    total = 0
    enable = ""
    for i in range(len(y)):
        if y[i] == "don't()" or y[i] == "do()":
            enable = y[i]
            
        if enable != "don't()" and y[i] != "do()" and y[i] != "don't()" :
            y[i]=y[i].replace("mul(", "").replace(")", "").split(",") 
            total += int(y[i][0]) * int(y[i][1])
    print(total)
if __name__ == "__main__":
    enableMul()
    findMul()
    
