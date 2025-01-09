f = open("2024/second/second.txt", "r")
line = f.read().split("\n")
safeReports = 0

for j in line:
    lineNums = list(map(int, j.split(" ")))
    isSafe = True

    for i in range(len(lineNums) - 1):  # Check up to the last pair
        difference = abs(lineNums[i] - lineNums[i + 1])

        if difference > 3 or difference < 1:
            if i > 0 and (lineNums[i] == lineNums[i + 1] or lineNums[i - 1] < lineNums[i] > lineNums[i + 1]):
                lineNums.pop(i)  # Remove the current element
                break  # Exit the loop after modifying the list
            else:
                isSafe = False
                break  # Unsafe, stop processing further

    if isSafe:
        safeReports += 1

print(safeReports)
