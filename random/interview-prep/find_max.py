



def find_max(a_list: list):
    """
    checking one value after the other
    """
    max = 0
    for i in range(len(a_list)):
        if a_list[i] > max:
            max = a_list[i]
        else:
            pass
    print(max)


def other_method(a_list:list):
    """
    using a two pointer method
    """
    pt_one = 0
    pt_two = (len(a_list)-1)
    max = 0

    for i in range(len(a_list)):
        if (a_list[pt_one]) > (a_list[pt_two]):
            pt_two -= 1
            max = a_list[pt_one]
        elif (a_list[pt_one]) < (a_list[pt_two]):
            pt_one += 1
            max = a_list[pt_two]
    print(max)
        

my_list = [8, 6, 7, 0]
sec_list = [4, 8 ,100, 11, 12, 0]
other_list = [100, 5, 4, 6, 76, 10 , 12, 43, 353 ,132, 53, 49 ,12 ]

other_method(my_list)
other_method(sec_list)
other_method(other_list)
# find_max(my_list)
# find_max(sec_list)