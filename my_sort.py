def sort_list(a_list: list, new_list:list)-> list:
    """
    """
    print(a_list)
    print(new_list)
    # new_list = []
    m_index = int( len(a_list) / 2 )
    mid = a_list[m_index]
    left_of_list = a_list[:m_index]
    left = a_list[m_index-1]
    right = a_list[m_index + 1]
    if mid < left:
        current_left = int(left)
        current_mid = int(mid)
        left_index = a_list.index(left)
        mid_index = a_list.index(mid)
        a_list[mid_index] = current_left
        a_list[left_index] = current_mid
        new_list.append(current_mid)
        new_list.append(current_left)
        return sort_list(left_of_list, new_list)
    elif mid == left:
        pass
    else:
        print('done')
    # elif 
    # if 
    # if left > right:
    #     current_left = left
    #     current_right = right
    #     left_index = a_list.index(left)
    #     right_index = a_list.index(right)
    #     a_list[right_index] = current_left
    #     a_list[left_index] = current_right


new_list = []
unsorted = [100000, 500, 499, 45, 40, 34, 33, 30, 20 ,19,  15, 14, 10 , 11]
sort_list(unsorted, new_list)