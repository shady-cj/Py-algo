# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


# This Solution Runs in 0(N) - Linear
def baseball(ops: list) -> int:
    newList = []
    sum_list = 0
    
    for i in ops:
        newValue = None
        if i == "+":
            newValue = int(newList[len(newList) - 1]) + int(newList[len (newList) - 2])
        elif i == "D":
            newValue = int(newList[len(newList) - 1]) * 2
        elif i != "C":
            newValue = int(i)
        if newValue == None:
            newList.pop()
        else:
            newList.append(str(newValue))
    for j in newList:
        sum_list += int(j)
    return sum_list
    
num = baseball(["5", "2", "C", "D", "+"])
print(num) # 30
num = baseball(["5", "-2", "4", "C", "D", "9", "+", "+"])
print(num) # 27

# Optimized Method 0(LogN)
def baseball_opt(ops, index = 0, arr = []):
    if (index == len(ops)):
        return 0
    sum = 0
    cancel = False
    if (ops[index] == "+"):
        sum += int(arr[len(arr) - 1]) + int(arr[len(arr) - 2])
    elif (ops[index] == "C"):
        sum -= int(arr.pop())
        cancel = True
    elif (ops[index] == "D"):
        sum += int(arr[len(arr) - 1]) * 2
    else:
        sum += int(ops[index])
    if (not cancel):
        arr.append(str(sum))
    sum += baseball_opt(ops, index + 1, arr)
   
    return sum
   
   
   
num = baseball_opt(["5", "2", "C", "D", "+"])
print(num) # 30
num = baseball_opt(["5", "-2", "4", "C", "D", "9", "+", "+"])
print(num) # 27

mapper = {
    "+":  lambda op: int(op[len(op) - 1]) + int(op[len(op) - 2]),
    "C": lambda op: -1 * int(op.pop()),
    "D": lambda op: int(op[len(op) - 1]) * 2
}
def baseball_opt2(ops, index = 0, arr = []):
    if (index == len(ops)):
        return 0
    sum = 0
    cancel = False
    if (ops[index] in mapper):
        if (ops[index] == "C"):
            cancel = True
        sum += mapper[ops[index]](arr)
    else:
        sum += int(ops[index ])
    if (not cancel):
        arr.append(str(sum))
    sum += baseball_opt2(ops, index + 1, arr)
   
    return sum
   
   
   
num = baseball_opt2(["5", "2", "C", "D", "+"])
print(num) #30
num = baseball_opt2(["5", "-2", "4", "C", "D", "9", "+", "+", "+", "5"])
print(num) #51
