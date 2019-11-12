import unittest
from unittest.mock import patch
import google_book

#from google_book import 
class TestGoogleBook(unittest.TestCase): 
    def setUp(self):
        self.reading_list = [['Mark Lutz', 'David Ascher', 'Learning Python', '"O\'reilly Media, Inc."'], 
                ['Joseph' 'Eddy' 'Fontenrose', 'Python', 'Biblo & Tannen Publishers']] 

    def test_user_input(self):
        """
        Testing get_input().  Gets user input and tests the type of it.  
        """
        self.assertIsInstance(google_book.get_input('design patterns'), str)
        self.assertIsInstance(google_book.get_input(1), str)
        self.assertIsInstance(google_book.get_input((tuple)), str)

    # def test_user_input(self):
    #     with mock.patch('builtins.input', return_value="view") 
    #         assert google_book.get_input()

    # def test_get_books(self):
    #     with patch('google_book.requests.get') as mocked_get:
    #         mocked_get.return_value.ok = True
    #         mocked_get.return_value = 'Success'
            
    #         google_book.get_books()
    #         mocked_get.assert_called_with('https://www.googleapis.com/books/v1/volumes?q=python&maxResults=5')
    #         self.assertEqual(google_book.get_books(), 'Success')

if __name__ == '__main__':
    unittest.main()