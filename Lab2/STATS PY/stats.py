# reads if list of variables exists, otherwise will stop execute and return to 0
def mean(list):
    if len(list) == 0:
        return 0
    average = 0
    for number in list:
        average += number
    return average/len(list)
# Sort the list and print the number at its midpoint
def median(list):
    list.sort()
    midpoint = len(list) // 2
    print("The median is", end=" ")
    if len(list) % 2 == 1:
        return list[midpoint]
    else:
        return(list[midpoint] + list[midpoint - 1]) / 2

def mode(list):
    theDictionary={}
    for word in list:
        number = theDictionary.get(word, None)
        if number == None:
            # word entered for the first time
            theDictionary[word] = 1
        else:
            # word already seen, increment its number
            theDictionary[word] = number + 1

    # Find the mode by obtaining the maximum value
    # in the dictionary and determining its key
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            print("The mode is", key)
    return theDictionary

def main():
    print("The mean is ", mean(range(1, 14)))
    print(mode([2, 8, 5, 2, 8, 8, 8, 5, 8, 5]))
    print(median([1, 2, 3, 4]))

main()