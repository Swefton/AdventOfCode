f = open("input.txt")
content = f.read()

muls = 0

states = {}
states["start"] = {"("}
states["("] = {"1","2","3","4","5","6","7","8","9","0",","}
states[","] = {"1","2","3","4","5","6","7","8","9","0",")"}
states["end"] = {")"}

dig1 = False
num1 = ""
num2 = ""
dig2 = False
state = "start"
buffer = ""
check = False
result = 0


for char in content:    
    buffer += char  
    if len(buffer) > 3:  
        buffer = buffer[-3:]

    if buffer == "mul":
        check = True
        continue

    if not check:
        continue

    if char in states[state]:    
        if state == "(" and char.isdigit():
            dig1 = True
            num1 += char
            continue

        if state == "," and char.isdigit():
            dig2 = True
            num2 += char
            continue
        
        match state:
            case "start":
                state = "("
            case "(":
                if dig1:
                    state = ","
                else:
                    state = "start"
            case ",":
                if dig2:
                    state = "end"
                else:
                    state = "start"
            case "end":
                state = "start"

        if state == "end":
            muls += 1
            check = False
            result += int(num1)*int(num2)
            dig1 = False
            dig2 = False
            num1 = ""
            num2 = ""
            state = "start"

    else:
        dig1 = False
        dig2 = False
        check = False
        num1 = ""
        num2 = ""
        state = "start"

print(muls)
print(result)

#part 2
muls = 0
dig1 = False
num1 = ""
num2 = ""
dig2 = False
state = "start"
buffer = ""
buffer1 = ""
buffer2 = ""
check = False
result = 0
do = True


for i, char in enumerate(content):
    buffer += char  
    if len(buffer) > 3:  
        buffer = buffer[-3:]
    
    if buffer == "mul":
        check = True
        continue

    buffer1 += char    
    if len(buffer1) > 7:
        buffer1 = buffer1[-7:]
    if buffer1 == "don't()":
        do = False
    
    buffer2 += char
    if len(buffer2) > 4:
        buffer2 = buffer2[-4:]
    if buffer2 == "do()":
        do = True

    if not do or not check:
        continue

    if char in states[state]:    
        if state == "(" and char.isdigit():
            dig1 = True
            num1 += char
            continue

        if state == "," and char.isdigit():
            dig2 = True
            num2 += char
            continue
        
        match state:
            case "start":
                state = "("
            case "(":
                if dig1:
                    state = ","
                else:
                    state = "start"
            case ",":
                if dig2:
                    state = "end"
                else:
                    state = "start"
            case "end":
                state = "start"

        if state == "end":
            muls += 1
            check = False
            result += int(num1)*int(num2)
            dig1 = False
            dig2 = False
            num1 = ""
            num2 = ""
            state = "start"
            #print(content[i-15:i+1])

    else:
        dig1 = False
        dig2 = False
        check = False
        num1 = ""
        num2 = ""
        state = "start"

print(muls)
print(result)
