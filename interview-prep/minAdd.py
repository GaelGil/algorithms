
# Input: "())"
# Output: 1


# Example 2:

# Input: "((("
# Output: 3


# Example 3:

# Input: "()"
# Output: 0
# [ (   ]


def minAddToMakeValid( S: str) -> int:
    """
            
        opened = closed = 0
        
        for i in S:
            if closed == 0 and i == ')':
                opened += 1
            else:
                if i == '(':
                    closed +=1
                else: 
                    closed -=1
        
        minVal = opened + closed
        
        return minVal
    """
    ans = bal = 0
    for i in S:
        currentChar = i
        if currentChar == '(':
            bal += 1
        else:
            bal -= 1
        if bal == -1:
            bal += 1 # 0
            ans += 1 # 1 
    return bal + ans


    



print(minAddToMakeValid('())'))
print(minAddToMakeValid('((('))
print(minAddToMakeValid('()'))
print(minAddToMakeValid('()))(('))