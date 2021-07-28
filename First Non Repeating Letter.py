#Algorithm that finds the first letter of a string that does not repeat 

def firstNonRepeatingLetter(line):
    # verfies length of string
    if len(line) < 1:
        return False

    Count = {}
    temp = []

    # creates the dictionary with all the counts of each letter
    for letter in line:
        Count[letter] = line.count(letter)

    # selects all the letter that have been coutned as 1
    for x in Count:
        if Count[x] == 1:
            temp.append(x)

    # if the letters counted as 1 is 0 then False 
    if len(temp) < 1:
        return False
    else:
        return temp[0]
    

first = firstNonRepeatingLetter("aaabcccdeeef")
second = firstNonRepeatingLetter("abcdabc")
third = firstNonRepeatingLetter("abcdabcd")


print("Test Case 1: {}".format(first))
print("Test Case 2: {}".format(second))
print("Test Case 3: {}".format(third))
