f = open("input2.txt")

safe_words = 0
new_safe_words = 0

for line in f:
    numbers = line.split()
    
    try:
        numbers = [int(num) for num in numbers]  
    except ValueError:
        continue  
    
    if len(numbers) < 2:
        continue  

    prev = numbers[0]
    safe = True
    violation = 0

    if numbers[1] - numbers[0] > 0:  # Gradual increase
        for i in range(1, len(numbers)):
            if (abs(numbers[i] - prev) > 3) or (numbers[i] - prev <= 0):
                safe = False
                violation += 1
                
            prev = numbers[i]
    else:  # Gradual decrease
        for i in range(1, len(numbers)):
            if (abs(numbers[i] - prev) > 3) or (numbers[i] - prev >= 0):
                safe = False
                violation += 1
            prev = numbers[i]
    
    if violation < 2:
        new_safe_words += 1

    if safe:
        safe_words += 1

print(safe_words)
print(new_safe_words)

f.close()
