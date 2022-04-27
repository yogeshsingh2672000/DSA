def checkZ(str_input):
    for i in range(len(str_input)-1, -1, -1):
        if str_input[i] == "Z":
            continue
        else:
            return changeMid(str_input, i)
    return -1

def changeMid(str_input, idx):
    ord_count = ord(str_input[idx])
    temp = list(str_input)
    if (ord(str_input[idx]) < 90):
        temp[idx] = chr(ord_count+1)
        for i in range(idx+1, len(temp)):
            temp[i] = "A"
    else:
        str_input[idx] = chr(ord_count+1)
    return "".join(temp)


result = []
def magicAlpha(user_input, itr):
    while itr > 0:
        ord_count = ord(user_input[-1])
        while ((ord_count >= 65)and(ord_count <= 90)):
            temp = user_input[0:len(user_input)-1]
            temp += chr(ord_count)
            result.append(temp)
            ord_count += 1
            itr -= 1
            if itr == 0:
                return
        else:
            check = checkZ(user_input)
            if check == -1:
                count = len(user_input)
                user_input = "A"*(count+1)
            else:
                user_input = check
    return

user_input = "AZZ"
itr = 100
magicAlpha(user_input, itr)

for i in range(len(result)):
    print(f"{i}  {result[i]}")

