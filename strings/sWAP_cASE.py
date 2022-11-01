#  You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to uppercase letters and vice versa.



def swap_case(s):
    output=''
    for character in s:
        if character.isupper():
            output=output+character.lower()
        elif character.islower():
            output=output+character.upper()
        else:
            output=output+character
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)