# SPAM_DICT = {} #maybe a global variable with spam likely words, idk
# NON_SPAM_DICT = {} #maybe to compare

# def is_spam_or_not(message:list, message_dict:dict):
#     """
#     This function detemines if message is spam or 
#     not based on ...
#     """
#     spam_num = 0
#     for val in message_dict.values():
#         spam_num += val
#     if spam_num >= (len(message) * 10):
#         add_to_spam(message)
#         print('spam')
#     else:
#         print('not spam')


# def add_to_spam(spam:list):
#     """
#     If the message is spam it'll append the words
#     from the message to a dict. If words are alredy
#     in the dict it'll add plus one the their excisting 
#     value. If the word is not in the dict it will get 
#     added as a key with a value of one.
#     """
#     for i in range(len(spam)):
#         word = spam[i]
#         if spam[i] in SPAM_DICT:
#             previous_val = SPAM_DICT.get(word)
#             new_val = previous_val + 1 
#             SPAM_DICT[i] = new_val 
#         else:
#             SPAM_DICT[spam(i)] = 0 #previously at 1 now at 0 idk


# def compare_to_words(message:str):
#     """
#     This function takes in a string as its argument. The
#     string is turned into a list which then is looped through
#     comparing everyword to words in a dictionay filled with
#     spam likely words. 
#     """
#     message = message.split()
#     message = [message.lower() for word in message] 
#     message_list = list(message)
#     message_dict = {}
#     for i in range(len(message_list)):
#         word = message_list[i]
#         message_dict[word] = int(0)
#         if word in SPAM_DICT:
#             previous_val = message_dict.get(word)
#             new_val = previous_val + 10 #change 1 to the value in SPAM_DICT maybe
#             message_dict[i] = new_val
#         elif message_list[i] not in SPAM_DICT:
#             pass
#     return message, message_dict


# def compare_to_phrases(phrases:dict):
#     """
#     """
#     for key in phrases:
#         phrase = key
#         if phrase in SPAM_DICT:
#             previous_val = phrases.get(key)
#             new_val = previous_val + 1 
#             phrases[key] = new_val
            

# def get_bigrams(message:str):
#     """
#     This function takes in a string as its argument and creates a 
#     dictionary of bigrams
#     """
#     words = message.split()
#     words = [words.lower() for word in words] 
#     words_list =  list(words)
#     phrases_dict = {}
#     for i in range(len(words_list)-1):
#         current_word = words_list[i]
#         next_word = words_list[i + 1]
#         phrase = current_word + ' ' + next_word
#         phrases_dict[phrase] = 0 
#     return message, phrases_dict

# #DRIVER FUNCTIONS
# def spam_words(text):
#     test_string = text
#     message, message_dict = compare_to_words(text)
#     is_spam_or_not(message, message_dict)


# def spam_bigrams(text):
#     test_string = text
#     message, phrases = get_bigrams(test_string)
    

# def basic_test():
#     sentence_list = [
#         'this is a sentence',
#     ]
#     for i in range(len(sentence_list)):
#         spam_words(sentence_list[i])


# basic_test()

# def algorithm_v1(sms: str) -> bool:
#     """
#     This function accepts an SMS message as a string and returns `True` if
#     it is spam. Otherwise, it returns `False` if it's ham.
#     """
#     if "Free" in sms:
#         return True

#     return False


# def algorithm_v2(sms:str):
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
    'For': 0,
    'ur' :0, 
    'chance' :0,
    'to' :0,
    'win' :0,
    'a':0,
    '£250':0,
    'wkly':0,
    'shopping':0,
    'spree':0, 
    'TXT:' :0, 
    'SHOP' :0, 
    'to':0, 
    '80878.':0, 
    'Ts&Cs':0, 
    'www.txt-2-shop.com':0, 
    'custcare':0, 
    '08715705022,':0, 
    '1x150p/wk':0
}

def add_to_spam(sms:list, sms_dict:dict):
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


def spam_or_ham(sms:list, sms_dict:dict):
    spam_val = 0 
    ham_val = 0
    for key in sms_dict:
        word = key
        spam_val += sms_dict[word]['spam']
    for key in sms_dict:
        word = key
        ham_val += sms_dict[word]['ham']
    if spam_val >= ham_val:
        print('spam')
        add_to_spam(sms, sms_dict)
    elif ham_val > spam_val:
        print('ham')
    else:
        pass


def compare_to_words(sms:list, sms_dict:dict):
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
    This function takes in a string as its arguments and creates 
    a dictionary with the keys as the words of the string and its 
    values as a dictionay with spam set to 0 and ham set to 0
    """
    sms = sms.split()
    sms = list(sms)
    sms_dict = {}
    for i in range(len(sms)):
        word = sms[i]
        sms_dict[word] = {'spam' : int(0), 'ham' : int(0)}
    return sms, sms_dict


def main_func(message):
    sms_list, sms_dict = crate_dict(message)
    message_list, message_dict = compare_to_words(sms_list, sms_dict)
    spam_or_ham(message_list, message_dict)
    


# text = 'hey are you free tomorrow'
# sms = 'you won free money try out claim prize get free you eligable'

# main_func(text)
#NOTES 
#I can add a final function that compares outcome to real label
#if algorithm got it right dont append to the SPAM_DICT but if
#its wrong append to dict. Run alg_v1 then alg_v2 and in the 
# end alg_v3 should start to better detect spam
#use same SPAM_DICT for all functions