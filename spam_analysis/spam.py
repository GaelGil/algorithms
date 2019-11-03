SPAM_DICT = {} #maybe a global variable with spam likely words, idk
NON_SPAM_DICT = {} #maybe to compare

def is_spam_or_not(message:str, message_dict:dict):
    """
    This function detemines if message is spam or 
    not based on ...
    """
    spam_num = 0
    for val in message_dict.values():
        spam_num += val
    if spam_num >= 80:
        add_to_spam(list(message))
        print('spam')
    else:
        print('not spam')

def add_to_spam(spam:list):
    """
    If the message is spam it'll append the words
    from the message to a dict. If words are alredy
    in the dict it'll add plus one the their excisting 
    value. If the word is not in the dict it will get 
    added as a key with a value of one.
    """
    # spam_list = list(spam)
    for i in range(len(spam_list)):
        if spam_list(i) in spam_dict:
            previous_val = spam_dict.get(i)
            new_val = previous_val + 1 
            spam_dict[i] = new_val 
        else:
            spam_dict[spam_list(i)] = 0 #previously at 1 now at 0 idk

def compare_to_spam(message:str):
    """
    This function takes in a string as its argument. The
    string is turned into a list which then is looped through
    comparing everyword to words in a dictionay filled with
    spam likely words. 
    """
    message_list = list(message)
    message_dict = {}
    for i in range(len(message_list)):
        word = message_list[i]
        message_dict[word] = 0
        if message_list[i] in SPAM_DICT:
            previous_val = message_dict.get(i)
            new_val = previous_val + 1 #change 1 to the value in SPAM_DICT maybe
            message_dict[i] = new_val
        elif message_list[i] not in SPAM_DICT:
            print('cool')
    return message, message_dict
    

#NOTES
#is_spam_or_not function will take in a dictonary and string as its argument
#based on value assigned to every word in compare_to_spam it will determine
#if the string/message is spam or not.
#The function add_to_spam wil either return 'spam' or 'not spam'.
#
#create a function to compare to non spam words same way it does with spam 
#words, idk.
#
#Use phrases instead
#Create driver/main function



#PROBLEMS 
#Adding all words to spam dict could add non spam words.
#
#Taking into account words like 'you', 'the', 'and', common words 
#that don't really mean much.
#
#Point system.
#
#Maybe instead of words use phrases.
#
#This would also require lots of entries to understand what spam words
#are meaning the first couple of times it would mostlikely fail. 




# not_spam = "Are you free for dinner?"
# spam = "Do you want free stuff?"

# words_and_nums = {
#     'num' : 5,
#     'red' : 2,
# }

# print(words_and_nums.get('num'))

# if 'num' in words_and_nums:
#     add = words_and_nums.get('num')
#     new_val = add + 1 
#     words_and_nums['num'] = new_val
# else:
#     print('no')

# print(words_and_nums.get('num'))


# is_spam_or_not(spam)
# is_spam_or_not(not_spam)