NUMS = [1, 3, 4, 6, 9, 11, 33, 99, 1089, 3454, 199089] # ordered numbers

# 
# we only care about how long things take to run in terms of the size of the input,
# size_of_input = N = len(NUMS)
# 

def is_num_in_list(num):
    """
    if the num is in NUMS, this function returns True, otherweise False.
    The time complexity of the algorithm is O(N)
    """
    for i in NUMS:
        if i == num:
            return True


def is_num_in_list_2(target, list):
    """
    This function takes in a list and a target to find as its argument
    we get the middle index to split lists in half if the middle is not
    the target it calls function again and repeats again until found.
    The time complexity of this algorithms is O(ln(N))
    """
    m_index = int( len(list) / 2 )
    m = list[m_index]
    l = list[:m_index]
    r = list[m_index + 1:]

    if target == m:
        print(f'found {m}')
        return True
    elif target > m:
        print('not found yet')
        is_num_in_list_2(target, r)
    elif target < m:
        # print(l, m, r)
        print('not found yet')
        is_num_in_list_2(target, l)

is_num_in_list_2(6, NUMS)