import re
PROBS = {}





def spam_or_ham(ham_val:int, spam_val:int, length_of_list:int, PROBS_HAM:float, PROBS_SPAM:float):
    """
    """
    ham = ham_val/length_of_list
    spam = spam_val/length_of_list
    prob_spam_sms = (spam * PROBS_SPAM)/(spam * PROBS_SPAM + ham * PROBS_HAM)
    prob_ham_sms = (ham * PROBS_HAM)/(ham * PROBS_HAM + spam * PROBS_SPAM)
    if prob_ham_sms > prob_spam_sms:
        return('ham')
    elif prob_spam_sms > prob_ham_sms:
        return('spam')
    elif prob_ham_sms == prob_ham_sms:
       return('spam')
    else:
        pass    


####FOR TEST DATA SET
def add_probabilites(sms_list:list, probs_dict:dict, PROBS_HAM:float, PROBS_SPAM:float):
    """
    """
    spam_val = 0
    ham_val = 0
    length_of_list = len(sms_list)
    for i in range(len(sms_list)):
        word = sms_list[i]
        spam = PROBS[word]['spam']
        ham = PROBS[word]['ham']
        prob_spam_word = (spam * PROBS_SPAM)/(spam * PROBS_SPAM + ham * PROBS_HAM)
        prob_ham_word = (ham * PROBS_HAM)/(ham * PROBS_HAM + spam * PROBS_SPAM)
    if prob_ham_word > prob_spam_word:
        ham_val +=1
    elif prob_spam_word > prob_ham_word:
        spam_val += 1
    elif prob_ham_word == prob_ham_word:
        ham_val += 1
        spam_val +=1
    else:
        pass
    return ham_val, spam_val, length_of_list


#####FOR TEST DATA SET
def get_probs_for_words(sms_list:list):
    """
    This function takes in the sms as a list so we can
    check their values in the dictionary. 
    """
    other_words = []
    probs_dict = {}
    spam_prob = 0 
    ham_prob = 0
    for i in range(len(sms_list)):
        word = sms_list[i]
        word = str(word)
        if word not in PROBS:
            other_words.append(word)
        else:
            # print(word)
            spam_prob = PROBS[word]['spam']
            ham_prob = PROBS[word]['ham']
            word_prob = spam_prob+ham_prob
            spam = float(spam_prob/word_prob)
            ham = float(ham_prob/word_prob)
            # print("HAMM")
            # print(ham_prob)
            # print("SPAM")
            # print(spam_prob)
            probs_dict[word] = {'spam' : spam, 'ham' : ham}
    # print(probs_dict)
    return probs_dict, other_words
    

#####FOR TRAINING DATA SET    
def assign_vals_to_words(label:str, sms_list:list):
    """
    This function takes in the label of the message and the
    dictionary we created. We then check 
    """
    spam = 'spam'
    ham = 'ham'
    if label == spam:
        for i in range(len(sms_list)):
            word = sms_list[i]
            PROBS[word][spam] += 1
    elif label == ham:
        for i in range(len(sms_list)):
            word = sms_list[i]
            PROBS[word][ham] += 1       
    else:
        pass


####FOR TRAIN DATA SETS
def add_words_to_dict(sms_list:list):
    """
    This function takes in a list as its argument and with
    the items of those list we create a dictonary with the
    words as keys. 
    """
    for i in range(len(sms_list)):
        word = sms_list[i]
        if word in PROBS:
            pass
        elif word not in PROBS:
            PROBS[word] = {'spam' : int(0), 'ham' : int(0)}


####FOR BOTH DATA SETS
def clean_string(sms:str) -> list:
    """
    This function takes in a string as its argument and
    removes some stuff and returns everything else as a
    list
    """
    clean = re.sub(r'[\.!#%*()@,:/;"{}+=-]', ' ', sms)
    clean = re.sub(r'[0-9]', ' ', clean)
    clean_sms = clean.split()
    clean_sms = [token.lower() for token in clean_sms] 
    return clean_sms


def train_func(label:str, sms:str):
    sms_list = clean_string(sms)
    add_words_to_dict(sms_list)
    assign_vals_to_words(label, sms_list)


def test_func(sms:str, PROBS_HAM:float, PROBS_SPAM:float):
    sms_list = clean_string(sms)
    probs_dict, other_words = get_probs_for_words(sms_list)
    ham_val, spam_val, length_of_list = add_probabilites(sms_list, probs_dict, PROBS_HAM, PROBS_SPAM)
    result = spam_or_ham(ham_val, spam_val, length_of_list, PROBS_HAM, PROBS_SPAM)
    if result == 'spam':
        for i in range(len(other_words)):
            word = other_words[i]
            PROBS[word] = {'spam' : int(0), 'ham' : int(0)}
    return result


#sometimes words will have no apperances in each others categories 
#leaving some words to have a value of 1 which can affect the result
#of a sentence