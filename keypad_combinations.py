# return possible strings of given keypad number

def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):

    digits = list(str(num))
    possiblestrings = []

    if len(digits) == 1:
        chars = [i for i in list(get_characters(int(digits[0])))]
        if len(chars) != 0:
            for c in chars:
                possiblestrings.append(c)
    else:
        first = [i for i in list(get_characters(int(digits[0])))] 
        remaining = ''
        for i in digits[1:]:
            remaining = remaining + i

        sub_possiblestrings = keypad(int(remaining))
        
        for sub_string in sub_possiblestrings:
            for f in first:
                newstring = f + str(sub_string)
                possiblestrings.append(newstring)
    
    if len(possiblestrings) == 0:
        possiblestrings.append("")
                
    return possiblestrings


print(keypad(345))