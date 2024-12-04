f = open("input.txt")
content = f.read()

muls = 0

states = {}
states["start"] = {"("}
states["("] = {"1","2","3","4","5","6","7","8","9","0",","}
dig1 = False
num1 = ""
states[","] = {"1","2","3","4","5","6","7","8","9","0",")"}
num2 = ""
dig2 = False
states["end"] = {")"}

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
            num1 = ""
            num2 = ""

    else:
        dig1 = False
        dig2 = False
        check = False
        num1 = ""
        num2 = ""
        state = "start"

print(muls)
print(result)