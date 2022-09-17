import sys

# opening the file in read mode
file = open(sys.argv[1], "r")
replacement = ""
# using the for loop
for line in file:
    line = line.strip()
    if line.find("M3")>-1:
        changes = "M3 S30"
    elif line.find("M5")>-1:
        changes = "M3 S90"
    else:
        changes = line
    replacement = replacement + changes + "\n"

file.close()
# opening the file in write mode
fout = open(sys.argv[1], "w")
fout.write(replacement)
fout.close()