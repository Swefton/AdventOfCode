with open("input.txt") as f:
    content = f.read()

char_array = [list(line) for line in content.splitlines()]

antennas_location = {}

for i in range(len(char_array)):
    for j in range(len(char_array[i])):
        antenna = char_array[i][j]

        if antenna.isalnum():
            if antenna in antennas_location:
                antennas_location[antenna].append((i,j))
            else:
                antennas_location[antenna] = [(i,j)]

antinodes = set()

height = len(char_array)
width = len(char_array[0])

for antenna in antennas_location:
    locations = antennas_location[antenna]
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            location1 = locations[i]
            location2 = locations[j]
            difference = (location2[0] - location1[0], location2[1] - location1[1])
            antinode1 = (location1[0] - difference[0], location1[1] - difference[1])
            antinode2 = (location2[0] + difference[0], location2[1] + difference[1])
            
            if(0 <= antinode1[0] < height and 0 <= antinode1[1] < width):
                antinodes.add(antinode1)
            if(0 <= antinode2[0] < height and 0 <= antinode2[1] < width):
                antinodes.add(antinode2)

print(len(antinodes))

#part 2

new_antinodes = set()

for antenna in antennas_location:
    locations = antennas_location[antenna]
    if len(locations) == 1:
        continue

    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            location1 = locations[i]
            location2 = locations[j]
            difference = (location2[0] - location1[0], location2[1] - location1[1])
            
            n = 1
            while True:
                antinode = (location1[0] + n*difference[0], location1[1] + n*difference[1])
                
                if not (0 <= antinode[0] < height and 0 <= antinode[1] < width):
                    #print("womp")
                    break

                new_antinodes.add(antinode)
                n += 1
            
            n = 1
            while True:
                antinode = (location2[0] - n*difference[0], location2[1] - n*difference[1])
                
                if not (0 <= antinode[0] < height and 0 <= antinode[1] < width):
                    #print("womp")
                    break

                new_antinodes.add(antinode)
                n += 1
            
print(new_antinodes)
print(len(new_antinodes))