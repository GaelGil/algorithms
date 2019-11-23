SPAM_DICT = {
    'you' : {'spam' : int(0), 'ham' : int(0)},
    'won' : {'spam' : int(0), 'ham' : int(0)},
    'free' : {'spam' : int(0), 'ham' : int(0)},
    'money' : {'spam' : int(0), 'ham' : int(0)},
    'try' : {'spam' : int(0), 'ham' : int(0)},
    'claim' : {'spam' : int(0), 'ham' : int(0)},
    'prize' : {'spam' : int(0), 'ham' : int(0)},
    'get' : {'spam' : int(0), 'ham' : int(0)},
    'eligable': {'spam' : int(0), 'ham' : int(0)},
    'For': {'spam' : int(0), 'ham' : int(0)},
    'ur' :{'spam' : int(0), 'ham' : int(0)}, 
    'chance' :{'spam' : int(0), 'ham' : int(0)},
    'to' :{'spam' : int(0), 'ham' : int(0)},
    'win' :{'spam' : int(0), 'ham' : int(0)},
    'a':{'spam' : int(0), 'ham' : int(0)},
    '£250':{'spam' : int(0), 'ham' : int(0)},
    'wkly':{'spam' : int(0), 'ham' : int(0)},
    'shopping':{'spam' : int(0), 'ham' : int(0)},
    'spree':{'spam' : int(0), 'ham' : int(0)}, 
    'TXT:' :{'spam' : int(0), 'ham' : int(0)}, 
    'SHOP' :{'spam' : int(0), 'ham' : int(0)}, 
    'to':{'spam' : int(0), 'ham' : int(0)}, 
    '80878.':{'spam' : int(0), 'ham' : int(0)}, 
    'Ts&Cs':{'spam' : int(0), 'ham' : int(0)}, 
    'www.txt-2-shop.com':{'spam' : int(0), 'ham' : int(0)}, 
    'custcare':{'spam' : int(0), 'ham' : int(0)}, 
    '08715705022,':{'spam' : int(0), 'ham' : int(0)}, 
    '1x150p/wk':{'spam' : int(0), 'ham' : int(0)},
}


def add_to_spam(sms:list):
    """
    If the message is spam it'll append the words
    from the message to a dict. If words are alredy
    in the dict it'll add plus one the their excisting 
    value. If the word is not in the dict it will get 
    added as a key with a value of one.
    """
    for i in range(len(sms)):
        word = sms[i]
        if word in SPAM_DICT:
            previous_val = SPAM_DICT.get(word)
            new_val = previous_val + 5
            SPAM_DICT[i] = new_val 
        else:
            SPAM_DICT[word] = 0 


def right_or_wrong(sms:list, result:str, label:str):
    """
    This function takes in the message, result of my function,
    and real label of the function. If the result matches the 
    labe everything is cool. If the result does not match the
    """
    if result == label:
        pass
        # print('correct')
    elif result != label:
        # print('fail')
        add_to_spam(sms)


def spam_or_ham(sms:list, sms_dict:dict):
    """
    This function takes in a list and a dict as its argument.
    We first loop through our dictionary and add up all the 
    values of spam and ham. In the end we compare which value
    is greater to decied weather if the message is spam or not. 
    """
    spam_val = 0 
    ham_val = 0
    for key in sms_dict:
        word = key
        nested_spam_val = sms_dict[word]['spam']
        spam_val += nested_spam_val
    for key in sms_dict:
        word = key
        nested_ham_val = sms_dict[word]['ham']
        ham_val += nested_ham_val
    if spam_val > ham_val:
        # print('spam')
        return('spam')
        add_to_spam(sms, sms_dict)
    elif ham_val > spam_val:
        # print('ham')
        return('ham')
    else:
        pass


def compare_to_dict(sms:list, sms_dict:dict):
    """
    This function takes in a list and dict as its argument and
    compares words in our list to words in SPAM_DICT. If the word
    is found in there we will change the key/word value for that word
    in our dictionay from its previous value of 0 to 1 in spam. 
    If it is not found in there we will change ham to 1
    """
    for key in sms_dict:
        word = key
        if word in SPAM_DICT:
            val = SPAM_DICT.get(key)
            sms_dict[key]['spam'] = val
        elif word not in SPAM_DICT:
            sms_dict[key]['ham'] = 1
        else:
            pass
    return sms, sms_dict 


def crate_dict(sms:str):
    """
    This function takes in a string as its argument and creates
    a nested dictionary with a word as its key and a dictonary 
    with keys set as spam and ham as keys and values set to 0
    """
    sms = sms.split()
    sms = list(sms)
    sms_dict = {}
    for i in range(len(sms)):
        word = sms[i]
        # TODO: make this a defaultdict
        sms_dict[word] = {'spam' : int(0), 'ham' : int(0)}
    return sms, sms_dict


def take_some_vals(sms:str, label:str):
    """
    This function is the same as the check function
    except it doest not return anything. It's just to
    populate the dict with some values
    """
    sms_list, sms_dict = crate_dict(sms)
    message_list, message_dict = compare_to_dict(sms_list, sms_dict)
    result = spam_or_ham(message_list, message_dict)
    right_or_wrong(sms_list, result, label)


def main_func(message):
    sms_list, sms_dict = crate_dict(message)
    message_list, message_dict = compare_to_dict(sms_list, sms_dict)
    result = spam_or_ham(message_list, message_dict)
    return result
