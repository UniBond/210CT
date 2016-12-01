#function definition. takes 1 argument
def flipWord(sentence):
    #variable declaration
    wordList = []
    #split sentence into words, add each word as list item
    wordList = sentence.split()
    newString = ""
    #each word in list is flipped backwards, loop over each word
    for word in wordList[::-1]:
        #add word to string, flipped alongside space.
        newString = newString + word + " "
    return newString #return string

#test function and print
print(flipWord("This is awesome"))

