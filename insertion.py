my_list = [5, 2, 4, 6, 1 ,3]
one_list = [5, 2, 4, 6, 1 ,3]
two_list = [7, 9, 11, 15 , 20]

def move_aroun(a_list):
    for j in range(1, len(a_list)):
        key = a_list[j]
        i = j-1
        while i >= 0 and a_list[i] > key:
            a_list[i+1] = a_list[i]
            i -= 1
        a_list[i + 1] = key

print(my_list)
move_aroun(my_list)
print(my_list)



def clean_my_two_list(a_list, another_list):
    