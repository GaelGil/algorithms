from collections import deque

balancedString = 'Im Cameron (Im 28 (and thats not old)).'
notBalancedString = 'Im Cameron (Im 28 (and thats not old).'
randString = '(((( ))'

def validator(aString:str):
    """
    This function takes in a string as its parameter and checks if the
    string has a balanced set of parenthesis. A string with a balanced
    set of parenthesis is a string that has opening and closing parenthesis
    i.e. ("this string is (balanced)", "this is not a (balanced string").
    Parameters:
    -----------
    aString: str
        A string containing paranthesis
    Returns:
    --------
    boolean
       True if the string contains a balanced set of parenthesis
       False if the string doesn't contain a balanced set of parenthesis
       False if it contains no parenthesis
    """
    cleanString = []
    stack = deque()
    for i in range(len(aString)):
        if aString[i] == ("(") or aString[i] == (")"):
            stack.append(aString[i])
            cleanString.append(aString[i])

    x = 0
    while (x < len(cleanString)):
        
        if (stack.pop() == cleanString[x]):
            return False
        x +=1
        
    return True



print(validator(balancedString))
print(validator(notBalancedString))
print(validator(randString))