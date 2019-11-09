text = "this is a sentence", "so is this one"
my_list = 'my words are here and they will be list'


words = my_list.split()
words_list =  list(words)

for i in range(len(words_list)-1):
    current_word = words_list[i]
    next_word = words_list[i + 1]
    phrase = current_word + ' ' + next_word
    print(phrase)
    
