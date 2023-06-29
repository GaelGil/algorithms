import random
DICE = [1,2,3,4,5,6]

def rollDiceThreeTimes():
    """
    This function rollls a dice three times and adds up the
    sum of those dice.
    """
    numOne = random.choice(DICE)
    numTwo = random.choice(DICE)
    numThree = random.choice(DICE)
    return 0
    
rollDiceThreeTimes()



def rollOneDice():
    """
    This function rolls a dice once and retuns the number
    """
    num =  random.choice(DICE)
    return num

def rollDice():
    """
    This function rolls a dice once and retuns the number
    """
    numOne =  random.choice(DICE)
    numTwo = random.choice(DICE)
    return numOne, numTwo


def probability_of_sum(n, k, bootstrap=10000):
    """
    This function returns the probability of getting a sum greater than
    or equal to k given n dice rolls. This function uses "bootstrapping"
    (repeated random sampling) to get an approximate answer. The higher
    the bootstrap value, the more accurate the estimate will be.
    """
    results = []
    for i in range(n):
        total = 0
        numOne, numTwo = rollDice()
        total += numOne
        total += numTwo
        results.append(total)
        
    kOrAbove = [i for i in results if i >= k]

    return (len(kOrAbove)/n)



def binomial_probability(n, k, p):
    """
    This function returns the probability of getting k "successes" in
    n trials, where the probability of a success in each trial is equal
    to p.
    For instance, the probability of getting two Heads (successes) in
    two fair coin flips (fair means the probability of success = 0.5)
    is 0.25, because you can get two heads (HH) with probability:
    0.5 * 0.5 = 0.25. You can also think about the total sample space:
    {HH, HT, TH, TT} and the "probability mass function" that assigns
    each of these possible outcomes with a probability:
    {HH: 0.25, HT: 0.25, TH: 0.25, TT: 0.25}. In this simple case, the
    probabilities are all the same (0.25) so we call the function that
    generates these probabilities "uniform" - a binomial function is
    different. Also, notice that the probability of getting exactly one
    head is p(HT) + p(TH) = 0.25 + 0.25 = 0.5.
    """

    probabilitiesDict = {} # {sum: probOfSum}
    totalSums = 0
    for i in range(len(DICE)):
        current = DICE[i]
        for j in range(len(DICE)):
            sum = current + DICE[j]
            if sum in probabilitiesDict:
                probabilitiesDict[sum] += 1
            else: 
                probabilitiesDict[sum] = 1
            totalSums +=1


    print(probabilitiesDict)
    print(totalSums)

    return 0



print(probability_of_sum(10000, 10))
binomial_probability(0, 0, 0)