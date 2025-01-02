f = open("second/second.txt", "r")
line=f.read().split("\n")
safeReports = 0
for j in line:
    increasing=decreasing=False
    isSafe = True
    lineNums = list(map(int, j.split(" ")))
    for i in range(len(lineNums)-1):
        difference = lineNums[i+1] - lineNums[i] 
        if abs(difference) < 1 or abs(difference) > 3:
            isSafe = False
            break
        if difference > 0:
            increasing = True
        elif difference < 0 :
            decreasing = True
        
        if increasing and decreasing:
            isSafe = False
            break

    if isSafe and (increasing or decreasing):
        safeReports += 1
print(safeReports)