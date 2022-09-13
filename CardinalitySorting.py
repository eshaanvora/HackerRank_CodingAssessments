
def binaryRep(numArray):

    dict = {num: 0 for num in numArray}

    for i in dict:
        cardinality = 0
        for k in bin(i):
            if k == "1":
                cardinality += 1
        dict[i] = cardinality

    #Sort numbers by cardinality and then by integer value
    #Key = number, Value = cardinality
    sorted_List = sorted(dict.items(), key=lambda x:(x[1],x[0]), reverse=True)

    #Convert sorted list to dictionary and return dictionary
    #sorted_Dict = {}
    #for i in sorted_List:
        #sorted_Dict[i[0]] = i[1]
    #return(sorted_Dict)

    #Convert sorted list to list and return
    result = []
    for i in sorted_List:
        result.append(i[0])

    return(result)

numArray = [5, 2, 3, 9, 4, 6, 7, 15, 32]

print(binaryRep(numArray))
