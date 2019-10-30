PEOPLE = []

def find_target(nums: list, target: int):
    for i in range(len(nums)):
        for j in range(len(nums)):
            first = nums[i]
            sec = nums[j]
            if (first + sec) == target:
                print(first, sec)
            

nums = [2, 7, 11, 15]
find_target(nums, 9)


"""
SWE / Full-stack dev
     - algorithms: leetcode/hackerrank (easily solve MEDIUM problems, make significant progress on HARD)
     - coding knowledge: avoiding globals, can you functionalize stuff, can add comments, avoid        single-letter variables
     - CS fundamentals:
        what kind of data structure is implemented by a python dictionary? -- hashmap: https://en.wikipedia.org/wiki/Hash_table
        python list = array
        what is a hash
    - can you do projects:
        technical blog -- why did you put your shoe data into a sqlite database instead of a redis database?
        can you make a simple flask serve that serves an html page
"""

"""
Full-stack: web-dev
- make servers
- work with databses
- create web apps
- phone apps
- front-end -html/css
- communicate ideas
- AWS
- bash
- CS fundamentals
"""
racecar