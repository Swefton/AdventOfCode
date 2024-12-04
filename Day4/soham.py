# Read the grid from the file
with open("input_spicy.txt") as f:
    content = f.read()

grid = [list(line) for line in content.strip().splitlines()]
rows = len(grid)
cols = len(grid[0])
word = "XMAS"
reverse_word = word[::-1]
word_len = len(word)
count = 0

# Directions represented as (dx, dy)
directions = [
    (-1, -1),  # Up-Left
    (-1, 0),   # Up
    (-1, 1),   # Up-Right
    (0, -1),   # Left
    (0, 1),    # Right
    (1, -1),   # Down-Left
    (1, 0),    # Down
    (1, 1)     # Down-Right
]

for row in range(rows):
    for col in range(cols):
        if grid[row][col] != "X":
            continue
        # Check each direction
        for dx, dy in directions:
            found_word = ""
            for k in range(word_len):
                nx, ny = row + dx * k, col + dy * k
                if 0 <= nx < rows and 0 <= ny < cols:
                    found_word += grid[nx][ny]
                else:
                    break
            if found_word == word or found_word == reverse_word:
                count += 1

print(count)

count = 0
myset = set()

for row in range(1, rows - 1):
    for col in range(1, cols -1):
        if grid[row][col] != "A":
            continue
        # Check each direction
        try:
            if ((grid[row-1][col-1] == "M" and grid[row+1][col+1] == "S") or (grid[row-1][col-1] == "S" and grid[row+1][col+1] == "M")):
                if ((grid[row-1][col+1] == "M" and grid[row+1][col-1] == "S") or (grid[row-1][col+1] == "S" and grid[row+1][col-1] == "M")):
                    if(row,col) in myset:
                        continue
                    else:
                        count += 1
                        myset.add((row,col))
                    
        except IndexError:
            pass

print(count)

# f = open("day4.txt")
# content = f.read()

# grid = [list(line) for line in content.splitlines()]

# count = 0

# for row in range(len(grid)):
#     for col in range(len(grid[row])):
        
#         if grid[row][col] != "X":
#             continue

#         try:
#             if "".join([grid[row][col+i] for i in range(4)]) == "XMAS" or "".join([grid[row][col+i] for i in range(4)]) == "SAMX":  # Right
#                 count += 1
#             if "".join([grid[row][col-i] for i in range(4)]) == "SAMX" or "".join([grid[row][col-i] for i in range(4)]) == "XMAS":  # Left
#                 count += 1
#             if "".join([grid[row+i][col] for i in range(4)]) == "XMAS" or "".join([grid[row+i][col] for i in range(4)]) == "SAMX":  # Down
#                 count += 1
#             if "".join([grid[row-i][col] for i in range(4)]) == "XMAS" or "".join([grid[row-i][col] for i in range(4)]) == "SAMX":  # Up
#                 count += 1
#             if "".join([grid[row+i][col+i] for i in range(4)]) == "XMAS" or "".join([grid[row+i][col+i] for i in range(4)]) == "SAMX":  # Down Right
#                 count += 1
#             if "".join([grid[row+i][col-i] for i in range(4)]) == "XMAS" or "".join([grid[row+i][col-i] for i in range(4)]) == "SAMX":  # Down Left
#                 count += 1
#             if "".join([grid[row-i][col+i] for i in range(4)]) == "XMAS" or "".join([grid[row-i][col+i] for i in range(4)]) == "SAMX":  # Up Right
#                 count += 1
#             if "".join([grid[row-i][col-i] for i in range(4)]) == "XMAS" or "".join([grid[row-i][col-i] for i in range(4)]) == "SAMX":  # Up Left
#                 count += 1
#         except IndexError:
#             pass

# print(count)







# import re

# f = open("day4.txt")
# content = f.read()


# xmas_count = len(re.findall(r'\bXMAS\b', content))
# samx_count = len(re.findall(r'\bSAMX\b', content))

# with open("day4.txt", "r") as f:
#     content = [line.strip().split() for line in f]

# transposed = zip(*content)

# with open("day4_transposed.txt", "w") as f:
#     f.writelines("\t".join(row) + "\n" for row in transposed)

# up_count = len(re.findall(r'\bXMAS\b', transposed))
# down_count = len(re.findall(r'\bSAMX\b', transposed))

# print(xmas_count)
# print(samx_count)
