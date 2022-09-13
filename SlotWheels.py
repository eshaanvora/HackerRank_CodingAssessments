def slotWheels(history):
    result = 0
    for k in range(len(history)-1):
        maxColumn = []
        counter = 0
        for l in range(0,len(history)):
            maxNum = int(max(history[l]))
            maxColumn.append(maxNum)
            history[counter] = history[counter].replace(str(maxNum),"")
            counter+=1
        result += max(maxColumn)

    return result

history = ["712","246","365","312"]

print(slotWheels(history))
