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
print(num)
num = baseball(["5", "-2", "4", "C", "D", "9", "+", "+"])
print(num)


# More Optimized Solution

def Optimized_solution(ops, index = 0):
    sum = 0
    if (index == len(ops)):
        return 0
    present = int(ops[index])
    prev = int(ops[index - 1])
    if (ops[index] == "+"):
        sum += present + prev
    elif (ops[index] == "D"):
        sum += prev * 2
    elif (ops[index] == "C"):
        sum -= prev
    else:
        sum += present
    sum += Optimized_solution(ops, index + 1)
    
    return sum
    
print("Optimized--------------------")
print(Optimized_solution(["5", "2", "C", "D", "+"]))
