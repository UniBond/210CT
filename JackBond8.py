#vowelRemove function, 3 arguments (string, string and int). Runs recursively
def vowelRemove(string, newString, num):
    #variable declaration
    newString = newString
    #list of vowels
    vowelList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    if num < len(string):
        try:
            #is character is a vowel
            if string[num] in vowelList:
                print(string[num] + " is in vowelList")
                #recursive call
                vowelRemove(string, newString, num + 1)
            #if character is not a vowel
            else:
                #append character to string
                newString = newString + string[num]
                #recursive call
                vowelRemove(string, newString, num + 1)
        except IndexError:
            pass
    #if number is now greater than string
    else:
        #print the string, with vowels removed
        print(newString)
        #return, exit program
        return


#allows program to run. Function call, and arguments. Test
print(vowelRemove("beautiful", "", 0))
