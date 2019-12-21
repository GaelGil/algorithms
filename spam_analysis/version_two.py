import re
PROBS = {}


def do_math(ham_prob:float, spam_prob:float, total_prob:int):
    """
    """


def count_vals(sms_list:list):
    """
    This function takes in the sms as a list so we can
    check their values in the dictionary. 
    """
    probs_list = []
    spam_prob = 0 
    ham_prob = 0
    for i in range(len(sms_list)):
        word = i 
        spam_prob = PROBS[word]['spam']
        ham_prob = PROBS[word]['ham']
        spam_prob += spam_prob
        ham_prob += ham_prob
    total_prob = ham_prob + spam_prob
    return (ham_prob/total_prob, spam_prob/total_prob, total_prob)
    
    
def assign_vals(label:str, sms_list:list):
    """
    This function takes in the label of the message and the
    dictionary we created. We then check 
    """
    spam = 'spam'
    ham = 'ham'
    if label == spam:
        for i in range(len(sms_list)):
            word = sms_list[i]
            PROBS[word][spam] = 1
    elif label == ham:
        for i in range(len(sms_list)):
            word = sms_list[i]
            PROBS[word][ham] = 1       
            # for key in sms_dict:
            # word = key
            ## if word in sms_dict:
            # PROBS[key]['spam'] = 1
    # elif label == HAM:
    #     for key in PROBS:
    #         word = key
    #         # if word in sms_dict:
    #         PROBS[key]['ham'] = 1
    else:
        pass


def create_dict(sms_list:list):
    """
    This function takes in a list as its argument and with
    the items of those list we create a dictonary with the
    words as keys. 
    """
    for i in range(len(sms_list)):
        word = sms[i]
        if word in PROBS:
            pass
        elif word not in PROBS:
            PROBS[word] = {'spam' : int(0), 'ham' : int(0)}


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




my_str = "my string has ! and ( and ) ; and as well as - = and . but even # $ but itll get cleaned"

print(clean_sms(my_str))

# def train_func(label:str, sms:str):


def test_func(sms:str):
    sms_list = clean_string(sms)
    count_vals(sms_list)



#find a way where when we are given the label we 