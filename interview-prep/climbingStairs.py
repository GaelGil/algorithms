"""
Climbing Stairs: You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1: Input: n = 2, Output: 2

Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Ex2: Input: n = 3, Output: 3

Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 2^n -> n: start with base case: What if we had 0 stairs how many ways are there to climb this? 1 -> not climbing 
 How many ways is there to climb 1 stair -> 1 thats by going up 1 
 dp[n]
 dp[0] = 1
 dp[1] = 1
 
 n = 2, dp[n] = 2
 dp[2] = dp[2-1] + dp[2-2] -> dp[2] = dp[1] + dp [0] -> dp[2] = 1 + 1  = 2
 dp[2] = 2


 n = 3
 dp[3] = dp[3-1] + dp[3-2] -> dp[3]= dp[2] + dp[1] -> dp[3] = 2 + 1 = 3

 n = 5
 for i=2 to 5:
     dp[i] = dp[i-1] + dp[i-2] -> 2
     i = 3 -> 3
     i = 4 -> 5
     i = 5 -> 8

"""

def numberOfWaysToClimb(n):
    if n == 0 or n == 1:
        return 1
    numberOfWays = []
    numberOfWays.append(1)
    numberOfWays.append(1)

    for currentIndex in range(2, n+1):
        numberOfWays[currentIndex].append(numberOfWays[currentIndex-1] + numberOfWays[currentIndex-2])
    return numberOfWays[len(numberOfWays) - 1]


print(numberOfWaysToClimb(10))
print(numberOfWaysToClimb(5))
print(numberOfWaysToClimb(2))
print(numberOfWaysToClimb(3))
