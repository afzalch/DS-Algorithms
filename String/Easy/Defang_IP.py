# Question: Given a list representing a number add one to it and return as list
# Solution: Loop through list, add 1 if not 9, otherwise change to 0, if head is 0 append 1 to head
# Difficulty: Easy
# Time complexity: O(n) where n is the length of the input string. The algorithm needs to iterate through all the characters in the input string.
#Space complexity:O(n) where n is the length of the input string. The algorithm needs to rebuild a string. In the worst case, the input string is made of n '.', The length of output string would be 3n. O(3n) = O(n)


def defangIPaddr(self, address: str) -> str:
    res = ''
    # Loop through characters in IP address string, and add characters to the string variable (res) above
    # If character is not a period, then add character as is to res variable
    # If character is a period, then add '[.]' to the res variable 
    for i in address:
        if i != '.':
            res += i
        else:
            res += '[.]'
    return res

    # below is another solution using the builtin replace function
    # return address.replace('.', '[.]')
                