# Read content from input.txt
with open("input.txt", "r") as f:
    content = f.read()

# Open output.txt for writing
with open("processed.txt", "w") as f_out:
    n = 0
    # Iterate through the content in pairs of characters
    for i in range(0, len(content) - 1, 2):  # Step by 2 to get pairs
        char1 = content[i]
        char2 = content[i + 1]
        
        # Write 'n' char1 times
        f_out.write(str(n) * int(char1))
        
        # Write '.' char2 times
        f_out.write("." * int(char2))
        
        # Increment n
        n += 1


# Read the content of output.txt
with open("processed.txt", "r") as f:
    content = f.read().strip()  # Remove any trailing newline

# Convert content into a list for easier modification
content_list = list(content)

# Propagate values from left to right
for i in range(1, len(content_list)):
    if content_list[i] == '.':
        content_list[i] = content_list[i - 1]

# Propagate values from right to left
for i in range(len(content_list) - 2, -1, -1):
    if content_list[i] == '.':
        content_list[i] = content_list[i + 1]

# Join the modified list back into a string
filled_content = ''.join(content_list)

# Write the modified content back to output.txt
with open("output.txt", "w") as f:
    f.write(filled_content)


with open("output.txt", "r") as f:
    content = list(f.read())

n = 0
sum = 0
for num in content:
    sum += n*int(num)
    n+=1

print(sum)