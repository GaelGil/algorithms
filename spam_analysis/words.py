SPAM_DICT = {
    'you' : 0,
    'won' : 0 ,
    'free' : 0,
    'money' : 0,
    'try' : 0,
    'claim' : 0,
    'prize' : 0,
    'get' : 0,
    'eligable': 0,
}



def is_spam_or_not(message:list, message_dict:dict):
    """
    This function detemines if message is spam or 
    not based on ...
    """
    spam_num = 0
    for val in message_dict.values():
        spam_num += val
    if spam_num >= ((len(message)/2) * 10):
        add_to_spam(message)
        print('spam')
        return('spam')
    else:
        return('ham')
        return('ham')

def add_to_spam(spam:list):
    """
    If the message is spam it'll append the words
    from the message to a dict. If words are alredy
    in the dict it'll add plus one the their excisting 
    value. If the word is not in the dict it will get 
    added as a key with a value of one.
    """
    for i in range(len(spam)):
        word = spam[i]
        if spam[i] in SPAM_DICT:
            previous_val = SPAM_DICT.get(word)
            new_val = previous_val + 5
            SPAM_DICT[i] = new_val 
        else:
            SPAM_DICT[word] = 0 #previously at 1 now at 0 idk

def compare_to_words(message:str):
    """
    This function takes in a string as its argument. The
    string is turned into a list which then is looped through
    comparing everyword to words in a dictionay filled with
    spam likely words. 
    """
    # message = message.lower()
    message = message.split()
    message_list = list(message)
    message_dict = {}
    for i in range(len(message_list)):
        word = message_list[i]
        message_dict[word] = int(0)
        if word in SPAM_DICT:
            previous_val = message_dict.get(word)
            new_val = previous_val + 10 #change 1 to the value in SPAM_DICT maybe
            message_dict[word] = new_val
        elif word not in SPAM_DICT:
            pass
    return message_list, message_dict

def right_or_wrong(sms:list, sms_dict:dict, result:str, laber:str):
    """
    """
    if result == label:
        pass
    elif result != label:
        add_to_spam(sms, sms_dict)


def check(sms:str, label:str):
    tru_label = string(label)
    message_list, message_dict = compare_to_words(sms)
    result = is_spam_or_not(message_list, message_dict)
    right_or_wrong(message_list, message_dict, result, tru_label)


def check_again(sms:str, label:str):
    message_list, message_dict = compare_to_words(sms)
    is_spam_or_not(message_list, message_dict)
