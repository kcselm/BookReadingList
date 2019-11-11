__author__ = "Kevin Selm"
__version__ = "0.1.0"

import requests

from config import URL
MAX_RESULTS = 5

def main():
    """ Main entry point of the app """
    reading_list = []
    get_books()


def get_books():
    """Query the books from the API"""
    book_query = input("Please enter a query to find books: ")
    url = URL + book_query + "&maxResults=" + str(MAX_RESULTS)
    PARAMS = {'volumes': book_query}

    res = requests.get(url=url, params=PARAMS)
    data = res.json()
    books = []

    for index in range(MAX_RESULTS):
        author = data['items'][index]['volumeInfo']['authors'][0]
        title = data['items'][index]['volumeInfo']['title']
        try:
            publisher = data['items'][index]['volumeInfo']['publisher']
        except:
            print("  No publishing company")

        # print(f'{index + 1} {author}\n  {title}\n  {publisher}\n') python version 3.6
        print('%s %s\n %s \n %s\n' % (index+1, author, title, publisher)) 
        book = [author, title, publisher]
        books.append(book)
    print_options(books)


def print_options(books, reading_list=[], option="query"):
    """
    Navigates the app based on the user input option
    :param list books: books returned from the users query
    :param list reading_list: a list of saved books for the user
    :param string option: the users input from the command line
    """
    option = input("Enter an option: \n\"view\" to view the reading_list\n1-5 to add a book to reading list\n" +
            "\"query\" to make another query \n\"exit\" to escape the program\n")

    if option == "view":
        view_reading_list(books, reading_list)
    elif option in map(str,(range(1, 6))):
        add_to_reading_list(books, reading_list, int(option))
    elif option == "query":
        get_books()
    elif option == "exit":
        exit()
    else: 
        print("Option not valid")
        print_options(books)


def add_to_reading_list(books, reading_list, option):
    """
    Add books from the query to the reading_list
    :param list books: books returned from the users query
    :param list reading_list: a list of saved books for the user
    :param string option: the users input from the command line
    """
    # reading_list +=  books[option-1]    
    reading_list.append(books[option-1])
    print_options(books, reading_list)


def view_reading_list(books, reading_list):
    """
    View the books added to the reading list
    :param list books: books returned from the users query
    :param list reading_list: a list of saved books for the user
    """
    for i in range(len(reading_list)):
        #print(f'{i} {reading_list[i][0]}\n  {reading_list[i][1]}\n {reading_list[i][2]}\n\n')
        index = reading_list[i]
        print('%s %s\n %s\n %s\n' % (i+1, index[0], index[1], index[2]))

    print_options(books, reading_list)
 
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()