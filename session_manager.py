# coding=utf-8

from session import Session


class SessionManager(object):
    SESSIONS_NUM = 10
    _session_index = 0

    def __init__(self):
        self._sessions = [Session(sess_id) for sess_id in range(self.SESSIONS_NUM)]

    @property
    def current_session(self):
        return self._sessions[self._session_index]

    def reset_cur_session(self):
        sess_id = self._sessions[self._session_index].session_id
        self._sessions[self._session_index] = Session(sess_id)

    def first(self):
        self._session_index = 0

    def last(self):
        self._session_index = self.SESSIONS_NUM - 1

    def next(self):
        if self._session_index < self.SESSIONS_NUM:
            self._session_index += 1
        else:
            self._session_index = 0

    def prev(self):
        if self._session_index > 0:
            self._session_index -= 1

