import unittest
from unittest.mock import patch
import google_book

#from google_book import 
class TestGoogleBook(unittest.TestCase): 
    def setUp(self):
        self.reading_list = [['Mark Lutz', 'David Ascher', 'Learning Python', '"O\'reilly Media, Inc."'], 
                ['Joseph' 'Eddy' 'Fontenrose', 'Python', 'Biblo & Tannen Publishers']] 

    # def test_user_input(self):
    #     with mock.patch('builtins.input', return_value="view") 
    #         assert google_book.get_input()

    # def test_get_books(self):
    #     with patch('google_book.requests.get') as mocked_get:
    #         mocked_get.return_value.ok = True
    #         mocked_get.return_value = 'Success'
            
    #         books = google_book.get_books()
    #         mocked_get.assert_called_with('https://www.googleapis.com/books/v1/volumes?q=python&maxResults=5')
    #         self.assertEqual(books, 'Success')

if __name__ == '__main__':
    unittest.main()