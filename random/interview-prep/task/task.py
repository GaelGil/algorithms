import re




def read_book(book):
    with open(book, 'r') as file:        
        data = file.read().replace('\n', ' ')  
    return data

def clean_book(book:list) -> list:
    """
    This function takes in a list as its argument which contains the words to a book.
    The function will clean the list by removing some punctuation, numbers, and make 
    all words lowercase. The function will then return the cleaned version of the book
    Parameters
    ----------
    book; list
        This is a list of all the words in the book 
    Returns
    -------
    list
        This function returns a list of all the words in the book without 
        any punctuation
    """
    cleaned = re.sub(r'[\!#$%*?[()@,:/;"{}+=-]', ' ', book)
    clean_nums = re.sub(r'[0-9]', ' ', cleaned)
    tokens = clean_nums.split()
    tokens = [token.lower() for token in tokens]
    return tokens


def check_longest_and_shortest(book:str) -> list:
    shortest_list = []
    longest_list = []
    shortest = book[0]
    longest = book[0]
    print(type(book))
    for i in book:
        if len(str(i)) < shortest:
            shortest_list.append(i)
        elif len(i) > longest: 
            longest_list.append(i)
    return [shortest_list[len(shortest_list)-1], longest_list[len(longest_list)-1]]
    

# def most_common_word():

def check_average_length_sentence(book:str):
    sentences = re.findall(r'.', book)
    return sentences


book_string = read_book('./book.txt')
book_list = clean_book(book_string)
# print(check_longest_and_shortest(book_list))
print(check_average_length_sentence(book_string))

#longest
#shortest
#most common
#average sentence length 