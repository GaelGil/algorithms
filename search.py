NUMS = [1, 3, 4, 6, 9, 11, 33, 99, 1089, 3454, 199089] # ordered numbers

"""
we only care about how long things take to run in terms of the size of the input,
size_of_input = N = len(NUMS)
"""

# The time complexity of the algorithm is O(N)
def is_num_in_list(num):
    """
    if the num is in NUMS, this function returns True, otherweise False
    """
    for i in NUMS:
        if i == num:
            return True


# The time complexity of this algorithms is O(ln(N))
def is_num_in_list_2(target, list):
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

