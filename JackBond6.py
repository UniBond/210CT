def flipWord(sentence):
    wordList = []
    wordList = sentence.split()
    newString = ""
    for word in wordList[::-1]:
        newString = newString + word + " "
    return newString

print(flipWord("This is awesome"))
