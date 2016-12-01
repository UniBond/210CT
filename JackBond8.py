def vowelRemove(string, newString, num):
    newString = newString
    vowelList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if num < len(string):
        try:
            if string[num] in vowelList:
                print(string[num] + " is in vowelList")
                vowelRemove(string, newString, num + 1)
            else:
                newString = newString + string[num]
                vowelRemove(string, newString, num + 1)
        except IndexError:
            pass
    else:
        print(newString)
        return



print(vowelRemove("beautiful", "", 0))
