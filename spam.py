def add_spam_to_spam():
    """
    if the message is spam I'll append
    the words the message to the dictionary 
    """


def is_spam_or_not(message:str):
    """
    """






not_spam = "Are you free for dinner?"
spam = "Do you want free stuff?"


words_and_nums = {
    'num' : 5,
    'red' : 2,
}

print(words_and_nums.get('num'))

if 'num' in words_and_nums:
    add = words_and_nums.get('num')
    new_val = add + 1 
    words_and_nums['num'] = new_val
else:
    print('no')

print(words_and_nums.get('num'))


is_spam_or_not(spam)
is_spam_or_not(not_spam)