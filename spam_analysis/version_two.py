SPAM_DICT = {
    'you won' : {'spam' : int(0), 'ham' : int(0)},
    'free money' : {'spam' : int(0), 'ham' : int(0)},
    'go to' : {'spam' : int(0), 'ham' : int(0)},
    'try out' : {'spam' : int(0), 'ham' : int(0)},
    'claim prize' : {'spam' : int(0), 'ham' : int(0)},
    'get free' : {'spam' : int(0), 'ham' : int(0)},
    'you aligble': {'spam' : int(0), 'ham' : int(0)},
    }
#AVG_LENGTH = 0
#OTHER VALS


def add_to_spam(spam:list):
    """
    If the message is spam it'll append the words
    from the message to a dict. If words are alredy
    in the dict it'll add plus one the their excisting 
    value. If the word is not in the dict it will get 
    added as a key with a value of one.
    """
    for i in range(len(spam)):
        bigram = spam[i]
        if bigram in SPAM_DICT:
            previous_val = SPAM_DICT.get(bigram)
            new_val = previous_val + 1 
            SPAM_DICT[bigram] = new_val 
        else:
            SPAM_DICT[bigram] = 0 


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
        spam_val += sms_dict[word]['spam']
    for key in sms_dict:
        word = key
        ham_val += sms_dict[word]['ham']
    if spam_val > ham_val:
        # print('spam')
        return('spam')
        add_to_spam(sms, sms_dict)
    elif ham_val > spam_val:
        # print('ham')
        return('ham')
    else:
        pass


def compare_to_dict(message:list, phrases:dict):
    """
    """
    for key in phrases:
        phrase = key
        if phrase in SPAM_DICT:
            previous_val = phrases.get(phrase)
            new_val = previous_val + 10 
            phrases[phrase] = new_val
        elif phrase not in SPAM_DICT:
            pass
    return message, phrases
            

def get_bigrams(message:str):
    """
    This function takes in a string as its argument and creates a 
    dictionary of bigrams

    This function takes in a string as its argument and creates
    a nested dictionary with a word as its key and a dictonary 
    with keys set as spam and ham as keys and values set to 0
    """
    # message = message.lower()
    words = message.split()
    words_list =  list(words)
    phrases_dict = {}
    for i in range(len(words_list)-1):
        current_word = words_list[i]
        next_word = words_list[i + 1]
        phrase = current_word + ' ' + next_word
        phrases_dict[word] = {'spam' : int(0), 'ham' : int(0)}
    return words_list, phrases_dict


def take_some_vals(sms:str, label:str):
    """
    This function is the same as the check function
    except it doest not return anything. It's just to
    populate the dict with some things
    """
    bigrams_list, bigrams_dict = get_bigrams(sms)
    message, bigrams_dict = compare_to_dict(bigrams_list, bigrams_dict)
    result = is_spam_or_not(message, bigrams_dict)
    right_or_wrong(bigrams_list, result, label)


def check(sms):
    words_list, phrases_dict = get_bigrams(sms)
    message, phrases_dict = compare_to_dict(words_list, phrases_dict)
    result = is_spam_or_not(message, phrases_dict)
    return result


