


def freq(nums:list) -> int:
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            seen[nums[i]] += 1
        else:
            seen[nums[i]] = 1

    answer = [0, 0]
    for i in seen:
        if seen[i] > answer[1]:
            answer = [i, seen[i]]
    print(answer)
    return answer


freq([1 , 231, 4, 3 ,4 ,4 ,4 , 19])