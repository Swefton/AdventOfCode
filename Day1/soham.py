f = open("file.txt")

array1 = []
array2 = []

for line in f:
    words = line.split()  
    for i, word in enumerate(words):
        if i % 2 == 0:
            array1.append(int(word))
        else:
            array2.append(int(word))

array1.sort()
array2.sort()

result = 0

for i in range(len(array1)):
    result += abs(array2[i] - array1[i])

print(result)

map = {}

for number in array1:
    map[number] = 0

for number in array2:
    if number in map:
        map[number] += 1

similarity_score = 0

for key in map:
    similarity_score += key * map[key]

print(similarity_score)