# Read contents from the input file
with open("file.txt", "r") as file:
    lines = file.readlines()

# Strip whitespace, sort the lines, and write to output file
with open("output.txt", "w") as file:
    for line in sorted(line.strip() for line in lines):
        file.write(line + "\n")