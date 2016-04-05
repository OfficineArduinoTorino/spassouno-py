import unittest
import sys
import os

from session_manager import SessionManager
from session import Session

class TestSessionManager(unittest.TestCase):

    def setUp(self):
        self.__sessionManager = SessionManager()

    def test_next_session(self):
        session = self.__sessionManager.current_session
        self.__sessionManager.next()
        next_session = self.__sessionManager.current_session

        self.assertNotEqual(session.session_id, next_session.session_id)

    def test_get_first_session(self):
        self.__sessionManager.first()
        session = self.__sessionManager.current_session
        self.__sessionManager.next()
        self.__sessionManager.first()
        first_session = self.__sessionManager.current_session

        self.assertEqual(session.session_id, first_session.session_id)


class TestSession(unittest.TestCase):

    def setUp(self):
        self.__session = Session(1)

    def test_get_file_name(self):
        file1 = self.__session.get_file_name()
        file2 = self.__session.get_file_name()

        self.assertIsNotNone(file1)
        self.assertIsNotNone(file2)
        self.assertNotEqual(file1, file2)


if __name__ == '__main__':
    unittest.main()

