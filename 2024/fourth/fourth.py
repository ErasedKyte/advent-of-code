# Read the input file
file = open("2024/fourth/fourth.txt", "r").read().split("\n")
lineLength = len(file[0])  # Number of columns
numOfLines = len(file)  # Number of rows
count = 0
word = ["X", "M", "A", "S"]  # Word to search for

for i in range(numOfLines):
    for j in range(lineLength):
        # Horizontal (right)
        if j + len(word) <= lineLength:
            if file[i][j:j+4] == ''.join(word):  # Forward
                count += 1
            if file[i][j:j+4] == ''.join(word[::-1]):  # Reverse
                count += 1

        # Vertical (down)
        if i + len(word) <= numOfLines:
            if all(file[i+k][j] == word[k] for k in range(len(word))):  # Forward
                count += 1
            if all(file[i+k][j] == word[::-1][k] for k in range(len(word))):  # Reverse
                count += 1

        # Diagonal (down-right)
        if i + len(word) <= numOfLines and j + len(word) <= lineLength:
            if all(file[i+k][j+k] == word[k] for k in range(len(word))):  # Forward
                count += 1
            if all(file[i+k][j+k] == word[::-1][k] for k in range(len(word))):  # Reverse
                count += 1

        # Diagonal (down-left)
        if i + len(word) <= numOfLines and j - len(word) >= -1:
            if all(file[i+k][j-k] == word[k] for k in range(len(word))):  # Forward
                count += 1
            if all(file[i+k][j-k] == word[::-1][k] for k in range(len(word))):  # Reverse
                count += 1

# Print the final count
print("Total occurrences of 'XMAS':", count)
