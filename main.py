file1Name = "file1.txt"
file2Name = "file2.txt"

file1 = open(file1Name, "r") # File to add ips not in already
file2 = open(file2Name, "r")

linesToAdd = []

for file2Line in file2.readlines():
    foundLineInFile1 = False
    for file1Line in file1.readlines():
        if file2Line == file1Line:
            foundLineInFile1 = True
            break
    file1.seek(0)
    if not foundLineInFile1:
        linesToAdd.append(file2Line)

file1.close()
file1 = open(file1Name, "a")

for line in linesToAdd:
    file1.write(line)

file1.close()
file2.close()
