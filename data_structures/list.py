
# intialize a list
sample_list = [[]]

# append to a list
sample_list[0].append(1)
sample_list[0].append(2)
sample_list[0].append(3)
sample_list[0].append(4)



sample_list.append([])
sample_list[1].append(1)
sample_list[1].append(2)
sample_list[1].append(3)
sample_list[1].append(4)

sample_list.append([])
sample_list[2].append(1)
sample_list[2].append(2)
sample_list[2].append(3)
sample_list[2].append(4)

sample_list.append([])
sample_list[3].append(1)
sample_list[3].append(2)
sample_list[3].append(3)
sample_list[3].append(4)

print(sample_list)

def display(sample_list:list):
    # witout indices
    for item in sample_list:
        for num in item:
            print(num)
    # with indices
    for i in range(len(sample_list)):
        for j in range(len(sample_list[i])):
            print(sample_list[i][j])

    return

print()
display(sample_list)